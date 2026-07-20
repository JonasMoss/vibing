import { createServer } from "node:http";
import { Readable } from "node:stream";

const { default: worker } = await import("../dist/server/index.js");
const host = process.env.HOST ?? "127.0.0.1";
const port = Number(process.env.PORT ?? 3000);

const server = createServer(async (incoming, outgoing) => {
  try {
    const url = new URL(incoming.url ?? "/", `http://${incoming.headers.host}`);
    const request = new Request(url, {
      method: incoming.method,
      headers: incoming.headers,
    });
    const response = await worker.fetch(request);
    outgoing.writeHead(response.status, Object.fromEntries(response.headers));

    if (response.body) {
      Readable.fromWeb(response.body).pipe(outgoing);
    } else {
      outgoing.end();
    }
  } catch (error) {
    console.error(error);
    outgoing.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
    outgoing.end("Internal server error");
  }
});

server.listen(port, host, () => {
  console.log(`Course site running at http://${host}:${port}`);
});

