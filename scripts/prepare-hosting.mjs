import { copyFile, mkdir, rename, rm, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const serverEntry = fileURLToPath(
  new URL("../dist/server/index.js", import.meta.url),
);
const vinextHandler = fileURLToPath(
  new URL("../dist/server/vinext-handler.js", import.meta.url),
);
const manifestSource = fileURLToPath(
  new URL("../.openai/hosting.json", import.meta.url),
);
const manifestDirectory = fileURLToPath(
  new URL("../dist/.openai/", import.meta.url),
);
const manifestTarget = fileURLToPath(
  new URL("../dist/.openai/hosting.json", import.meta.url),
);

await rm(vinextHandler, { force: true });
await rename(serverEntry, vinextHandler);
await writeFile(
  serverEntry,
  [
    'import handleRequest from "./vinext-handler.js";',
    "",
    "async function worker(request, ...context) {",
    "  return handleRequest(request, ...context);",
    "}",
    "",
    "worker.fetch = handleRequest;",
    "",
    "export { handleRequest as fetch };",
    "export default worker;",
    "",
  ].join("\n"),
);

await mkdir(manifestDirectory, { recursive: true });
await copyFile(manifestSource, manifestTarget);

console.log("Prepared hosting manifest.");
