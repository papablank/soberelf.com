# soberelf.com/day — Clean For Today QR pages

The printed booklet's QR codes point here, never straight at YouTube.
If a video moves, gets re-cut, or comes down, you change one line and every booklet still works.

## Put it on the site (once)
1. The `day` folder lives in the root of this repo, next to `index.html`.
2. Commit and push. After a minute, soberelf.com/day/1/ through soberelf.com/day/28/ are live.

## When a video goes up
1. Open `make_days.py` and paste the YouTube link next to that day, e.g.
   `("Gloves Down", "https://www.youtube.com/watch?v=..."),`
2. Run `python3 make_days.py` (it rewrites the `day` folder).
3. Copy the new `day` folder into the repo, commit, push.

When the playlist exists, paste its link into `PLAYLIST` at the top too.

## What each page does
- Every page shows that day's reflection written out (CFT: Online text, locked 2026-11-09).
- Link filled in: a "Watch Day N" button at the top opens the video.
- Link empty: a short note says the video is coming soon.
- To change a day's words, edit SCRIPTS in make_days.py and run it again.
- Every page carries the 988 line.
- `soberelf.com/day/` lists all 28 days for counselors to bookmark.

## Privacy
No analytics, trackers, cookies, outside fonts or scripts, and pages are hidden from search engines.
Nothing here can tell anyone who scanned a QR code. Keep it that way: don't add tracking to these pages.
