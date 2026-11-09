"""Data for fresh.py. One entry per graphic: (name, kind, formats, data).
Testimonials are quoted exactly as they appear on SuperBowlPoolSite.com."""

FUND = "SuperBowlPoolSite.com/football-squares-fundraiser"
EYEBROW = "What our commissioners say"

JENNIFER = dict(theme="forest", eyebrow=EYEBROW,
                quote="We use the Super Bowl Pool Site every year to raise money for our yearly team softball trip!",
                name="Coach Jennifer F.", team="Lightning 12U Girls Softball", place="Long Island, NY")
CINDY = dict(theme="paper", eyebrow=EYEBROW, quote="Makes watching the game so much more fun!",
             name="Cindy D.", team="Eagles Jr. Hockey", place="Chicago, IL",
             filled=[2, 11, 12, 24, 33, 35, 47, 58, 61, 66, 72, 79, 84, 90, 97])
TIM = dict(theme="purple", eyebrow=EYEBROW,
           quote="The absolute BEST way to raise money for a youth team. Believe me, I've tried them all.",
           name="Tim S.", team="FC Strikers 12U", place="Dallas, TX",
           filled=[5, 16, 18, 21, 30, 44, 49, 53, 62, 68, 75, 83, 86, 91, 99])

MA = [("Boston Latin", "Boston English", "Since 1887"), ("Malden", "Medford"), ("Fitchburg", "Leominster"),
      ("Natick", "Framingham"), ("Winchester", "Woburn"), ("Marblehead", "Swampscott"), ("Beverly", "Salem"),
      ("Attleboro", "North Attleborough"), ("Foxborough", "Mansfield"), ("BC High", "Catholic Memorial"),
      ("Xaverian", "St. John's Prep")]
CT = [("Norwich Free Academy", "New London", "Since 1875"), ("Greenwich", "Staples (Westport)"),
      ("Ansonia", "Naugatuck"), ("Derby", "Shelton"), ("Hillhouse", "Wilbur Cross", "Elm City Bowl"),
      ("Southington", "Cheshire", "Apple Valley Classic"), ("Fairfield Ludlowe", "Fairfield Warde"),
      ("Stamford", "Westhill")]
RI_NE = ["Rhode Island", ("Westerly", "Stonington, CT", "Since 1911"), ("Cranston East", "Cranston West"),
         ("East Providence", "La Salle"), "Elsewhere in the Northeast",
         ("Easton, PA", "Phillipsburg, NJ", "Lafayette College"), ("Vineland", "Millville, NJ", "Since 1893"),
         ("Central", "Northeast", "Philly, 1890s"), ("Fordham Prep", "Xavier", "NYC Turkey Bowl"),
         ("Portland", "Deering", "Maine")]
OLDEST = [("Norwich Free Academy", "New London", "1875"), ("Boston Latin", "Boston English", "1887"),
          ("Vineland", "Millville", "1893"), ("Central", "Northeast", "1890s"),
          ("Westerly", "Stonington", "1911"), ("Easton", "Phillipsburg", "PA vs NJ"),
          ("Hillhouse", "Wilbur Cross", "Elm City Bowl"), ("Southington", "Cheshire", "Apple Valley"),
          ("Fordham Prep", "Xavier", "Turkey Bowl"), ("Malden", "Medford", "Mass.")]

LAND_PROGRAM = """
.land .band{padding:5rem 8rem 3.4rem}
.land .band h2{font-size:9rem}
.land .band .count{bottom:3.4rem;right:8rem}
.land .band .count b{font-size:9rem}
.land .rows{columns:2;column-gap:7rem;padding:2rem 8rem 0}
.land .row{break-inside:avoid;padding:1.55rem 0}
.land .row .m{font-size:3.5rem}
.land .row .n{font-size:1.9rem}
.land .pfoot{padding:0 8rem 4.5rem}
"""
PIN_PROGRAM = """
.f2x3 .row{padding:2.5rem 0}
.f2x3 .row .m{font-size:4.4rem}
.f2x3 .band h2{font-size:12rem}
"""

POSTS = [
    # testimonials
    ("quote-jennifer", "quote", ["4x5", "9x16", "16x9"], JENNIFER),
    ("quote-cindy", "quote", ["4x5", "2x3", "16x9"], CINDY),
    ("quote-tim", "quote", ["4x5", "2x3", "16x9"], TIM),
    ("cta-testimonials", "cta", ["4x5"], dict(
        eyebrow="Your turn", title="Your team<br><em>is next.</em>", cause="to your team",
        lede="Make a free 100 square board for a Thanksgiving game, sell the squares to family and friends, and split the pot.",
        url_label=FUND)),

    # type your two teams
    ("form-texas-lsu", "form", ["16x9"], dict(
        eyebrow="Any game, any two teams", title="Your game.<br><em>Your two teams.</em>",
        lede="After you create your contest, open Basic Details and type the two team names into Top Team Label and Left Team Label.",
        contest="Texas at LSU Squares", top="LSU", left="TEXAS", url_label="SuperBowlPoolSite.com")),
    ("form-calvert-loyola", "form", ["2x3"], dict(
        eyebrow="Turkey Bowl, Baltimore", title="Run a board on<br><em>the Turkey Bowl.</em>",
        lede="Create your contest, then set the Top Team Label and Left Team Label to the two schools.",
        contest="Turkey Bowl Squares", top="CALVERT HALL", left="LOYOLA BLAKEFIELD")),
    ("form-boston", "form", ["4x5"], dict(
        eyebrow="Make one for your game", title="Two labels.<br><em>Any rivalry.</em>",
        lede="Create your contest, open Basic Details, and type the two schools into Top Team Label and Left Team Label.",
        contest="Latin vs English Squares", top="BOSTON LATIN", left="BOSTON ENGLISH")),
    ("form-malden-medford", "form", ["4x5"], dict(
        eyebrow="Not just the NFL", title="Your town's game<br><em>counts too.</em>",
        lede="Create your contest, then type your two teams into Top Team Label and Left Team Label.",
        contest="Thanksgiving Rivalry Squares", top="MALDEN", left="MEDFORD")),

    # Thanksgiving rivalry program (Instagram carousel)
    ("rivalry-01-cover", "cover", ["4x5"], dict(
        ticket="Thanksgiving morning 2026", title="The other<br><em>Thanksgiving</em><br>games.",
        lede="Before the NFL kicks off, towns across the Northeast play rivalries that go back more than a century. 27 of them, by state.",
        states=["Massachusetts", "Connecticut", "Rhode Island", "NY", "NJ", "PA", "Maine"], hand="swipe for yours")),
    ("rivalry-02-massachusetts", "program", ["4x5"], dict(
        eyebrow="Thanksgiving rivalries", title="Massachusetts", tag="The heart of the tradition", count=11,
        rows=MA, page="2 / 6", css=".row{padding:1.55rem 0}")),
    ("rivalry-03-connecticut", "program", ["4x5"], dict(
        eyebrow="Thanksgiving rivalries", title="Connecticut", tag="Home of the oldest one on the list", count=8,
        rows=CT, page="3 / 6")),
    ("rivalry-04-ri-northeast", "program", ["4x5"], dict(
        eyebrow="Thanksgiving rivalries", title="Rhode Island<br>and beyond", count=8, rows=RI_NE, page="4 / 6",
        css=".band h2{font-size:9rem}.row{padding:1.6rem 0}.sub{margin-top:2.4rem}")),
    ("rivalry-06-cta", "cta", ["4x5"], dict(
        eyebrow="Thanksgiving morning", title="Your town's game<br><em>can fund your team.</em>",
        cause="to the team or boosters",
        lede="One free board on the rivalry game, shared with families and alumni. Then run another on the NFL games that follow.",
        url_label="SuperBowlPoolSite.com/thx")),

    # rivalry list for Pinterest and X
    ("rivalry-classics", "program", ["2x3", "16x9"], dict(
        eyebrow="Save this", title="Ten Thanksgiving<br>classics", count=10, rows=OLDEST,
        fine="Type both schools into Top Team Label and Left Team Label to make a board for any of them.",
        css=LAND_PROGRAM + PIN_PROGRAM)),
]
