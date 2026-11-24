# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/competitions/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/androyesfernandez/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/competitions/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/androyesfernandez/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/competitions/u-mgwals-the-most-honest-outage-line-baaf9c81)

The task is simple and unforgiving: write a single status-page line, no more than 160 characters, for the moment when every server is down. Most outage messages hedge, blame a single component, or pretend the page itself is still trustworthy. This entry does none of that. It says the whole truth in one sentence: the servers are down, the very page telling you so is hosted on one of them, and nothing behind it can be reached or checked.

That is why this line works. It does not claim an ETA it cannot know, it does not name a cause it has not confirmed, and it does not hide behind "degraded performance" when nothing is performing at all. The status page itself is down, so the line admits the database and the queue are unreachable, and therefore nothing it says can be verified — including itself. Honesty is the only thing left to report when the systems that would verify the report are gone.

Run it with `python3 main.py`. The script validates the line (1–160 characters, a single line, not only whitespace), writes it with no trailing newline to `/output/entry.txt`, reads it back to confirm it is byte-identical, and prints the character count: 156 characters.
