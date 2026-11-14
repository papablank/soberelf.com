#!/usr/bin/env python3
"""Builds soberelf.com/day/1 ... /day/28 for GitHub Pages.

Edit the VIDEOS list below, then run:  python3 make_days.py
It writes a  day/  folder next to this script. Copy that folder into the root
of your soberelf.com repo, commit, and push.

- Every day page shows that day's reflection, written out.
- A day with a YouTube link also gets a Watch button for the video.
- A day left as "" says the video is coming soon.
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

# Each day's reflection (CFT: Online r18, 2026-11-14). Each string is one paragraph.
SCRIPTS = [["Nobody walks into recovery proud. We get here beaten. Out of tricks. Out of excuses. Out of people who still believe what we say.", "But here's the good news: admitting we're powerless over our addiction isn't losing the fight. It's finally seeing the fight was rigged. For years we were swinging at something that never got tired, never slept, never missed a chance. Today we get to put the gloves down.", "We don't have to win. We just have to quit lying about who's been winning. That honesty feels like defeat at first. It isn't. It's the first solid ground we've stood on in a long time. Today, we tell the truth about it. And we stay clean while we do."],
    ["The disease of addiction loves big numbers. Never again. The rest of your life. Forever. The disease hands us forever like a weight that's too heavy to lift, and laughs at us when we drop it.", "We don't carry forever. We carry today. Today has edges. It has a morning and a night and a pillow at the end. We can stay clean from here to that pillow. Nobody in the rooms got years of clean time by staring at years. They got them the same way we get this one: one day stacked against another. Most of those days were ordinary. Some of them were ugly. Every one of them was enough.", "So put forever down. Nobody can lift it. We pick up today. It fits in our hands."],
    ["Somewhere tonight there's a folding chair with nobody in it yet. A warm cup of coffee. A few friendly faces. A room that smells like second chances.", "We used to think we were too smart for rooms like that. Too different. Too far gone. Or not far gone enough. Then we sat down, and somebody said something we recognize. It was our story in a stranger's mouth.", "That's the miracle nobody advertises. Not the speeches. The recognition. The moment we realize we were never as alone as the disease of addiction told us. The chair's still there. It doesn't care what we did. It only asks that we sit down and keep coming back."],
    ["There's a phone in your pocket that weighs about six ounces. Except when we need to call our counselor or sponsor. Then it weighs a thousand pounds.", "Funny how that works. We'd text a dealer at three in the morning without a second thought. But asking for help feels like lifting a truck. That's not weakness talking. That's the disease of addiction, protecting itself. It knows a phone call can kill it.", "So we lift it anyway. We don't need the right words. \"Hey, it's me, I'm having a day\" is a whole sentence. Someone on the other end has been exactly where we are, and they're waiting for that call more than we know. We pick it up. It gets lighter every time."],
    ["Nobody warned us about this part. We put the drugs down, and the feelings showed up all at once, like they'd been waiting in the parking lot for years.", "Anger with nowhere to go. Grief we skipped. Joy so sharp it almost hurts. For a long time we kept all of it at arm's length. Now it's right up close.", "Here's what the people with time will tell us: feelings aren't facts, and they aren't emergencies. They pass. Every single one of them passes, if we don't use over it. But if a feeling includes wanting to die or hurt yourself, that is an emergency. Tell someone now, or call or text 988. This is what being alive feels like: loud, messy, and ours. We're not broken because it hurts. We're healing because we can finally feel it."],
    ["Recovery doesn't usually look like a movie. No big soundtrack, no sunrise on a mountaintop. Mostly it looks like a made bed. A paycheck that goes where it's supposed to. A promise kept on a Tuesday when nobody's watching.", "We used to chase big. Big highs, big plans, big comebacks that never came. Now the miracle is small and quiet, and it happens every day. Showing up on time. Answering the phone. Looking someone in the eye.", "We don't skip the small things. They're not the warm-up to recovery. They are recovery. Stack enough of them together, and one day you look up and realize you've built a life."],
    ["If you're hearing this, you're still here. Don't rush past that.", "Some of us didn't make it. A lot of us have lost people to the disease of addiction, and we carry their names with us. Every morning we wake up clean, we're doing something they didn't get the chance to do. Some of us feel guilty about that. We don't have to. Staying clean is how we honor them.", "And if yesterday went sideways, if you used, if you ran, if you're hearing this from the bottom again, the door didn't lock behind you. It never does. Nobody in the rooms is keeping score. We're just glad you came back.", "Today is new. It doesn't know what you did yesterday. It only knows you're here. So let's start there. Together."],
    ["Powerless is only half of it. The other half is what our lives looked like while we pretended we were in charge. Missed rent. Missed birthdays. Phones we were afraid to answer. We called it bad luck. We called it a rough patch. We called it anything but what it was.", "Unmanageable isn't an insult. It's just the truth. And there's a strange relief in finally saying it out loud. No spin. No excuses. No story about how it wasn't that bad. Once we stop defending the wreckage, we can start clearing it. One piece at a time. Starting with today."],
    ["Hope is a hard word to trust when we've lied to ourselves with it a hundred times. This time will be different. This time I've got it handled.", "So when someone says there's a power that can restore us to sanity, it's fair to be skeptical. Here's the thing, though. We don't have to believe it all at once. We just have to look around the room. People who were worse off than us are laughing. Holding jobs. Raising kids. Something worked for them that never worked when they tried it alone. Call it the group. Call it whatever you want. We don't need a definition. We just need to be willing to believe it might work for us too."],
    ["We are experts at holding on. Holding grudges. Holding secrets. Holding the steering wheel with both fists while the car goes straight into the ditch. Letting go sounds like giving up. It feels like falling.", "But look at what our grip has actually gotten us.", "Letting go doesn't mean we stop caring or stop trying. It means we stop running the whole show on our own broken judgment. We make a decision to let go, and then we make it again tomorrow, and the day after that. Our hands were never built to hold this much. We open them. We see what lands."],
    ["It usually shows up as a whisper. Just one. Just this weekend. Just to take the edge off.", "The disease of addiction is patient. It doesn't need us to use today. It just needs us to keep a little door open in the back of our minds. We call it a reservation, a someday, a special occasion. That door is how a lot of us went back to the bottom.", "So we close it out loud. We tell someone about the whisper the moment we hear it. Secrets keep it alive. Daylight takes away its voice. There is no \"just one\" for us. There's just today. And today, we stay clean."],
    ["A craving feels like it will last forever. It feels like a wall we can't get around, a noise that won't stop until we feed it. Our disease of addiction lies about that, too.", "Cravings rise, crest, and fall. Every single one passes, as long as we don't use over it. So we ride it out. We call someone. We eat something. We go to a meeting, take a walk, take a shower, pray if we pray. We do anything except the one thing. And before long, we notice it's gone, and we're still standing. That's a win. Count it."],
    ["We came in knowing everything. We knew what would work, what wouldn't, and why the people in the rooms were different from us.", "Then we looked around. A room full of people who've been exactly where we are, and who want us to make it. Plenty of people who need that never find it. Maybe it's time to let somebody else's experience in. An open mind doesn't mean we believe everything. It means we stop arguing long enough to listen. Some of us say clean. Some of us say sober. It's the same road.", "And if you take medication for addiction as prescribed, that's clean time too. We try the suggestion before we decide it won't work. We let the old-timer finish the sentence. Some of the best things in recovery came wrapped in advice we almost ignored."],
    ["We don't have to be ready. We don't have to be sure. Most of us weren't.", "What we needed was a lot smaller than that. We needed a little willingness. A crack in the door. Enough to show up one more time, make one more call, try one more thing we swore we'd never do. Willingness isn't a feeling. It's an action. We do it scared. We do it tired. We do it while the voice in our head says this won't work. And somewhere in the doing, the feeling catches up.", "So don't wait to feel it. Show up. Do the next right thing, and let the feeling find you there."],
    ["Hungry. Angry. Lonely. Tired.", "Four ordinary things, and every one of them can make a perfectly good day feel like an emergency. It used to feel like the end of the world. A lot of the time, it was an empty stomach and a bad night's sleep.", "So before we decide the whole world is falling apart, we check the basics. Eat something. Breathe first. Call somebody. Lie down. Recovery isn't always deep. Sometimes it's a sandwich and a nap."],
    ["We replay it. What they said, what they did, what we should have said back. We've run the tape so many times we know every word. Resentment feels like justice. It feels like keeping score for the good guys.", "But the person we're angry at usually isn't losing any sleep. We are. We're the ones swallowing the poison and waiting for them to get sick.", "So try something different. Play the tape forward. Where does this one end if we keep running it? For a lot of us, it ends with using. We don't have to pretend it didn't happen. We just have to look at what our part was, and what we're willing to set down. And if what happened to us was abuse, there's no part to find. That one was never ours. Either way, we don't carry it alone. Talk it through with a counselor or sponsor. Write it out. Let it out of the dark. Freedom is worth more than being right."],
    ["Fear has been driving a lot longer than we've been clean. Fear of being found out. Fear of being alone. Fear that this is all we'll ever be. For years, using kept it quiet. Now we're clean, and there's nothing left to drown it out.", "Here's what we learn: fear is a feeling, not a forecast. It tells us a lot about our past and almost nothing true about tomorrow. Courage isn't the absence of fear. It's doing the next right thing with our hands still shaking. We don't need to beat fear today. It can ride along. It just doesn't get to drive."],
    ["Somebody had to make the coffee. Somebody unlocked the door, set out the chairs, and stayed late to stack them again.", "For a long time, we never wondered who that somebody was. Then one night, someone handed us the keys. Service sounds like a big word, but it's mostly small things. Greeting the newcomer. Washing the pot. Giving someone a ride. And here's the secret: it's not only for them. When we're busy being useful, there's less room for the self-obsession that kept us sick. Grab a job at your home group. Any job. It's the easiest way to keep coming back."],
    ["Isolation doesn't feel dangerous. It feels like rest. Like staying in tonight, skipping one meeting, not answering the phone for a few days.", "That's exactly how it gets in. The disease of addiction does its best work when we're alone, in a quiet room, with nobody asking how we're really doing.", "The answer is almost embarrassingly simple: other people. One text. One call. One chair in one room with another addict. We don't have to like it. We don't have to say much. We just have to show up where we can be seen. We stay clean together."],
    ["Some roads still pull at us. The old neighborhood. The old number still saved in the phone. The friend who's still using, says they're doing fine, and just wants to hang out like old times. We tell ourselves we're strong enough now. That we can just visit.", "Here's a question worth asking: why would we want to? Changing people, places, and things isn't punishment. It's protection. We delete the number. We take a different way home. We find new people who'll show up for our clean birthday. Some of those losses hurt. But the road behind us has already shown us exactly where it goes."],
    ["We wanted to be fixed by now. The anger gone, the patience perfect, the old habits erased. Then we snapped at someone in line at the store and decided we were doing recovery wrong.", "Hold on. Not long ago, would we even have noticed? Would we have apologized? Would we have stayed clean through it? We're not aiming for perfect. We're aiming for a little better than yesterday. And being honest about where we fell short. Progress is slow, quiet, and real. Look how far you've already walked."],
    ["Guilt says, I did something bad. Shame says, I am something bad.", "Shame is the one that kept us using. It told us we were too far gone, too damaged, too much to fix. So why bother trying? And shame loves the dark. It grows in secrets. It shrinks the moment we say it out loud to someone who doesn't flinch.", "That's what the rooms are for. We tell the truth, and someone nods, because they've been there. We are not the worst thing we ever did. We're people with a disease, getting better. We can put the shame down. It was never ours to carry."],
    ["We're good at taking other people's inventory. What they did wrong. Why they're the problem. We could write books about everybody else.", "Eventually, recovery hands us a pencil and asks us to write about ourselves. That's terrifying, because we know what's in there. Or we think we do.", "Here's what most of us found: it wasn't the horror story we expected. It was full of the same things everyone else had. Fear. Selfishness. Hurt. Not monsters. People. An honest look in the mirror isn't about beating ourselves up. It's about finally seeing clearly enough to change. We don't do it alone. We do it with a counselor or sponsor."],
    ["Leaving treatment feels like a finish line. It isn't. It's the starting line, and those first days are when a lot of us went back out. Not because we wanted to. Because we walked out with no plan, and the old life had one waiting for us.", "So we build ours ahead of time. Where are we sleeping tonight? Who's picking us up? Where's the next meeting, and what time does it start? Whose numbers are in the phone? When's the next appointment?", "Write it down. Go over it with a counselor or sponsor. A plan won't make us feel ready. It doesn't have to. It just has to be there when the feeling isn't. Today, we start writing ours."],
    ["We got clean and expected everyone to throw a parade in our honor. Instead, our family still checks our eyes. Still counts the money. Still flinches when the phone rings late.", "That hurts. And it's fair. We spent years teaching them not to trust us. It's going to take more than a few good weeks to teach them something new. So we stop demanding trust and start earning it. Quietly. Consistently. Day after day, until our actions say what our words never could. Their healing runs on its own clock, not ours. Our job isn't to rush them. Our job is to keep showing up, clean."],
    ["Nobody warned us about Saturday nights. The work week ends, the phone goes quiet, and suddenly there's a whole evening with nothing in it.", "Boredom used to be our cue. The disease of addiction likes to remind us the old life was never boring. That's a lie. It was the same people, the same places, the same night over and over.", "So we plan the weekend like it matters, because it does. A meeting, then coffee with whoever's still in the parking lot. A movie. A long ride. The thing we always said we'd learn. Clean fun is a skill, and like any skill, it's awkward at first. Then one night we realize we laughed until midnight and never once thought about using."],
    ["Some days are just hard. The car won't start. The rent is late. Somebody we love won't call back.", "And on those days, someone at the meeting says they're grateful, and we want to tell them exactly where they can shove their gratitude. But gratitude isn't pretending the bad stuff isn't happening. It's noticing what's still standing in the middle of it. A bed. A phone someone's number in it who'll pick up. A bad day that we didn't make worse. Write three things down tonight. Small ones count. Especially small ones. Gratitude on a bad day is the strongest kind."],
    ["Somebody did this for us. Somebody told the truth in a room we almost didn't walk into.", "For a while, we sat in the back and said nothing. Listening felt like enough. It wasn't. When we keep quiet, nobody knows what we're carrying, and nobody can help us carry it.", "There's an old saying in recovery: we can't keep what we have unless we give it away. Here's what it means: recovery we keep to ourselves starts to fade, but recovery we say out loud stays real. So we raise our hand. Not a speech. Just a quick check-in: here's where I'm at today.", "It's for the newcomer in the back. And it's for us."]]

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
.reading p{font-size:1.15rem;line-height:1.65}
.soon{color:#666;font-style:italic}
.help{border-left:4px solid #ffd21f;background:#fff;padding:.8rem 1rem;font-size:1rem}
small{display:block;color:#777;margin-top:1.6rem;font:.8rem/1.4 Arial,sans-serif}
ol{padding-left:1.4rem;font-size:1.05rem;line-height:1.7}
"""

HELP = ('<p class="help"><strong>If a feeling includes wanting to die or hurt yourself, that is an emergency.</strong> '
        'Tell someone now, or call or text <a href="tel:988">988</a>.</p>')
FOOT = '<small>Clean For Today · © 2026 Sober Elf Studio LLC · soberelf.com · All rights reserved.</small>'

def page(title, head_extra, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="referrer" content="no-referrer">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
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
    text = "\n".join(f"<p>{html.escape(p)}</p>" for p in SCRIPTS[n - 1])
    if url:
        u = html.escape(url, quote=True)
        watch = f'<a class="btn" href="{u}">Watch Day {n}</a>\n'
    else:
        watch = '<p class="soon">The video for this day is coming soon.</p>\n'
    body = (f'<span class="tag">Day {n}</span>\n<h1>{html.escape(title)}</h1>\n'
            f'{watch}<div class="reading">\n{text}\n</div>\n'
            f'<a class="btn" href="/day/">See all 28 days</a>\n{HELP}\n{FOOT}')
    return page(f"{label} · Clean For Today", '', body)

def index_page():
    items = []
    for n, (title, url) in enumerate(VIDEOS, 1):
        items.append(f'<li><a href="/day/{n}/">{html.escape(title)}</a>{"" if url else " <em>(video coming soon)</em>"}</li>')
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
    print(f"Wrote day/index.html and day/1–28. {live} have a video link, {28 - live} say the video is coming soon.")
