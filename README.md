# PrusaSlicer 2.9.6 profiles for Creality Ender 3 V3 SE

A curated PrusaSlicer profile set for **Creality Ender 3 V3 SE** with stock **Marlin 2** firmware and a **0.4 mm nozzle**.

This repository contains printer, filament, and print presets tuned for PLA/PLA+/Silk PLA/PETG on the Ender 3 V3 SE.

## Presets included

### Printer

- `Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle`

### Filament

- `Soroush PLA - 1.75mm`
- `Soroush PLA+ - 1.75mm`
- `Soroush Silk PLA - 1.75mm`
- `Soroush PETG - 1.75mm`

### Print settings

- `Soroush PLA - Ultra Quality` — decorative and final surface quality
- `Soroush PLA - Quality` — balanced default profile
- `Soroush PLA - Cosplay Mask Organic Supports` — masks, horns, cosplay models, easy support removal
- `Soroush PLA - Fast Draft` — prototypes and fit checks
- `Soroush PLA - Mechanical Strong` — brackets, mounts, stronger functional parts

## Recommended install method

In PrusaSlicer:

```text
File > Import > Import Config Bundle
```

Then select:

```text
dist/Soroush_Ender3V3SE_PrusaSlicer_2.9.6_config_bundle.ini
```

## Optional direct install on Linux

```bash
./scripts/install-to-prusaslicer.sh
```

The script detects both common PrusaSlicer config locations:

- Native package: `~/.config/PrusaSlicer`
- Flatpak: `~/.var/app/com.prusa3d.PrusaSlicer/config/PrusaSlicer`

## Horn_L / mask recommendation

For the Horn_L mask model, start with:

- Printer: `Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle`
- Filament: `Soroush PLA - 1.75mm` or `Soroush PLA+ - 1.75mm`
- Print: `Soroush PLA - Cosplay Mask Organic Supports`
- Supports: organic, build plate only
- Layer height: 0.20 mm
- Infill: Gyroid 12%
- Perimeters: 4

The original `Horn_L.3mf` model is intentionally **not included** in this public repository because it may have its own license or copyright restrictions.

## Before printing important parts

Run these once for your exact spool:

1. First-layer calibration / Z-offset check
2. Temperature tower
3. Flow / extrusion multiplier calibration
4. Retraction test
5. Small support-removal test

The presets are a strong baseline, not a substitute for spool-specific calibration.
