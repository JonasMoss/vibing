"use client";

import Link from "next/link";
import { useCallback, useEffect, useState } from "react";

type SlideDeckProps = {
  slides: string[];
  title: string;
  kicker: string;
};

export default function SlideDeck({
  slides,
  title,
  kicker,
}: SlideDeckProps) {
  const [current, setCurrent] = useState(0);

  const goTo = useCallback(
    (index: number) => {
      setCurrent(Math.min(Math.max(index, 0), slides.length - 1));
    },
    [slides.length],
  );

  const toggleFullscreen = useCallback(async () => {
    if (document.fullscreenElement) {
      await document.exitFullscreen();
    } else {
      await document.documentElement.requestFullscreen();
    }
  }, []);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
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
        void toggleFullscreen();
      }

      if (event.key === "Home") {
        goTo(0);
      }

      if (event.key === "End") {
        goTo(slides.length - 1);
      }
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [current, goTo, slides.length, toggleFullscreen]);

  return (
    <main className="deck-shell">
      <header className="deck-header">
        <Link href="/">← Course</Link>
        <div>
          <span>{kicker}</span>
          <strong>{title}</strong>
        </div>
        <button onClick={() => void toggleFullscreen()} type="button">
          Fullscreen <kbd>F</kbd>
        </button>
      </header>

      <section
        className={`slide slide-${(current % 4) + 1}`}
        aria-live="polite"
      >
        <div
          className="slide-content"
          dangerouslySetInnerHTML={{ __html: slides[current] }}
        />
        <span className="slide-corner" aria-hidden="true">
          &gt;_
        </span>
      </section>

      <footer className="deck-controls">
        <button
          aria-label="Previous slide"
          disabled={current === 0}
          onClick={() => goTo(current - 1)}
          type="button"
        >
          ←
        </button>
        <div className="deck-progress" aria-label="Slide progress">
          <span>
            {String(current + 1).padStart(2, "0")} /{" "}
            {String(slides.length).padStart(2, "0")}
          </span>
          <div>
            <i
              style={{ width: `${((current + 1) / slides.length) * 100}%` }}
            />
          </div>
        </div>
        <button
          aria-label="Next slide"
          disabled={current === slides.length - 1}
          onClick={() => goTo(current + 1)}
          type="button"
        >
          →
        </button>
      </footer>
    </main>
  );
}

