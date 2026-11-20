# PrusaSlicer presets for the Ender 3 V3 SE

This profile set targets a stock Marlin 2 Ender 3 V3 SE with a 0.4 mm nozzle. Printer, filament and print presets are maintained separately and assembled into distributable INI bundles.

The printer preset describes the machine, while filament presets capture material-specific settings. The Python scripts assemble and validate the profiles. Their checks cover configuration data. Physical results depend on printer and filament calibration.

- [Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle.ini](profiles/printer/Creality%20Ender%203%20V3%20SE%20-%20Stock%20Marlin2%20-%200.4%20nozzle.ini)
- [build-bundle.py](scripts/build-bundle.py)
- [validate-profiles.py](scripts/validate-profiles.py)
- [CALIBRATION.md](docs/CALIBRATION.md)

## Presets included

### Printer

- `Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle`

### Filament

- `Soroush PLA - 1.75mm`
- `Soroush PLA+ - 1.75mm`
- `Soroush PLA+ - eSUN 1.75mm` — tuned for eSUN PLA+ spool
- `Soroush Silk PLA - 1.75mm`
- `Soroush PETG - 1.75mm`

### Print settings

- `Soroush PLA - Ultra Quality` — decorative and final surface quality
- `Soroush PLA - Quality` — balanced default profile
- `Soroush PLA - Cosplay Mask Organic Supports` — masks, horns, cosplay models, easy support removal
- `Soroush PLA - Fast Draft` — prototypes and fit checks
- `Soroush PLA - Mechanical Strong` — brackets, mounts, stronger functional parts

## Horn_L / mask recommendation

For the Horn_L mask model, start with:

- Printer: `Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle`
- Filament: `Soroush PLA+ - eSUN 1.75mm` for the eSUN PLA+ spool, or `Soroush PLA+ - 1.75mm` for a generic PLA+ baseline
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

## eSUN PLA+ spool

For the eSUN PLA+ spool, import the bundle and select:

```text
Filament: Soroush PLA+ - eSUN 1.75mm
```

See `docs/ESUN_PLA_PLUS.md` for temperature and support tuning notes.
