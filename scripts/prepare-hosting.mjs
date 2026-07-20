import { copyFile, mkdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const manifestSource = fileURLToPath(
  new URL("../.openai/hosting.json", import.meta.url),
);
const manifestDirectory = fileURLToPath(
  new URL("../dist/.openai/", import.meta.url),
);
const manifestTarget = fileURLToPath(
  new URL("../dist/.openai/hosting.json", import.meta.url),
);

await mkdir(manifestDirectory, { recursive: true });
await copyFile(manifestSource, manifestTarget);

console.log("Prepared hosting manifest.");
