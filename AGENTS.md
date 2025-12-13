# Root `AGENTS.md` — Nuxt + Shopify + Freedomation SNAPPS (v0.1)
Readable by **Claude Code** + **OpenAI Codex**. Applies repo-wide, with strict overrides inside `/freedomation/`.

---

## 0) Repo Overview
This repo contains:
- A **Nuxt app** (`app/`, `pages/`, `components/`, `assets/`, `public/`)
- A **Shopify module** (`modules/shopify/`)
- A **server API** (`server/api/`)
- The **Freedomation / SNAPPS Agentic OS** documentation and workflow specs (`freedomation/`)

**Rule:** Product code and Freedomation specs must remain cleanly separated.

---

## 1) Global Non-Negotiables (All Folders)
1) **No secrets committed** (API keys, tokens, private URLs, customer PII).
2) **Truth-only content** (no fabricated proof, no invented personalization).
3) **Readable outputs**: prefer concise Markdown and clean YAML.
4) **Small PRs**: one change theme per PR.

---

## 2) Folder Intent
- `/app`, `/pages`, `/components`, `/assets`, `/public`
  - **Nuxt app code** only.
- `/modules/shopify`
  - Shopify integration: composables, queries, types.
- `/server/api`
  - API routes (e.g., sitemap).
- `/freedomation`
  - **Freedomation + SNAPPS specs**: KBs, Flowgrams, Gates, Artifact Schemas.

---

## 3) Changes Policy (Very Important)
### If you are working on Nuxt / Shopify code
- Follow existing conventions and file structure.
- Don't introduce Freedomation concepts into app code unless explicitly requested.

### If you are working on Freedomation
- Only edit files inside `/freedomation/**`.
- Prefer adding/adjusting **specs, schemas, and gates** before writing runtime code.

---

## 4) Freedomation Philosophy (Applies in `/freedomation/`)
**Authentic Inspiration (Motivation vs Manipulation)**:
- No shame/pressure tactics
- No fake urgency/scarcity
- Permission-based CTAs
- Supportive, warm, human tone (no therapy/clinical framing)

---

## 5) Progressive Disclosure (Knowledge Discipline)
- L1: quick reference
- L2: core execution
- L3: edge cases & diagnostics
- L4: technical specs (schemas, algorithms, tests)

Keep artifacts small and composable.

---

## 6) Overrides
This repo uses folder-specific instructions:
- `/freedomation/AGENTS.override.md` (authoring + governance rules)

**When working inside `/freedomation/`, treat the override as higher priority than this file.**

---
END Root AGENTS.md
