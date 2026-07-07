# eSUN PLA+ profile

This profile is for the eSUN PLA+ spool shown in the chat.

Use this preset in PrusaSlicer:

```text
Filament: Soroush PLA+ - eSUN 1.75mm
```

Recommended first print settings:

```text
Nozzle first layer: 225°C
Nozzle other layers: 220°C
Bed first layer:    60°C
Bed other layers:   55°C
Fan:                100%
```

For Horn_L, masks, figures, and detailed models:

```text
Printer:  Creality Ender 3 V3 SE - Stock Marlin2 - 0.4 nozzle
Filament: Soroush PLA+ - eSUN 1.75mm
Print:    Soroush PLA - Cosplay Mask Organic Supports
```

Troubleshooting:

- If layer adhesion is weak or the part is brittle, try `225°C` for all layers.
- If supports are too hard to remove, keep the filament at `220°C` or try `218°C`, and increase support contact Z distance to `0.28 mm` in the print profile.
- If there is stringing, keep temperature at `220°C` and run a retraction test before changing the printer retraction profile.
