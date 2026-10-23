# Graphic templates

Data-driven graphics in the style of the "Today's Winners" board.
Colors are the site brand: purple rgb(99, 102, 241) and green rgb(34, 197, 94), set at the top of `base.css`. Edit a JSON
file, run one command, get PNGs for every channel.

## Make a new graphic
1. Copy a file in `data/` (for winners, start from `winners-TEMPLATE.json`).
2. Change the games, scores, dates and text.
3. Run `python3 render.py data/your-file.json`
4. PNGs appear in `renders/` as `your-file-4x5.png`, `-9x16.png`, `-2x3.png`.

| Format | Size | Use for |
|---|---|---|
| 4x5 | 1080x1350 | Instagram and Facebook feed |
| 9x16 | 1080x1920 | Stories, Reels covers, TikTok photo posts (content kept out of the button zones) |
| 2x3 | 1000x1500 | Pinterest |
| 16x9 | 1600x900 | X (two-column layout: title and facts left, games or steps right) |

Add `--formats 4x5` to render just one size.

## Templates
- **winners**: final score board. Give each game's real final score; the big digits (last digit) are worked out for you. Up to 10 games fit in two columns; 11 or more switch to three.
- **slate**: a list of upcoming games with day, date, time and network. Optional blocks:
  - `how`: three "how squares work" steps
  - `math`: example pot, e.g. `{"price": 10}` shows $1,000 / $500 / $500
  - `cta`: the colored call to action bar
  - `group_by_day` plus a `group` on each game adds day headings (used for Thanksgiving)
  - `tag` and `feature: true` highlight one game
  - `theme: "harvest"` adds a purple glow behind the title (used for Thanksgiving)
- **feature**: one post, one message. A big title (`title`, or `title_lines`; "X at Y" lights up the "at"),
  `facts` chips (day, kickoff, network), then any of: `board` (sample squares board with `top`/`side`
  team names), `games` (same rows as slate), `steps` (big numbered how-to), `prices` (price guide with
  pot and cause), `hook` (one line of copy), `cta`.
- **artframe**: puts existing art (`art`, a file in `art/`) into the channel's frame without cropping it,
  with a top band (`eyebrow`, `title`, `facts`) and a bottom band (`lines`, `cta`). Used to turn the 4:5
  rivalry art into 2:3 pins and 9:16 TikTok slides.
- A data file can set `formats` (e.g. `["2x3"]` for a pin) so it only renders the size its channel uses.
- `only_in` limits a block to some formats, e.g. `{"how": ["9x16"]}` shows the steps only on the tall version.

If text doesn't fit, game rows shrink automatically. If it still doesn't fit, the
command prints a WARNING; drop a game or shorten a line.

## Per-post graphics
`data/posts/` holds one data file per scheduled post, named by post date (ET), channel and topic.
Render them into the hosted `posts/` folder with:
`python3 render.py data/posts/*.json --out ../posts`

## Rules baked in
- Team names in plain type only. No logos, helmets or footage.
- No em dashes in any copy you type into the data files.
- Footnotes say the site is free and never touches the money.

## Running it yourself
Needs Python 3 and Playwright: `pip install playwright && playwright install chromium`.
This works on a Mac or PC, or in a GitHub Codespace if you put this folder in a repo.
Fonts (Barlow and Barlow Condensed, open license) are in `fonts/`.

## Sample data
- `winners-2026-10-04.json`: the Oct 4 board from the example, rebuilt
- `slate-nfl-week6.json`: NFL Week 6, Oct 15 to 19
- `slate-college-oct17.json`: College Saturday, Oct 17
- `thanksgiving-2026.json`: the five holiday games, linking SuperBowlPoolSite.com/thx

Afternoon NFL times and networks come from `../schedule-2026.md` and can still change; check before posting.

## Instagram carousels
`data/carousels/` holds one file per scheduled Instagram post. Each file has a `slides` list
(4x5 only) and the post's Buffer id and caption under `instagram`. Settings in `defaults`
apply to every slide; a slide can override any of them, including `template` (use
`artframe` with `art` for a rivalry art cover). Every slide gets a progress bar at the top,
and every slide but the last gets a "Swipe" cue, so the set reads as one story:
cover hook, the problem, the idea, the proof or math, then the ask.

Extra blocks for story slides (feature template): `body` (one or more short paragraphs),
`stat` (one or more big numbers with labels), `chat` (group chat bubbles, `me: true` for
the right side), `bullets` (a checklist) and `picture` (a file in `art/`).

Render them into the hosted `carousels/` folder with:
`python3 render.py data/carousels/*.json --out ../carousels`
Files come out as `<name>-01-4x5.png`, `-02-4x5.png` and so on, in slide order.
