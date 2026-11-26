# soberelf.com/day — Clean For Today QR pages

The printed booklet's QR codes point here, never straight at YouTube.
If a video moves, gets re-cut, or comes down, you change one line and every booklet still works.

## Put it on the site (once)
1. The `day` folder lives in the root of this repo, next to `index.html`.
2. Commit and push. After a minute, soberelf.com/day/1/ through soberelf.com/day/28/ are live.

## When a recording is ready
1. Export the day's mix (voice plus Aaron's cue) as `audio/dayNN.mp3`, 128 kbps, with every tag stripped:
   `ffmpeg -i mix.mp4 -vn -map_metadata -1 -c:a libmp3lame -b:a 128k -id3v2_version 0 -write_id3v1 0 audio/day05.mp3`
   The file name is the day number only. Never a reader's name.
2. Run `python3 make_days.py`.
3. Commit and push.

## What each page does
- Every page shows that day's reflection written out (CFT: Online r23, matched to what each reader says).
- Recording in place: a player, with "Every day is spoken by someone who has been in treatment for addiction. Their names stay private." under it, and "Music by Aaron Scharmer." under the reading.
- No recording yet: a note says the recording is coming soon.
- Every page carries the 988 line.
- `soberelf.com/day/` lists all 28 days for counselors to bookmark.

## Privacy
No analytics, trackers, cookies, outside fonts or scripts, and pages are hidden from search engines.
Nothing here can tell anyone who scanned a QR code. Keep it that way: don't add tracking to these pages.
