import { copyFile, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";

const root = fileURLToPath(new URL("../", import.meta.url));
const fromRoot = (...parts) => join(root, ...parts);

marked.use({
  gfm: true,
  breaks: false,
});

const read = (relativePath) => readFile(fromRoot(relativePath), "utf8");
const markdown = (source) => marked.parse(source, { async: false });
const escapeHtml = (value) =>
  String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");

const [styles, overviewSource, dayOneSource, dayTwoSource, dayThreeSource, openingSource] =
  await Promise.all([
    read("site/styles.css"),
    read("content/course-overview.md"),
    read("content/day-1.md"),
    read("content/day-2.md"),
    read("content/day-3.md"),
    read("content/slides/opening.md"),
  ]);

const days = [
  {
    slug: "day-1",
    number: "01",
    date: "Wednesday 12 August",
    eyebrow: "Files",
    title: "Your new intern",
    promise: "Make the terminal useful before we make it familiar.",
    accent: "coral",
    source: dayOneSource,
  },
  {
    slug: "day-2",
    number: "02",
    date: "Thursday 13 August",
    eyebrow: "Research",
    title: "From material to insight",
    promise: "Use an agent on real research work, then check what it did.",
    accent: "blue",
    source: dayTwoSource,
  },
  {
    slug: "day-3",
    number: "03",
    date: "Friday 14 August",
    eyebrow: "Teaching",
    title: "Make something worth keeping",
    promise: "Build, revise, and ship a real teaching artifact.",
    accent: "green",
    source: dayThreeSource,
  },
];

const siteHeader = `
  <header class="site-header">
    <a class="wordmark" href="/">
      <span class="wordmark-mark" aria-hidden="true">&gt;_</span>
      <span>AI in the terminal</span>
    </a>
    <nav aria-label="Main navigation">
      <a href="/#course-map">Three days</a>
      <a href="/slides/opening">Opening deck</a>
    </nav>
  </header>`;

function documentPage({ title, body, description, includeHeader = true, script = "" }) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${escapeHtml(description)}">
  <title>${escapeHtml(title)} · AI in the terminal</title>
  <style>${styles}</style>
</head>
<body>
${includeHeader ? siteHeader : ""}
${body}
${script ? `<script>${script}</script>` : ""}
</body>
</html>`;
}

const dayCards = days
  .map(
    (day) => `
      <a class="day-card day-card-${day.accent}" href="/days/${day.slug}">
        <div class="day-card-top">
          <span class="day-number">${day.number}</span>
          <span class="day-date">${day.date}</span>
        </div>
        <span class="eyebrow">${day.eyebrow}</span>
        <h3>${day.title}</h3>
        <p>${day.promise}</p>
        <span class="card-link">
          Open the rough plan <span aria-hidden="true">→</span>
        </span>
      </a>`,
  )
  .join("");

const homeBody = `
<main>
  <section class="hero">
    <div class="hero-kicker">
      <span>BI faculty course</span>
      <span>Oslo · August 2026</span>
    </div>

    <div class="hero-grid">
      <div>
        <h1>AI in the<br><em>terminal</em></h1>
        <p class="hero-subtitle">Claude Code and Codex for research and teaching</p>
      </div>

      <aside class="hero-note" aria-label="Course details">
        <p class="scribble">Three days of doing.</p>
        <dl>
          <div><dt>When</dt><dd>12–14 August 2026</dd></div>
          <div><dt>Time</dt><dd>10:00–16:00</dd></div>
          <div><dt>Where</dt><dd>C2-040 “Harvard”</dd></div>
        </dl>
      </aside>
    </div>

    <div class="hero-actions">
      <a class="button button-primary" href="/slides/opening">
        Open the first deck <span aria-hidden="true">↗</span>
      </a>
      <a class="button button-quiet" href="#course-map">See the course</a>
    </div>
  </section>

  <section class="manifesto section-shell">
    <div class="section-label">The premise</div>
    <div class="prose prose-large">${markdown(overviewSource)}</div>
  </section>

  <section class="agent-demo section-shell" aria-label="Core idea">
    <div class="terminal-card">
      <div class="terminal-bar">
        <span></span><span></span><span></span>
        <small>your-course-folder</small>
      </div>
      <div class="terminal-copy">
        <span class="terminal-prompt">&gt;</span>
        <p>Look through this mess. Tell me what you see, propose a sensible
        structure, and wait for my approval before changing anything.</p>
      </div>
    </div>
    <div class="agent-demo-copy">
      <span class="eyebrow">The whole course, really</span>
      <h2>Give the model a folder and something real to do.</h2>
      <p>A chatbot can suggest. An agent can inspect, create, organise,
      build, check, and revise—while you remain responsible for the work.</p>
    </div>
  </section>

  <section class="course-map section-shell" id="course-map">
    <div class="section-heading">
      <div>
        <span class="eyebrow">15 hours · mostly hands-on</span>
        <h2>Three days, three kinds of mess</h2>
      </div>
      <p>Each day ends with something that exists outside the chat window.</p>
    </div>
    <div class="day-grid">${dayCards}</div>
  </section>

  <section class="principles section-shell">
    <div class="section-label">Our working agreement</div>
    <div class="principle-grid">
      <article>
        <span>01</span><h3>Start with copies</h3>
        <p>Experiments are cheap when the original is safe.</p>
      </article>
      <article>
        <span>02</span><h3>Talk normally</h3>
        <p>Describe the outcome. Argue with the plan. Refine as you go.</p>
      </article>
      <article>
        <span>03</span><h3>Look at the work</h3>
        <p>The model supplies speed. You supply judgement.</p>
      </article>
    </div>
  </section>

  <footer class="site-footer">
    <p><strong>AI in the terminal</strong><br>BI Norwegian Business School</p>
    <p>Jonas Moss<br><a href="mailto:jonas.moss@bi.no">jonas.moss@bi.no</a></p>
  </footer>
</main>`;

function renderDay(day, index) {
  const previous = days[index - 1];
  const next = days[index + 1];
  const previousLink = previous
    ? `<a href="/days/${previous.slug}"><small>Previous</small><span>← ${previous.title}</span></a>`
    : "<span></span>";
  const nextLink = next
    ? `<a href="/days/${next.slug}"><small>Next</small><span>${next.title} →</span></a>`
    : `<a href="/slides/opening"><small>Slides</small><span>Opening deck ↗</span></a>`;

  const body = `
<main class="day-page day-page-${day.accent}">
  <header class="day-hero section-shell">
    <a class="back-link" href="/#course-map">← Course map</a>
    <div class="day-hero-grid">
      <span class="day-hero-number">${day.number}</span>
      <div>
        <span class="eyebrow">${day.date} · ${day.eyebrow}</span>
        <h1>${day.title}</h1>
        <p>${day.promise}</p>
      </div>
    </div>
  </header>
  <article class="prose day-content">${markdown(day.source)}</article>
  <nav class="day-pagination section-shell" aria-label="Course days">
    ${previousLink}
    ${nextLink}
  </nav>
</main>`;

  return documentPage({
    title: `${day.date}: ${day.title}`,
    description: day.promise,
    body,
  });
}

const slides = openingSource
  .split(/\n---\n/g)
  .map((slide) => slide.trim())
  .filter(Boolean)
  .map(markdown);

const slideData = JSON.stringify(slides).replaceAll("<", "\\u003c");
const slideScript = `
(() => {
  const slides = ${slideData};
  let current = 0;
  const slide = document.querySelector(".slide");
  const content = document.querySelector(".slide-content");
  const counter = document.querySelector(".deck-progress span");
  const bar = document.querySelector(".deck-progress i");
  const previous = document.querySelector('[data-action="previous"]');
  const next = document.querySelector('[data-action="next"]');
  const fullscreen = document.querySelector('[data-action="fullscreen"]');

  function goTo(index) {
    current = Math.min(Math.max(index, 0), slides.length - 1);
    content.innerHTML = slides[current];
    slide.className = "slide slide-" + ((current % 4) + 1);
    counter.textContent =
      String(current + 1).padStart(2, "0") + " / " +
      String(slides.length).padStart(2, "0");
    bar.style.width = (((current + 1) / slides.length) * 100) + "%";
    previous.disabled = current === 0;
    next.disabled = current === slides.length - 1;
  }

  async function toggleFullscreen() {
    if (document.fullscreenElement) {
      await document.exitFullscreen();
    } else {
      await document.documentElement.requestFullscreen();
    }
  }

  previous.addEventListener("click", () => goTo(current - 1));
  next.addEventListener("click", () => goTo(current + 1));
  fullscreen.addEventListener("click", toggleFullscreen);

  window.addEventListener("keydown", (event) => {
    if (["ArrowRight", "ArrowDown", " ", "PageDown"].includes(event.key)) {
      event.preventDefault();
      goTo(current + 1);
    }
    if (["ArrowLeft", "ArrowUp", "PageUp"].includes(event.key)) {
      event.preventDefault();
      goTo(current - 1);
    }
    if (event.key.toLowerCase() === "f") {
      event.preventDefault();
      toggleFullscreen();
    }
    if (event.key === "Home") goTo(0);
    if (event.key === "End") goTo(slides.length - 1);
  });

  goTo(0);
})();`;

const slideBody = `
<main class="deck-shell">
  <header class="deck-header">
    <a href="/">← Course</a>
    <div><span>Day 1 · 10:00</span><strong>Opening: give the model hands</strong></div>
    <button data-action="fullscreen" type="button">Fullscreen <kbd>F</kbd></button>
  </header>
  <section class="slide slide-1" aria-live="polite">
    <div class="slide-content">${slides[0]}</div>
    <span class="slide-corner" aria-hidden="true">&gt;_</span>
  </section>
  <footer class="deck-controls">
    <button data-action="previous" aria-label="Previous slide" type="button">←</button>
    <div class="deck-progress" aria-label="Slide progress">
      <span>01 / ${String(slides.length).padStart(2, "0")}</span>
      <div><i style="width:${100 / slides.length}%"></i></div>
    </div>
    <button data-action="next" aria-label="Next slide" type="button">→</button>
  </footer>
</main>`;

const pages = {
  "/": documentPage({
    title: "Course hub",
    description:
      "AI in the terminal: Claude Code and Codex for research and teaching.",
    body: homeBody,
  }),
  "/slides/opening": documentPage({
    title: "Opening: give the model hands",
    description: "Opening slides for AI in the terminal.",
    body: slideBody,
    includeHeader: false,
    script: slideScript,
  }),
};

for (const [index, day] of days.entries()) {
  pages[`/days/${day.slug}`] = renderDay(day, index);
}

const notFound = documentPage({
  title: "Page not found",
  description: "This course page does not exist.",
  body: `
    <main class="day-content prose">
      <h1>Nothing here.</h1>
      <p>The agent may have tidied this page a little too enthusiastically.</p>
      <p><a class="button button-primary" href="/">Return to the course</a></p>
    </main>`,
});

const workerSource = `const pages = ${JSON.stringify(pages)};
const notFound = ${JSON.stringify(notFound)};

function routePath(url) {
  const pathname = new URL(url).pathname;
  return pathname.length > 1 ? pathname.replace(/\\/+$/, "") : "/";
}

export default {
  async fetch(request) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", {
        status: 405,
        headers: { Allow: "GET, HEAD" },
      });
    }

    const html = pages[routePath(request.url)];
    const status = html ? 200 : 404;
    const body = request.method === "HEAD" ? null : (html || notFound);

    return new Response(body, {
      status,
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "public, max-age=60",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "X-Content-Type-Options": "nosniff",
      },
    });
  },
};
`;

const dist = fromRoot("dist");
await rm(dist, { recursive: true, force: true });
await mkdir(fromRoot("dist/server"), { recursive: true });
await mkdir(fromRoot("dist/.openai"), { recursive: true });
await writeFile(fromRoot("dist/server/index.js"), workerSource);
await copyFile(
  fromRoot(".openai/hosting.json"),
  fromRoot("dist/.openai/hosting.json"),
);

console.log(`Built ${Object.keys(pages).length} course pages.`);

// Reused by scripts/build-pages.mjs to emit a static site for GitHub Pages.
export { pages, notFound };

