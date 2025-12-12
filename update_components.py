#!/usr/bin/env python3
"""
Update Somerset American Legion HTML files to use component placeholders.
Run from the site root directory (somerset-american-legion/).
"""

import re
import os
from pathlib import Path

# Files to skip
SKIP_FILES = {'README.md'}

def update_html_file(filepath):
    """Update a single HTML file with component placeholders."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern for top-bar (with or without comment)
    # Matches from <!-- Top Header Bar --> or <div class="top-bar"> through closing </div>
    top_bar_pattern = r'(\s*)(?:<!--\s*Top(?:\s+Header)?\s+Bar\s*-->\s*)?<div class="top-bar">.*?</div>\s*</div>\s*</div>'
    content = re.sub(top_bar_pattern, r'\1<div data-component="top-bar"></div>', content, flags=re.DOTALL)
    
    # Pattern for header
    header_pattern = r'(\s*)(?:<!--\s*Main Header\s*-->\s*)?<header class="main-header">.*?</header>'
    content = re.sub(header_pattern, r'\1<div data-component="header"></div>', content, flags=re.DOTALL)
    
    # Pattern for nav
    nav_pattern = r'(\s*)(?:<!--\s*Navigation\s*-->\s*)?<nav class="main-nav">.*?</nav>'
    content = re.sub(nav_pattern, r'\1<div data-component="nav"></div>', content, flags=re.DOTALL)
    
    # Pattern for footer
    footer_pattern = r'(\s*)(?:<!--\s*Footer\s*-->\s*)?<footer class="main-footer">.*?</footer>'
    content = re.sub(footer_pattern, r'\1<div data-component="footer"></div>', content, flags=re.DOTALL)
    
    # Add components.js before main.js if not already present
    if 'components.js' not in content:
        content = re.sub(
            r'(<script src="js/main\.js"></script>)',
            r'<script src="js/components.js"></script>\n    \1',
            content
        )
    
    # Only write if changes were made
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    # Get all HTML files in current directory
    html_files = list(Path('.').glob('*.html'))
    
    if not html_files:
        print("No HTML files found. Make sure you're in the somerset-american-legion directory.")
        return
    
    updated = 0
    skipped = 0
    
    for filepath in html_files:
        if filepath.name in SKIP_FILES:
            continue
            
        try:
            if update_html_file(filepath):
                print(f"✓ Updated: {filepath.name}")
                updated += 1
            else:
                print(f"- No changes: {filepath.name}")
                skipped += 1
        except Exception as e:
            print(f"✗ Error with {filepath.name}: {e}")
    
    print(f"\nDone! Updated {updated} files, {skipped} unchanged.")

if __name__ == '__main__':
    main()
