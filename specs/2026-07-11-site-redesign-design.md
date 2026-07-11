# Site Redesign — Mission Control (Amber)

**Date:** 2026-07-11
**Status:** Design approved, implementation pending

## Goal

Replace the stock MkDocs Material indigo look with a distinctive "Mission
Control" visual identity across the whole site: a dark flight-console
aesthetic with monospace telemetry accents, applied to the landing page and
all documentation pages, without losing any Material functionality (search,
light/dark toggle, MathJax, Mermaid, blog, CI deploy).

## Decision summary

- **Direction:** Mission Control — chosen from four presented options
  (Mission Control, Blueprint, Nordic Minimal, Launch Day).
- **Accent:** Amber (A1), chosen over Ice cyan (A2) and Phosphor green (A3).
- **Scheme:** Dark by default; light-mode toggle retained with a warm-white
  variant.
- **Implementation surface:** three files only — `mkdocs.yml`,
  `docs/stylesheets/extra.css`, `docs/index.md`. No Jinja template
  overrides, no new fonts, no content changes on other pages.

## Design tokens

### Dark scheme (default)

| Token | Value | Use |
|---|---|---|
| bg-page | `#0a0e17` | Page background |
| bg-panel | `#0d1220` | Cards, tiles, sidebar, code/formula panels |
| border | `#1f2937` | Panel borders, dividers |
| border-subtle | `#131a2b` | Table row separators, log rows |
| text-primary | `#f8fafc` | Headings, emphasized text |
| text-body | `#cbd5e1` | Body copy |
| text-muted | `#94a3b8` | Secondary text, inactive nav |
| text-faint | `#64748b` | Micro-labels, captions |
| accent | `#fbbf24` | Data readouts, links, active nav, table header rules, warnings |
| success | `#34d399` | Status LED, checkmarks, "nominal" states only |
| info | `#22d3ee` | Note admonitions, sparing secondary accent |

### Light scheme (toggle)

Same structure, remapped: warm-white page (`#faf9f7`), panel `#f1efeb`,
ink text (`#16181d`), borders `#e2ded6`. Text-level amber accents use
`#b45309` (amber-700) because `#fbbf24` fails contrast on white; large
non-text rules/underlines may stay `#fbbf24`. Success `#047857`.

Both palettes are defined as CSS custom properties under
`[data-md-color-scheme="slate"]` and `[data-md-color-scheme="default"]`.

## Typography

- **Body:** Inter (already configured) — all prose, table contents.
- **Data/labels/code:** JetBrains Mono (already configured) — telemetry
  values, micro-labels, code.
- **Micro-label idiom:** 10–11px mono, uppercase, letter-spacing
  0.15–0.25em, text-faint color. Used for eyebrows, table headers, card
  numbers, section labels.
- H1 Inter 700, H2 Inter 600 with a subtle border-bottom rule.
- No new font loads.

## Home page (`docs/index.md`)

Front matter hides the sidebar and TOC (`hide: [navigation, toc]`); the
top nav tabs remain. Sections in order:

1. **Hero** — mono eyebrow `MISSION STATUS ● ALL SYSTEMS NOMINAL` with a
   glowing green LED dot; H1 `SIPSIK — TRIPOLI L2 CERTIFIED`; two mono
   sub-lines (Apogee Peregrine · 100 mm · dual deploy via CATS Vega /
   built in Estonia · flown at Enköping, Sweden · next objective: L3).
   Background: faint horizontal scanlines + amber radial glow.
2. **Telemetry tiles** (4-up grid, 1px-gap borders): CERTS COMPLETE
   `L1 + L2` · LAST MOTOR `J350` · LIFTOFF MASS `3100 g` · MAIN DEPLOY
   `146 m`.
3. **Mission Log** — one row per cert flight with green check, date,
   title, mono details, and an amber `REPORT →` link:
   - `✓ 2026-02-22 FLIGHT 02 — L2 CERTIFICATION · J350 · DUAL DEPLOY · NOMINAL` → `flight/flight2-analysis.md`
   - `✓ 2026-01-24 FLIGHT 01 — L1 CERTIFICATION · H128W · 140.8 M · MOTOR EJECT` → `flight/flight1-analysis.md`
4. **Documentation grid** — six numbered cards (01 Certification,
   02 Construction, 03 Calculations, 04 Simulations, 05 Flight,
   06 Photos), each with a one-line mono description. A compact links
   row below covers Configurations, Decisions, Blog, References.
5. **Story + acknowledgments** — existing Sipsik story text and
   acknowledgments preserved as prose, restyled; build-hash footer line
   preserved.

## Documentation pages (CSS-only restyle)

- **Nav tabs:** mono uppercase 11px letterspaced; active tab gets a 2px
  amber underline. Header bar `bg-panel`.
- **Site identity:** `site_name` changes `Peregrine` → `SIPSIK` to match
  the approved mockups (affects browser titles). Logo image retained.
- **Sidebar:** section titles as micro-labels; active item amber text,
  2px amber left bar, faint amber background tint.
- **Search:** dark pill-style input.
- **Tables:** header cells become micro-labels with an amber
  border-bottom rule (replaces the solid indigo header background); body
  stays Inter; row separators `border-subtle`; existing `.specs-table`
  and comparison tables must remain readable.
- **Admonitions:** flat `bg-panel` with a 1px type-colored border and
  colored title — warning/danger amber-red family, note/info cyan,
  success green. No heavy shadows.
- **Formula blocks (MathJax display math):** `bg-panel` panel with 2px
  amber left border and padding; text color inherits scheme.
- **Code blocks:** `bg-panel` with `border` outline.
- **Images:** 1px `border`, 6px radius; current drop shadow removed.
- **Status badges** (`.status-*`): recolored to console palette.
- **Existing `.card`/`.grid` classes** (used on configurations page
  etc.): restyled to match the documentation grid.
- **Footer:** dark, minimal, mono micro-labels.

## Out of scope

No nav restructuring, no content edits beyond the `index.md` layout, no
new pages, no template overrides, no font additions, no changes to CI.

## Risks and mitigations

- **Mermaid on dark:** Material themes Mermaid per scheme automatically;
  verify diagram contrast on the dark scheme and override Mermaid CSS
  variables only if needed.
- **MathJax legibility:** formulas inherit text color; verify on both
  schemes on `calculations/ejection-charges.md`.
- **Amber contrast in light mode:** mitigated via `#b45309` for
  text-level accents.
- **Table restyle regressions:** visual pass on `configurations.md` and
  `simulations/` pages, which have the densest tables.

## Verification plan

1. `mkdocs build` completes with no new warnings (compare against a
   baseline build from main).
2. Visual pass in both schemes at desktop and mobile widths: home,
   `calculations/ejection-charges.md` (MathJax), `simulations/openrocket.md`
   (tables), `configurations.md` (cards + tables), a Mermaid-bearing page,
   `photos/index.md`, one blog post.
3. Check nav tabs, sidebar highlight, search styling, footer, and the
   light/dark toggle round-trip.
