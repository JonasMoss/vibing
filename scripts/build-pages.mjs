import { mkdir, rm, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { pages, notFound } from "./build-site.mjs";

const root = fileURLToPath(new URL("../", import.meta.url));
const outDir = join(root, "_site");

// GitHub Pages serves extensionless URLs from a matching ".html" file, so we
// write flat files (e.g. /days/day-1 -> days/day-1.html). This mirrors the
// site's own root-absolute links exactly, with no redirect hops.
function outputPath(route) {
  if (route === "/") return "index.html";
  return `${route.replace(/^\/+/, "").replace(/\/+$/, "")}.html`;
}

await rm(outDir, { recursive: true, force: true });

for (const [route, html] of Object.entries(pages)) {
  const filePath = join(outDir, outputPath(route));
  await mkdir(dirname(filePath), { recursive: true });
  await writeFile(filePath, html);
}

// GitHub Pages serves 404.html for unknown paths.
await writeFile(join(outDir, "404.html"), notFound);
// CNAME binds this artifact to the custom domain on every deploy.
await writeFile(join(outDir, "CNAME"), "vibing.jonasmoss.com\n");
// Belt-and-suspenders: keep GitHub from running Jekyll over the output.
await writeFile(join(outDir, ".nojekyll"), "");

console.log(
  `Wrote ${Object.keys(pages).length} pages + 404 to _site/ (domain: vibing.jonasmoss.com).`,
);
