# How these things work

Three stages of training, and which model to use.

---

# Three stages

<div class="figure">
<svg class="diagram" viewBox="0 0 1264 310" preserveAspectRatio="xMinYMid meet" role="img" aria-label="Three stages: pre-training, feedback, thinking"><defs><marker id="pipe-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#17201f"/></marker></defs><rect x="2" y="10" width="390" height="290" rx="18" fill="#fffdf8" stroke="#17201f" stroke-width="3"/><circle cx="52" cy="72" r="30" fill="#f0674d"/><text x="52" y="84" text-anchor="middle" font-size="34" font-weight="800" fill="#17201f">1</text><text x="100" y="86" font-size="40" font-weight="800" fill="#17201f">Pre-training</text><text x="30" y="178" font-size="31" fill="#17201f">Reads the internet</text><text x="30" y="234" font-size="31" fill="#17201f">Predicts the next word</text><g class="reveal" data-step="1"><line x1="396" y1="160" x2="429" y2="160" stroke="#17201f" stroke-width="4" marker-end="url(#pipe-arrow)"/><rect x="437" y="10" width="390" height="290" rx="18" fill="#fffdf8" stroke="#17201f" stroke-width="3"/><circle cx="487" cy="72" r="30" fill="#f0674d"/><text x="487" y="84" text-anchor="middle" font-size="34" font-weight="800" fill="#17201f">2</text><text x="535" y="86" font-size="40" font-weight="800" fill="#17201f">Feedback</text><text x="465" y="178" font-size="31" fill="#17201f">People rank answers</text><text x="465" y="234" font-size="31" fill="#17201f">Maths and code checked</text></g><g class="reveal" data-step="2"><line x1="831" y1="160" x2="864" y2="160" stroke="#17201f" stroke-width="4" marker-end="url(#pipe-arrow)"/><rect x="872" y="10" width="390" height="290" rx="18" fill="#fffdf8" stroke="#17201f" stroke-width="3"/><circle cx="922" cy="72" r="30" fill="#f0674d"/><text x="922" y="84" text-anchor="middle" font-size="34" font-weight="800" fill="#17201f">3</text><text x="970" y="86" font-size="40" font-weight="800" fill="#17201f">Thinking</text><text x="900" y="178" font-size="31" fill="#17201f">Works it out first</text><text x="900" y="234" font-size="31" fill="#17201f">More effort, slower</text></g></svg>
</div>

---

# Why it can prove theorems

- Pre-training gives it language and broad knowledge, but not reliability.
- Feedback with a checker rewards answers that are actually right: a proof that verifies, code that runs.
- Thinking lets it try, check and revise before it answers.
- It writes what is likely. It does not look things up unless it searches.

---

# Which model

| | Claude Code | Codex |
|---|---|---|
| **Good** | Opus, Fable | Astra, Sol |
| **Fast** | Sonnet, Haiku | Terra, Luna |

- Use the Good model by default.
- Fast is for quick, simple questions.
- Switch with `/model` in either tool.
