await import("./build-site.mjs");
const { default: worker } = await import(
  `../dist/server/index.js?check=${Date.now()}`
);

const routes = [
  "/",
  "/days/day-1",
  "/days/day-2",
  "/days/day-3",
  "/slides/opening",
];

for (const route of routes) {
  const response = await worker.fetch(new Request(`https://example.test${route}`));
  const html = await response.text();

  if (response.status !== 200 || !html.startsWith("<!doctype html>")) {
    throw new Error(`Invalid output for ${route}: HTTP ${response.status}`);
  }
}

const missing = await worker.fetch(
  new Request("https://example.test/does-not-exist"),
);

if (missing.status !== 404) {
  throw new Error(`Expected a 404, received HTTP ${missing.status}`);
}

console.log(`Checked ${routes.length} course routes and the 404 page.`);
