import { marked } from "marked";
import courseOverview from "@/content/course-overview.md?raw";
import dayOne from "@/content/day-1.md?raw";
import dayTwo from "@/content/day-2.md?raw";
import dayThree from "@/content/day-3.md?raw";
import openingSlides from "@/content/slides/opening.md?raw";

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
  const pages: Record<string, string> = {
    "course-overview.md": courseOverview,
    "day-1.md": dayOne,
    "day-2.md": dayTwo,
    "day-3.md": dayThree,
  };
  const source = pages[relativePath];

  if (!source) {
    throw new Error(`Unknown course page: ${relativePath}`);
  }

  return markdownToHtml(source);
}

export function readSlides(slug: string): string[] {
  const decks: Record<string, string> = {
    opening: openingSlides,
  };
  const source = decks[slug];

  if (!source) {
    throw new Error(`Unknown slide deck: ${slug}`);
  }

  return source
    .split(/\n---\n/g)
    .map((slide) => slide.trim())
    .filter(Boolean)
    .map(markdownToHtml);
}

