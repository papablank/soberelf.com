#!/usr/bin/env python3
"""Builds soberelf.com/day/1 ... /day/28 for GitHub Pages.

Edit the VIDEOS list below, then run:  python3 make_days.py
It writes a  day/  folder next to this script. Copy that folder into the root
of your soberelf.com repo, commit, and push.

- A day with a YouTube link forwards straight to that video.
- A day left as "" shows a calm "coming soon" page instead.
- No analytics, no trackers, no outside fonts or scripts: nothing on these
  pages can identify who scanned a QR code.
"""
import html, os

PLAYLIST = ""   # paste the "Clean For Today — Days 1–28" playlist link here when it exists

# (title, YouTube link). Paste each link as you publish. Leave "" until then.
VIDEOS = [
    ("Gloves Down", ""),
    ("Forever Is Too Heavy", ""),
    ("The Chair", ""),
    ("The Heaviest Phone", ""),
    ("Clean Isn't Numb", ""),
    ("Small Things", ""),
    ("Still Here", ""),
    ("Wreckage", ""),
    ("Hope", ""),
    ("Letting Go", ""),
    ("Just One", ""),
    ("It Passes", ""),
    ("Open Mind", ""),
    ("Willing", ""),
    ("Halt", ""),
    ("The Tape", ""),
    ("Fear", ""),
    ("The Coffee", ""),
    ("Alone", ""),
    ("Old Roads", ""),
    ("Progress", ""),
    ("Shame", ""),
    ("The Mirror", ""),
    ("The Plan", ""),
    ("Earning It Back", ""),
    ("Saturday Night", ""),
    ("Grateful Anyway", ""),
    ("Pass It On", ""),
]

CSS = """
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
  background:#f4f3f1;color:#1d1d1d;font-family:Georgia,'Times New Roman',serif;padding:28px}
main{max-width:30rem;width:100%}
.tag{display:inline-block;background:#ffd21f;color:#111;font:700 .95rem/1 'Arial Narrow',Arial,sans-serif;
  letter-spacing:.04em;text-transform:uppercase;padding:.45rem .6rem}
h1{color:#6e1414;font:700 2.6rem/1 'Arial Narrow',Arial,sans-serif;text-transform:uppercase;margin:.6rem 0 1rem}
p{font-size:1.15rem;line-height:1.55;margin:0 0 1rem}
a{color:#6e1414}
.btn{display:inline-block;background:#6e1414;color:#fff;text-decoration:none;font:600 1.05rem/1 Arial,sans-serif;
  padding:.9rem 1.2rem;border-radius:4px;margin:.4rem 0 1.2rem}
.help{border-left:4px solid #ffd21f;background:#fff;padding:.8rem 1rem;font-size:1rem}
small{display:block;color:#777;margin-top:1.6rem;font:.8rem/1.4 Arial,sans-serif}
ol{padding-left:1.4rem;font-size:1.05rem;line-height:1.7}
"""

HELP = ('<p class="help"><strong>If a feeling includes wanting to die or hurt yourself, that is an emergency.</strong> '
        'Tell someone now, or call or text <a href="tel:988">988</a>.</p>')
FOOT = '<small>Clean For Today · Sober Elf Studio LLC · soberelf.com</small>'

def page(title, head_extra, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="referrer" content="no-referrer">
<title>{html.escape(title)}</title>
{head_extra}<style>{CSS}</style>
</head>
<body><main>
{body}
</main></body>
</html>
"""

def day_page(n, title, url):
    label = f"Day {n}: {title}"
    if url:
        u = html.escape(url, quote=True)
        head = (f'<meta http-equiv="refresh" content="0; url={u}">\n'
                f'<script>location.replace({url!r});</script>\n')
        body = (f'<span class="tag">Day {n}</span>\n<h1>{html.escape(title)}</h1>\n'
                f'<p>Taking you to today\'s video…</p>\n'
                f'<a class="btn" href="{u}">Watch Day {n}</a>\n{HELP}\n{FOOT}')
    else:
        head = ''
        body = (f'<span class="tag">Day {n}</span>\n<h1>{html.escape(title)}</h1>\n'
                f'<p>This video isn\'t up yet. Today\'s page in your booklet says everything it will say.</p>\n'
                f'<p>Read it. Then stay through today.</p>\n'
                f'<a class="btn" href="/day/">See all 28 days</a>\n{HELP}\n{FOOT}')
    return page(f"{label} · Clean For Today", head, body)

def index_page():
    items = []
    for n, (title, url) in enumerate(VIDEOS, 1):
        items.append(f'<li><a href="/day/{n}/">{html.escape(title)}</a>{"" if url else " <em>(coming soon)</em>"}</li>')
    pl = (f'<a class="btn" href="{html.escape(PLAYLIST, quote=True)}">Watch all 28 in order</a>\n' if PLAYLIST else '')
    body = (f'<span class="tag">Your first 28 days</span>\n<h1>Clean For Today</h1>\n'
            f'<p>From people who\'ve sat where you\'re sitting. One page a day, in any order.</p>\n'
            f'{pl}<ol>\n' + "\n".join(items) + f'\n</ol>\n{HELP}\n{FOOT}')
    return page("Clean For Today · All 28 days", '', body)

if __name__ == "__main__":
    assert len(VIDEOS) == 28
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day")
    os.makedirs(root, exist_ok=True)
    with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page())
    for n, (title, url) in enumerate(VIDEOS, 1):
        d = os.path.join(root, str(n)); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(day_page(n, title, url))
    live = sum(1 for _, u in VIDEOS if u)
    print(f"Wrote day/index.html and day/1–28. {live} forward to a video, {28 - live} show 'coming soon'.")
