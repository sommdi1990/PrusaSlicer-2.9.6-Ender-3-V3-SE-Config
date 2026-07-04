#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "Soroush_Ender3V3SE_PrusaSlicer_2.9.6_config_bundle.ini"

parts = ["# Soroush PrusaSlicer config bundle\n# Rebuilt from profiles/* by scripts/build-bundle.py\n\n"]
for subdir in ["print", "filament", "printer"]:
    for path in sorted((ROOT / "profiles" / subdir).glob("*.ini")):
        parts.append(path.read_text(encoding="utf-8").strip() + "\n\n")
parts.append("[presets]\n")
parts.append("print = Soroush PLA - Cosplay Mask Organic Supports\n")
parts.append("sla_print = \n")
parts.append("sla_material = \n")
parts.append("printer = Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle\n")
parts.append("filament = Soroush PLA - 1.75mm\n")
parts.append("physical_printer = \n")
OUT.write_text("".join(parts), encoding="utf-8")
print(f"Wrote {OUT}")
