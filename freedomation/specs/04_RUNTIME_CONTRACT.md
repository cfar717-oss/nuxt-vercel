# Runtime Contract (v0.1)

## What is the Runtime Contract?

The **Runtime Contract** defines the rules and guarantees that every Freedomation-compatible runtime must implement. It specifies how flowgrams are executed, how artifacts flow between nodes, how gates validate outputs, and how failures are handled.

**Think of it as:** The "API specification" for Freedomation runtimes.

**Goal:** Ensure that a flowgram written once can run on any compliant runtime with predictable behavior.

---

## 1) Execution Lifecycle

Every flowgram execution follows this lifecycle:

```
┌──────────┐
│ INTAKE   │  User provides inputs + selects flowgram
└────┬─────┘
     │
     ▼
┌──────────┐
│ ROUTE    │  Runtime selects mode (trial/full) + initializes Run
└────┬─────┘
     │
     ▼
┌──────────┐
│ EXECUTE  │  Runtime runs nodes sequentially (or in parallel where possible)
└────┬─────┘
     │
     ▼
┌──────────┐
│ GATE     │  Artifacts pass through validation gates
└────┬─────┘
     │
     ├─── PASS ──▶ ┌──────────┐
     │             │ DELIVER  │  Output artifacts delivered to user
     │             └──────────┘
     │                  │
     │                  ▼
     │             ┌──────────┐
     │             │ OBSERVE  │  Log results, collect metrics
     │             └──────────┘
     │
     └─── FAIL ──▶ ┌──────────┐
                   │ FIX      │  Generate qa_report, apply deterministic fixes
                   └────┬─────┘
                        │
                        └──▶ (Re-run from failed node)
```

### Phase Descriptions

**INTAKE**: Accept user inputs, validate initial artifacts
**ROUTE**: Determine execution mode, initialize Run object
**EXECUTE**: Run nodes in dependency order
**GATE**: Validate outputs against gate rules
**DELIVER**: Return final artifacts to user
**OBSERVE**: Log execution data, collect metrics
**PATCH**: (Not shown) Apply updates to flowgrams/KBs based on learnings

---

## 2) Node Execution Rules

### Sequential Execution (Default)
By default, nodes execute in the order defined by edges:

```yaml
nodes:
  - node_id: "n1_draft"
    ...
  - node_id: "n2_review"
    ...

edges:
  - from: "n1_draft"
    to: "n2_review"
    artifact_type: "artifact.draft.v0_1"
```

**Execution:** `n1_draft` runs first, produces `artifact.draft.v0_1`, then `n2_review` consumes it.

### Parallel Execution (Optional)
If nodes have no dependencies, runtime MAY execute them in parallel:

```yaml
nodes:
  - node_id: "n1_research_A"
    ...
  - node_id: "n2_research_B"
    ...
  - node_id: "n3_synthesize"
    ...

edges:
  - from: "n1_research_A"
    to: "n3_synthesize"
  - from: "n2_research_B"
    to: "n3_synthesize"
```

**Execution:** `n1_research_A` and `n2_research_B` can run in parallel. `n3_synthesize` waits for both to complete.

### Node Inputs & Outputs
Each node declares:
- `inputs_required`: Artifacts that MUST be available
- `inputs_optional`: Artifacts that MAY be available
- `outputs_primary`: Artifacts this node produces
- `outputs_secondary`: Additional artifacts (e.g., logs, metadata)

**Runtime Guarantee:** A node will NOT execute until all `inputs_required` are available.

---

## 3) Artifact Flow

### Artifact Types
Artifacts are strongly typed. An edge declares which artifact type it carries:

```yaml
edges:
  - from: "n1_draft"
    to: "n2_review"
    artifact_type: "artifact.email_draft.v0_1"
```

**Runtime Guarantee:** The runtime will validate that the artifact produced by `n1_draft` matches the schema for `artifact.email_draft.v0_1`.

### Artifact Schemas
All artifacts must have a schema file in `/freedomation/artifacts/`:

```yaml
artifact_id: "artifact.email_draft.v0_1"
version: "0.1.0"
schema:
  required:
    - subject_line
    - body
    - cta
  optional:
    - preheader_text
    - personalization_tokens
```

**Runtime Guarantee:** Artifacts are validated against their schema before being passed to the next node.

### Artifact Immutability
Once an artifact is produced, it SHOULD NOT be modified. If a node needs to update an artifact, it produces a new version.

**Example:**
- `n1_draft` produces `artifact.email_draft.v0_1`
- `n2_review` produces `artifact.email_draft_reviewed.v0_1` (new artifact, not mutation)

---

## 4) Gate Validation

### Gate Placement
Gates can be placed:
- **Before delivery** (most common): Validate final outputs before user sees them
- **Between nodes** (optional): Validate intermediate artifacts

```yaml
gates:
  - gate_id: "ethics_gate"
    position: "before_delivery"
    gate_ref: "gate.ethics_integrity.v0_1"
    applies_to:
      - "artifact.email_draft.v0_1"
```

### Gate Execution
When a gate runs:
1. Runtime fetches gate definition (`gate.ethics_integrity.v0_1.yaml`)
2. Runtime applies validation rules to specified artifacts
3. Gate returns: `PASS` or `FAIL` + details

### Gate Pass
If gate passes:
- Execution continues to next phase (DELIVER)

### Gate Fail
If gate fails:
- Runtime produces `artifact.qa_report.v0_1` with:
  - List of failures (e.g., "Detected shame-based language in paragraph 2")
  - Remediation instructions (e.g., "Rewrite paragraph 2 without pressure tactics")
- Runtime enters **FIX loop**

---

## 5) FIX Loop Semantics

When a gate fails, the runtime attempts **deterministic auto-remediation**:

### Step 1: Generate QA Report
```yaml
artifact_id: "artifact.qa_report.v0_1"
failures:
  - rule: "no_shame_tactics"
    location: "body.paragraph_2"
    description: "Detected phrase 'You'll regret not acting now'"
    remediation: "Replace with permission-based CTA (e.g., 'If this resonates, here's the next step')"
```

### Step 2: Apply Fixes
Runtime re-invokes the failed node with:
- Original inputs
- QA report as additional input
- Instruction: "Apply remediations from QA report"

### Step 3: Re-Validate
Runtime re-runs the gate. If it passes → continue. If it fails again → escalate.

### Step 4: Escalation
After **N retries** (default: 3), runtime either:
- Returns partial output + QA report to user (manual fix required)
- OR: Fails the entire Run

**Runtime Guarantee:** FIX loops are deterministic. Same inputs + same QA report → same fixes.

---

## 6) Mode-Specific Behavior

### Trial Surface Mode
- Skip optional gates
- Allow draft-quality outputs
- Minimize latency
- Use cheaper/faster models

**Use for:** Experimentation, brainstorming, quick iterations

### Full Deep Mode
- Run all gates
- Enforce strict validation
- Use production models
- Log all execution details

**Use for:** Final deliverables, client-facing work, compliance scenarios

**Flowgrams must declare which modes they support:**
```yaml
modes:
  - trial_surface
  - full_deep
```

**Runtime Guarantee:** If a flowgram doesn't support the requested mode, runtime returns an error.

---

## 7) Minimal Determinism Rules

Freedomation aims for **practical determinism**, not absolute determinism:

### What IS Deterministic
- **Artifact schemas**: Same inputs → same validation results
- **Gate validation**: Same artifact → same pass/fail result
- **FIX loop**: Same QA report → same remediation steps
- **Node execution order**: Same flowgram → same execution sequence

### What is NOT Deterministic
- **LLM outputs**: Same prompt may produce slightly different text (this is expected)
- **Parallel execution timing**: Nodes may finish in different orders across runs
- **External API calls**: Third-party services may return different results

**Goal:** Ensure workflows are **repeatable and debuggable**, not byte-for-byte identical.

---

## 8) Error Handling

### Node Failures
If a node throws an error (e.g., API timeout, invalid input):
- Runtime logs error
- Runtime produces `artifact.error_report.v0_1`
- Runtime either:
  - **Retry** (if error is transient)
  - **Fail Run** (if error is fatal)

### Gate Failures
Gate failures trigger FIX loop (see section 5).

### Catastrophic Failures
If runtime itself crashes:
- Run status → `failed`
- User notified with error details
- Execution does NOT auto-resume (requires manual intervention)

---

## 9) Observability

Every Run produces:
- `run_id`: Unique identifier
- `start_time`, `end_time`: Timestamps
- `status`: `running | completed | failed`
- `artifacts_produced`: List of output artifacts
- `gate_results`: Pass/fail for each gate
- `node_logs`: Execution details for each node

**Runtime Guarantee:** All Runs are logged for debugging and analytics.

### Observability Levels
- **L1 (Minimal)**: Run ID, status, final outputs
- **L2 (Standard)**: + node execution times, gate results
- **L3 (Detailed)**: + full artifact payloads, LLM prompts/responses
- **L4 (Debug)**: + internal runtime state, error stack traces

**Default:** L2 (Standard)

---

## 10) Runtime Responsibilities

A Freedomation-compliant runtime MUST:
1. Parse flowgram YAML correctly
2. Execute nodes in dependency order
3. Validate artifacts against schemas
4. Run gates at specified positions
5. Implement FIX loop on gate failures
6. Support both trial and full modes
7. Log Run execution details
8. Handle errors gracefully

A runtime MAY:
1. Execute independent nodes in parallel
2. Cache artifact schemas for performance
3. Provide UI for flowgram authoring
4. Integrate with external tools (e.g., email providers)

---

## 11) Runtime Certification

Runtimes can be certified as Freedomation-compliant by:
1. Passing the **Runtime Compliance Test Suite** (future)
2. Demonstrating correct execution of reference flowgrams
3. Adhering to all MUST requirements in this document

**Certified runtimes** will be listed in the Freedomation registry.

---

## 12) Example: Outbound Value Fast Track Execution

**Flowgram:** `outbound_value_fast_track_v0_1.yaml`

**User Inputs:**
- `artifact.brand_kit.v0_1`
- `artifact.persona_sketch.v0_1`

**Execution:**
1. **INTAKE**: Validate inputs against schemas → ✅
2. **ROUTE**: Mode = `trial_surface`, create Run #12345
3. **EXECUTE**:
   - Node `n1_draft`: Run `KB-001` → produces `artifact.email_draft.v0_1`
   - Node `n2_personalize`: Run `KB-002` → produces `artifact.email_personalized.v0_1`
4. **GATE**: Run `gate.ethics_integrity.v0_1` on `artifact.email_personalized.v0_1`
   - Result: **FAIL** (detected fake urgency)
   - Generate `artifact.qa_report.v0_1`
   - **FIX**: Re-run `n2_personalize` with QA report
   - Re-validate → **PASS** ✅
5. **DELIVER**: Return `artifact.email_personalized.v0_1` to user
6. **OBSERVE**: Log Run #12345 with gate results, execution time

**Output:**
- Email draft (personalized, ethics-compliant)
- QA report (showing what was fixed)

---

## Summary

The Runtime Contract defines:
- **Lifecycle**: INTAKE → ROUTE → EXECUTE → GATE → DELIVER → OBSERVE
- **Node execution**: Sequential or parallel, inputs/outputs declared
- **Artifact flow**: Strongly typed, schema-validated, immutable
- **Gate validation**: Before delivery or between nodes
- **FIX loop**: Deterministic auto-remediation on gate failures
- **Modes**: Trial (fast) vs Full (production)
- **Determinism**: Practical, not absolute
- **Observability**: All Runs logged with execution details

**Goal:** Portable, predictable, debuggable workflows across any compliant runtime.

---

**Version:** 0.1.0
**Status:** stable
**Last Updated:** 2025-12-13
