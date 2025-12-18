---
skill_id: [skill_id]
name: "[Skill Name]"
codename: "[The Nickname]"
description: "[One sentence: what this skill does]"
version: "[version]"
tier: [system|meta|production|experimental]
status: [draft|beta|active|deprecated]
model: [sonnet|opus|haiku]
tools: []
inputs_required: ["INPUT_1", "INPUT_2"]
inputs_optional: ["OPTIONAL_1"]
outputs_primary: ["OUTPUT_1"]
outputs_secondary: ["OUTPUT_2"]
dependencies_upstream: ["upstream_skill_1"]
dependencies_downstream: ["downstream_skill_1"]
quality_gates: ["gate_1", "gate_2"]
guardrails: ["no_fabrication", "clarity_over_clever", "trust_over_tricks"]
---

# [Skill Name] v[version]

## L1 — Quick Reference (Always Loaded)

**Core Purpose:** [One sentence: what this skill does]

**When to Use:**
- [Trigger scenario 1]
- [Trigger scenario 2]
- [Trigger scenario 3]

**Fast Decision Tree:**
- IF [condition] → [action]
- IF [condition] → [action]
- IF [condition] → [action]

**Required Outputs:**
- `[output_1]` — [description]
- `[output_2]` — [description]

**Success Metrics:**
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]

---

## L2 — Core Procedure (Deterministic Execution)

### Step 0 — Parse Inputs

**Purpose:** [Why this step exists]

**Inputs:**
- **[INPUT_NAME]** (required): [What this provides]
- **[INPUT_NAME]** (optional): [What this provides]

**Actions:**
1. [First action with specific details]
2. [Second action with specific details]
3. [Third action with specific details]

**Validation:**
- If [condition] → [action or error]
- Check: [validation rule]

**Output:**
```yaml
parsed_inputs:
  field_1: ""
  field_2: ""
```

---

### Step 1 — [Main Procedure Step Name]

**Purpose:** [Why this step exists]

**Actions:**
1. [Action with specific instructions]
2. [Action with specific instructions]

**Validation:**
- [Required condition]
- [Quality threshold]

**Output:** [What this step produces]

---

### Step 2 — [Next Step Name]

**Purpose:** [Why this step exists]

**Actions:**
1. [Action]
2. [Action]

**Validation:**
- [Check 1]
- [Check 2]

**Output:** [Artifact produced]

---

### Step N — Generate Final Output (Required)

**Purpose:** Package all work into standard output format

**Actions:**
1. Combine all intermediate results
2. Apply final quality checks
3. Format per output schema
4. Add metadata (version, timestamp, agent)

**Validation:**
- All required sections present?
- Passes MMA quality gates?
- SSOT discipline maintained?

**Output:** [FINAL_OUTPUT_NAME]

---

## L2 — Decision Heuristics (IF/THEN Rules)

1) **If [condition]** → [action] (rationale: [why])
2) **If [condition]** → [action] (rationale: [why])
3) **If [condition]** → [action] (rationale: [why])
4) **If [condition]** → [action] (rationale: [why])
5) **If [condition]** → [action] (rationale: [why])
6) **If [condition]** → [action] (rationale: [why])
7) **If [condition]** → [action] (rationale: [why])
8) **If [condition]** → [action] (rationale: [why])

---

## L2 — Quality Standards (Checklist)

**Before delivering output, verify:**

- [ ] **Strategy Alignment** — Serves core objective from PROJECT_BRIEF
- [ ] **Clarity** — Clear, scannable, well-organized
- [ ] **Voice Consistency** — Matches VOICE_GUIDE (if provided)
- [ ] **Proof Discipline** — Claims backed by EVIDENCE_PACK or qualified
- [ ] **Neuro-Resonance** — Activates target axes with proper balance
- [ ] **CTA Integrity** — Clear, singular, appropriately urgent
- [ ] **Ethics** — No manipulation, fake urgency, fabrication
- [ ] **SSOT Discipline** — No invented fields or values
- [ ] **Completeness** — All required sections present
- [ ] **Token Efficiency** — Within budget without sacrificing quality

---

## L2 — Coordination Protocols

**When to wake other skills:**

- **[skill_id]** (high priority) — [When/why coordination needed]
- **[skill_id]** (medium priority) — [When/why coordination needed]
- **[skill_id]** (low priority) — [When/why coordination needed]

**Handoff protocol:**
```yaml
handoff:
  from_skill: "[this_skill_id]"
  to_skill: "[downstream_skill_id]"
  artifact: "[artifact_name]"
  validation:
    - "Schema matches expected format"
    - "Required fields present"
  coordination_notes: "[Special instructions for downstream]"
```

---

## L2 — Agent Behavior Rules

1. **[Category]**: [Guideline]
   - Example: [Concrete example]

2. **[Category]**: [Guideline]
   - Example: [Concrete example]

3. **[Category]**: [Guideline]
   - Example: [Concrete example]

4. **[Category]**: [Guideline]
   - Example: [Concrete example]

5. **[Category]**: [Guideline]
   - Example: [Concrete example]

---

## L2 — Constitutional Compliance (Embedded)

**Every execution must honor:**

```yaml
constitutional_compliance:
  - principle: "human_first"
    declaration: "This skill augments human operators; humans own final truth"
    human_role: "[What humans must review/approve]"

  - principle: "evidence_honesty"
    declaration: "No fabricated proof; qualify uncertainty"
    enforcement: "All claims validated against EVIDENCE_PACK or softened"

  - principle: "consent_intent"
    declaration: "Persuasion respects autonomy; no deceptive patterns"
    guardrails:
      - "No fake urgency/scarcity"
      - "No fear-mongering beyond reality-stating"
      - "Transparency allowed (breaking 4th wall)"

  - principle: "radical_clarity"
    declaration: "Audience, promise, mechanism, proof, and CTA explicit"
    enforcement: "4-question test: Promise? Proof? Trust? Deal?"
```

---

## L3 — Advanced Usage

### Edge Cases

**Case 1: [Edge Case Name]**
- **Trigger:** [When this happens]
- **Approach:** [How to handle]
- **Modifications:** [What changes from standard procedure]

**Case 2: [Edge Case Name]**
- **Trigger:** [When this happens]
- **Approach:** [How to handle]
- **Modifications:** [What changes]

---

### Anti-Patterns (Failure Modes)

**AP1: [Anti-Pattern Name]**
- **Detection:** [How to spot it]
- **Root Cause:** [Why it happens]
- **Recovery:** [How to fix]
- **Prevention:** [How to avoid in future]

**AP2: [Anti-Pattern Name]**
- **Detection:** [How to spot it]
- **Root Cause:** [Why it happens]
- **Recovery:** [How to fix]
- **Prevention:** [How to avoid]

---

### Failure Mode Playbook (Micro-Heal)

**FM1: [Failure Name]**
- **Detection:** [Symptom description]
- **Recovery:**
  1. [Recovery action]
  2. [Recovery action]
  3. Rerun MMA
  4. If still failing → [escalation path]

**FM2: [Failure Name]**
- **Detection:** [Symptom]
- **Recovery:**
  1. [Step]
  2. [Step]
  3. Rerun MMA

**FM3: [Failure Name]**
- **Detection:** [Symptom]
- **Recovery:**
  1. [Step]
  2. [Step]
  3. Rerun MMA

---

### Optimization Patterns

**Pattern 1: [Optimization Name]**
- **Description:** [What this optimizes]
- **Implementation:** [How to apply]
- **Best For:** [When to use]

**Pattern 2: [Optimization Name]**
- **Description:** [What this optimizes]
- **Implementation:** [How to apply]
- **Best For:** [When to use]

---

### Extended Examples

**Example 1: [Complete Walkthrough]**

**Scenario:** [Detailed scenario description]

**Inputs:**
```yaml
[exact inputs provided]
```

**Process:**
1. Step 0: [What happened]
2. Step 1: [What happened]
3. Step 2: [What happened]
   ...

**Output:**
```markdown
[final result with annotations]
```

**Quality Scores:**
- Strategy Alignment: 8.5
- Clarity: 8.0
- Voice: 8.0
- Proof: 9.0
- Neuro: 8.0
- CTA: 8.0
- Ethics: 9.5
- **Average: 8.4**

---

### Troubleshooting Guide

**Issue:** [Observable problem]
- **Diagnosis:** [Likely cause]
- **Solution:** [Fix steps]

**Issue:** [Observable problem]
- **Diagnosis:** [Likely cause]
- **Solution:** [Fix steps]

---

## L4 — Technical Specification

### Input Schemas

**PROJECT_BRIEF Schema:**
```yaml
PROJECT_BRIEF:
  # Required fields
  project_id: string           # Must be unique
  asset_id: string             # Must be unique within project
  version: string              # Semantic versioning
  owner_agent: string          # skill_id that owns this asset
  date: string                 # YYYY-MM-DD

  # Required content
  objective:
    primary_goal: string
    success_metric: string

  avatar:
    primary_segment: string
    pains: list[string]
    desires: list[string]
    sophistication_level: string

  offer:
    name: string
    price: string
    mechanism: string
    differentiators: list[string]
    cta_primary: string

  # Constraints
  nonnegotiables:
    claims_limits: list[string]
    compliance: list[string]
    brand_donts: list[string]

  # Optional
  tone_controls:
    warmth: 0-10
    authority: 0-10
    humor: 0-10
    urgency: 0-10
    mystique: 0-10

  evidence_pack_refs: list[string]
```

---

### Output Schemas

**[PRIMARY_OUTPUT_NAME] Schema:**
```markdown
# [Output Format]

## Section 1
[Content structure]

## Section 2
[Content structure]

## Required Metadata
- skill_id: [this_skill]
- version: [skill_version]
- generated: [timestamp]
- mma_score: [if_scored]
```

---

### Algorithms

**Algorithm: [Algorithm Name]**

**Purpose:** [What this computes]

**Pseudocode:**
```python
def algorithm_name(inputs):
    # Step 1: [description]
    result = process(inputs)

    # Step 2: [description]
    validated = validate(result)

    # Step 3: [description]
    if validated:
        return result
    else:
        return error_message
```

---

### Performance Benchmarks

**Target Metrics:**
- **Output Quality:** MMA average >= 8.0 (minimum 7.0)
- **Token Efficiency:** < 3000 tokens per execution
- **Execution Time:** < 2 minutes (typical case)
- **Success Rate:** > 90% PASS on first run

---

### Formal Constraints

**Constraint 1:** [Type]
- **Rule:** [Precise definition]
- **Enforcement:** [How enforced]

**Constraint 2:** [Type]
- **Rule:** [Precise definition]
- **Enforcement:** [How enforced]

---

### Testing Specifications

**Golden Run 1:**
```yaml
GOLDEN_RUN:
  id: "GR-[SKILL]-[SCENARIO]-01"
  name: "[Test case name]"

  inputs:
    PROJECT_BRIEF_ref: "[path or inline]"
    MESSAGE_SPINE_ref: "[path or inline]"
    task: "[exact task description]"

  expected_output:
    format: "[markdown|yaml|json]"
    structure: [list of required sections]
    quality_benchmarks:
      clarity: 8.0
      proof_discipline: 9.0

  pass_criteria:
    - "MMA scores all >= 7.0"
    - "[Specific quality check]"
    - "[Specific compliance check]"

  baseline_scores:
    strategy_alignment: 0.0
    clarity_structure: 0.0
    voice_consistency: 0.0
    proof_discipline: 0.0
    neuro_resonance: 0.0
    cta_integrity: 0.0
    ethical_guardrails: 0.0
    average: 0.0
```

---

### Integration Protocols

**MOD Integration:**
- **Required Output Shape:** MOD_PLAN
- **Context Budget:** [estimated tokens]
- **Awakening Protocol:** [which skills to wake, when]

**MMA Integration:**
- **Required Output Shape:** MMA_QUALITY_REPORT
- **Scoring Algorithm:** [reference to algorithm]
- **Fix Routing:** [deterministic routing rules]

---

## Version History

### v[version] — [YYYY-MM-DD]

**Status:** [draft|beta|active]

**Changes:**
- [feature] [Description of change]
- [bugfix] [Description of fix]
- [enhancement] [Description of improvement]

**Baseline Scores:**
```yaml
strategy_alignment: 0.0
clarity_structure: 0.0
voice_consistency: 0.0
proof_discipline: 0.0
neuro_resonance: 0.0
cta_integrity: 0.0
ethical_guardrails: 0.0
average: 0.0
```

**Known Issues:** [List any known limitations or bugs]

**Next Evolution:** [Planned improvements for next version]

---

## MOD Routing Hooks (Reference)

```yaml
mod_integration:
  routing_triggers:
    - "task_type == '[task_type]'"
    - "deliverable == '[output_format]'"
    - "user_requests == '[natural_language_trigger]'"

  layer_load_default: "L1+L2"

  layer_load_conditions:
    L3: "complexity >= 4 OR edge_case_detected"
    L4: "skill_building OR debugging OR schema_work"

  awaken_recommendations:
    high: ["[skill_id_1]", "[skill_id_2]"]
    medium: ["[skill_id_3]"]
    low: ["[skill_id_4]"]

  context_budget:
    estimated: [typical_token_count]
    maximum: [max_allowable_tokens]
```

---

## MMA Quality Gates (Reference)

```yaml
quality_dimensions:
  - dimension: strategy_alignment
    weight: critical
    threshold: 7.0
    validation: "Does output serve the core objective?"

  - dimension: clarity_structure
    weight: high
    threshold: 7.0
    validation: "Is output clear and scannable?"

  - dimension: voice_consistency
    weight: high
    threshold: 7.0
    validation: "Does output match VOICE_GUIDE?"

  - dimension: proof_discipline
    weight: critical
    threshold: 8.0
    validation: "Are claims backed by EVIDENCE_PACK?"

  - dimension: neuro_resonance
    weight: high
    threshold: 7.0
    validation: "Activates target neuro-axes with balance?"

  - dimension: cta_integrity
    weight: medium
    threshold: 7.0
    validation: "Is CTA clear and singular?"

  - dimension: ethical_guardrails
    weight: critical
    threshold: 9.0
    validation: "Is output honest and manipulation-free?"

hard_gates:
  - name: no_fabrication
    severity: critical
    on_violation: "HALT + ESCALATE_HUMAN"

  - name: no_disease_claims
    severity: critical
    on_violation: "HALT + ESCALATE_HUMAN"

  - name: evidence_backed
    severity: high
    on_violation: "FIX + rerun_mma"

fix_routing:
  - condition: "proof_discipline < 6"
    action: "ADD_EVIDENCE_PACK_REFERENCES or DOWNGRADE_LANGUAGE"

  - condition: "voice_consistency < 6"
    action: "ROUTE_TO_master_writing_partner"

  - condition: "overall_avg < 6"
    action: "ESCALATE_TO_human_persuasion_editor"

  - condition: "overall_avg < 4"
    action: "ESCALATE_TO_strategic_copy_director"
```

---

## END SKILL TEMPLATE v2.0
