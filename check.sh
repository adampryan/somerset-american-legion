#!/usr/bin/env bash
# Everything I can check about this site without a browser.
#
#   ./check.sh
#
# Worth running before every push: GitHub Pages serves whatever lands on main
# straight to the bar and to the officers, with no build step in between and
# no way to roll back except another push.
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
    echo "node is not installed — cannot parse the inline scripts" >&2
    exit 1
fi

fail=0
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

echo "── inline JavaScript parses ──────────────────────────────────────"
for f in *.html; do
    python3 - "$f" > "$tmp/x.js" <<'PY'
import re, sys
html = open(sys.argv[1]).read()
# Only scripts with a body; <script src=…> has nothing to parse.
print("\n".join(re.findall(r"<script>(.*?)</script>", html, re.S)))
PY
    [ -s "$tmp/x.js" ] || continue
    if node --check "$tmp/x.js" 2>"$tmp/err"; then
        printf '  ok   %s\n' "$f"
    else
        printf '  FAIL %s\n' "$f"; sed 's/^/       /' "$tmp/err"; fail=1
    fi
done

# The register and the admin panel both poll their own page and reload when the
# build meta changes. Ship a change without moving that string and every tab
# already open keeps running the old file until someone hard-refreshes it —
# which is exactly how the admin page sat on its July build through seven
# deploys. Nothing at runtime notices, so it gets checked here.
echo
echo "── the auto-update meta exists ───────────────────────────────────"
for f in admin.html pos.html; do
    if grep -q '<meta name="build" content="[^"]\+"' "$f"; then
        printf '  ok   %s → %s\n' "$f" "$(grep -o 'name="build" content="[^"]*"' "$f" | head -1 | cut -d'"' -f4)"
    else
        printf '  FAIL %s has no build meta — auto-update cannot work\n' "$f"; fail=1
    fi
done

echo
[ "$fail" -eq 0 ] && echo "all checks passed" || { echo "CHECKS FAILED"; exit 1; }
