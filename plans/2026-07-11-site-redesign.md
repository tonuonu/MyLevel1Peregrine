# Mission Control Site Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the entire MkDocs site to the approved "Mission Control / Amber" dark-first console aesthetic per `specs/2026-07-11-site-redesign-design.md`.

**Architecture:** Pure theme-layer change on MkDocs Material 9.7.6 — flip the palette to dark-default in `mkdocs.yml`, rewrite `docs/stylesheets/extra.css` around a console token set (CSS custom properties for both schemes), and rebuild `docs/index.md` as a mission-control landing page. No Jinja overrides, no new fonts, no new dependencies.

**Tech Stack:** MkDocs 1.6.1, mkdocs-material 9.7.6 (`/usr/local/bin/mkdocs`), CSS custom properties, Markdown with `attr_list` + `md_in_html`.

## Global Constraints

- Work on branch `feature/site-redesign`; never push to `main`; end with a PR and STOP (no merge).
- NO attribution lines anywhere: no `Co-Authored-By: Claude`, no `🤖 Generated with…` in commits or the PR body — strip them from any tool-suggested template.
- Only these files may change: `mkdocs.yml`, `docs/stylesheets/extra.css`, `docs/index.md` (plus checkbox ticks in `plans/2026-07-11-site-redesign.md`).
- Design tokens verbatim from the spec — dark: bg `#0a0e17`, panel `#0d1220`, border `#1f2937`, border-subtle `#131a2b`, text `#f8fafc`, body `#cbd5e1`, muted `#94a3b8`, faint `#64748b`, accent `#fbbf24`, success `#34d399`, info `#22d3ee`; light: bg `#faf9f7`, panel `#f1efeb`, ink `#16181d`, borders `#e2ded6`, accent `#b45309`, success `#047857`.
- Fonts stay Inter (body) + JetBrains Mono (data/code). No font additions.
- `mkdocs build` must stay warning-clean relative to the baseline captured in Task 1.

---

### Task 1: Dark-first palette + site identity (`mkdocs.yml`)

**Files:**
- Modify: `mkdocs.yml:1` (site_name) and `mkdocs.yml:29-43` (palette block)

**Interfaces:**
- Produces: color schemes `slate` (default) and `default` (toggle) with `primary: custom` / `accent: custom` — Tasks 2–4 hang all CSS off `[data-md-color-scheme="slate"]` and `[data-md-color-scheme="default"]`.

- [ ] **Step 1: Capture baseline build log**

```bash
cd /Users/tonu/MyLevel1Peregrine
mkdocs build 2>&1 | tee /private/tmp/claude-501/-Users-tonu-MyLevel1Peregrine/b9a5f7da-ea26-491d-9aac-bafcdf538158/scratchpad/baseline-build.log
```

Expected: exits 0. Note any pre-existing WARNING lines — they are the baseline.

- [ ] **Step 2: Edit `mkdocs.yml`**

Change line 1:

```yaml
site_name: SIPSIK
```

Replace the whole `palette:` block (currently lines 29–43, the two `media:`-keyed entries) with:

```yaml
  palette:
    - scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-night
        name: Switch to light mode
    - scheme: default
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode
```

Note: no `media:` keys — the first entry (slate) becomes the default for everyone regardless of OS preference, per spec "dark by default".

- [ ] **Step 3: Rebuild and diff against baseline**

```bash
mkdocs build 2>&1 | tee /private/tmp/claude-501/-Users-tonu-MyLevel1Peregrine/b9a5f7da-ea26-491d-9aac-bafcdf538158/scratchpad/task1-build.log
grep -c 'data-md-color-scheme="slate"' site/index.html
```

Expected: build exits 0 with no NEW warnings vs `baseline-build.log`; grep prints `1` (dark scheme is the default in rendered HTML).

- [ ] **Step 4: Commit**

```bash
git add mkdocs.yml
git commit -m "Switch site to dark-first custom palette, rename site to SIPSIK"
```

---

### Task 2: Console tokens + global chrome (`extra.css` rewrite, part 1)

**Files:**
- Modify: `docs/stylesheets/extra.css` (full replacement)

**Interfaces:**
- Consumes: `primary: custom` schemes from Task 1.
- Produces: CSS custom properties `--mc-bg`, `--mc-panel`, `--mc-border`, `--mc-border-subtle`, `--mc-text`, `--mc-body`, `--mc-muted`, `--mc-faint`, `--mc-accent`, `--mc-accent-soft`, `--mc-success`, `--mc-info`, `--mc-danger`, `--mc-scanline`, and `--mc-mono` — Tasks 3–4 reference these names exactly.

- [ ] **Step 1: Replace the entire contents of `docs/stylesheets/extra.css` with:**

```css
/* Mission Control theme — SIPSIK / Peregrine docs
   Spec: specs/2026-07-11-site-redesign-design.md */

:root {
  --mc-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}

/* ---------- tokens: dark (default) ---------- */
[data-md-color-scheme="slate"] {
  --mc-bg: #0a0e17;
  --mc-panel: #0d1220;
  --mc-border: #1f2937;
  --mc-border-subtle: #131a2b;
  --mc-text: #f8fafc;
  --mc-body: #cbd5e1;
  --mc-muted: #94a3b8;
  --mc-faint: #64748b;
  --mc-accent: #fbbf24;
  --mc-accent-soft: rgba(251, 191, 36, 0.07);
  --mc-success: #34d399;
  --mc-info: #22d3ee;
  --mc-danger: #f87171;
  --mc-scanline: rgba(148, 163, 184, 0.05);

  /* map tokens onto Material */
  --md-default-bg-color: var(--mc-bg);
  --md-default-fg-color: var(--mc-text);
  --md-default-fg-color--light: var(--mc-body);
  --md-default-fg-color--lighter: var(--mc-muted);
  --md-default-fg-color--lightest: var(--mc-border);
  --md-primary-fg-color: var(--mc-panel);
  --md-primary-fg-color--dark: var(--mc-panel);
  --md-primary-bg-color: var(--mc-text);
  --md-primary-bg-color--light: var(--mc-muted);
  --md-accent-fg-color: var(--mc-accent);
  --md-accent-fg-color--transparent: var(--mc-accent-soft);
  --md-typeset-a-color: var(--mc-accent);
  --md-code-bg-color: var(--mc-panel);
  --md-code-fg-color: #e2e8f0;
  --md-footer-bg-color: var(--mc-panel);
  --md-footer-bg-color--dark: var(--mc-bg);
  --md-footer-fg-color: var(--mc-muted);
  --md-footer-fg-color--light: var(--mc-faint);
  --md-footer-fg-color--lighter: var(--mc-faint);
}

/* ---------- tokens: light (toggle) ---------- */
[data-md-color-scheme="default"] {
  --mc-bg: #faf9f7;
  --mc-panel: #f1efeb;
  --mc-border: #e2ded6;
  --mc-border-subtle: #ece9e3;
  --mc-text: #16181d;
  --mc-body: #333944;
  --mc-muted: #5f6672;
  --mc-faint: #8a8f99;
  --mc-accent: #b45309;
  --mc-accent-soft: rgba(180, 83, 9, 0.08);
  --mc-success: #047857;
  --mc-info: #0e7490;
  --mc-danger: #b91c1c;
  --mc-scanline: rgba(22, 24, 29, 0.04);

  --md-default-bg-color: var(--mc-bg);
  --md-default-fg-color: var(--mc-text);
  --md-default-fg-color--light: var(--mc-body);
  --md-default-fg-color--lighter: var(--mc-muted);
  --md-default-fg-color--lightest: var(--mc-border);
  --md-primary-fg-color: var(--mc-panel);
  --md-primary-fg-color--dark: var(--mc-panel);
  --md-primary-bg-color: var(--mc-text);
  --md-primary-bg-color--light: var(--mc-muted);
  --md-accent-fg-color: var(--mc-accent);
  --md-accent-fg-color--transparent: var(--mc-accent-soft);
  --md-typeset-a-color: var(--mc-accent);
  --md-code-bg-color: var(--mc-panel);
  --md-code-fg-color: #1f2430;
  --md-footer-bg-color: var(--mc-panel);
  --md-footer-bg-color--dark: var(--mc-bg);
  --md-footer-fg-color: var(--mc-muted);
  --md-footer-fg-color--light: var(--mc-faint);
  --md-footer-fg-color--lighter: var(--mc-faint);
}

/* ---------- header & nav tabs ---------- */
.md-header {
  border-bottom: 1px solid var(--mc-border);
  box-shadow: none;
}

.md-header__topic {
  font-family: var(--mc-mono);
  font-weight: 600;
  letter-spacing: 0.06em;
}

.md-tabs {
  border-bottom: 1px solid var(--mc-border);
}

.md-tabs__link {
  font-family: var(--mc-mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  opacity: 0.75;
}

.md-tabs__link--active,
.md-tabs__item--active .md-tabs__link {
  color: var(--mc-accent);
  border-bottom: 2px solid var(--mc-accent);
  opacity: 1;
}

/* search box */
.md-search__form {
  border: 1px solid var(--mc-border);
  border-radius: 6px;
}

/* ---------- sidebar navigation ---------- */
.md-nav__title {
  font-family: var(--mc-mono);
  font-size: 0.55rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--mc-faint);
}

.md-nav__item .md-nav__link--active,
.md-nav__item .md-nav__link--active code {
  color: var(--mc-accent);
}

.md-nav__item .md-nav__link--active {
  border-left: 2px solid var(--mc-accent);
  background: var(--mc-accent-soft);
  padding-left: 0.35rem;
}

/* ---------- footer ---------- */
.md-footer {
  border-top: 1px solid var(--mc-border);
}

.md-footer-meta {
  font-family: var(--mc-mono);
  font-size: 0.55rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* hide "made with mkdocs" */
.md-footer-copyright {
  display: none;
}

/* ---------- base typography ---------- */
.md-typeset h1 {
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--mc-text);
}

.md-typeset h2 {
  font-weight: 600;
  margin-top: 1.6em;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--mc-border);
}
```

- [ ] **Step 2: Rebuild and verify tokens landed**

```bash
mkdocs build 2>&1 | tail -5
grep -c 'mc-accent' site/stylesheets/extra.css
```

Expected: build exits 0, no new warnings; grep prints a number ≥ 10.

- [ ] **Step 3: Visual smoke check (dark chrome)**

```bash
mkdocs serve -a 127.0.0.1:8000 &
sleep 3
curl -s http://127.0.0.1:8000/ | grep -o 'data-md-color-scheme="slate"' | head -1
kill %1
```

Expected: `data-md-color-scheme="slate"`. (Full visual pass happens in Task 5.)

- [ ] **Step 4: Commit**

```bash
git add docs/stylesheets/extra.css
git commit -m "Rewrite extra.css: console tokens, dark/light schemes, chrome"
```

---

### Task 3: Content components — tables, admonitions, math, code, images (`extra.css` part 2)

**Files:**
- Modify: `docs/stylesheets/extra.css` (append to end of file)

**Interfaces:**
- Consumes: `--mc-*` custom properties from Task 2 (exact names listed there).
- Produces: restyled Material components used across all ~40 docs pages; `.status`/`.status-*` badge classes preserved for content use.

- [ ] **Step 1: Append to `docs/stylesheets/extra.css`:**

```css
/* ---------- tables ---------- */
.md-typeset table:not([class]) {
  border: 1px solid var(--mc-border);
  border-radius: 6px;
  box-shadow: none;
}

.md-typeset table:not([class]) th {
  background: transparent;
  color: var(--mc-faint);
  font-family: var(--mc-mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  border-bottom: 2px solid var(--mc-accent);
}

.md-typeset table:not([class]) td {
  border-top: 1px solid var(--mc-border-subtle);
}

/* ---------- admonitions: flat console panels ---------- */
.md-typeset .admonition,
.md-typeset details {
  background: var(--mc-panel);
  border: 1px solid var(--mc-border);
  border-left-width: 3px;
  border-radius: 6px;
  box-shadow: none;
}

.md-typeset .admonition-title,
.md-typeset summary {
  background: transparent !important;
  font-family: var(--mc-mono);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.58rem;
}

/* icons inherit the title color */
.md-typeset .admonition-title::before,
.md-typeset summary::before {
  background-color: currentColor !important;
}

/* type colors: note/info/question = cyan */
.md-typeset .admonition.note,
.md-typeset .admonition.info,
.md-typeset .admonition.question {
  border-left-color: var(--mc-info);
}
.md-typeset .note > .admonition-title,
.md-typeset .info > .admonition-title,
.md-typeset .question > .admonition-title {
  color: var(--mc-info);
}

/* tip/success = green */
.md-typeset .admonition.tip,
.md-typeset .admonition.success {
  border-left-color: var(--mc-success);
}
.md-typeset .tip > .admonition-title,
.md-typeset .success > .admonition-title {
  color: var(--mc-success);
}

/* warning/important = amber */
.md-typeset .admonition.warning,
.md-typeset .admonition.important {
  border-left-color: var(--mc-accent);
}
.md-typeset .warning > .admonition-title,
.md-typeset .important > .admonition-title {
  color: var(--mc-accent);
}

/* danger/failure = red */
.md-typeset .admonition.danger,
.md-typeset .admonition.failure {
  border-left-color: var(--mc-danger);
}
.md-typeset .danger > .admonition-title,
.md-typeset .failure > .admonition-title {
  color: var(--mc-danger);
}

/* ---------- display math (MathJax / arithmatex) ---------- */
.md-typeset div.arithmatex {
  background: var(--mc-panel);
  border-left: 2px solid var(--mc-accent);
  border-radius: 0 6px 6px 0;
  padding: 0.7em 1em;
  overflow-x: auto;
}

/* ---------- code blocks ---------- */
.md-typeset pre {
  border: 1px solid var(--mc-border);
  border-radius: 6px;
}

/* ---------- images (skip inline emoji) ---------- */
.md-typeset img:not(.twemoji) {
  border-radius: 6px;
  border: 1px solid var(--mc-border);
  box-shadow: none;
}

/* ---------- status badges ---------- */
.md-typeset .status {
  display: inline-block;
  font-family: var(--mc-mono);
  font-size: 0.55rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  padding: 0.25em 0.7em;
  border-radius: 4px;
  border: 1px solid;
}

.md-typeset .status-complete {
  color: var(--mc-success);
  border-color: var(--mc-success);
  background: transparent;
}

.md-typeset .status-pending {
  color: var(--mc-accent);
  border-color: var(--mc-accent);
  background: transparent;
}

.md-typeset .status-inprogress {
  color: var(--mc-info);
  border-color: var(--mc-info);
  background: transparent;
}
```

- [ ] **Step 2: Rebuild and verify a MathJax page and an admonition page render**

```bash
mkdocs build 2>&1 | tail -3
grep -c 'arithmatex' site/calculations/ejection-charges/index.html
grep -c 'admonition warning' site/construction/recovery/index.html
```

Expected: build exits 0; both greps print ≥ 1 (the CSS hooks have matching targets in real pages).

- [ ] **Step 3: Commit**

```bash
git add docs/stylesheets/extra.css
git commit -m "Restyle tables, admonitions, math panels, code and images"
```

---

### Task 4: Mission-control home page (`index.md` + home CSS)

**Files:**
- Modify: `docs/index.md` (full replacement)
- Modify: `docs/stylesheets/extra.css` (append home components)

**Interfaces:**
- Consumes: `--mc-*` tokens (Task 2). Class names used by BOTH files (must match exactly): `mc-hero`, `mc-eyebrow`, `mc-led`, `mc-sub`, `mc-telemetry`, `mc-tile`, `mc-tile-label`, `mc-tile-value`, `mc-label`, `mc-log`, `mc-log-row`, `mc-log-ok`, `mc-log-date`, `mc-log-title`, `mc-log-detail`, `mc-doc-grid`, `mc-doc-card`, `mc-doc-num`, `mc-links`.

- [ ] **Step 1: Append home components to `docs/stylesheets/extra.css`:**

```css
/* ---------- home page: mission control components ---------- */
.mc-hero {
  padding: 2.2rem 0 1.6rem;
  background:
    radial-gradient(60rem 16rem at 15% 0%, var(--mc-accent-soft), transparent),
    repeating-linear-gradient(0deg, transparent 0 23px, var(--mc-scanline) 23px 24px);
}

.mc-eyebrow {
  font-family: var(--mc-mono);
  font-size: 0.6rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--mc-accent);
  margin-bottom: 0.6rem;
}

.mc-led {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--mc-success);
  box-shadow: 0 0 8px var(--mc-success);
  margin: 0 0.3em;
}

.md-typeset .mc-hero h1 {
  font-size: 1.9rem;
  margin: 0 0 0.4rem;
}

.mc-sub {
  font-family: var(--mc-mono);
  font-size: 0.62rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--mc-muted);
  line-height: 1.8;
}

.mc-telemetry {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1px;
  background: var(--mc-border);
  border: 1px solid var(--mc-border);
  border-radius: 8px;
  overflow: hidden;
  margin: 1.4rem 0;
}

.md-typeset .mc-tile {
  background: var(--mc-panel);
  padding: 0.9rem 1rem;
  margin: 0;
}

.mc-tile-label {
  font-family: var(--mc-mono);
  font-size: 0.52rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mc-faint);
}

.mc-tile-value {
  font-family: var(--mc-mono);
  font-size: 1.05rem;
  color: var(--mc-accent);
  margin-top: 0.3rem;
}

.md-typeset .mc-label {
  font-family: var(--mc-mono);
  font-size: 0.55rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mc-faint);
  margin: 1.6rem 0 0.6rem;
}

.mc-log {
  border-top: 1px solid var(--mc-border);
}

.md-typeset .mc-log-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  align-items: baseline;
  padding: 0.55rem 0;
  margin: 0;
  border-bottom: 1px solid var(--mc-border-subtle);
  font-family: var(--mc-mono);
  font-size: 0.62rem;
}

.mc-log-ok { color: var(--mc-success); }
.mc-log-date { color: var(--mc-muted); }
.mc-log-title { color: var(--mc-text); }
.mc-log-detail { color: var(--mc-faint); }
.md-typeset .mc-log-row a { margin-left: auto; }

.mc-doc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 0.7rem;
  margin: 0.8rem 0 1.6rem;
}

.md-typeset .mc-doc-card {
  background: var(--mc-panel);
  border: 1px solid var(--mc-border);
  border-radius: 8px;
  padding: 0.9rem 1rem;
  margin: 0;
  transition: border-color 0.15s;
}

.md-typeset .mc-doc-card:hover {
  border-color: var(--mc-accent);
}

.mc-doc-num {
  font-family: var(--mc-mono);
  font-size: 0.55rem;
  color: var(--mc-accent);
}

.md-typeset .mc-doc-card h3 {
  margin: 0.25rem 0 0.2rem;
  font-size: 0.78rem;
  font-family: var(--mc-mono);
  letter-spacing: 0.06em;
}

.md-typeset .mc-doc-card h3 a {
  color: var(--mc-text);
}

.md-typeset .mc-doc-card p {
  margin: 0;
  font-size: 0.6rem;
  color: var(--mc-faint);
  font-family: var(--mc-mono);
}

.md-typeset .mc-links {
  font-family: var(--mc-mono);
  font-size: 0.62rem;
  display: flex;
  gap: 1.2rem;
  flex-wrap: wrap;
  margin-bottom: 1.6rem;
}
```

- [ ] **Step 2: Replace the entire contents of `docs/index.md` with:**

```markdown
---
hide:
  - navigation
  - toc
---

<div class="mc-hero" markdown>
<p class="mc-eyebrow">Mission Status <span class="mc-led"></span> All Systems Nominal</p>

# SIPSIK — Tripoli L2 Certified

<p class="mc-sub">Apogee Peregrine · 100 mm · dual deploy via CATS Vega<br>
Built in Estonia · flown at Enköping, Sweden · next objective: L3</p>
</div>

<div class="mc-telemetry" markdown>
<div class="mc-tile" markdown>
<div class="mc-tile-label">Certs complete</div>
<div class="mc-tile-value">L1 + L2</div>
</div>
<div class="mc-tile" markdown>
<div class="mc-tile-label">Last motor</div>
<div class="mc-tile-value">J350</div>
</div>
<div class="mc-tile" markdown>
<div class="mc-tile-label">Liftoff mass</div>
<div class="mc-tile-value">3100 g</div>
</div>
<div class="mc-tile" markdown>
<div class="mc-tile-label">Main deploy</div>
<div class="mc-tile-value">146 m</div>
</div>
</div>

<p class="mc-label">Mission log</p>

<div class="mc-log" markdown>
<div class="mc-log-row" markdown>
<span class="mc-log-ok">✓</span><span class="mc-log-date">2026-02-22</span><span class="mc-log-title">FLIGHT 02 — L2 CERTIFICATION</span><span class="mc-log-detail">J350 · DUAL DEPLOY · NOMINAL</span>[REPORT →](flight/flight2-analysis.md)
</div>
<div class="mc-log-row" markdown>
<span class="mc-log-ok">✓</span><span class="mc-log-date">2026-01-24</span><span class="mc-log-title">FLIGHT 01 — L1 CERTIFICATION</span><span class="mc-log-detail">H128W · 140.8 M · MOTOR EJECT</span>[REPORT →](flight/flight1-analysis.md)
</div>
</div>

<p class="mc-label">Documentation</p>

<div class="mc-doc-grid" markdown>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">01</div>
### [Certification](certification/index.md)
<p>L1 ✓ · L2 ✓ · L3 planning</p>
</div>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">02</div>
### [Construction](construction/build-log.md)
<p>Build log · ebay · fins · recovery</p>
</div>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">03</div>
### [Calculations](calculations/stability.md)
<p>Stability · BP charges · vent holes</p>
</div>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">04</div>
### [Simulations](simulations/openrocket.md)
<p>OpenRocket · motor selection</p>
</div>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">05</div>
### [Flight](flight/log.md)
<p>Checklists · logs · analysis</p>
</div>
<div class="mc-doc-card" markdown>
<div class="mc-doc-num">06</div>
### [Photos](photos/index.md)
<p>Build & launch gallery</p>
</div>
</div>

<div class="mc-links" markdown>
[Configurations](configurations.md)
[Decisions](decisions/index.md)
[Blog](blog/index.md)
[References](references.md)
</div>

## The Story Behind Sipsik

This rocket, named **SIPSIK** after the beloved Estonian cartoon character, achieved Tripoli L2 certification on 22 February 2026 at Enköping, Sweden, flying on an AeroTech J350 with dual deployment recovery via CATS Vega. L1 certification was achieved one month earlier on 24 January 2026 at the same location.

The blue rocket connects to Estonian children's culture: in the Sipsik cartoon, a girl named Anu and her brother Mart build a cardboard rocket hoping to send their toy Sipsik to the moon. This rocket teaches my daughters Liza (5) and Elsa (2) how we *actually* send rockets to the sky.

## Acknowledgments

- **Rolf Örell** (TRA# 3728) — Certifying authority for both L1 and L2, first European Tripoli Prefect
- **Peter Steen** — Launch support and guidance
- **Anton Vannesjö** — Launch support and guidance

---

<small>
[Tõnu Samuel](https://www.linkedin.com/in/tonusamuel/) • Software engineer • Tallinn, Estonia
Build: [BUILD_COMMIT_HASH](BUILD_COMMIT_URL) (BUILD_DATE)
</small>
```

Note: the `Build: [BUILD_COMMIT_HASH](BUILD_COMMIT_URL) (BUILD_DATE)` line is a CI placeholder — keep it byte-identical.

- [ ] **Step 3: Rebuild and verify home structure**

```bash
mkdocs build 2>&1 | tail -3
grep -c 'mc-tile-value' site/index.html
grep -c 'mc-doc-card' site/index.html
grep -c 'flight/flight2-analysis' site/index.html
```

Expected: build exits 0 with no new warnings (watch for "contains a link, but the target is not found" — that means a `.md` link path is wrong); `mc-tile-value` count = 4; `mc-doc-card` count ≥ 6; flight2 link count ≥ 1.

- [ ] **Step 4: Commit**

```bash
git add docs/index.md docs/stylesheets/extra.css
git commit -m "Rebuild home page as mission-control console"
```

---

### Task 5: Full verification pass, push, PR

**Files:**
- No source changes expected. Fixes discovered here belong to the task that introduced them (amend via a follow-up commit).

**Interfaces:**
- Consumes: everything from Tasks 1–4.

- [ ] **Step 1: Final clean build vs baseline**

```bash
mkdocs build 2>&1 | tee /private/tmp/claude-501/-Users-tonu-MyLevel1Peregrine/b9a5f7da-ea26-491d-9aac-bafcdf538158/scratchpad/final-build.log
diff <(grep -i warning /private/tmp/claude-501/-Users-tonu-MyLevel1Peregrine/b9a5f7da-ea26-491d-9aac-bafcdf538158/scratchpad/baseline-build.log) \
     <(grep -i warning /private/tmp/claude-501/-Users-tonu-MyLevel1Peregrine/b9a5f7da-ea26-491d-9aac-bafcdf538158/scratchpad/final-build.log)
```

Expected: diff prints nothing (no new warnings).

- [ ] **Step 2: Visual pass in the browser (both schemes, desktop + ~400px width)**

```bash
mkdocs serve -a 127.0.0.1:8000
```

Check these pages in dark, then toggle to light and re-check: `/` (hero, tiles, log, grid), `/calculations/ejection-charges/` (formula panels readable), `/simulations/openrocket/` (dense tables), `/configurations.md`→`/configurations/` (tables), `/construction/recovery/` (Mermaid diagram contrast + warning admonition), `/photos/` (image borders), `/blog/2026-01-24-l1-certification/`. Confirm: nav tab underline, sidebar active highlight, search styling, footer, toggle round-trip. If the executor has browser tooling, screenshot each; otherwise ask the user to eyeball and confirm before proceeding. Known contingency: if the Mermaid diagram is unreadable on dark, STOP and report — do not improvise CSS overrides; that needs a decision.

- [ ] **Step 3: Push branch and open PR (no attribution footer)**

```bash
git push -u origin feature/site-redesign
gh pr create --title "Site redesign: Mission Control theme" --body "$(cat <<'EOF'
## Summary
- Dark-first "Mission Control" theme: console tokens, amber accent, mono telemetry accents (spec: specs/2026-07-11-site-redesign-design.md)
- mkdocs.yml: dark default + custom palette, site_name → SIPSIK
- extra.css: full rewrite (chrome, tables, admonitions, MathJax panels, code, images, home components)
- index.md: rebuilt as mission-control landing (hero, telemetry tiles, mission log, documentation grid); story + acknowledgments preserved

## Verification
- mkdocs build clean vs baseline (no new warnings)
- Visual pass in both schemes: home, ejection-charges (MathJax), openrocket (tables), recovery (Mermaid + admonitions), photos, blog
EOF
)"
```

Expected: PR URL printed. **STOP here — do not merge.**

---

## Self-review notes

- Spec coverage: tokens (T2), typography (T2), home page (T4), nav tabs/sidebar/search/footer (T2), tables/admonitions/math/code/images/badges (T3), site_name (T1), dark default + light toggle (T1+T2), out-of-scope respected (no other files), risks → T5 step 2 (Mermaid, MathJax, light-mode contrast, dense tables).
- Class names cross-checked between T4 CSS and T4 index.md — 19 `mc-*` classes match.
- No placeholders; every code step contains full content.
