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
