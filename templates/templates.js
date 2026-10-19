// Builds a graphic from window.DATA. render.py injects DATA and the format
// ("4x5", "9x16" or "2x3"), then takes the screenshot.
(function () {
  const D = window.DATA;
  const FMT = window.FORMAT;
  const esc = (v) => String(v == null ? "" : v)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const lastDigit = (n) => Math.abs(parseInt(n, 10)) % 10;
  const shows = (section) => {
    const only = (D.only_in || {})[section];
    return !only || only.includes(FMT);
  };

  function header() {
    const dates = (D.date_lines || []).map(esc).join("<br>");
    return `
      <div class="eyebrow">${esc(D.eyebrow)}</div>
      <div class="head">
        <div class="title">${esc(D.title)}</div>
        ${dates ? `<div class="dateblock">${dates}</div>` : ""}
      </div>
      ${D.subtitle ? `<div class="sub">${esc(D.subtitle)}</div>` : ""}
      <div class="rule"></div>`;
  }

  function cta() {
    if (!D.cta || !shows("cta")) return "";
    return `<div class="cta"><div class="ask">${esc(D.cta.ask)}</div><div class="url">${esc(D.cta.url)}</div></div>`;
  }

  function footer() {
    // The call to action already shows the address, so skip it in the footer.
    const site = cta() ? "" : `<span class="site">${esc(D.site || "SuperBowlPoolSite.com")}</span>`;
    return `<div class="foot"><span>${esc(D.footnote || "")}</span>${site}</div>`;
  }

  function winners() {
    const games = D.games || [];
    const cols = games.length > 10 ? 3 : (games.length <= 3 && FMT !== "4x5" ? 1 : 2);
    const rows = Math.ceil(games.length / cols);
    const cards = games.map((g, i) => {
      const lonely = cols === 2 && games.length % 2 === 1 && i === games.length - 1;
      const line = `${esc(g.away)} ${esc(g.away_score)} &middot; ${esc(g.home)} ${esc(g.home_score)}`;
      return `
        <div class="game ${lonely ? "span" : ""}">
          <div class="game-top"><span class="label">${esc(g.label || "Final")}</span><span class="line">${line}</span></div>
          <div class="tiles">
            <div class="tile"><div class="team">${esc(g.away)}</div><div class="digit">${lastDigit(g.away_score)}</div></div>
            <div class="tile"><div class="team">${esc(g.home)}</div><div class="digit">${lastDigit(g.home_score)}</div></div>
          </div>
        </div>`;
    }).join("");
    return `${header()}
      <div class="grid${cols === 3 ? " dense" : ""}" style="grid-template-columns:repeat(${cols},minmax(0,1fr));grid-template-rows:repeat(${rows},1fr)">${cards}</div>
      ${cta()}${footer()}`;
  }

  function gameRow(g) {
    const tag = g.tag ? `<span class="tag">${esc(g.tag)}</span>` : "";
    const meta = [g.note, g.tv].filter(Boolean).map(esc).join(" &middot; ");
    return `
      <div class="row ${g.feature ? "feature" : ""}">
        <div class="when"><div class="d">${esc(g.day)}</div><div class="n">${esc(g.date)}</div></div>
        <div>
          <div class="match">${esc(g.away)}<span class="at">${g.vs ? "vs" : "at"}</span>${esc(g.home)}</div>
          <div class="meta">${tag}${meta}</div>
        </div>
        <div class="time">${esc(g.time)}${g.time_note ? `<small>${esc(g.time_note)}</small>` : ""}</div>
      </div>`;
  }

  function slate() {
    let list = "";
    let lastHead = null;
    (D.games || []).forEach((g) => {
      if (D.group_by_day && g.group !== lastHead) {
        list += `<div class="dayhead">${esc(g.group)}</div>`;
        lastHead = g.group;
      }
      list += gameRow(g);
    });

    let how = "";
    if (D.how && shows("how")) {
      how = `<div class="how">${D.how.map((s, i) => `
        <div class="step"><div class="num">${i + 1}</div><div class="txt"><b>${esc(s.title)}</b>${esc(s.text)}</div></div>`).join("")}</div>`;
    }

    let math = "";
    if (D.math && shows("math")) {
      const price = Number(D.math.price);
      const pot = price * 100;
      const half = pot / 2;
      const money = (n) => "$" + n.toLocaleString("en-US");
      math = `<div class="math">
        <div><div class="big">${money(pot)}</div><div class="lbl">100 squares at ${money(price)}</div></div>
        <div><div class="big">${money(half)}</div><div class="lbl">${esc(D.math.winner_label || "to the winners")}</div></div>
        <div><div class="big">${money(half)}</div><div class="lbl">${esc(D.math.cause_label || "to your team")}</div></div>
      </div>`;
    }

    return `${header()}<div class="list">${list}</div>${how}${math}${cta()}${footer()}`;
  }

  // A sample 10x10 board: the squares motif from the site, with one
  // winning row and column lit up. Names and digits are fixed so the same
  // data always renders the same picture.
  const NAMES = ["Mel", "Ken", "Luis", "Gabby", "Joey", "Kate", "Rob", "Sue", "Alex", "Joan",
    "Matt", "Coy", "Beck", "Sara", "Jeff", "Ron", "Mom", "Dad", "Leo", "Cathy", "Tim", "Ava"];
  function board(b) {
    const top = b.top_digits || [9, 7, 0, 8, 6, 4, 5, 3, 1, 2];
    const side = b.side_digits || [4, 1, 6, 3, 9, 7, 2, 0, 5, 8];
    const winRow = b.win_row == null ? 7 : b.win_row;
    const winCol = b.win_col == null ? 7 : b.win_col;
    const filled = b.filled == null ? 0.72 : b.filled;
    let cells = `<div class="bx corner"></div>`;
    top.forEach((d, c) => { cells += `<div class="bx dig ${c === winCol ? "hot" : ""}">${d}</div>`; });
    side.forEach((d, r) => {
      cells += `<div class="bx dig ${r === winRow ? "hot" : ""}">${d}</div>`;
      for (let c = 0; c < 10; c++) {
        const n = r * 10 + c;
        const open = ((n * 37) % 100) / 100 > filled;
        const name = open ? "" : NAMES[(n * 7 + r) % NAMES.length];
        const cls = r === winRow && c === winCol ? "win" : (r === winRow || c === winCol ? "lit" : "");
        cells += `<div class="bx sq ${cls} ${open ? "open" : ""}">${r === winRow && c === winCol ? esc(b.win_label || "Winner") : name}</div>`;
      }
    });
    return `<div class="boardwrap"><div class="board">
      <div class="btop">${esc(b.top)}</div>
      <div class="bside"><span>${esc(b.side)}</span></div>
      <div class="bgrid">${cells}</div>
    </div></div>`;
  }

  function facts() {
    if (!D.facts) return "";
    return `<div class="facts">${D.facts.map((f, i) =>
      `<span class="fact ${i === 0 ? "first" : ""}">${esc(f)}</span>`).join("")}</div>`;
  }

  // One post, one message: a matchup or idea as the headline, the facts that
  // make it useful (day, kickoff, network), then the board, steps, prices or
  // games that back it up.
  function feature() {
    const title = (D.title_lines || [D.title]).map((t) => `<div>${t.split(" at ").map(esc).join('<span class="at">at</span>')}</div>`).join("");
    let body = "";
    if (D.games && shows("games")) {
      let list = "";
      let lastHead = null;
      D.games.forEach((g) => {
        if (D.group_by_day && g.group !== lastHead) {
          list += `<div class="dayhead">${esc(g.group)}</div>`;
          lastHead = g.group;
        }
        list += gameRow(g);
      });
      body += `<div class="list">${list}</div>`;
    }
    if (D.steps && shows("steps")) {
      body += `<div class="steps">${D.steps.map((s, i) => `
        <div class="bigstep"><div class="num">${i + 1}</div><div class="txt"><b>${esc(s.title)}</b>${esc(s.text || "")}</div></div>`).join("")}</div>`;
    }
    if (D.prices && shows("prices")) {
      const money = (n) => "$" + Number(n).toLocaleString("en-US");
      body += `<div class="prices">
        <div class="ph"><span>Per square</span><span>Pot</span><span>${esc(D.prices_cause || "To your cause")}</span></div>
        ${D.prices.map((p) => `<div class="pr ${p.feature ? "feature" : ""}">
          <span class="pp">${money(p.price)}<small>${esc(p.who || "")}</small></span>
          <span>${money(p.price * 100)}</span><span class="pc">${money(p.price * 50)}</span></div>`).join("")}
      </div>`;
    }
    if (D.board && shows("board")) body += board(D.board);
    const hook = D.hook ? `<div class="hook">${esc(D.hook)}</div>` : "";
    return `
      <div class="eyebrow">${esc(D.eyebrow)}</div>
      <div class="ftitle">${title}</div>
      ${facts()}
      <div class="rule"></div>
      <div class="fbody">${body}</div>
      ${hook}${cta()}${footer()}`;
  }

  // Wraps an existing picture (rivalry art, team photos) in the right frame
  // for the channel, with a band that says what this post is about.
  function artframe() {
    const lines = (D.lines || []).map((l) => `<div class="aline">${esc(l)}</div>`).join("");
    return `
      <div class="aband top">
        <div class="eyebrow">${esc(D.eyebrow)}</div>
        <div class="atitle">${esc(D.title)}</div>
        ${facts()}
      </div>
      <div class="aart"><img class="blur" src="${D.art}"><img class="main" src="${D.art}"></div>
      <div class="aband bottom">
        ${lines ? `<div class="alines">${lines}</div>` : ""}
        <div class="apill"><span>${esc((D.cta || {}).ask || "Start a free board")}</span><b>${esc((D.cta || {}).url || "SuperBowlPoolSite.com")}</b></div>
      </div>`;
  }

  const builders = { winners, slate, feature, artframe };
  document.body.className = `fmt-${FMT} ${D.theme ? "theme-" + D.theme : ""}`;
  document.getElementById("page").innerHTML = builders[D.template]();

  // Keep the title on one line beside the date, shrinking it if needed;
  // very long titles wrap instead.
  const page = document.getElementById("page");
  const title = page.querySelector(".title");
  const head = page.querySelector(".head");
  let size = 128;
  while (head && head.scrollWidth > head.clientWidth + 1 && size > 92) {
    size -= 4;
    title.style.fontSize = size + "px";
  }
  if (head && head.scrollWidth > head.clientWidth + 1) title.classList.add("wrap");

  const at = page.querySelector(".atitle");
  if (at) {
    let fs = 76;
    while (at.scrollWidth > at.clientWidth + 1 && fs > 44) {
      fs -= 2;
      at.style.fontSize = fs + "px";
    }
  }

  // Feature titles: as big as fits the width, on as few lines as possible.
  const ft = page.querySelector(".ftitle");
  if (ft) {
    let fs = D.title_size || (FMT === "16x9" ? 120 : 150);
    ft.style.fontSize = fs + "px";
    while ([...ft.children].some((c) => c.scrollWidth > ft.clientWidth + 1) && fs > 60) {
      fs -= 4;
      ft.style.fontSize = fs + "px";
    }
  }

  // Shrink game rows until everything fits the frame.
  let s = 1;
  while (page.scrollHeight > page.clientHeight + 1 && s > 0.55) {
    s -= 0.05;
    document.documentElement.style.setProperty("--s", s.toFixed(2));
  }
  document.title = page.scrollHeight > page.clientHeight + 1 ? "OVERFLOW" : "OK";
})();
