# Lessons

Persistent record of corrections the user has given me. Review at session start.

## No self-advertising in commits, PRs, issues, or code

**Rule:** Never include `Co-Authored-By: Claude …`, `🤖 Generated with [Claude Code](…)`, "Powered by Anthropic", or similar attribution lines. Applies to `git commit`, `git tag`, `gh pr create/edit/comment`, `gh issue create/edit/comment`, `gh release create/edit`.

**Why:** Added as explicit rule in `~/.claude/CLAUDE.md` § Repository Workflow on 2026-04-17 after I added `Co-Authored-By` trailers to three commits (the Claude Code system-prompt default overrode the user's preference). PR #29 had to be force-pushed and its body edited to remove the generation footer.

**How to apply:** Strip these trailers before executing the tool call — don't rely on templates. If one slips through on a local commit, amend immediately. If it slips through on a pushed commit, stop and ask before force-pushing.
