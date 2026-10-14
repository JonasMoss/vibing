#!/usr/bin/env bash
# Ask one question as several different people (one call each) and show the answers.
#
#   ./ask.sh                                   # Claude Code, the coffee set
#   ./ask.sh codex                             # same with Codex
#   ./ask.sh claude schools                    # the frequentist-vs-Bayesian set
#   ./ask.sh claude coffee "Why is the sky blue?"   # a set, with your own question
#
# A set is a folder: question.txt plus one profile per .md file, in display order
# (1-..., 2-..., ...). Edit them, add new ones, rerun. "blank" (no profile at all)
# always goes first.

set -uo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
tool="${1:-claude}"
set_dir="$here/${2:-coffee}"
[ -f "$set_dir/question.txt" ] || { echo "no such set: ${2:-coffee} (need $set_dir/question.txt)" >&2; exit 1; }
question="${3:-$(cat "$set_dir/question.txt")}"

case "$tool" in claude|codex) ;; *) echo "usage: $0 [claude|codex] [set] [question]" >&2; exit 1 ;; esac

# Work outside any repo: both tools also read context files from the folders
# above, so running inside the course repo would leak its AGENTS.md into everyone.
work="$(mktemp -d "${TMPDIR:-/tmp}/who-is-asking.XXXX")"

names=(blank); mkdir -p "$work/blank"
for f in "$set_dir"/*.md; do
  name="$(basename "$f" .md)"; name="${name#[0-9]-}"
  names+=("$name"); mkdir -p "$work/$name"
  cp "$f" "$work/$name/AGENTS.md"                # Codex reads AGENTS.md
  echo "@AGENTS.md" > "$work/$name/CLAUDE.md"    # Claude Code reads CLAUDE.md
done

ask() {
  cd "$work/$1" || return 1
  case "$tool" in
    # --strict-mcp-config + the env var: no connectors, so no "Google Calendar
    # isn't authorised" chatter tacked onto every answer.
    claude) env -u CLAUDECODE ENABLE_CLAUDEAI_MCP_SERVERS=false \
              claude -p "$question" --no-session-persistence --strict-mcp-config ;;
    codex)  codex exec --skip-git-repo-check --ephemeral "$question" ;;
  esac > "$work/$1.out" 2> "$work/$1.err"
}

# All calls run at once; answers are printed in a fixed order as they arrive.
pids=()
for n in "${names[@]}"; do ask "$n" & pids+=($!); done

if [ -t 1 ]; then B=$'\e[1m' D=$'\e[2m' C=$'\e[36m' R=$'\e[0m'; else B= D= C= R=; fi
rule() { printf '%s%s%s\n' "$C" "━━━ $1 $(printf '━%.0s' $(seq 1 $((60 - ${#1}))))" "$R"; }

printf '\n%sQuestion:%s %s   %s(%s)%s\n\n' "$B" "$R" "$question" "$D" "$tool" "$R"

for i in "${!names[@]}"; do
  n="${names[$i]}"
  wait "${pids[$i]}"
  rule "$n"
  if [ -f "$work/$n/AGENTS.md" ]; then
    profile="$(tr '\n' ' ' < "$work/$n/AGENTS.md" | tr -s ' ')"
    words=$(wc -w < "$work/$n/AGENTS.md")
    [ ${#profile} -gt 90 ] && profile="${profile:0:87}..."
    printf '%sProfile (%s words): %s%s\n\n' "$D" "$words" "$profile" "$R"
  else
    printf '%sProfile: none%s\n\n' "$D" "$R"
  fi
  if [ -s "$work/$n.out" ]; then
    cat "$work/$n.out"
    printf '\n%s(%s words)%s\n\n' "$D" "$(wc -w < "$work/$n.out")" "$R"
  else
    printf '%s[no answer; last lines of the error log:]%s\n' "$B" "$R"; tail -5 "$work/$n.err"; echo
  fi
done

printf '%sAnswers saved in %s%s\n' "$D" "$work" "$R"
