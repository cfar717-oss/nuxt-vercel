---
skill_id: skill_builder
name: Skill Builder
description: Create or upgrade production skills (MD or XML) that integrate with SSOT + MOD routing + MMA quality gates, preserving L1–L4 progressive disclosure.
version: 1.1.0
tier: meta
status: stable
model: sonnet
tools: [view, create_file]
inputs_required: [SKILL_SPEC]
inputs_optional: [EXISTING_SKILL, SSOT_TEMPLATES, PATCH_MODULES]
outputs_primary: [SKILL_PACKAGE]
outputs_secondary: [REGISTRY_ENTRY, TEST_HARNESS, CHANGELOG]
dependencies_upstream: []
dependencies_downstream: [skill_upgrader, patch_refiner, xml_package_installer]
quality_gates: [contract_complete, l1_l4_present, mod_hooks_present, mma_gates_present, honesty_proof_policy, deterministic_outputs]
guardrails: [no_fabrication, clarity_over_clever, trust_over_tricks, lean_context]
---

# Skill Builder (Meta)

## L1 — Quick Reference (Always Loaded)

**Core Purpose:** Turn a skill specification into a production-ready **skill package** (MD + XML options), with SSOT contracts, MOD routing hooks, and MMA quality gates.

**When to Use:**
- You're creating a brand-new skill from a spec.
- You're converting a Markdown skill into lean XML.
- You're standardizing a skill to v2 (SSOT + MOD/MMA + L1–L4).

**Fast Decision Tree:**
- IF spec is vague → generate a **SPEC_QUESTIONS** list (do not build yet).
- IF existing skill provided → run **UPGRADE MODE** (preserve L2 logic).
- IF target = Claude Code XML → output **SKILL.xml + knowledge modules**.

**Outputs You Must Produce:**
- `SKILL.md` (human-readable operating manual)
- `SKILL.xml` (lean, structured, Claude Code friendly)
- `config/dependencies.yml`
- `tests/test_harness.md`
- `registry_entry.yml`
- (optional) `CHANGELOG.md`

**Success Metrics:**
- Skill has a clear IO contract + L1–L4 layering.
- MOD can route to it using triggers.
- MMA can score it with explicit gates.
- Outputs are deterministic file blocks (copy/paste = installable).

---

## L2 — Core Procedure (Deterministic Build)

### Step 0 — Parse Inputs

**Inputs:**
- **SKILL_SPEC** (required): purpose, triggers, outputs, constraints, example outputs
- **EXISTING_SKILL** (optional): prior MD/XML to preserve core logic
- **PATCH_MODULES** (optional): reusable frameworks to embed (e.g., Smooth Transitions, Neuro-Resonance)

**Action:**
1. Identify: `skill_id`, audience, job-to-be-done, and "definition of done".
2. Extract required SSOT objects (PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK, VOICE_GUIDE)
3. Choose output formats:
   - Always: SKILL.md (human-readable documentation)
   - If Claude Code / lean: SKILL.xml + knowledge modules

**Validation:**
- If any of these are missing: triggers, outputs, constraints, examples → output **SPEC_QUESTIONS** and STOP.

**PATCH BLOCK v1.1+ (2025-12-18):** Require SSOT IDs in PROJECT_BRIEF + forbid invention of missing fields.
- If PROJECT_BRIEF required: must include project_id, asset_id, owner_agent, version
- Never invent values for missing SSOT fields
- Generate EVIDENCE_REQUEST section if proof missing but claims present
- Flag missing MESSAGE_SPINE for multi-asset projects

**Output:**
```yaml
parsed_spec:
  skill_id: ""
  skill_name: ""
  codename: ""
  purpose: ""
  ssot_required: []
  ssot_optional: []
  outputs_primary: []
  outputs_secondary: []
  # v1.1+ SSOT discipline
  requires_ssot_ids: true|false
  forbids_invention: true  # Always true
```

---

### Step 1 — Define the Skill Contract

**Produce `contract`:**

```yaml
skill_contract:
  inputs_required: []      # SSOT objects + minimum fields
  inputs_optional: []      # Nice-to-have inputs
  outputs_primary: []      # Main deliverable artifact
  outputs_secondary: []    # Supporting artifacts
  non_goals: []            # What this skill is NOT for
  hard_guardrails: []      # Honesty, compliance, consent, no manipulation
```

**Required Contract Elements:**
- At least one required input
- At least one primary output
- Clear definition of what the skill does NOT do
- Explicit guardrails (no fabrication, no fake urgency, etc.)

**Validation:**
- If primary output format unclear → request clarification
- If inputs don't match standard SSOT objects → flag non-standard inputs

---

### Step 2 — Build L1–L4 (Progressive Disclosure)

**L1 — Quick Reference (200-250 tokens)**

**Must Include:**
- Core purpose (one sentence)
- When to use (3-5 triggers)
- Fast decision tree (IF/THEN for common scenarios)
- Success metrics (3-5 measurable outcomes)

**Rules:**
- Extreme brevity (bullet points only)
- No full procedures (that's L2)
- No edge cases (that's L3)
- No technical specs (that's L4)

**Template:**
```markdown
## L1 — Quick Reference (Always Loaded)

**Core Purpose:** [One sentence]

**When to Use:**
- [Trigger 1]
- [Trigger 2]
- [Trigger 3]

**Fast Decision Tree:**
- IF [condition] → [action]
- IF [condition] → [action]

**Success Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]
```

---

**L2 — Core Procedure (1800-2500 tokens)**

**Must Include:**
- Complete step-by-step procedure (4-8 steps typical)
- Each step has: purpose, actions, validation, output
- Decision heuristics (8-10 IF/THEN rules)
- Quality standards (checklist with 7-10 items)
- Coordination protocols (who to wake, when)
- Agent behavior rules (5-8 implementation guidelines)

**Rules:**
- Procedures must be deterministic (same input → same output)
- Each step must have validation criteria
- No framework variations (that's L3)
- No algorithmic details (that's L4)

**Template:**
```markdown
## L2 — Core Procedure

### Step 0 — [Step Name]
**Purpose:** [Why this step]
**Actions:**
1. [Action 1]
2. [Action 2]
**Validation:**
- [Check 1]
- [Check 2]
**Output:** [What this step produces]

### Step 1 — [Step Name]
...

## L2 — Decision Heuristics (IF/THEN Rules)
1) If [condition] → [action] (rationale)
2) If [condition] → [action] (rationale)
...
```

---

**L3 — Advanced Usage (3500-5000 tokens)**

**Must Include:**
- Framework variations (for different contexts)
- Edge case handling (specific scenarios)
- Anti-pattern diagnostics (with examples)
- Extended examples (complete walkthroughs)
- Troubleshooting guides (when things break)
- Optimization patterns

**Load Triggers:**
- Task complexity high
- Edge case detected
- Optimization requested
- Troubleshooting needed

**Unload Triggers:**
- Task completed
- Edge case resolved
- Context pressure (approaching token limit)

**Template:**
```markdown
## L3 — Advanced Usage

### Edge Cases
**Case 1: [Scenario Name]**
- **Trigger:** [When this happens]
- **Approach:** [How to handle]
- **Modification:** [What changes]

### Anti-Patterns (Failure Modes)
**AP1: [Anti-Pattern Name]**
- **Detection:** [How to spot it]
- **Root Cause:** [Why it happens]
- **Recovery:** [How to fix]

### Optimization Patterns
**Pattern 1: [Pattern Name]**
- **Description:** [What this optimizes]
- **Implementation:** [How to apply]
```

---

**L4 — Technical Specification (2000-3000 tokens)**

**Must Include:**
- Input/output schemas (formal contracts)
- Algorithms (with pseudocode if applicable)
- Performance benchmarks (with metrics)
- Formal constraints (precise definitions)
- Testing specifications (validation logic)
- Integration protocols (MOD/MMA hooks)

**Load Triggers:**
- Building new skill
- Optimizing architecture
- Debugging system
- Meta-operation

**Audience:** Primarily for system architects, not end users

**Template:**
```markdown
## L4 — Technical Specification

### Input Schema
\`\`\`yaml
input_schema:
  required:
    - field_name:
        type: string|list|object
        validation: [rules]
\`\`\`

### Output Schema
\`\`\`yaml
output_schema:
  primary:
    format: markdown|yaml|json
    structure: [sections]
\`\`\`

### Quality Gates
\`\`\`yaml
quality_gates:
  - gate_name:
      severity: critical|high|medium
      rule: [validation rule]
      threshold: [numeric if applicable]
\`\`\`

### Failure Modes
\`\`\`python
def handle_failure_mode(symptom, root_cause):
    # Recovery logic
    pass
\`\`\`
```

---

### Step 3 — Add MOD Routing Hooks

**Create routing integration:**

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
    high: []      # Skills that should always wake (sister skills, dependencies)
    medium: []    # Skills that often coordinate
    low: []       # Skills rarely needed but good to have aware

  context_budget:
    estimated: 0  # Typical token count
    maximum: 0    # Max allowable
```

**Validation:**
- At least one routing trigger defined
- Context budget estimated (realistic, not placeholder)
- Awakening recommendations categorized

---

### Step 4 — Add MMA Quality Gates

**Create quality validation:**

```yaml
mma_integration:
  quality_dimensions:
    - dimension_name:
        weight: critical|high|medium|low
        threshold: 0-10
        validation: "[what gets checked]"

  hard_gates:
    - gate_name:
        severity: critical|high
        description: "[what this prevents]"

  fix_routing:
    - condition: "[dimension] < [threshold]"
      route: "[skill_id to fix]"
      reason: "[why this skill]"
```

**Required Dimensions (choose applicable):**
- Strategy Alignment (does it serve objective?)
- Clarity & Structure (is it clear and scannable?)
- Voice Consistency (matches VOICE_GUIDE?)
- Proof Discipline (claims backed by EVIDENCE_PACK?)
- Neuro-Resonance (activates correct neuro-axes?)
- CTA Integrity (clear call-to-action?)
- Ethical Guardrails (no manipulation?)

**Validation:**
- At least 3 quality dimensions defined
- At least 1 hard gate (critical severity)
- Fix routing deterministic (specific skills, not vague)

---

### Step 5 — Emit the Package as File Blocks

**You MUST output using this exact delimiter pattern:**

```
===FILE: path/filename.ext===
[contents]
===END FILE===
```

**No extra commentary between files.**

**Required Files:**
1. `SKILL.md` — Human-readable documentation (L1-L4 layers)
2. `SKILL.xml` — Structured XML (if Claude Code target)
3. `config/dependencies.yml` — Upstream/downstream skill relationships
4. `tests/test_harness.md` — How to test this skill
5. `registry_entry.yml` — Entry for MOD skill registry

**Optional Files:**
6. `CHANGELOG.md` — Version history
7. `knowledge/modules.xml` — Reusable knowledge modules
8. `examples/` — Example inputs and expected outputs

---

### Step 6 — Add Required Output Shapes (v1.1+)

**PATCH BLOCK v1.1+ (2025-12-18):** Add SSOT schemas, MOD_PLAN + MMA_REPORT shapes, Golden Runs, Failure Mode Playbooks.

**Every skill must include these standard output shapes:**

#### MOD_PLAN Output Shape
```yaml
MOD_PLAN:
  task_classification:
    type: "research|strategy|copy|polish|teardown|meta"
    complexity: 1-5
    stakes: "low|medium|high"
  skill_plan:
    primary_skill: ""
    layers: "L1+L2|L1+L2+L3|ALL"
    awaken_L1: []
    execution_order: []
  context_budget:
    max_total_tokens: 12000
    allocations: {}
    do_not_load: []
  ssot_artifacts:
    load: []
    missing: []
  coordination:
    conflict_risk: "none|low|medium|high"
```

#### MMA_REPORT Output Shape
```yaml
MMA_QUALITY_REPORT:
  overall: "PASS|FIX|ESCALATE_HPE|ESCALATE_SCD|ESCALATE_HUMAN"
  scores:
    strategy_alignment: 0-10
    clarity_structure: 0-10
    voice_consistency: 0-10
    proof_discipline: 0-10
    neuro_resonance: 0-10
    cta_integrity: 0-10
    ethical_guardrails: 0-10
  top_3_fixes:
    - dimension: ""
      issue: ""
      fix: ""
      impact: "critical|high|moderate|low"
  route_to: ""
```

#### SSOT Scaffolds (Auto-include in L4)

**PROJECT_BRIEF Template:**
```yaml
PROJECT_BRIEF:
  project_id: ""           # Required
  asset_id: ""             # Required
  version: "1.0"          # Required
  owner_agent: ""         # Required (skill_id)
  date: ""                # YYYY-MM-DD
  objective: {}
  avatar: {}
  offer: {}
  nonnegotiables: {}
  tone_controls: {}
  evidence_pack_refs: []
```

**MESSAGE_SPINE Template:**
```yaml
MESSAGE_SPINE:
  project_id: ""
  version: "1.0"
  core_promise: ""
  mechanism_paragraph_canonical: ""
  proof_pillars: []
  objection_counters: []
  cta_frame: {}
  taboo_claims_forbidden: []
```

**EVIDENCE_PACK Template:**
```yaml
EVIDENCE_PACK:
  project_id: ""
  version: "1.0"
  proof_items:
    - id: "PROOF_01"
      type: "study|testimonial|case_study|narrative|technical"
      source: ""
      confidence: "STRONG|MODERATE|WEAK"
      allowed_claims: []
      forbidden_claims: []
  claim_rules: {}
```

#### Golden Runs Scaffold (Auto-include in tests/)

```yaml
GOLDEN_RUN:
  id: "GR-[SKILL]-[SCENARIO]-01"
  name: "[Descriptive Name]"
  inputs:
    PROJECT_BRIEF_ref: "..."
    MESSAGE_SPINE_ref: "..."
    task: "[task description]"
  expected_output:
    [output_criteria]
  pass_criteria:
    - "MMA scores all >= 7"
    - "[specific quality check]"
```

#### Failure Mode Playbook (Auto-include in L3)

```yaml
FAILURE_MODE_PLAYBOOK:
  FM1_[failure_name]:
    detection: "[how to spot it]"
    recovery:
      - "[step 1]"
      - "[step 2]"
      - "rerun MMA"
  FM2_[failure_name]:
    detection: "[how to spot it]"
    recovery:
      - "[recovery steps]"
```

#### CBM Policy Module (Auto-embed in MOD references)

```yaml
context_budget_manager:
  load_rules:
    L1_always_on: []
    L2_executing_only: []
    L3_conditional:
      triggers: []
      unload: []
    L4_meta_only:
      triggers: []
  unload_rules:
    immediate: []
    pressure_based: []
  budget_enforcement:
    max_total: 12000
    if_exceeded: []
```

#### Conflict Resolution Protocol (Auto-reference in coordination)

```yaml
CONFLICT_RESOLUTION_PROTOCOL:
  hierarchy:
    strategy: ["Strategic Copy Director", "Offer Architect"]
    execution: ["Sales Page Copywriter", "Email Campaign Genius", "VSL*"]
    refinement: ["Human Persuasion Editor", "Master Writing Partner"]
  deterministic_rules:
    - "IF execution contradicts strategy THEN strategy wins"
    - "IF two execution agents conflict THEN escalate to SCD"
    - "IF refinement requests major rewrite THEN escalate to human"
    - "IF compliance/ethics risk THEN HALT + human review"
```

---

## L2 — Constitutional Compliance (Embedded in Every Skill)

**Every skill must include:**

```yaml
constitutional_compliance:
  - principle: "human_first"
    declaration: "This skill augments human operators; humans own final truth"
    human_role: "[what humans must review/approve]"

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
```

---

## L3 — Advanced Usage

### Upgrade Mode (Existing Skill Provided)

**Hard rules:**
- Preserve L2 core logic unless it is contradictory or unsafe.
- Move verbosity into L3/L4 knowledge files.
- Add missing MOD/MMA specs without rewriting the "engine".
- Never remove existing quality gates (only add new ones).

**Process:**
1. Read existing skill completely
2. Identify L1-L4 structure (or lack thereof)
3. Extract core procedures into L2
4. Move edge cases/examples into L3
5. Move technical specs into L4
6. Add MOD/MMA integration
7. Update version number (increment appropriately)
8. Generate CHANGELOG entry

---

### Patch Mode

**If a patch module is provided:**
- Add it to `knowledge/modules/` as a reusable unit
- Reference it from L2 procedure ("When flow drop-off detected, apply module X")
- Update version number (minor increment, e.g., 1.0 → 1.1)
- Document in CHANGELOG

**Patch Block Format:**
```markdown
## [SECTION NAME] (v1.1+)

**PATCH BLOCK: Integrated [DATE] | [Brief Description]**

[New content here]

**End Patch Block**
```

---

### XML Generation Mode

**When target format is XML:**

Use this structure (based on Ultramind v2.0 schema):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Skill skill_id="[id]" version="[version]" status="[status]">

  <Meta>
    <Name>[Skill Name]</Name>
    <Description>[Brief description]</Description>
    <CreatedBy agent_or_human="agent" agent_id="skill_builder_skill"/>
    <DateCreated>[YYYY-MM-DD]</DateCreated>
    <Tier>[tier]</Tier>
    <Status>[status]</Status>
    <Model>[model]</Model>
  </Meta>

  <Contract>
    <InputsRequired>
      <Input>[input_name]</Input>
    </InputsRequired>
    <InputsOptional>
      <Input>[input_name]</Input>
    </InputsOptional>
    <OutputsPrimary>
      <Output format="[format]">[output_name]</Output>
    </OutputsPrimary>
    <OutputsSecondary>
      <Output format="[format]">[output_name]</Output>
    </OutputsSecondary>
  </Contract>

  <Dependencies>
    <UpstreamDependencies>
      <Skill priority="high">[skill_id]</Skill>
    </UpstreamDependencies>
    <DownstreamConsumers>
      <Skill>[skill_id]</Skill>
    </DownstreamConsumers>
  </Dependencies>

  <MODIntegration>
    <RoutingTriggers>
      <Trigger>[trigger_condition]</Trigger>
    </RoutingTriggers>
    <LayerLoadDefault>[L1+L2]</LayerLoadDefault>
    <AwakenRecommendations>
      <High><Skill>[skill_id]</Skill></High>
    </AwakenRecommendations>
    <ContextBudget>
      <Estimated>[tokens]</Estimated>
      <Maximum>[tokens]</Maximum>
    </ContextBudget>
  </MODIntegration>

  <MMAIntegration>
    <QualityDimensions>
      <Dimension name="[name]" weight="[weight]">
        <Threshold>[0-10]</Threshold>
        <Validation>[description]</Validation>
      </Dimension>
    </QualityDimensions>
    <HardGates>
      <Gate severity="[severity]">[gate_name]</Gate>
    </HardGates>
  </MMAIntegration>

  <ConstitutionalCompliance>
    <Principle name="[name]">
      <Declaration>[text]</Declaration>
    </Principle>
  </ConstitutionalCompliance>

  <Guardrails>
    <Guardrail priority="[priority]">
      <Rule>[rule_name]</Rule>
      <Description>[description]</Description>
    </Guardrail>
  </Guardrails>

  <Layer level="1" name="Quick Reference">
    <LoadPriority>always</LoadPriority>
    <Purpose>[purpose]</Purpose>
    <TokenBudget>[range]</TokenBudget>
    <!-- L1 content -->
  </Layer>

  <Layer level="2" name="Core Procedure">
    <LoadPriority>when_executing</LoadPriority>
    <Purpose>[purpose]</Purpose>
    <TokenBudget>[range]</TokenBudget>
    <!-- L2 content -->
  </Layer>

  <Layer level="3" name="Advanced Usage">
    <LoadPriority>when_complexity_high_OR_edge_case</LoadPriority>
    <Purpose>[purpose]</Purpose>
    <TokenBudget>[range]</TokenBudget>
    <!-- L3 content -->
  </Layer>

  <Layer level="4" name="Technical Specification">
    <LoadPriority>meta_work_only</LoadPriority>
    <Purpose>[purpose]</Purpose>
    <TokenBudget>[range]</TokenBudget>
    <!-- L4 content -->
  </Layer>

  <VersionHistory>
    <Version number="[version]" date="[date]">
      <Changes>
        <Change>[description]</Change>
      </Changes>
      <Status>[status]</Status>
    </Version>
  </VersionHistory>

</Skill>
```

---

## L4 — Technical Spec (Builder Internals)

### Output Package Layout

```
/skills/{tier}/{skill_id}/
  SKILL.md
  SKILL.xml
  knowledge/
    modules.xml
    level3_advanced.md
    level4_technical_spec.md
  config/dependencies.yml
  tests/test_harness.md
  registry_entry.yml
  CHANGELOG.md (optional)
```

---

### Determinism Rules

1. **Never invent proof, outcomes, medical claims, numbers, or testimonials.**
2. If proof is missing, generate an "EVIDENCE_REQUEST" section.
3. Always include example invocations + expected output shape.
4. Token budgets must be realistic (not placeholder zeros).
5. Quality gates must be specific and measurable.
6. Fix routing must be deterministic (specific skills, not "review").

---

### Token Budget Validation

```python
def validate_layer_size(layer, content):
    token_count = estimate_tokens(content)

    limits = {
        "L1": (200, 250),
        "L2": (1800, 2500),
        "L3": (3500, 5000),
        "L4": (2000, 3000)
    }

    min_tokens, max_tokens = limits[layer]

    if token_count < min_tokens:
        return "INSUFFICIENT", "Add more essential content"
    elif token_count > max_tokens:
        return "BLOATED", "Compress or move to higher layer"
    else:
        return "VALID", "Within acceptable range"
```

---

### SSOT Integration Enforcement

**Every production skill must:**
- Declare required SSOT inputs (PROJECT_BRIEF minimum)
- Reference RESONANCE_CONSTITUTION.xml (if persuasion/copy skill)
- Use MESSAGE_SPINE for consistency (if multi-asset project)
- Validate against EVIDENCE_PACK (if making claims)
- Match VOICE_GUIDE tone controls (if specified)

**Validation:**
```python
def enforce_ssot_discipline(skill):
    if skill.involves_claims and not skill.requires_evidence_pack:
        flag("Missing EVIDENCE_PACK requirement")

    if skill.creates_copy and not skill.references_message_spine:
        warn("Consider MESSAGE_SPINE for consistency")

    if skill.persuasion_based and not skill.references_neuro_constitution:
        flag("Must reference RESONANCE_CONSTITUTION.xml")
```

---

### Registry Entry Generation

**Auto-generate registry entry:**

```yaml
skill_registry_entry:
  id: "[skill_id]"
  name: "[Skill Name]"
  codename: "[Codename]"
  version: "[version]"
  type: "[skill_type]"
  primary_outcome: "[what_it_produces]"

  inputs_required: []
  inputs_optional: []
  outputs: []

  dependencies:
    upstream: []
    downstream: []

  tags: []
```

---

### Test Harness Generation

**Auto-generate test structure:**

```yaml
skill_test_harness:
  skill_id: "[skill_id]"
  version: "[version]"

  test_cases:
    - test_name: "[descriptive_name]"
      input:
        - [input_artifact]: [sample_or_ref]
      expected_output:
        - [output_format]: [structure]
        - [quality_metric]: [threshold]
      quality_checks:
        - [check_name]: true
      pass_criteria:
        - [criterion]: true

  integration_tests:
    - workflow: "[multi-skill_workflow]"
      steps: []
      validation: []

  regression_tests:
    baseline_version: "[version]"
    golden_runs: []
```

---

## END SKILL BUILDER v1.0

**Next Evolution (v1.1):**
- Native support for canonical SSOT IDs
- Message Spine + Evidence Pack scaffolds (auto-generate if missing)
- MOD/MMA forms (required outputs)
- CBM enforcement block (auto-embed)
- Golden Runs + Failure Mode Playbooks as default shipped artifacts
