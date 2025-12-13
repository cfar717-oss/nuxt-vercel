# Freedomation Specs — Quick Start

## Purpose of `/freedomation/`

This directory contains the **Freedomation / SNAPPS Agentic OS** specification and implementation artifacts. Freedomation is an agentic operating system that orchestrates AI-powered workflows through composable, portable components.

**Core Principle:** Authentic Inspiration over Manipulation. Truth-only personalization, permission-based CTAs, supportive tone without therapy framing.

---

## Directory Structure

### `/freedomation/specs/`
System specifications, architecture docs, and governance rules.
- Doctrine, KB templates, runtime contracts, trust tiers

### `/freedomation/kbs/`
**Knowledge Blocks (KBs)** — Atomic, versioned units of procedural knowledge.
- Format: `KB-###.md` (e.g., `KB-001.md`, `KB-042.md`)
- Each KB is self-contained with clear inputs, outputs, process steps

### `/freedomation/flowgrams/`
**Flowgrams** — YAML workflow definitions that orchestrate KBs and artifacts.
- Format: `<snake_case_name>_v0_1.yaml`
- Define nodes, edges, gates, modes (trial/full)

### `/freedomation/artifacts/`
**Artifact Schemas** — YAML schemas defining data structures passed between nodes.
- Format: `artifact.<name>.v0_1.yaml`
- Each artifact has strict schema with required/optional fields

### `/freedomation/gates/`
**Gates** — Validation checkpoints ensuring quality and integrity.
- Format: `gate.<name>.v0_1.yaml`
- Minimum required: Ethics & Integrity Gate, Deliverability Gate

---

## Quick Start

### How to Add a Knowledge Block (KB)

1. **Create the file** in `/freedomation/kbs/`
   ```
   /freedomation/kbs/KB-001.md
   ```

2. **Use the KB template** (see `02_KB_SPEC_GOVERNANCE.md` for full template)
   ```markdown
   # KB-001: [Your KB Title]

   **Version:** 0.1.0
   **Status:** draft
   **Layer:** L2
   **Type:** procedural
   **Category:** content-creation

   ## Purpose
   [What this KB does in 1-2 sentences]

   ## Inputs
   - Input 1: description
   - Input 2: description

   ## Outputs
   - Output 1: description

   ## Process
   1. Step one
   2. Step two
   3. Step three

   ## Examples
   [Concrete examples]

   ## Edge Cases & Warnings
   [What can go wrong]

   ## Quality Checks
   [How to verify success]

   ## Related KBs
   - KB-XXX: relationship description
   ```

3. **Follow naming rules**
   - File name must match KB ID: `KB-001.md` contains `# KB-001:`
   - Use zero-padded numbers: `KB-001`, `KB-042`, `KB-123`

### How to Add a Flowgram

1. **Create the file** in `/freedomation/flowgrams/`
   ```
   /freedomation/flowgrams/outbound_value_fast_track_v0_1.yaml
   ```

2. **Define required fields**
   ```yaml
   fg_id: "outbound_value_fast_track"
   version: "0.1.0"
   name: "Outbound Value Fast Track"
   description: "Brief description of workflow purpose"

   modes:
     - trial_surface
     - full_deep

   initial_artifacts:
     required:
       - artifact.brand_kit.v0_1
     optional:
       - artifact.persona_sketch.v0_1

   nodes:
     - node_id: "n1_intake"
       kb_ref: "KB-001"
       inputs_required:
         - artifact.brand_kit.v0_1
       outputs_primary:
         - artifact.initial_brief.v0_1

   edges:
     - from: "n1_intake"
       to: "n2_process"
       artifact_type: "artifact.initial_brief.v0_1"

   gates:
     - gate_id: "ethics_gate"
       position: "before_delivery"
       gate_ref: "gate.ethics_integrity.v0_1"

   outputs:
     - artifact.final_deliverable.v0_1

   acceptance_criteria:
     - "All gates pass"
     - "Output artifact validates against schema"
   ```

3. **Reference existing artifacts and KBs**
   - Nodes reference KBs by ID (`KB-001`)
   - Edges move specific artifact types
   - Gates reference gate definitions

---

## Key Governance Rules

1. **Truth-only content** — No invented testimonials, fake proof, or fabricated personalization
2. **No manipulation** — No shame, pressure tactics, fake urgency/scarcity
3. **Permission-based CTAs** — Clean invitations, never coercive
4. **Artifacts > vibes** — All handoffs must be structured artifacts with schemas
5. **Small, composable pieces** — Keep KBs atomic, flowgrams focused

---

## Learn More

- `01_DOCTRINE_AGENTIC_RESONANCE.md` — Core philosophy and ethical guidelines
- `02_KB_SPEC_GOVERNANCE.md` — Complete KB template and rules
- `03_SNAPPS_ARCHITECTURE.md` — System architecture and layer model
- `04_RUNTIME_CONTRACT.md` — How workflows execute
- `05_TRUST_TIERS_AND_CERTIFICATION.md` — Quality and credibility framework

---

**Version:** 0.1.0
**Last Updated:** 2025-12-13
