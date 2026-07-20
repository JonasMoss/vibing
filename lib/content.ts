import fs from "node:fs";
import path from "node:path";
import { marked } from "marked";

const contentRoot = path.join(process.cwd(), "content");

marked.use({
  gfm: true,
  breaks: false,
});

function markdownToHtml(markdown: string): string {
  return marked.parse(markdown, { async: false }) as string;
}

export type Day = {
  slug: string;
  number: string;
  date: string;
  eyebrow: string;
  title: string;
  promise: string;
  accent: string;
};

export const days: Day[] = [
  {
    slug: "day-1",
    number: "01",
    date: "Wednesday 12 August",
    eyebrow: "Files",
    title: "Your new intern",
    promise: "Make the terminal useful before we make it familiar.",
    accent: "coral",
  },
  {
    slug: "day-2",
    number: "02",
    date: "Thursday 13 August",
    eyebrow: "Research",
    title: "From material to insight",
    promise: "Use an agent on real research work, then check what it did.",
    accent: "blue",
  },
  {
    slug: "day-3",
    number: "03",
    date: "Friday 14 August",
    eyebrow: "Teaching",
    title: "Make something worth keeping",
    promise: "Build, revise, and ship a real teaching artifact.",
    accent: "green",
  },
];

export function getDay(slug: string): Day | undefined {
  return days.find((day) => day.slug === slug);
}

export function readMarkdown(relativePath: string): string {
  const source = fs.readFileSync(path.join(contentRoot, relativePath), "utf8");
  return markdownToHtml(source);
}

export function readSlides(slug: string): string[] {
  const source = fs.readFileSync(
    path.join(contentRoot, "slides", `${slug}.md`),
    "utf8",
  );

  return source
    .split(/\n---\n/g)
    .map((slide) => slide.trim())
    .filter(Boolean)
    .map(markdownToHtml);
}

