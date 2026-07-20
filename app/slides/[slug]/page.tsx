import type { Metadata } from "next";
import { notFound } from "next/navigation";
import SlideDeck from "@/components/SlideDeck";
import { readSlides } from "@/lib/content";

type SlidePageProps = {
  params: Promise<{ slug: string }>;
};

const decks = {
  opening: {
    title: "Opening: give the model hands",
    kicker: "Day 1 · 10:00",
  },
} as const;

export function generateStaticParams() {
  return Object.keys(decks).map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: SlidePageProps): Promise<Metadata> {
  const { slug } = await params;
  const deck = decks[slug as keyof typeof decks];

  return {
    title: deck?.title ?? "Slides",
  };
}

export default async function SlidePage({ params }: SlidePageProps) {
  const { slug } = await params;
  const deck = decks[slug as keyof typeof decks];

  if (!deck) {
    notFound();
  }

  const slides = readSlides(slug);

  return (
    <SlideDeck slides={slides} title={deck.title} kicker={deck.kicker} />
  );
}

