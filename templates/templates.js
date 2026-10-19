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
          <div class="match">${esc(g.away)}<span class="at">at</span>${esc(g.home)}</div>
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

  const builders = { winners, slate };
  document.body.className = `fmt-${FMT} ${D.theme ? "theme-" + D.theme : ""}`;
  document.getElementById("page").innerHTML = builders[D.template]();

  // Keep the title on one line beside the date, shrinking it if needed;
  // very long titles wrap instead.
  const page = document.getElementById("page");
  const title = page.querySelector(".title");
  const head = page.querySelector(".head");
  let size = 128;
  while (head.scrollWidth > head.clientWidth + 1 && size > 92) {
    size -= 4;
    title.style.fontSize = size + "px";
  }
  if (head.scrollWidth > head.clientWidth + 1) title.classList.add("wrap");

  // Shrink game rows until everything fits the frame.
  let s = 1;
  while (page.scrollHeight > page.clientHeight + 1 && s > 0.55) {
    s -= 0.05;
    document.documentElement.style.setProperty("--s", s.toFixed(2));
  }
  document.title = page.scrollHeight > page.clientHeight + 1 ? "OVERFLOW" : "OK";
})();
