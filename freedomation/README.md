# Freedomation — SNAPPS Agentic OS (v0.1)

**Status:** Draft
**Trust Tier:** 🟡 Draft
**Last Updated:** 2025-12-13

---

## What is Freedomation?

**Freedomation** is an Agentic Operating System for building **SNAPPS** (Smart Networked Agentic Applications) — AI-powered workflows grounded in **Authentic Inspiration**, not manipulation.

**Core Principle:** Truth-only personalization, permission-based CTAs, value-first offers. No fake urgency, no shame tactics, no fabricated proof.

---

## Directory Structure

```
/freedomation/
├── specs/              # System specifications
├── kbs/                # Knowledge Blocks (KB-001...KB-010)
├── flowgrams/          # Workflow definitions (YAML)
├── artifacts/          # Artifact schemas (YAML)
├── gates/              # Validation gates (YAML)
├── tools/              # Validators and utilities
└── tests/              # Fixtures and golden run scenarios
```

---

## Quick Start

### 1. Run Validators

Ensure your flowgram and KBs are compliant:

```bash
# Validate flowgram
python3 freedomation/tools/flowgram_validate.py \
  freedomation/flowgrams/outbound_value_fast_track_v0_1.yaml

# Lint all KBs
python3 freedomation/tools/kb_lint.py
```

### 2. Review Golden Run

See expected behavior in `/freedomation/tests/golden_run_outbound_v0_1.md`

### 3. Explore Fixtures

Example artifacts in `/freedomation/tests/fixtures/`

---

## How to Add a Knowledge Block (KB)

1. **Create file** in `/freedomation/kbs/`
   ```
   KB-011.md
   ```

2. **Follow the template** (see `specs/02_KB_SPEC_GOVERNANCE.md`)
   - Include all required sections: Purpose, Inputs, Outputs, Process, Examples, Edge Cases, Quality Checks, Related KBs
   - Add metadata: version, status, layer, type, category, credibility, risk

3. **Required metadata format:**
   ```markdown
   # KB-011: Your KB Title

   **Version:** 0.1.0
   **Status:** draft
   **Layer:** L2
   **Type:** procedural
   **Category:** your-category
   **Credibility:** medium
   **Risk:** low
   ```

4. **Lint your KB:**
   ```bash
   python3 freedomation/tools/kb_lint.py
   ```

---

## How to Add a Flowgram

1. **Create file** in `/freedomation/flowgrams/`
   ```
   your_workflow_v0_1.yaml
   ```

2. **Required top-level fields:**
   ```yaml
   fg_id: "your_workflow"
   version: "0.1.0"
   human_title: "Your Workflow Name"
   constitutional_title: "Authentic Inspiration [Purpose]"
   modes:
     - trial_surface
     - full_deep
   artifacts:
     - artifact.input1.v0_1
     - artifact.output1.v0_1
   initial_artifacts:
     required:
       - artifact.input1.v0_1
   nodes:
     - node_id: "n1_first_step"
       kb_ref: "KB-001"
       inputs_required: [...]
       outputs_primary: [...]
   edges:
     - from: "n1_first_step"
       to: "n2_second_step"
       artifact_type: "artifact.intermediate.v0_1"
   gates:
     - gate_id: "ethics_gate"
       position: "before_delivery"
       gate_ref: "gate.ethics_integrity.v0_1"
   outputs:
     - artifact.output1.v0_1
   ```

3. **Validate your flowgram:**
   ```bash
   python3 freedomation/tools/flowgram_validate.py \
     freedomation/flowgrams/your_workflow_v0_1.yaml
   ```

---

## Artifact Schemas

All artifacts must have YAML schemas in `/freedomation/artifacts/`

**Naming convention:**
```
artifact.<name>.v0_1.yaml
```

**Required fields:**
```yaml
artifact_id: "artifact.your_artifact.v0_1"
version: "0.1.0"
schema_type: "yaml"
name: "Your Artifact Name"
description: "Brief description"
required_fields:
  - field: "field_name"
    type: "string"
    description: "What this field is"
```

---

## Gates

Gates validate artifacts before delivery. Two mandatory gates:

### 1. Ethics & Integrity Gate
- Enforces Agentic Resonance doctrine
- Checks for manipulation tactics (fake urgency, shame, pressure)
- Ensures truth-only personalization

### 2. Deliverability Gate
- Validates formatting (subject line length, paragraph length)
- Checks for spam triggers
- Ensures channel-appropriate content

**Gate failure → FIX loop:**
- Produces `artifact.qa_report.v0_1`
- Includes specific violations + remediation instructions
- Re-runs node with QA report
- Retries validation

---

## Current SNAPPS

### Outbound Value Fast Track v0.1
**Purpose:** Ethics-first outbound business development system

**Flowgram:** `outbound_value_fast_track_v0_1.yaml`

**Nodes (6):**
1. n1_prospect_research (KB-002)
2. n2_value_offer_design (KB-006)
3. n3_asset_selection (KB-005)
4. n4_outreach_sequence (KB-004)
5. n5_community_invitation (KB-009)
6. n6_resonance_dashboard (KB-010)

**Outputs:**
- Validated outreach sequence
- Community invitation script
- Resonance metrics dashboard

---

## Philosophy

### Agentic Resonance Doctrine

**Truth-Only Personalization:**
- Only use observable facts from public sources
- Never invent personal details

**Permission-Based CTAs:**
- Every CTA is an invitation, not demand
- Users can say "no" without guilt

**Value-First Offers:**
- Give genuinely useful resources before asking
- No "bait and switch" lead magnets

**Supportive Tone:**
- Warm and encouraging
- Not clinical or therapeutic
- No shame or pressure tactics

**See:** `/freedomation/specs/01_DOCTRINE_AGENTIC_RESONANCE.md`

---

## Documentation

### Specs (Read These First)
1. `00_README.md` — Quick start
2. `01_DOCTRINE_AGENTIC_RESONANCE.md` — Core philosophy
3. `02_KB_SPEC_GOVERNANCE.md` — KB template and rules
4. `03_SNAPPS_ARCHITECTURE.md` — System architecture
5. `04_RUNTIME_CONTRACT.md` — Execution lifecycle
6. `05_TRUST_TIERS_AND_CERTIFICATION.md` — Quality framework

### Knowledge Blocks (KB-001 to KB-010)
All KBs documented in `/freedomation/kbs/`

**Key KBs:**
- KB-001: Outbound Value Fast Track Overview
- KB-002: Resonant Persona Mapping
- KB-003: Trauma-Informed Messaging Guidelines
- KB-004: Value-First Outreach Templates
- KB-008: Business Resonance Doctrine

---

## Running Tests

### Validate Everything
```bash
# Flowgram
python3 freedomation/tools/flowgram_validate.py \
  freedomation/flowgrams/outbound_value_fast_track_v0_1.yaml

# KBs
python3 freedomation/tools/kb_lint.py
```

### Golden Run
See `/freedomation/tests/golden_run_outbound_v0_1.md` for expected behavior

---

## Contributing

### Before Committing
1. Run validators (flowgram + KB lint)
2. Ensure all artifact references have matching schemas
3. Follow naming conventions strictly
4. Update change logs

### PR Standards
Every PR must include:
- Summary (what changed)
- Why (the intention)
- Risk (low/medium/high)
- Rollback note (what to revert)

**Small PRs only:**
- "Add KB-011"
- "Add artifact schemas"
- "Update ethics gate rules"

---

## Trust Tiers

- 🟡 **Draft**: Experimental, use at your own risk
- 🟢 **Stable**: Tested, ready for use
- 🔵 **Verified**: Peer-reviewed, production-ready
- ⭐ **Certified**: Formally certified, mission-critical ready

**Current status:** All components are 🟡 Draft (v0.1)

---

## License

See `/LICENSE.md` at repo root

---

## Questions?

See `/freedomation/specs/00_README.md` for detailed quick start guide

---

**Version:** 0.1.0
**Status:** Draft
**Doctrine:** Agentic Resonance (Authentic Inspiration)
