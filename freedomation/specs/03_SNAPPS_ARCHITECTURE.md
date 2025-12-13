# SNAPPS Architecture (v0.1)

## What is SNAPPS?

**SNAPPS** = **Smart Networked Agentic Applications**

SNAPPS are AI-powered applications that run on the **Freedomation Agentic OS**. They orchestrate workflows through composable, portable components called **Flowgrams**, which execute **Knowledge Blocks (KBs)** and pass **Artifacts** between nodes, validated by **Gates**.

**Key Characteristics:**
- **Agentic**: Autonomous execution with minimal human intervention
- **Networked**: Components communicate via structured artifacts
- **Smart**: Adaptive, context-aware decision-making
- **Portable**: Flowgrams are runtime-agnostic YAML specifications

---

## 1) System Layers (L0–L6)

Freedomation organizes knowledge and execution into **7 layers** using the **Progressive Disclosure** model:

### L0: Meta-System
System-level governance, runtime specifications, architecture docs.
- This file (`03_SNAPPS_ARCHITECTURE.md`)
- Runtime contracts (`04_RUNTIME_CONTRACT.md`)
- Trust tiers (`05_TRUST_TIERS_AND_CERTIFICATION.md`)

### L1: Quick Reference
One-page cheat sheets, API quick starts, command references.
- Fast lookup for experienced users
- No explanations, just facts
- Example: "KB Quick Start", "Gate Cheat Sheet"

### L2: Core Execution
The primary operational layer. Most KBs, Flowgrams, and Artifacts live here.
- Step-by-step procedural KBs
- Standard flowgram definitions
- Core artifact schemas
- **This is where 80% of the work happens**

### L3: Edge Cases & Diagnostics
Troubleshooting, debugging, exception handling.
- What to do when things go wrong
- How to interpret error messages
- Recovery procedures
- Example: "KB-042: Diagnose Email Deliverability Failures"

### L4: Technical Specs
Deep implementation details, schemas, algorithms.
- Artifact schema definitions (YAML)
- Gate validation logic
- Data structures and types
- Example: `artifact.email_draft.v0_1.yaml`

### L5: Research & Development
Experimental features, proposed enhancements, research notes.
- Not production-ready
- Speculative or exploratory content
- Example: "Proposal: Multi-Agent Negotiation Protocol"

### L6: Historical Archive
Deprecated components, old versions, legacy documentation.
- Kept for reference, not active use
- Example: `KB-001_v0_1_deprecated.md`

**Most users will primarily interact with L1 (quick reference) and L2 (core execution).**

---

## 2) Object Model

Freedomation's core objects:

### Flowgram
**Definition:** A YAML workflow specification that orchestrates KBs, artifacts, and gates.

**Analogy:** A Flowgram is like a recipe that tells agents which KBs to execute, in what order, and how to pass data between them.

**Key Fields:**
- `fg_id`: Unique identifier
- `nodes`: Work units (usually mapping to KBs)
- `edges`: Data flow between nodes (artifact types)
- `gates`: Validation checkpoints
- `modes`: Execution modes (trial vs full)

**File Location:** `/freedomation/flowgrams/`

**Example:** `outbound_value_fast_track_v0_1.yaml`

---

### Knowledge Block (KB)
**Definition:** An atomic, versioned unit of procedural knowledge.

**Analogy:** A KB is like a function in code — it takes inputs, performs a specific task, and returns outputs.

**Key Fields:**
- KB ID (e.g., `KB-001`)
- Inputs, Outputs, Process steps
- Status, Layer, Type, Category

**File Location:** `/freedomation/kbs/`

**Example:** `KB-001.md`

See `02_KB_SPEC_GOVERNANCE.md` for full specification.

---

### Artifact
**Definition:** A structured data object passed between nodes in a flowgram.

**Analogy:** Artifacts are like typed parameters in a function call. They carry data from one node to the next.

**Key Fields:**
- `artifact_id`: Unique identifier (e.g., `artifact.email_draft.v0_1`)
- `schema`: YAML schema defining required/optional fields
- `version`: Semantic version

**File Location:** `/freedomation/artifacts/`

**Example:** `artifact.email_draft.v0_1.yaml`

**Common Artifact Types:**
- `artifact.brand_kit.v0_1` (inputs: brand voice, colors, messaging)
- `artifact.persona_sketch.v0_1` (inputs: audience details)
- `artifact.email_draft.v0_1` (outputs: subject line, body, CTA)
- `artifact.qa_report.v0_1` (outputs: pass/fail + remediation instructions)

---

### Gate
**Definition:** A validation checkpoint that enforces quality and integrity rules.

**Analogy:** Gates are like unit tests or linters — they check artifacts before they proceed.

**Key Fields:**
- `gate_id`: Unique identifier (e.g., `gate.ethics_integrity.v0_1`)
- `validation_rules`: Specific checks to perform
- `failure_action`: What happens if validation fails

**File Location:** `/freedomation/gates/`

**Example:** `gate.ethics_integrity.v0_1.yaml`

**Mandatory Gates (v0.1):**
- **Ethics & Integrity Gate**: Checks for manipulation, fabricated claims, shame tactics
- **Deliverability Gate**: Checks for spam triggers, formatting issues

---

### Run
**Definition:** A single execution instance of a flowgram.

**Analogy:** A Run is like a process or job — it has a start time, end time, status, and outputs.

**Key Fields:**
- `run_id`: Unique identifier for this execution
- `fg_id`: Which flowgram is being executed
- `mode`: Trial or full
- `status`: Running, completed, failed
- `artifacts_produced`: Outputs from this run
- `gate_results`: Pass/fail for each gate

**Storage:** Runtime-dependent (could be database, file system, etc.)

---

## 3) Freedomation vs Flowgrams vs SNAPPS

### Freedomation
**The Operating System**
- Defines the rules, object model, and runtime contract
- Provides the infrastructure for executing workflows
- Enforces doctrine (Agentic Resonance)
- Think: "The platform"

### Flowgrams
**The Workflows**
- Portable YAML specifications for specific tasks
- Orchestrate KBs, artifacts, and gates
- Can be shared, forked, and composed
- Think: "The programs"

### SNAPPS
**The Applications**
- Complete AI-powered applications built on Freedomation
- May include multiple flowgrams, custom KBs, and UI layers
- User-facing products (e.g., "Outbound Value Engine", "Content Repurposing Studio")
- Think: "The apps"

**Example:**
- **Freedomation**: The OS (like iOS)
- **Flowgram**: A workflow (like a Shortcut in iOS)
- **SNAPP**: An app (like Instagram on iOS)

---

## 4) SNAPPS Component Relationships

```
┌─────────────────────────────────────────────────┐
│              SNAPP (Application)                │
│  (e.g., "Outbound Value Engine")                │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │   Flowgram: outbound_value_fast_track     │ │
│  │                                           │ │
│  │   ┌─────────┐   ┌─────────┐   ┌────────┐│ │
│  │   │ Node 1  │──▶│ Node 2  │──▶│ Node 3 ││ │
│  │   │ KB-001  │   │ KB-002  │   │ KB-003 ││ │
│  │   └─────────┘   └─────────┘   └────────┘│ │
│  │        │             │            │      │ │
│  │        ▼             ▼            ▼      │ │
│  │   [Artifact]    [Artifact]   [Artifact] │ │
│  │        │             │            │      │ │
│  │        └─────── [Gate] ──────────┘      │ │
│  │                     │                    │ │
│  │                     ▼                    │ │
│  │                 [Output]                 │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
└─────────────────────────────────────────────────┘
        │                                    │
        ▼                                    ▼
   [Freedomation OS]              [Trust & Governance]
   (Runtime Contract)              (Certification)
```

**Flow:**
1. User requests a task (e.g., "Create an outbound email campaign")
2. SNAPP selects appropriate Flowgram
3. Flowgram executes nodes sequentially
4. Each node runs a KB with specific inputs
5. KBs produce artifacts
6. Artifacts pass through gates
7. Final output delivered to user

---

## 5) Execution Modes

### Trial Surface Mode
- Fast, lightweight execution
- Skips optional validation
- Produces draft-quality outputs
- Use for: Experimentation, quick iterations

### Full Deep Mode
- Complete execution with all validation
- Runs all gates
- Produces production-quality outputs
- Use for: Final deliverables, client-facing work

Flowgrams must declare which modes they support:
```yaml
modes:
  - trial_surface
  - full_deep
```

---

## 6) Composability & Portability

### Composability
Flowgrams can reference other flowgrams as sub-workflows:

```yaml
nodes:
  - node_id: "n1_run_sub_workflow"
    flowgram_ref: "other_workflow_v0_1"
    inputs_required:
      - artifact.initial_data.v0_1
    outputs_primary:
      - artifact.processed_data.v0_1
```

### Portability
Flowgrams are runtime-agnostic YAML files. They can run on:
- Cloud platforms
- Local machines
- CI/CD pipelines
- Different AI providers (OpenAI, Anthropic, custom models)

**As long as the runtime implements the Freedomation contract, flowgrams are portable.**

---

## 7) SNAPPS Design Principles

### Principle 1: Artifacts > Vibes
All handoffs must be structured artifacts with schemas. No vague "good energy" outputs.

### Principle 2: Small, Composable Units
KBs should be atomic. Flowgrams should be focused. Compose small units into larger workflows.

### Principle 3: Fail Fast, Fix Deterministically
Gates catch errors early. When a gate fails, the system produces a `qa_report` with specific remediation steps (not vague "try again").

### Principle 4: Truth-Only Personalization
No invented user details. Personalization based on explicit inputs only.

### Principle 5: Progressive Disclosure
Complexity is hidden in higher layers. L1/L2 users don't need to see L4 implementation details.

---

## 8) Example SNAPP: Outbound Value Engine

**Purpose:** Generate personalized outbound email campaigns that inspire action (no manipulation).

**Components:**
- **Flowgram:** `outbound_value_fast_track_v0_1.yaml`
- **KBs:**
  - `KB-001`: Draft email content
  - `KB-002`: Personalize based on persona sketch
  - `KB-003`: Validate against ethics gate
- **Artifacts:**
  - `artifact.brand_kit.v0_1` (input)
  - `artifact.persona_sketch.v0_1` (input)
  - `artifact.email_draft.v0_1` (output)
- **Gates:**
  - `gate.ethics_integrity.v0_1`
  - `gate.deliverability.v0_1`

**User Flow:**
1. User provides brand kit + persona sketch
2. SNAPP runs flowgram in trial mode
3. Draft email produced, validated by gates
4. If gates pass → deliver to user
5. If gates fail → produce QA report, auto-fix, re-run

---

## 9) Relationship to Trust Tiers

SNAPPS can be certified at different trust levels:
- **Draft**: Experimental, use at your own risk
- **Stable**: Tested, ready for use
- **Verified**: Independently reviewed
- **Certified**: Meets Freedomation certification standards

See `05_TRUST_TIERS_AND_CERTIFICATION.md` for details.

---

## Summary

**Freedomation** is the OS. **Flowgrams** are the workflows. **SNAPPS** are the applications.

Together, they create a composable, portable, trust-worthy ecosystem for agentic AI applications grounded in **Authentic Inspiration**.

**Core Objects:**
- Flowgrams orchestrate workflows
- KBs define procedural knowledge
- Artifacts carry structured data
- Gates enforce quality
- Runs track execution instances

**Layers (L0–L6):** Progressive disclosure from meta-system to archive

**Modes:** Trial (fast) vs Full (production)

**Principles:** Artifacts > vibes, composability, fail fast, truth-only personalization

---

**Version:** 0.1.0
**Status:** stable
**Last Updated:** 2025-12-13
