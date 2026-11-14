#!/usr/bin/env python3
"""Builds the main soberelf.com pages from the Site Blueprint (Nov 13, 2026).

Run: python3 make_site.py
Writes: index.html, counselors/, booklet/, studio/, about/
Does NOT touch /day/ (QR pages, see DAY-PAGES.md) or /dave/ (hand-edited).
No analytics, trackers, cookies or outside fonts. Keep it that way.
"""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "thesoberelf@gmail.com"
PHONE = "715-622-0011"
PHONE_TEL = "+17156220011"

NAV = [("/counselors/", "For Counselors"), ("/booklet/", "Free PDF"),
       ("/dave/", "Dave's Story"), ("/studio/", "Studio"), ("/about/", "About")]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/dm-serif-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<title>{title}</title>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def top(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap">
<a class="logo" href="/"><img src="/sober-elf-typeface.png" alt="sober elf, home" width="230" height="46"></a>
<nav aria-label="Main">{links}</nav>
</div></header>
<main id="main">
"""


FOOT = f"""</main>
<footer><div class="wrap">
<p class="help"><strong>If a feeling includes wanting to die or hurt yourself, that is an emergency.</strong> Tell someone now, or call or text <a href="tel:988">988</a>.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="/day/">Days 1 to 28</a></p>
<p class="fine">Clean For Today is an independent project of Sober Elf Studio LLC. It is not affiliated with or endorsed by any twelve-step fellowship or treatment facility. It is not medical advice or a substitute for your care team.</p>
<p class="fine">© 2026 Sober Elf Studio LLC · soberelf.com</p>
</div></footer>
</body>
</html>
"""


def page(path, current, title, desc, body):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head(title, desc) + top(current) + body + FOOT, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


HOME = """<section class="hero"><div class="wrap">
<p class="label">Clean For Today: Your First 28 Days</p>
<h1>Something to read when the unit goes quiet.</h1>
<p class="lead">A pocket booklet of 28 one-page reflections for people in inpatient treatment. It works without a phone or a screen, and each day is being made into a short animated video so it keeps working after discharge.</p>
<div class="btns"><a class="btn main" href="/counselors/">For Counselors</a><a class="btn alt" href="/booklet/">Get the free PDF</a></div>
</div></section>

<section><div class="wrap">
<p class="label">Written from the chair</p>
<p class="quote">"I've sat in that chair six times. The first five times, I thought I was the exception. Three of those times, I walked out before it was over."</p>
<p class="sig">Dave B.</p>
</div></section>

<section><div class="wrap">
<p class="label">Built for the unit</p>
<h2>One page a day. No screen needed.</h2>
<ul class="plain">
<li>No phone or screen needed. One page a day, about two minutes to read.</li>
<li>The "Before You Walk Out" page asks the reader to wait an hour and tell a person before they leave.</li>
<li>Each day is read by a different person in recovery. Day 1 is recorded, and ten more readers have agreed to record.</li>
</ul>
</div></section>

<section><div class="wrap two">
<a class="card" href="/dave/"><img src="/img/dave/daves_story_ep01_thumb.jpg" alt="Dave's Story, Episode 1"><div class="body"><h3>Dave's Story</h3><p>A 7-part animated series with an original score by Aaron Scharmer. Five episodes are out.</p></div></a>
<a class="card" href="/studio/"><img src="/img/cft-card.jpg" alt="Clean For Today puppets, side by side"><div class="body"><h3>Studio</h3><p>We also make video, animation, websites and logos for treatment programs, recovery organizations and independent artists.</p></div></a>
</div></section>

<section><div class="wrap">
<p class="label">Coming 2027</p>
<p class="lead">A one-hour documentary on addiction and the brain, weaving its biology with the spiritual healing of 12-step recovery.</p>
</div></section>
"""

COUNSELORS = f"""<section class="hero"><div class="wrap">
<p class="label">For counselors</p>
<h1>If the answer is no, or not yet, I still want your notes.</h1>
<p class="lead">Clean For Today is 28 one-page reflections for your patients' first weeks. I'm asking counselors to read it before anyone else does.</p>
<div class="btns"><a class="btn main" href="#request">Request a proof</a></div>
</div></section>

<section><div class="wrap two">
<div><p class="label">What I'm asking</p>
<ul class="plain"><li>Read the proof and mark it up.</li><li>Tell us honestly if it's worth trying with a few patients.</li><li>Point us to whoever would approve a small pilot.</li></ul></div>
<div><p class="label">What I'm not asking for</p>
<ul class="plain"><li>Money, now or later.</li><li>An endorsement of me, the booklet, or any fellowship.</li><li>Patient names, stories, photos, or any information about who is in treatment.</li><li>Permission to use the center's name, unless the center gives it in writing.</li></ul></div>
</div></section>

<section><div class="wrap">
<p class="label">Look inside</p>
<h2>Three days from the booklet</h2>
<div class="grid">
<figure class="card page" style="margin:0"><img src="/img/look/day1.jpg" alt="Booklet page, Day 1: Gloves Down" loading="lazy"><figcaption class="body"><p>Day 1: where every stay starts.</p></figcaption></figure>
<figure class="card page" style="margin:0"><img src="/img/look/day4.jpg" alt="Booklet page, Day 4: The Longest Hallway" loading="lazy"><figcaption class="body"><p>Day 4: sends the reader to the nurses' station.</p></figcaption></figure>
<figure class="card page" style="margin:0"><img src="/img/look/day24.jpg" alt="Booklet page, Day 24: The Plan" loading="lazy"><figcaption class="body"><p>Day 24: the reader writes a plan for the first days after discharge and goes over it with their counselor.</p></figcaption></figure>
</div>
</div></section>

<section><div class="wrap">
<p class="label">How it works on the unit</p>
<p>One page a day, about two minutes to read, no phone needed. The days can stand alone, so a reader can start anywhere, skip ahead, or take the rest home.</p>
<p class="label" style="margin-top:28px">Where it stands</p>
<p>No licensed clinician has reviewed it yet. That's why it comes to you first.</p>
<p class="quote">"I'll make every change you ask for. If you'd cut a page, it's cut."</p>
</div></section>

<section><div class="wrap">
<p class="label">How a pilot works</p>
<p class="lead">"Nothing happens without your OK, and you can stop it at any step."</p>
<ol class="steps">
<li>"You review the proof, on whatever timeline works for you."</li>
<li>"I make your changes and bring back a clean copy."</li>
<li>"The center gives written permission, from whoever needs to approve it. A short letter is enough, and it protects you."</li>
<li>"I print 10–30 copies at no cost to the center, with your readmission number on the walk-out page."</li>
<li>"You hand them out to whoever you think it would help."</li>
<li>"Feedback stays anonymous. An optional tear-out card on the last page asks two questions: 'Which day helped most?' and 'Which page did you read twice?' Staff collect the cards. There are no fields for names, dates or initials."</li>
<li>"We talk afterward and decide together whether to keep going, change it, or stop."</li>
</ol>
</div></section>

<section><div class="wrap">
<p class="label">For your program director</p>
<p>A one-page summary to hand to whoever approves patient materials.</p>
<div class="btns"><a class="btn alt" href="/counselors/CFT_Program_Director_OnePager.pdf" download>Download the one-pager</a></div>
</div></section>

<section id="request"><div class="wrap">
<p class="label">Request a proof</p>
<h2>Tell me what would help</h2>
<form class="box" action="mailto:{EMAIL}?subject=Clean%20For%20Today%20request" method="post" enctype="text/plain">
<label>Name<input name="Name" autocomplete="name" required></label>
<label>Role<input name="Role" placeholder="AODA counselor"></label>
<label>Email or phone<input name="Contact" required></label>
<label>What would help?<select name="Request"><option>Send me a proof</option><option>Talk about a pilot</option><option>Just the free PDF</option></select></label>
<p class="note">Please don't include anything about patients.</p>
<button class="btn main" type="submit">Send</button>
<p class="note">Sending opens your email app with this message filled in. Or write to <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
</form>
</div></section>
"""

BOOKLET = """<section class="hero"><div class="wrap">
<p class="label">Free PDF</p>
<h1>The whole booklet, free to download.</h1>
<p class="lead">Clean For Today: Your First 28 Days. All 28 pages, free for anyone in recovery who wants a copy for themselves.</p>
<div class="btns"><a class="btn main" href="/booklet/CFT_Booklet_28_Days_r23.pdf" download>Download the free PDF</a></div>
<p class="note" style="margin-top:12px">PDF, about 13 MB</p>
</div></section>

<section><div class="wrap">
<p class="label">Running a facility?</p>
<p>For printed packs, or a version with your readmission number on the back, see <a href="/counselors/">For Counselors</a>.</p>
</div></section>

<section><div class="wrap">
<p class="label">Watch along</p>
<p>Every day has its own page at soberelf.com/day. The videos are being made, and each one shows up there when it's ready.</p>
<div class="btns"><a class="btn alt" href="/day/">See all 28 days</a></div>
</div></section>

<section><div class="wrap">
<p class="label">Rights</p>
<p>Free to download for your own use. © 2026 Sober Elf Studio LLC. All rights reserved.</p>
</div></section>
"""

STUDIO = f"""<section class="hero"><div class="wrap">
<p class="label">Studio</p>
<h1>The studio behind Clean For Today and Dave's Story.</h1>
<p class="lead">Now taking on work for recovery organizations, treatment programs and independent artists.</p>
<div class="btns"><a class="btn main" href="#start">Start a project</a></div>
</div></section>

<section><div class="wrap">
<p class="label">What we make</p>
<p class="lead">Video editing (Adobe Premiere Pro), motion graphics, character animation, websites, logos and graphics.</p>
</div></section>

<section><div class="wrap">
<p class="label">Work</p>
<div class="grid">
<a class="card" href="/dave/"><img src="/img/dave/daves_story_ep01_thumb.jpg" alt="Dave's Story, Episode 1" loading="lazy"><div class="body"><h3>Dave's Story</h3><p>Animated series, 5 of 7 episodes out, original score by Aaron Scharmer.</p></div></a>
<div class="card"><img src="/img/cft-card.jpg" alt="Clean For Today puppets, side by side" loading="lazy"><div class="body"><h3>Clean For Today</h3><p>28 animated daily reflections, in production.</p></div></div>
<div class="card"><div class="photo" style="border:0;border-radius:0">Aaron Scharmer Music</div><div class="body"><h3>Aaron Scharmer Music</h3><p>Website and logo, in progress.</p></div></div>
</div>
</div></section>

<section id="start"><div class="wrap">
<p class="label">Start a project</p>
<h2>What do you need?</h2>
<form class="box" action="mailto:{EMAIL}?subject=Studio%20project" method="post" enctype="text/plain">
<label>Name<input name="Name" autocomplete="name" required></label>
<label>Email<input name="Email" type="email" autocomplete="email" required></label>
<label>Organization<input name="Organization" autocomplete="organization"></label>
<label>What do you need?<textarea name="Project"></textarea></label>
<button class="btn main" type="submit">Send</button>
<p class="note">Sending opens your email app with this message filled in. Or write to <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
</form>
</div></section>
"""

ABOUT = """<section class="hero"><div class="wrap two" style="align-items:center">
<div><p class="label">About</p>
<h1>"I've sat where you're sitting. Six times."</h1>
<p class="sig">Dave B.</p></div>
<img src="/img/dave/daves_story_ep02_thumb.jpg" alt="Dave's Story animation still" style="width:100%;border-radius:6px;border:1px solid rgba(138,101,69,.35)">
</div></section>

<section><div class="wrap">
<p class="quote">"It took me six inpatient rehabs, two overdoses that almost killed me, and a prison sentence. The first five times, I thought I was the exception. Three of those times, I walked out before it was over. My addiction had a story for every occasion, and I believed every one. The sixth time, I came in from a tent along the highway in Oregon. I'd lost custody of my son, my marriage, my career, and every dollar I'd ever made. The rehab didn't change the sixth time. I did. I stopped doing it my way, and I let people help me."</p>
<p class="note">From the foreword to Clean For Today</p>
</div></section>

<section><div class="wrap">
<p class="label">Why I made this</p>
<p class="quote">"What I needed in those first nights was something short, plain and honest, from someone who had been there, to read when the unit went quiet and my head got loud."</p>
<p>The long version is Dave's Story.</p>
<div class="btns"><a class="btn alt" href="/dave/">Watch Dave's Story</a></div>
</div></section>

<section><div class="wrap two">
<div><p class="label">Who makes it</p>
<p><strong>Dave B.</strong>, Director. Writing, voice, editing, animation, VFX and production.</p>
<p><strong>Aaron Scharmer</strong>, Composer. Scores Dave's Story and Clean For Today.</p></div>
<div><p class="label">What we stand for</p>
<dl class="values"><dt>Honest</dt><dd>We tell the truth about addiction, about ourselves, and about what the work has and hasn't earned.</dd>
<dt>Open-minded</dt><dd>We take the hard notes, from counselors, critics and newcomers, and change the work.</dd>
<dt>Willing</dt><dd>We do the next right thing before we feel ready.</dd></dl></div>
</div></section>

<section><div class="wrap">
<p class="label">What we don't do</p>
<ul class="plain"><li>We don't speak for, or claim affiliation with, any twelve-step fellowship.</li><li>We don't give medical advice or replace a patient's care team.</li><li>We don't collect information on anyone in treatment.</li><li>We don't use a facility's name without its written permission.</li></ul>
<div class="btns"><a class="btn main" href="/counselors/">For Counselors</a></div>
</div></section>
"""

EPISODES = [  # (number, title, length, YouTube id, thumbnail)
    (1, "The Exception", "0:43", "WsrGWYxnHoQ", "/img/dave/daves_story_ep01_thumb.jpg"),
    (2, "The Golden Boy", "2:16", "rWHAB5nlIWU", "/img/dave/daves_story_ep02_thumb.jpg"),
    (3, "The Career", "1:52", "mSqkOI--yGs", "/img/dave/daves_story_ep03_thumb.jpg"),
    (4, "The Message", "1:55", "JuuJgM8pEZA", "/img/dave/daves_story_ep04_thumb.jpg"),
    (5, "The Clean Time", "", "SBGQN-KArFY", ""),  # add length and a local thumbnail when ready
]


def dave_body():
    def card(n, t, ln, vid, img):
        pic = (f'<img src="{img}" alt="" loading="lazy">' if img else
               f'<span class="photo" style="border:0;border-radius:0;font-family:DM Serif Display,Georgia,serif;font-size:1.6rem">Episode {n}</span>')
        name = f"Episode {n}: {t}" if t else f"Episode {n}"
        meta = f"{ln} · Original series" if ln else "Original series"
        return (f'<button class="card ep" type="button" data-id="{vid}" style="padding:0;text-align:left;font:inherit;cursor:pointer;width:100%">'
                f'{pic}<span class="body" style="display:block"><h3>{name}</h3><p>{meta}</p></span></button>')
    cards = "".join(card(*e) for e in EPISODES)
    return f"""<section class="hero"><div class="wrap">
<p class="label">An original animated series</p>
<h1>Dave's Story</h1>
<p class="lead">He was born to be exceptional. His addiction had other plans. A seven-part story of addiction and recovery.</p>
</div></section>

<section><div class="wrap">
<p class="label">Episodes · 5 of 7 out</p>
<div class="grid">{cards}</div>
<p class="muted" style="margin-top:22px">Episodes 6 and 7 coming soon. Original music by Aaron Scharmer.</p>
<div class="btns"><a class="btn alt" href="https://youtube.com/@SoberElf?sub_confirmation=1" target="_blank" rel="noopener">Subscribe on YouTube</a></div>
</div></section>

<dialog id="player" style="width:min(860px,94vw);padding:0;border:1px solid var(--oak);background:var(--deep)">
<form method="dialog" style="display:flex;justify-content:flex-end"><button class="btn alt" style="min-height:44px;border:0">Close</button></form>
<div style="position:relative;padding-top:56.25%"><iframe id="frame" title="Dave's Story episode" style="position:absolute;inset:0;width:100%;height:100%;border:0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>
</dialog>
<script>
const d=document.getElementById('player'),f=document.getElementById('frame');
document.querySelectorAll('.ep').forEach(b=>b.addEventListener('click',()=>{{f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1';d.showModal();}}));
d.addEventListener('close',()=>{{f.src='';}});
</script>
"""


if __name__ == "__main__":
    page("dave/index.html", "/dave/", "Dave's Story · Sober Elf Studio",
         "Dave's Story, a seven-part animated series about addiction and recovery.", dave_body())
    page("index.html", "/", "Sober Elf Studio · Clean For Today",
         "Clean For Today: a pocket booklet of 28 one-page reflections for people in inpatient treatment, from Sober Elf Studio.", HOME)
    page("counselors/index.html", "/counselors/", "For Counselors · Sober Elf Studio",
         "Read the Clean For Today proof, mark it up, and tell us if it's worth trying with a few patients.", COUNSELORS)
    page("booklet/index.html", "/booklet/", "Free PDF · Clean For Today",
         "Download Clean For Today: Your First 28 Days, free for your own use.", BOOKLET)
    page("studio/index.html", "/studio/", "Studio · Sober Elf Studio",
         "Video editing, motion graphics, character animation, websites, logos and graphics.", STUDIO)
    page("about/index.html", "/about/", "About · Sober Elf Studio",
         "Dave B. and the people behind Clean For Today and Dave's Story.", ABOUT)
