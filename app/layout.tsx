import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "AI in the terminal",
    template: "%s · AI in the terminal",
  },
  description:
    "Course materials for AI in the terminal: Claude Code and Codex for research and teaching.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <Link className="wordmark" href="/">
            <span className="wordmark-mark" aria-hidden="true">
              &gt;_
            </span>
            <span>AI in the terminal</span>
          </Link>
          <nav aria-label="Main navigation">
            <Link href="/#course-map">Three days</Link>
            <Link href="/slides/opening">Opening deck</Link>
          </nav>
        </header>
        {children}
      </body>
    </html>
  );
}

