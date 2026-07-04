#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -n "${PRUSASLICER_CONFIG_DIR:-}" ]]; then
  CONFIG_DIR="$PRUSASLICER_CONFIG_DIR"
elif [[ -d "$HOME/.var/app/com.prusa3d.PrusaSlicer/config/PrusaSlicer" ]]; then
  CONFIG_DIR="$HOME/.var/app/com.prusa3d.PrusaSlicer/config/PrusaSlicer"
else
  CONFIG_DIR="$HOME/.config/PrusaSlicer"
fi

mkdir -p "$CONFIG_DIR/print" "$CONFIG_DIR/filament" "$CONFIG_DIR/printer"
BACKUP_DIR="$CONFIG_DIR/backup-soroush-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

for kind in print filament printer; do
  if compgen -G "$CONFIG_DIR/$kind/Soroush*.ini" > /dev/null || compgen -G "$CONFIG_DIR/$kind/Creality Ender 3 V3 SE*.ini" > /dev/null; then
    mkdir -p "$BACKUP_DIR/$kind"
    cp -a "$CONFIG_DIR/$kind"/*.ini "$BACKUP_DIR/$kind/" 2>/dev/null || true
  fi
  cp -v "$ROOT/profiles/$kind"/*.ini "$CONFIG_DIR/$kind/"
done

echo
echo "Installed profiles into: $CONFIG_DIR"
echo "Backup, if needed: $BACKUP_DIR"
echo "Restart PrusaSlicer, then select the Soroush presets."
echo "Alternative safe method: PrusaSlicer > File > Import > Import Config Bundle > dist/Soroush_Ender3V3SE_PrusaSlicer_2.9.6_config_bundle.ini"
