import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { days, getDay, readMarkdown } from "@/lib/content";

type DayPageProps = {
  params: Promise<{ slug: string }>;
};

export function generateStaticParams() {
  return days.map((day) => ({ slug: day.slug }));
}

export async function generateMetadata({
  params,
}: DayPageProps): Promise<Metadata> {
  const { slug } = await params;
  const day = getDay(slug);

  return {
    title: day ? `${day.date}: ${day.title}` : "Course day",
  };
}

export default async function DayPage({ params }: DayPageProps) {
  const { slug } = await params;
  const day = getDay(slug);

  if (!day) {
    notFound();
  }

  const content = readMarkdown(`${slug}.md`);
  const currentIndex = days.findIndex((item) => item.slug === slug);
  const previous = days[currentIndex - 1];
  const next = days[currentIndex + 1];

  return (
    <main className={`day-page day-page-${day.accent}`}>
      <header className="day-hero section-shell">
        <Link className="back-link" href="/#course-map">
          ← Course map
        </Link>
        <div className="day-hero-grid">
          <span className="day-hero-number">{day.number}</span>
          <div>
            <span className="eyebrow">
              {day.date} · {day.eyebrow}
            </span>
            <h1>{day.title}</h1>
            <p>{day.promise}</p>
          </div>
        </div>
      </header>

      <article
        className="prose day-content"
        dangerouslySetInnerHTML={{ __html: content }}
      />

      <nav className="day-pagination section-shell" aria-label="Course days">
        {previous ? (
          <Link href={`/days/${previous.slug}`}>
            <small>Previous</small>
            <span>← {previous.title}</span>
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link href={`/days/${next.slug}`}>
            <small>Next</small>
            <span>{next.title} →</span>
          </Link>
        ) : (
          <Link href="/slides/opening">
            <small>Slides</small>
            <span>Opening deck ↗</span>
          </Link>
        )}
      </nav>
    </main>
  );
}

