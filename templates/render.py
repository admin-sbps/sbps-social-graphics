#!/usr/bin/env python3
"""Render SuperBowlPoolSite graphics from a JSON data file.

Usage:
    python3 render.py data/winners-2026-10-04.json            # all formats
    python3 render.py data/slate-nfl-week6.json --formats 4x5  # one format

PNG files land in renders/<data file name>-<format>.png.
Needs Python 3 and Playwright:
    pip install playwright && playwright install chromium
If Playwright's own browser is missing it falls back to an installed
Chrome or Chromium (set CHROME=/path/to/chrome to choose one).
"""
import argparse
import base64
import json
import os
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
FORMATS = {
    "4x5": (1080, 1350),   # Instagram and Facebook feed
    "9x16": (1080, 1920),  # Stories, Reels, TikTok
    "2x3": (1000, 1500),   # Pinterest
    "16x9": (1600, 900),   # X (Twitter) in-feed image
}
# Design width in CSS pixels. Portrait formats are laid out at 1080 and
# scaled; the landscape X card has its own two-column layout at 1600.
DESIGN_WIDTH = {"16x9": 1600}
FONTS = [
    ("Barlow", 500), ("Barlow", 600), ("Barlow", 700),
    ("Barlow Condensed", 600), ("Barlow Condensed", 700), ("Barlow Condensed", 800),
]


def find_chrome():
    candidates = [
        os.environ.get("CHROME"),
        "/opt/pw-browsers/chromium",
        shutil.which("chromium"), shutil.which("chromium-browser"),
        shutil.which("google-chrome"), shutil.which("google-chrome-stable"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    sys.exit("Chrome or Chromium not found. Set CHROME=/path/to/chrome")


def font_css():
    out = []
    for family, weight in FONTS:
        path = HERE / "fonts" / f"{family.replace(' ', '')}-{weight}.ttf"
        b64 = base64.b64encode(path.read_bytes()).decode()
        out.append(
            f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"src:url(data:font/ttf;base64,{b64}) format('truetype');}}"
        )
    return "\n".join(out)


def embed_art(data):
    # Artframe graphics wrap an existing picture; inline it so the page needs no files.
    art = data.get("art")
    if art and not art.startswith("data:"):
        path = HERE / art
        mime = "image/png" if path.suffix == ".png" else "image/jpeg"
        data = dict(data, art=f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}")
    return data


def build_html(data, fmt, width, height):
    # Pinterest is 1000 wide; scale the 1080 design down so sizes stay consistent.
    zoom = width / DESIGN_WIDTH.get(fmt, 1080)
    data = embed_art(data)
    css = (HERE / "base.css").read_text()
    js = (HERE / "templates.js").read_text()
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{font_css()}\n{css}\nhtml{{zoom:{zoom}}}
.page{{width:{round(width / zoom)}px;height:{round(height / zoom)}px}}</style></head>
<body><div class="page" id="page"></div>
<script>window.DATA = {json.dumps(data)}; window.FORMAT = "{fmt}";</script>
<script>{js}</script></body></html>"""


def launch(p):
    try:
        return p.chromium.launch()
    except Exception:
        # Fall back to any Chrome or Chromium already on the machine.
        return p.chromium.launch(executable_path=find_chrome())


def render(data_path, formats, browser, out_dir=None):
    data = json.loads(Path(data_path).read_text())
    # A data file can name its own formats, e.g. a Pinterest-only pin.
    formats = formats or data.get("formats") or list(FORMATS)
    out_dir = Path(out_dir) if out_dir else HERE / "renders"
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(data_path).stem
    for fmt in formats:
        width, height = FORMATS[fmt]
        page = browser.new_page(viewport={"width": width, "height": height})
        page.set_content(build_html(data, fmt, width, height))
        page.evaluate("document.fonts.ready")
        out = out_dir / f"{stem}-{fmt}.png"
        page.screenshot(path=str(out))
        warn = ""
        if page.title() == "OVERFLOW":
            warn = "  WARNING: content does not fit, shorten text or remove a game"
        print(f"{out}{warn}")
        page.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data", nargs="+", help="JSON data file(s)")
    ap.add_argument("--formats", help="comma list, default: the data file's formats or all")
    ap.add_argument("--out", help="output folder, default renders/")
    args = ap.parse_args()
    with sync_playwright() as p:
        browser = launch(p)
        for d in args.data:
            render(d, args.formats.split(",") if args.formats else None, browser, args.out)
        browser.close()


if __name__ == "__main__":
    main()
