# Lessons

Persistent record of corrections the user has given me. Review at session start.

## No self-advertising in commits, PRs, issues, or code

**Rule:** Never include `Co-Authored-By: Claude …`, `🤖 Generated with [Claude Code](…)`, "Powered by Anthropic", or similar attribution lines. Applies to `git commit`, `git tag`, `gh pr create/edit/comment`, `gh issue create/edit/comment`, `gh release create/edit`.

**Why:** Added as explicit rule in `~/.claude/CLAUDE.md` § Repository Workflow on 2026-04-17 after I added `Co-Authored-By` trailers to three commits (the Claude Code system-prompt default overrode the user's preference). PR #29 had to be force-pushed and its body edited to remove the generation footer.

**How to apply:** Strip these trailers before executing the tool call — don't rely on templates. If one slips through on a local commit, amend immediately. If it slips through on a pushed commit, stop and ask before force-pushing.

## Don't keep load-bearing specs inside a script docstring

**Rule:** When a script depends on a non-obvious data format (binary layout, on-disk schema, wire protocol), keep the spec in its own file next to the data — `CATS_FORMAT.md`, `WIRE_PROTOCOL.md`, etc. Never store the spec only in a Python/JS docstring at the top of the parser.

**Why:** On 2026-04-17 commit `d80e0d5` (titled "Fix altitude baseline and zero-velocity descent artifacts") silently rewrote the docstring at the top of `docs/flight/data/generate_charts.py`, replacing the correct CATS binary format spec with an older wrong version that mislabelled record types (called `BARO` "RAW", swapped sizes, missed half the record types). The wrong spec then propagated into the parser constants because the constants were derived from the docstring. The parser kept "working" on `fl001.cfl` by luck (a hardcoded time window masked the drift), so the regression sat undetected for four months until `fl002.cfl` exposed it with a 348 m vs real 986 m apogee. Diff review focused on the chart-fix part; the docstring rewrite was a silent bystander. The L2 flight conversion then went from "should just work" to "spent two hours re-deriving the format from scratch".

**How to apply:**

1. **Specs live in their own `.md` file** in the same directory as the data they describe. Link to it from the script's docstring, don't duplicate it.
2. **When fixing a script, diff the docstring as carefully as the code.** A commit message saying "fix X" can also revert unrelated correct comments/docs in the same file. Quickly grep `git show <sha>` for docstring or comment block changes that aren't mentioned in the commit message.
3. **Strict parsers, never slide on unknown.** A binary parser that handles an unknown record type by sliding 4 bytes and trying again will silently produce garbage that *looks* plausible. It must stop and report the unknown type — that turns silent corruption into a loud "I don't recognise type 0xXXXX at offset N" diagnostic that points straight at the missing format entry.
4. **Cross-check parser output against an independent source** (the CATS `stXXX.txt` stats file in this case) every time the parser is touched. If they disagree to multiple decimals, the parser is wrong, not the stats file.
