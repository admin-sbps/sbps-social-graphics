#!/usr/bin/env python3
"""Second look for the feed: testimonial cards, a "type your teams" how-to,
and a Thanksgiving rivalry program. Light paper and solid color grounds with
a serif display face, so they read differently from the dark slate template.

Usage:
    python3 fresh.py                 # render everything in posts.py
    python3 fresh.py quote-cindy     # render names that start with this

PNGs land in ../../fresh/<name>-<format>.png
"""
import base64
import html
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
FONTS_DIR = HERE.parent / "fonts"
OUT = HERE.parent.parent / "fresh"

SIZES = {"4x5": (1080, 1350), "9x16": (1080, 1920), "2x3": (1000, 1500), "16x9": (1600, 900)}

FONT_FILES = [
    ("Barlow", 500, "normal", "Barlow-500.ttf", "truetype"),
    ("Barlow", 600, "normal", "Barlow-600.ttf", "truetype"),
    ("Barlow", 700, "normal", "Barlow-700.ttf", "truetype"),
    ("Barlow Condensed", 700, "normal", "BarlowCondensed-700.ttf", "truetype"),
    ("Barlow Condensed", 800, "normal", "BarlowCondensed-800.ttf", "truetype"),
    ("DM Serif Display", 400, "normal", "DMSerifDisplay-Regular.woff2", "woff2"),
]


def font_css():
    out = []
    for fam, w, style, f, kind in FONT_FILES:
        b64 = base64.b64encode((FONTS_DIR / f).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{style};"
                   f"src:url(data:font/{kind};base64,{b64}) format('{kind}');}}")
    return "\n".join(out)


FONT_CSS = None
E = html.escape

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--paper:#f5f0e6;--ink:#17171f;--purple:#6366f1;--deep:#312e81;--green:#22c55e;
--forest:#0f3d24;--orange:#ea580c;--muted:#6b6878}
html,body{width:100%;height:100%}
body{font-family:Barlow,sans-serif;-webkit-font-smoothing:antialiased}
.page{position:relative;overflow:hidden;width:100vw;height:100vh;display:flex;flex-direction:column}
.serif{font-family:'DM Serif Display',serif;font-weight:400}
.cond{font-family:'Barlow Condensed',sans-serif;font-weight:800;text-transform:uppercase}
.eyebrow{font-family:'Barlow Condensed';font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:2.6rem}
.url{font-weight:700;font-size:2.7rem;letter-spacing:.01em}
.fine{font-weight:500;font-size:2.1rem;opacity:.75}
"""


def page(fmt, body, css, cls=""):
    w, h = SIZES[fmt]
    land = fmt == "16x9"
    rem = h / 90 if land else min(w / 108, h / 135)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
{BASE_CSS}
html{{font-size:{rem:.3f}px}}
{css}</style></head><body><div class="page f{fmt} {'land' if land else 'port'} {cls}">{body}</div></body></html>"""


# ---------------------------------------------------------------- quote card
QUOTE_THEMES = {
    "forest": dict(bg="#0f3d24", fg="#f5f0e6", mark="#22c55e", sub="#a7d7b8", grid="#22c55e", chip="#22c55e", chipfg="#06210f"),
    "paper": dict(bg="#f5f0e6", fg="#17171f", mark="#6366f1", sub="#6b6878", grid="#6366f1", chip="#6366f1", chipfg="#ffffff"),
    "purple": dict(bg="#4f46e5", fg="#ffffff", mark="#c7d2fe", sub="#dfe3ff", grid="#ffffff", chip="#22c55e", chipfg="#06210f"),
}


def mini_grid(color, filled):
    cells = []
    for i in range(100):
        on = i in filled
        cells.append(f'<i style="background:{color};opacity:{0.95 if on else 0.16}"></i>')
    return f'<div class="mg">{"".join(cells)}</div>'


def quote_card(fmt, q):
    t = QUOTE_THEMES[q["theme"]]
    n = len(q["quote"])
    size = 12 if n < 50 else (9.6 if n < 95 else 8.6)
    if fmt == "16x9":
        size = size * 0.8
    if fmt == "9x16":
        size *= 1.08
    initials = "".join(p[0] for p in q["name"].replace("Coach ", "").split()[:2])
    filled = q.get("filled", [3, 14, 15, 27, 38, 42, 51, 56, 63, 64, 70, 77, 81, 89, 95])
    css = f"""
.page{{background:{t['bg']};color:{t['fg']};padding:9rem 8rem 7rem}}
.f9x16{{padding:22rem 8rem 30rem}}
.mark{{position:absolute;font-family:'DM Serif Display';color:{t['mark']};font-size:46rem;line-height:1;top:-6rem;left:4rem;opacity:.9}}
.f9x16 .mark{{top:7rem}}
.eyebrow{{color:{t['mark']};position:relative;padding-top:11rem}}
.q{{font-family:'DM Serif Display';font-size:{size}rem;line-height:1.08;letter-spacing:-.01em;margin-top:auto;position:relative}}
.who{{display:flex;align-items:center;gap:3rem;margin-top:6rem}}
.av{{width:12rem;height:12rem;border-radius:50%;background:{t['chip']};color:{t['chipfg']};display:flex;align-items:center;justify-content:center;font-family:'Barlow Condensed';font-weight:800;font-size:5rem;flex:none}}
.name{{font-weight:700;font-size:4.2rem;line-height:1.1}}
.team{{font-weight:500;font-size:3.1rem;color:{t['sub']};line-height:1.25}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:4rem}}
.port .who{{margin-bottom:2rem}}
.foot .fine{{margin-top:1rem}}
.mg{{display:grid;grid-template-columns:repeat(10,1fr);gap:.6rem;width:22rem;height:22rem;flex:none;transform:rotate(-6deg)}}
.mg i{{display:block;border-radius:.3rem}}
.land{{flex-direction:row;padding:8rem 9rem;gap:8rem}}
.land .mark{{font-size:44rem;top:-9rem;left:3rem}}
.land .colA{{flex:1.55;display:flex;flex-direction:column}}
.land .colB{{flex:1;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-end;text-align:right}}
.land .q{{margin-top:6rem;margin-bottom:5rem}}
.land .who{{flex-direction:row-reverse;margin-top:0}}
.land .mg{{width:26rem;height:26rem}}
"""
    who = f"""<div class="who"><div class="av">{E(initials)}</div><div><div class="name">{E(q['name'])}</div>
<div class="team">{E(q['team'])}<br>{E(q['place'])}</div></div></div>"""
    foot_txt = f"""<div><div class="url">{E(q.get('url_label', 'SuperBowlPoolSite.com/football-squares-fundraiser'))}</div>
<div class="fine">Free to create. We never touch the money.</div></div>"""
    if fmt == "16x9":
        body = f"""<div class="mark">&ldquo;</div><div class="colA"><div class="eyebrow">{E(q['eyebrow'])}</div>
<div class="q">{E(q['quote'])}</div><div style="margin-top:auto">{foot_txt}</div></div>
<div class="colB">{mini_grid(t['grid'], filled)}{who}</div>"""
    else:
        body = f"""<div class="mark">&ldquo;</div><div class="eyebrow">{E(q['eyebrow'])}</div>
<div class="q">{E(q['quote'])}</div>{who}<div class="foot">{foot_txt}{mini_grid(t['grid'], filled)}</div>"""
    return page(fmt, body, css)


# ------------------------------------------------------------ type your teams
def form_card(fmt, d):
    css = """
.page{background:#eef0fb;color:#17171f;padding:8rem 8rem 6rem;
}
.f9x16{padding:22rem 8rem 30rem}
.eyebrow{color:#6366f1}
h1{font-family:'DM Serif Display';font-weight:400;font-size:10rem;line-height:1;margin-top:2.4rem;letter-spacing:-.01em}
h1 em{font-style:normal;color:#4f46e5}
.lede{font-size:3.5rem;font-weight:500;line-height:1.3;margin-top:3rem;color:#3b3a48;max-width:88rem}
.card{background:#fff;border-radius:1.6rem;box-shadow:0 2.4rem 6rem rgba(23,23,31,.18);overflow:hidden;margin-top:6rem;width:76rem;position:relative}
.card .hd{background:#0b1626;color:#fff;font-weight:600;font-size:3.2rem;padding:3.4rem 4.4rem}
.card .bd{padding:3.6rem 4.4rem 4.4rem}
.lab{font-weight:600;font-size:2.7rem;margin:2.6rem 0 1.4rem}
.lab:first-child{margin-top:0}
.in{border:2px solid #d5dbe5;border-radius:.9rem;padding:1.9rem 2.4rem;font-size:3.2rem;font-weight:500;color:#333;width:62%}
.in.hl{border:3px solid #22c55e;box-shadow:0 0 0 .9rem rgba(34,197,94,.22);font-weight:700;color:#0b1626;width:78%}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end}
.steps{display:flex;gap:2.4rem;font-weight:600;font-size:2.6rem;margin-top:auto;margin-bottom:4rem}
.f2x3 h1{font-size:12rem}.f2x3 .lede{font-size:4rem}.f2x3 .card{width:88rem;margin-top:7rem}.f2x3 .in{font-size:3.6rem}.f2x3 .lab{font-size:3rem}.f2x3 .steps{font-size:2.7rem;gap:2rem}.steps div{white-space:nowrap}
.steps div{display:flex;align-items:center;gap:1.4rem}
.steps b{width:5.4rem;height:5.4rem;border-radius:50%;background:#17171f;color:#fff;display:flex;align-items:center;justify-content:center;font-size:2.8rem;flex:none}
.land{flex-direction:row;gap:7rem;padding:7rem 8rem}
.land .colA{flex:1;display:flex;flex-direction:column}
.land h1{font-size:9rem}
.land .lede{font-size:3.1rem}
.land .card{margin-top:0;width:66rem;align-self:center}
.land .in{font-size:2.9rem;padding:1.6rem 2.2rem}
.land .lab{font-size:2.4rem;margin:2rem 0 1.1rem}
"""
    labels = f"""<div class="lab">Contest Name</div><div class="in">{E(d['contest'])}</div>
<div class="lab">Top Team Label</div><div class="in hl">{E(d['top'])}</div>
<div class="lab">Left Team Label</div><div class="in hl">{E(d['left'])}</div>"""
    card = f"""<div class="card"><div class="hd">Basic Details</div><div class="bd">{labels}</div></div>"""
    foot = f"""<div class="foot"><div><div class="url">{E(d.get('url_label', 'SuperBowlPoolSite.com/thx'))}</div>
<div class="fine">Free to create. We never touch the money.</div></div></div>"""
    steps = """<div class="steps"><div><b>1</b>Create your contest</div><div><b>2</b>Open Basic Details</div><div><b>3</b>Type both teams</div></div>"""
    if fmt == "16x9":
        body = f"""<div class="colA"><div class="eyebrow">{E(d['eyebrow'])}</div><h1>{d['title']}</h1>
<div class="lede">{E(d['lede'])}</div><div style="margin-top:auto">{foot}</div></div>
<div style="position:relative;display:flex;align-items:center">{card}</div>"""
    else:
        body = f"""<div class="eyebrow">{E(d['eyebrow'])}</div><h1>{d['title']}</h1>
<div class="lede">{E(d['lede'])}</div>
<div style="position:relative">{card}</div>
{steps if fmt != '2x3' else steps}{foot}"""
    return page(fmt, body, css)


# ------------------------------------------------------------ rivalry program
PROGRAM_CSS = """
.page{background:#f4efe4;color:#17171f;padding:0}
.band{background:#17171f;color:#f4efe4;padding:7rem 7rem 5rem;position:relative}
.f9x16 .band{padding-top:20rem}
.band .eyebrow{color:#f59e0b;font-size:2.4rem}
.band h2{font-family:'Barlow Condensed';font-weight:800;text-transform:uppercase;font-size:11rem;line-height:.9;margin-top:1.6rem;letter-spacing:.005em}
.band .tag{font-family:'DM Serif Display';font-size:4rem;color:#c7c2b6;margin-top:1.4rem}
.band .count{position:absolute;right:7rem;bottom:5rem;text-align:right;font-family:'Barlow Condensed';font-weight:700;font-size:2.6rem;letter-spacing:.2em;color:#c7c2b6}
.band .count b{display:block;font-size:12rem;line-height:.85;letter-spacing:0;color:#f4efe4}
.rows{padding:3rem 7rem 0;position:relative}
.row{display:flex;align-items:baseline;justify-content:space-between;gap:2rem;border-bottom:2px solid rgba(23,23,31,.14);padding:2.05rem 0}
.row .m{font-family:'DM Serif Display';font-size:4.15rem;line-height:1.05}
.row .m i{font-style:normal;color:#ea580c;font-size:.8em;padding:0 .9rem}
.row .n{font-family:'Barlow Condensed';font-weight:700;text-transform:uppercase;letter-spacing:.12em;font-size:2.2rem;color:#4f46e5;white-space:nowrap}
.sub{font-family:'Barlow Condensed';font-weight:800;text-transform:uppercase;letter-spacing:.18em;font-size:2.6rem;color:#ea580c;margin:3.4rem 0 .4rem}
.pfoot{margin-top:auto;padding:0 7rem 5.5rem;display:flex;justify-content:space-between;align-items:flex-end;position:relative}
.f9x16 .pfoot{padding-bottom:28rem}
.pfoot .fine{font-size:2rem}
.pg{font-family:'Barlow Condensed';font-weight:700;letter-spacing:.2em;font-size:2.4rem;color:#6b6878}
"""


def rows_html(rows):
    out = []
    for r in rows:
        if isinstance(r, str):
            out.append(f'<div class="sub">{E(r)}</div>')
            continue
        a, b, note = (r + ("",))[:3]
        out.append(f'<div class="row"><div class="m">{E(a)}<i>vs.</i>{E(b)}</div><div class="n">{E(note)}</div></div>')
    return "".join(out)


def program_list(fmt, d):
    css = PROGRAM_CSS + d.get("css", "")
    body = f"""<div class="band"><div class="eyebrow">{E(d['eyebrow'])}</div><h2>{d['title']}</h2>
<div class="tag">{E(d.get('tag', ''))}</div>
{f'<div class="count"><b>{d["count"]}</b>GAMES</div>' if d.get('count') else ''}</div>
<div class="rows">{rows_html(d['rows'])}</div>
<div class="pfoot"><div><div class="url">{E(d.get('url_label', 'SuperBowlPoolSite.com/thx'))}</div>
<div class="fine">{E(d.get('fine', 'Rivalry list for Thanksgiving week. Check your school for kickoff times.'))}</div></div>
<div class="pg">{E(d.get('page', ''))}</div></div>"""
    return page(fmt, body, css)


def program_cover(fmt, d):
    css = PROGRAM_CSS + """
.cover{flex:1;display:flex;flex-direction:column;padding:9rem 8rem 6rem;position:relative}
.f9x16 .cover{padding:22rem 8rem 28rem}
.tk{border:3px solid #17171f;border-radius:1.4rem;padding:1.6rem 2.6rem;align-self:flex-start;font-family:'Barlow Condensed';font-weight:700;letter-spacing:.24em;font-size:2.6rem;text-transform:uppercase}
.big{font-family:'DM Serif Display';font-size:15rem;line-height:.92;margin-top:5rem;letter-spacing:-.015em}
.big em{color:#ea580c;font-style:normal}
.lede{font-size:3.8rem;font-weight:500;line-height:1.3;margin-top:4.5rem;max-width:84rem;color:#3b3a48}
.states{display:flex;gap:1.6rem;flex-wrap:wrap;margin-top:6rem}
.states span{background:#17171f;color:#f4efe4;font-family:'Barlow Condensed';font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:2.7rem;padding:1.3rem 2.4rem;border-radius:99px}
.swipe{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end}
.swipe .hand{font-family:'Barlow Condensed';font-weight:700;letter-spacing:.24em;text-transform:uppercase;font-size:2.6rem;color:#4f46e5}
"""
    body = f"""<div class="cover"><div class="tk">{E(d['ticket'])}</div><div class="big">{d['title']}</div>
<div class="lede">{E(d['lede'])}</div><div class="states">{''.join(f'<span>{E(s)}</span>' for s in d['states'])}</div>
<div class="swipe"><div><div class="url">{E(d.get('url_label', 'SuperBowlPoolSite.com/thx'))}</div></div><div class="hand">{E(d.get('hand', ''))}</div></div></div>"""
    return page(fmt, body, css)


def cta_card(fmt, d):
    css = """
.page{background:#17171f;color:#f4efe4;padding:9rem 8rem 7rem}
.f9x16{padding:22rem 8rem 30rem}
.eyebrow{color:#f59e0b}
.big{font-family:'DM Serif Display';font-size:12.5rem;line-height:.95;margin-top:3rem;letter-spacing:-.01em}
.big em{color:#22c55e;font-style:normal}
.split{display:flex;margin-top:7rem;border-radius:1.6rem;overflow:hidden;font-family:'Barlow Condensed';font-weight:800;text-transform:uppercase}
.split div{flex:1;padding:4rem 3.6rem}
.split .a{background:#6366f1;color:#fff}.split .b{background:#22c55e;color:#06210f}
.split b{display:block;font-size:9rem;line-height:.9}
.split span{font-size:3rem;letter-spacing:.08em}
.lede{font-size:3.6rem;font-weight:500;line-height:1.35;margin-top:5rem;color:#d8d3c8}
.go{margin-top:auto;background:#f4efe4;color:#17171f;border-radius:1.6rem;padding:3.6rem 4rem}
.go .url{font-size:3.4rem}
.go .fine{opacity:.7;margin-top:.6rem}
"""
    body = f"""<div class="eyebrow">{E(d['eyebrow'])}</div><div class="big">{d['title']}</div>
<div class="split"><div class="a"><b>50%</b><span>to the winning square</span></div><div class="b"><b>50%</b><span>{E(d['cause'])}</span></div></div>
<div class="lede">{E(d['lede'])}</div>
<div class="go"><div class="url">{E(d['url_label'])}</div><div class="fine">Free to create and share. We never touch the money.</div></div>"""
    return page(fmt, body, css)


KINDS = {"quote": quote_card, "form": form_card, "program": program_list, "cover": program_cover, "cta": cta_card}


def main():
    global FONT_CSS
    FONT_CSS = font_css()
    sys.path.insert(0, str(HERE))
    from posts import POSTS
    pick = sys.argv[1:]
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        for name, kind, fmts, data in POSTS:
            if pick and not any(name.startswith(x) for x in pick):
                continue
            for fmt in fmts:
                w, h = SIZES[fmt]
                pg = b.new_page(viewport={"width": w, "height": h})
                pg.set_content(KINDS[kind](fmt, data))
                pg.evaluate("document.fonts.ready")
                over = pg.evaluate("""() => { const p=document.querySelector('.page');
                  return [...p.querySelectorAll('*')].some(e => { const r=e.getBoundingClientRect();
                  return r.bottom > innerHeight + 1 || r.right > innerWidth + 1; }) }""")
                out = OUT / f"{name}-{fmt}.png"
                pg.screenshot(path=str(out))
                print(out.name, "  WARNING overflow" if over else "")
                pg.close()
        b.close()


if __name__ == "__main__":
    main()
