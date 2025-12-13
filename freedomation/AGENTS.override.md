# /freedomation/AGENTS.override.md — Freedomation + SNAPPS Authoring Rules (v0.1)
This file governs *everything* inside `/freedomation/**`.

---

## 0) System Identity
- **Agentic OS:** Freedomation
- **Applications:** SNAPPS (Smart Networked Agentic Applications)
- **Workflows:** Flowgrams (portable)
- **Knowledge:** KBs (atomic) + Skill Packs
- **Core Doctrine:** Agentic Resonance → **Authentic Inspiration**

---

## 1) Hard Guardrails (Freedomation)
1) **Truth-only personalization** (no invented details)
2) **No manipulation** (no shame, pressure, tricks, fake scarcity)
3) **Permission-based CTAs** (clean invitations)
4) **No fabricated proof** (no invented testimonials/results)
5) **No therapy claims** (supportive + inspiring only)
6) **Artifacts > vibes** (handoffs must be artifacts with schemas)

---

## 2) Freedomation Directory Map
- `/freedomation/specs/` — System specs (SNAPPS, runtime, governance)
- `/freedomation/flowgrams/` — Flowgram YAML workflows
- `/freedomation/artifacts/` — Artifact schemas (and optionally example artifacts)
- `/freedomation/gates/` — Gate specs (validators)
- `/freedomation/kbs/` — Knowledge Blocks (KB-001…)

**Rule:** specs define the rules; flowgrams execute the rules; artifacts carry the data; gates enforce integrity; KBs hold the knowledge.

---

## 3) Strict Naming Conventions
### Knowledge Blocks
- File: `/freedomation/kbs/KB-###.md`
- KB ID inside file must match filename.

### Artifact Schemas
- File: `/freedomation/artifacts/artifact.<name>.v0_1.yaml`
- `artifact_id:` must match filename.

### Gates
- File: `/freedomation/gates/gate.<name>.v0_1.yaml`
- `gate_id:` must match filename.

### Flowgrams
- File: `/freedomation/flowgrams/<snake_case_name>_v0_1.yaml`
- `fg_id:` should be stable and human readable.

---

## 4) Required KB Template
Every KB must include:
1. Purpose
2. Inputs
3. Outputs
4. Process (step-by-step)
5. Examples/Templates
6. Edge Cases & Warnings
7. Quality Checks
8. Related KBs

Every KB must declare:
- version
- status (draft|stable|deprecated)
- layer (L1–L4)
- type + category

---

## 5) Required Flowgram Fields
Every Flowgram must define:
- modes: `trial_surface`, `full_deep`
- initial_artifacts required/optional
- nodes + edges + gates
- outputs + acceptance criteria

Nodes must declare:
- `inputs_required`
- `outputs_primary`

Edges move artifact types only.

---

## 6) Gates (Minimum for Outbound v0.1)
Two mandatory gates:
- **Ethics & Integrity Gate**
- **Deliverability Gate**

When a gate fails:
- produce `artifact.qa_report.v0_1`
- fix via a deterministic instruction set
- re-run only the necessary nodes

---

## 7) Versioning Rules
- Use semantic versioning: `0.1.0` → `0.1.1` for small changes
- Changes that break schemas or flow fields require a minor bump: `0.2.0`

---

## 8) PR Standards (Freedomation)
Every PR must include:
- Summary (what changed)
- Why (the intention)
- Risk (low/med/high)
- Rollback note (what file/version to revert)

Small PRs only:
- "Add KB-001"
- "Add artifact schemas"
- "Add ethics gate rules"
- "Add Outbound Value Fast Track flowgram"

---
END /freedomation override
