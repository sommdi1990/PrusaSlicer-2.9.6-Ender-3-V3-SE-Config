# Horn_L / mask printing guide

Use:

```text
Print Settings: Soroush PLA - Cosplay Mask Organic Supports
Filament:       Soroush PLA - 1.75mm or Soroush PLA+ - 1.75mm
Printer:        Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle
```

## Why this profile

The profile uses:

- 0.20 mm layer height for stronger layer bonding than 0.12/0.16 on tall thin geometry
- 4 perimeters for shell strength
- 12% gyroid infill for light cosplay parts
- organic supports, build-plate only
- 0.25 mm top Z contact distance
- looser XY separation for easier support removal
- lower maximum fan in the PLA filament profile to improve layer adhesion

## Orientation

For a mask/horn model, do not blindly print it upright. Rotate the model so the visible front surface gets fewer support scars.

Good starting point:

- Tilt the face/mask backward about 30–45 degrees
- Keep support generation mostly behind/under the model
- Use organic supports from build plate only whenever possible

## If supports still stick too hard

Increase only one thing at a time:

```text
Support contact Z distance: 0.25 -> 0.28
Support XY separation:      80% -> 100%
Interface layers:           2 -> 1
```

## If layers separate or the horns break

Try:

```text
Filament temperature: 215 -> 220 for PLA
Max fan speed:        85% -> 70–75%
Print profile:        Cosplay Mask, not Ultra Quality
Filament:             dry 4–6h around 45–50C for PLA
```
