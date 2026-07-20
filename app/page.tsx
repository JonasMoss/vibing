import Link from "next/link";
import { days, readMarkdown } from "@/lib/content";

export default function Home() {
  const overview = readMarkdown("course-overview.md");

  return (
    <main>
      <section className="hero">
        <div className="hero-kicker">
          <span>BI faculty course</span>
          <span>Oslo · August 2026</span>
        </div>

        <div className="hero-grid">
          <div>
            <h1>
              AI in the
              <br />
              <em>terminal</em>
            </h1>
            <p className="hero-subtitle">
              Claude Code and Codex for research and teaching
            </p>
          </div>

          <aside className="hero-note" aria-label="Course details">
            <p className="scribble">Three days of doing.</p>
            <dl>
              <div>
                <dt>When</dt>
                <dd>12–14 August 2026</dd>
              </div>
              <div>
                <dt>Time</dt>
                <dd>10:00–16:00</dd>
              </div>
              <div>
                <dt>Where</dt>
                <dd>C2-040 “Harvard”</dd>
              </div>
            </dl>
          </aside>
        </div>

        <div className="hero-actions">
          <Link className="button button-primary" href="/slides/opening">
            Open the first deck <span aria-hidden="true">↗</span>
          </Link>
          <a className="button button-quiet" href="#course-map">
            See the course
          </a>
        </div>
      </section>

      <section className="manifesto section-shell">
        <div className="section-label">The premise</div>
        <div
          className="prose prose-large"
          dangerouslySetInnerHTML={{ __html: overview }}
        />
      </section>

      <section className="agent-demo section-shell" aria-label="Core idea">
        <div className="terminal-card">
          <div className="terminal-bar">
            <span />
            <span />
            <span />
            <small>your-course-folder</small>
          </div>
          <div className="terminal-copy">
            <span className="terminal-prompt">&gt;</span>
            <p>
              Look through this mess. Tell me what you see, propose a sensible
              structure, and wait for my approval before changing anything.
            </p>
          </div>
        </div>
        <div className="agent-demo-copy">
          <span className="eyebrow">The whole course, really</span>
          <h2>Give the model a folder and something real to do.</h2>
          <p>
            A chatbot can suggest. An agent can inspect, create, organise,
            build, check, and revise—while you remain responsible for the work.
          </p>
        </div>
      </section>

      <section className="course-map section-shell" id="course-map">
        <div className="section-heading">
          <div>
            <span className="eyebrow">15 hours · mostly hands-on</span>
            <h2>Three days, three kinds of mess</h2>
          </div>
          <p>
            Each day ends with something that exists outside the chat window.
          </p>
        </div>

        <div className="day-grid">
          {days.map((day) => (
            <Link
              className={`day-card day-card-${day.accent}`}
              href={`/days/${day.slug}`}
              key={day.slug}
            >
              <div className="day-card-top">
                <span className="day-number">{day.number}</span>
                <span className="day-date">{day.date}</span>
              </div>
              <span className="eyebrow">{day.eyebrow}</span>
              <h3>{day.title}</h3>
              <p>{day.promise}</p>
              <span className="card-link">
                Open the rough plan <span aria-hidden="true">→</span>
              </span>
            </Link>
          ))}
        </div>
      </section>

      <section className="principles section-shell">
        <div className="section-label">Our working agreement</div>
        <div className="principle-grid">
          <article>
            <span>01</span>
            <h3>Start with copies</h3>
            <p>Experiments are cheap when the original is safe.</p>
          </article>
          <article>
            <span>02</span>
            <h3>Talk normally</h3>
            <p>Describe the outcome. Argue with the plan. Refine as you go.</p>
          </article>
          <article>
            <span>03</span>
            <h3>Look at the work</h3>
            <p>The model supplies speed. You supply judgement.</p>
          </article>
        </div>
      </section>

      <footer className="site-footer">
        <p>
          <strong>AI in the terminal</strong>
          <br />
          BI Norwegian Business School
        </p>
        <p>
          Jonas Moss
          <br />
          <a href="mailto:jonas.moss@bi.no">jonas.moss@bi.no</a>
        </p>
      </footer>
    </main>
  );
}

