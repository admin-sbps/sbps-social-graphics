# Per-post images swapped in Buffer (Oct 17, 2026)

SBPS asked for images that are specific to each post and sized for its channel.
21 scheduled posts got a new image. Copy, times and status were not changed
(Pinterest edits re-sent the same text because Buffer requires it).

Images are hosted from the sbps-social-graphics repo, pinned to commit 76b0bef:
`https://raw.githubusercontent.com/admin-sbps/sbps-social-graphics/76b0befc1c4a111d8d12dc2eaf45db69e6ed5901/posts/<file>`
Source data: `templates/data/posts/`. Render: `python3 render.py data/posts/*.json --out ../posts`.

| Post date (ET) | Channel | Post id | New image (size) | Replaced |
|---|---|---|---|---|
| Oct 18 | Instagram | 6accfefb176c301054878098 | snf-cowboys-packers 1080x1350 | generic site board 700x595 |
| Oct 19 | Pinterest | 6accff0e176c301054878357 | baltimore-turkey-bowl 1000x1500 | Baltimore art 825x1024 |
| Oct 20 | Pinterest | 6accff120e025935d3b82f7c | price-guide 1000x1500 | generic site board |
| Oct 21 | Pinterest | 6accff1c176c301054878533 | bronx-manhattan 1000x1500 | Bronx art 825x1024 |
| Oct 24 | Instagram | 6accff120e025935d3b82fa5 | rivalry-saturday 1080x1350 | generic site board |
| Oct 27 | Pinterest | 6accff30ba9a2573f195972a | wellesley-needham 1000x1500 | Wellesley art 825x1024 |
| Oct 30 | Instagram | 6accff25522c31be02385d37 | halloween-weekend 1080x1350 | generic site board |
| Nov 2 | Instagram | 6accff390e025935d3b838ff | bears-lions 1080x1350 | generic site board |
| Nov 3 | TikTok | 6accff690e025935d3b8420e | how-it-works + thanksgiving-lineup 1080x1920 x2 | generic board + Baltimore art |
| Nov 3 | Pinterest | 6accff56225b47b7f7b7e24c | how-it-works 1000x1500 | generic site board |
| Nov 4 | Pinterest | 6accff5a0e025935d3b83f07 | wellesley-team-example 1000x1500 | Wellesley art 825x1024 |
| Nov 6 | Pinterest | 6accff61ba9a2573f195a7a1 | new-canaan-boosters 1000x1500 | New Canaan art 825x1024 |
| Nov 7 | Instagram | 6accff500e025935d3b83bfb | college-saturday 1080x1350 | generic site board |
| Nov 12 | Instagram | 6acd1264358c83a3d376b9d2 | baseball-price-guide 1080x1350 | baseball photo 687x1024 (too tall for IG) |
| Nov 17 | Pinterest | 6acd1268e0a62e05555e6949 | baltimore-week 1000x1500 | Baltimore art 825x1024 |
| Nov 18 | Pinterest | 6acd12aaacb90f71c6d2b44e | friendsgiving 1000x1500 | generic site board |
| Nov 21 | Instagram | 6acd12ac358c83a3d376d593 | dance-competition-qr 1080x1350 | dance photo 687x1024 (too tall for IG) |
| Nov 23 | Pinterest | 6acd12ad7eb16fd28e944215 | new-canaan-save-this 1000x1500 | New Canaan art 825x1024 |
| Nov 24 | TikTok | 6acd12aeacb90f71c6d2b74a | boston-latin-english 1080x1920 | Boston art 825x1024 |
| Nov 25 | Pinterest | 6acd12aeacb90f71c6d2b773 | thanksgiving-eve 1000x1500 | Baltimore art 825x1024 |
| Nov 26 | TikTok | 6acd12b6fd425063ef4a3517 | happy-thanksgiving 1080x1920 | Wellesley art 825x1024 |

## Not changed
- Instagram and Threads posts using the 825x1024 rivalry art: already 4:5 and the art matches the caption.
- TikTok fundraiser photo posts (Nov 6, 10, 13, 17, 20): the photos live on marketing.superbowlpoolsite.com, which this environment cannot reach, so they could not be reframed to 9:16.
- Nov 7 Instagram college card shows no kickoff times; networks announce them about a week ahead. Re-render `2026-11-07-instagram-college-saturday.json` with times and swap once announced.

## X posts (Oct 19, 2026)

All 27 scheduled X posts were text only. Each now carries its own 1600x900 (16:9) image.
Copy, times and status were not changed. Parked duplicate drafts were left alone.
The Nov 3 thread has the image on its first tweet; all four thread texts were kept.

Pinned to commit 2555da7:
`https://raw.githubusercontent.com/admin-sbps/sbps-social-graphics/2555da7fa2e57da92dd02b9d4e1b2cfbf7b88378/posts/<file>`

| Post date (ET) | Post id | New image (size) | Replaced |
|---|---|---|---|
| 2026-10-19 | 6accfecdba9a2573f1958575 | 2026-10-19-x-thanksgiving-5-games-16x9.png (1600x900) | none (text only) |
| 2026-10-21 | 6accfecf522c31be02384c60 | 2026-10-21-x-dance-cheer-studios-16x9.png (1600x900) | none (text only) |
| 2026-10-24 | 6accfedb522c31be02384e87 | 2026-10-24-x-big-saturday-16x9.png (1600x900) | none (text only) |
| 2026-10-25 | 6accfedd522c31be02384edf | 2026-10-25-x-bears-lions-thanksgiving-16x9.png (1600x900) | none (text only) |
| 2026-10-26 | 6accfedf176c301054877c2f | 2026-10-26-x-cowboys-eagles-rematch-16x9.png (1600x900) | none (text only) |
| 2026-10-28 | 6accfed8522c31be02384e1d | 2026-10-28-x-sell-the-uncle-a-square-16x9.png (1600x900) | none (text only) |
| 2026-10-30 | 6accfee1225b47b7f7b7ca24 | 2026-10-30-x-halloween-weekend-16x9.png (1600x900) | none (text only) |
| 2026-10-31 | 6accfee4176c301054877ca5 | 2026-10-31-x-georgia-florida-16x9.png (1600x900) | none (text only) |
| 2026-11-01 | 6accfee617154ed8aaf474a1 | 2026-11-01-x-25-days-16x9.png (1600x900) | none (text only) |
| 2026-11-02 | 6accfeee17154ed8aaf47613 | 2026-11-02-x-bears-week-16x9.png (1600x900) | none (text only) |
| 2026-11-03 | 6accfef0225b47b7f7b7cc84 | 2026-11-03-x-4-steps-thread-16x9.png (1600x900) | none (text only) |
| 2026-11-04 | 6accfef30e025935d3b82a73 | 2026-11-04-x-12u-softball-math-16x9.png (1600x900) | none (text only) |
| 2026-11-05 | 6accfef5176c301054877fb6 | 2026-11-05-x-jaguars-ravens-tnf-16x9.png (1600x900) | none (text only) |
| 2026-11-06 | 6accfef80e025935d3b82b47 | 2026-11-06-x-booster-clubs-16x9.png (1600x900) | none (text only) |
| 2026-11-07 | 6accfefa0e025935d3b82b9d | 2026-11-07-x-packed-saturday-16x9.png (1600x900) | none (text only) |
| 2026-11-08 | 6accfefcba9a2573f1958cf7 | 2026-11-08-x-18-days-16x9.png (1600x900) | none (text only) |
| 2026-11-09 | 6acd1262fd425063ef4a0ee8 | 2026-11-09-x-chiefs-bills-finale-16x9.png (1600x900) | none (text only) |
| 2026-11-12 | 6acd1264fd425063ef4a0fad | 2026-11-12-x-two-weeks-out-16x9.png (1600x900) | none (text only) |
| 2026-11-14 | 6acd1266fd425063ef4a1006 | 2026-11-14-x-saturday-warm-up-16x9.png (1600x900) | none (text only) |
| 2026-11-15 | 6acd1266358c83a3d376babb | 2026-11-15-x-cowboys-double-16x9.png (1600x900) | none (text only) |
| 2026-11-16 | 6acd1267358c83a3d376baee | 2026-11-16-x-10-days-16x9.png (1600x900) | none (text only) |
| 2026-11-19 | 6acd12ab4f588aad4fd83d12 | 2026-11-19-x-black-friday-16x9.png (1600x900) | none (text only) |
| 2026-11-21 | 6acd12ace0a62e05555e82e1 | 2026-11-21-x-tournament-qr-16x9.png (1600x900) | none (text only) |
| 2026-11-22 | 6acd12ace0a62e05555e8325 | 2026-11-22-x-4-days-left-16x9.png (1600x900) | none (text only) |
| 2026-11-23 | 6acd12acacb90f71c6d2b6af | 2026-11-23-x-full-lineup-16x9.png (1600x900) | none (text only) |
| 2026-11-25 | 6acd12ae358c83a3d376d633 | 2026-11-25-x-packers-rams-tonight-16x9.png (1600x900) | none (text only) |
| 2026-11-26 | 6acd12af4f588aad4fd83fd3 | 2026-11-26-x-happy-thanksgiving-16x9.png (1600x900) | none (text only) |

X caveats:
- Nov 7 and Nov 14 college cards show no kickoff times; networks have not announced them yet.
- MNF and TNF cards use 8:15 PM ET from schedule-2026.md.
- Oct 24 college times come from TV listings; Ole Miss at Texas 7:30 PM has a single source.

