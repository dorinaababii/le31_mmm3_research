#!/usr/bin/env bash
# Wires this folder's skills + SOUL.md into a Hermes Agent install.
# Run this from inside the sparse-checked-out `hermes/` folder itself, i.e.:
#   cd ~/hermes-config/hermes && ./install.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
CONFIG_FILE="$HERMES_HOME/config.yaml"
SKILLS_DIR="$SCRIPT_DIR/skills"
SOUL_SRC="$SCRIPT_DIR/SOUL.md"
SOUL_DEST="$HERMES_HOME/SOUL.md"

if [ ! -d "$HERMES_HOME" ]; then
  echo "Error: $HERMES_HOME not found. Install Hermes Agent first (see hermes-agent.nousresearch.com), then re-run this script." >&2
  exit 1
fi

echo "Hermes home: $HERMES_HOME"
echo "Skills dir to register: $SKILLS_DIR"

# --- SOUL.md ---------------------------------------------------------------
if [ -e "$SOUL_DEST" ] && [ ! -L "$SOUL_DEST" ]; then
  backup="$SOUL_DEST.bak.$(date +%Y%m%d%H%M%S)"
  echo "Existing SOUL.md found (not a symlink) — backing up to $backup"
  mv "$SOUL_DEST" "$backup"
fi
ln -sfn "$SOUL_SRC" "$SOUL_DEST"
echo "Linked SOUL.md -> $SOUL_SRC"

# --- config.yaml: skills.external_dirs -------------------------------------
mkdir -p "$HERMES_HOME"
touch "$CONFIG_FILE"

python3 - "$CONFIG_FILE" "$SKILLS_DIR" <<'PYEOF'
import sys
try:
    import yaml
except ImportError:
    print("PyYAML not available — add this to %s by hand:" % sys.argv[1])
    print("skills:\n  external_dirs:\n    - \"%s\"" % sys.argv[2])
    sys.exit(0)

config_path, skills_dir = sys.argv[1], sys.argv[2]

with open(config_path) as f:
    data = yaml.safe_load(f) or {}

skills_cfg = data.setdefault("skills", {})
dirs = skills_cfg.setdefault("external_dirs", [])
if skills_dir not in dirs:
    dirs.append(skills_dir)
    with open(config_path, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
    print("Added %s to skills.external_dirs in %s" % (skills_dir, config_path))
else:
    print("skills.external_dirs already includes %s — no change made" % skills_dir)
PYEOF

echo
echo "Done. Remaining manual steps:"
echo "  1. Restart the Hermes gateway/CLI so it picks up the new config."
echo "  2. (Optional, for Linear-backed specs) run:"
echo "       hermes mcp add linear --url https://mcp.linear.app/mcp"
echo "     and complete the OAuth flow it prompts for."
echo "  3. In each project you want this workflow active, copy AGENTS.md.template"
echo "     to that project's AGENTS.md and fill in its Structure/Stack/Workflow sections."
echo "  4. Verify: run 'hermes' and try '/development' — it should load from this pack."
