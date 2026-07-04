# Calibration checklist

These profiles assume the printer is mechanically healthy. Run this checklist before judging the presets.

## 1. First layer

- Clean the build plate.
- Let the bed reach temperature for a few minutes.
- Run a first-layer square.
- Adjust Z-offset until the line is smooth and joined, not round and not scraped.

## 2. Temperature

For PLA, test roughly 205–225C.

If layers split, go warmer or reduce fan.
If details melt or stringing increases, go cooler.

## 3. Flow / extrusion multiplier

Start at `1.00`. Adjust only after temperature is reasonable.

## 4. Retraction

Ender 3 V3 SE is direct drive. Start with:

```text
Retraction length: 0.8 mm
Retraction speed:  40 mm/s
Z lift:            0.2 mm
```

Do not jump to Bowden values like 4–6 mm.

## 5. Support removal test

Before printing a long mask, print a small supported overhang test with the Cosplay profile.
