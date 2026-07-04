#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
required_sections = {"print", "filament", "printer"}
counts = {k: 0 for k in required_sections}

for path in sorted((ROOT / "profiles").rglob("*.ini")):
    text = path.read_text(encoding="utf-8")
    headers = re.findall(r"^\[(print|filament|printer):([^\]]+)\]", text, re.M)
    if len(headers) != 1:
        errors.append(f"{path}: expected exactly one preset section, found {len(headers)}")
        continue
    kind, name = headers[0]
    counts[kind] += 1
    for token in ["= nil", " = nil"]:
        # nil is allowed in PrusaSlicer, so only warn by not failing.
        pass
    if kind == "printer":
        for key in ["bed_shape", "gcode_flavor", "nozzle_diameter", "retract_length", "start_gcode", "end_gcode"]:
            if not re.search(rf"^{re.escape(key)}\s*=", text, re.M):
                errors.append(f"{path}: missing {key}")
    if kind == "print":
        for key in ["layer_height", "perimeters", "fill_density", "perimeter_generator"]:
            if not re.search(rf"^{re.escape(key)}\s*=", text, re.M):
                errors.append(f"{path}: missing {key}")
    if kind == "filament":
        for key in ["filament_type", "temperature", "bed_temperature", "filament_diameter"]:
            if not re.search(rf"^{re.escape(key)}\s*=", text, re.M):
                errors.append(f"{path}: missing {key}")

for kind in required_sections:
    if counts[kind] == 0:
        errors.append(f"No {kind} profiles found")

if errors:
    print("Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Validation OK:", counts)
