---
skill_id: skill_builder
version: 1.1.0
owner: "Ultramind Meta-Infrastructure"
tier: meta
last_updated: "2025-12-17"

intent: "Transform masterclass content and expert knowledge into production-grade XML skills with progressive disclosure (L1-L4), SSOT integration, MOD routing, MMA validation, and self-healing capabilities."

inputs_required:
  - MASTERCLASS_TRANSCRIPT
  - SKILL_INTENT

inputs_optional:
  - EXISTING_SKILL_FOR_UPGRADE
  - RELATED_SKILLS_CONTEXT
  - GOLDEN_RUN_EXAMPLES

outputs_primary:
  - SKILL_XML
  - SKILL_MARKDOWN_REFERENCE

outputs_secondary:
  - MOD_ROUTING_CONFIG
  - MMA_VALIDATION_SPEC
  - GOLDEN_RUN_TEST_CASES
  - FAILURE_MODE_PLAYBOOK

dependencies_upstream:
  - xml_synthesizer: "provides structured knowledge extraction from masterclasses"
  - knowledge_organizer: "provides organized concept hierarchy and relationship mapping"

dependencies_downstream:
  - mod: "receives routing configuration and awakening protocol specs"
  - mma: "receives validation gates and scoring criteria"
  - test_harness: "receives golden run test cases"

quality_gates:
  - progressive_disclosure_enforced: "L1 (≤250 tokens), L2 (≤2800 tokens), L3 (≤5500 tokens), L4 (≤3200 tokens)"
  - ssot_contracts_clear: "Required/optional inputs and outputs explicitly defined"
  - mod_integration_complete: "Routing triggers, awakening protocol, and layer load conditions specified"
  - mma_hooks_present: "Quality gates and validation criteria defined"
  - failure_modes_documented: "At least 3 failure modes with detection and recovery patterns"
  - golden_runs_scaffolded: "At least 1 example golden run provided"

guardrails:
  - no_bloat: "Each layer must respect token budgets; cut ruthlessly to essentials"
  - no_guessing_contracts: "If input requirements unclear, flag for clarification"
  - no_generic_validation: "MMA hooks must be specific to the skill's domain"
  - version_properly: "Use semantic versioning; document breaking changes"

token_budget:
  L1: 300
  L2: 3000
  L3: 6000
  L4: 3500

mod_integration:
  routing_triggers:
    - "Create a new skill from masterclass content"
    - "Upgrade an existing skill to v2 XML format"
    - "Convert markdown skill to XML with progressive disclosure"
    - "Build skill failure mode playbook"
  default_layers: "L1+L2"
  load_L3_when: ["complex_domain", "multi_framework_skill", "regulatory_constraints"]
  load_L4_when: ["building_meta_skills", "schema_design", "automation_packaging"]

mma_integration:
  evaluate_with: ["contract_clarity", "layer_compliance", "integration_completeness", "documentation_quality"]
  pass_threshold: ">=8 on all dimensions"
---

# Skill Builder v1.1.0

## L1 — Quick Reference

**Purpose:** Turn masterclass transcripts and expert knowledge into production XML skills with progressive disclosure, SSOT integration, and self-healing capabilities.

**Input Checklist:**
- [ ] MASTERCLASS_TRANSCRIPT (or organized notes)
- [ ] SKILL_INTENT (1-2 sentence purpose statement)
- [ ] Optional: EXISTING_SKILL_FOR_UPGRADE
- [ ] Optional: RELATED_SKILLS_CONTEXT (for awakening protocol)
- [ ] Optional: GOLDEN_RUN_EXAMPLES (for testing)

**Output Checklist:**
- [ ] SKILL_XML (production-ready)
- [ ] SKILL_MARKDOWN_REFERENCE (human-readable backup)
- [ ] MOD_ROUTING_CONFIG (triggers, awakening, layer conditions)
- [ ] MMA_VALIDATION_SPEC (quality gates, scoring criteria)
- [ ] GOLDEN_RUN_TEST_CASES (at least 1)
- [ ] FAILURE_MODE_PLAYBOOK (at least 3 FMs)

**Token Budget Enforcement:**
- L1: ≤250 tokens (Quick Reference)
- L2: ≤2800 tokens (Core Procedure)
- L3: ≤5500 tokens (Advanced Usage / Edge Cases / Failure Modes)
- L4: ≤3200 tokens (Technical Spec / Schemas / Automation)

**Quality Gates:**
1. **Contract Clarity:** Inputs/outputs explicitly defined with SSOT flags
2. **Layer Compliance:** Token budgets respected; progressive disclosure enforced
3. **MOD Integration:** Routing triggers, awakening protocol, layer load conditions complete
4. **MMA Hooks:** Quality gates specific to skill domain
5. **Self-Healing:** Failure modes with detection + recovery patterns
6. **Golden Runs:** At least 1 test case with expected outputs

**Golden Rule:** If a layer exceeds its budget, split into sub-frameworks or move details to higher layer.

---

## L2 — Core Procedure (Production)

### Step 0 — Intake & Contract Definition

**Inputs Required:**
1. **MASTERCLASS_TRANSCRIPT** (or organized expert knowledge)
2. **SKILL_INTENT** (1-2 sentence purpose statement)

**If Upgrading Existing Skill:**
3. **EXISTING_SKILL_FOR_UPGRADE** (markdown or XML v1)
4. Version history and breaking changes log

**Optional Context:**
5. **RELATED_SKILLS_CONTEXT** (for awakening protocol design)
6. **GOLDEN_RUN_EXAMPLES** (for test case generation)

**Hard Checks:**
- If SKILL_INTENT is vague → request clarification
- If MASTERCLASS_TRANSCRIPT is incomplete → flag missing sections
- If upgrading → verify version bump is appropriate (patch/minor/major)

**Output from Step 0:**
- Confirmed skill_id (follow naming convention: `skill.[domain].[name].v[X_Y_Z]`)
- Confirmed tier (meta / production / experimental)
- SSOT requirements identified (which objects does this skill consume?)

---

### Framework 1: Knowledge Extraction & Layer Assignment

**Purpose:** Extract core concepts from masterclass and assign to appropriate progressive disclosure layers.

**Steps:**

**1. Extract Core Concepts**
- Read through MASTERCLASS_TRANSCRIPT
- Identify:
  - Core principles (L1 candidates)
  - Step-by-step procedures (L2 candidates)
  - Edge cases and advanced techniques (L3 candidates)
  - Technical specs, schemas, automation rules (L4 candidates)

**2. Assign to Layers (Progressive Disclosure)**

**L1 (≤250 tokens):** Quick Reference
- Golden rules (max 7)
- Input/output checklist
- Quality gate summary
- Canonical examples (1-2)
- When to use / when NOT to use

**L2 (≤2800 tokens):** Core Procedure
- Step-by-step workflows (3-7 steps typical)
- Primary frameworks (2-4 frameworks typical)
- Validation checks at each step
- Expected outputs

**L3 (≤5500 tokens):** Advanced Usage
- Edge case handling
- Failure Mode Playbook (FM1-FM7 typical)
- Domain-specific advanced techniques
- Integration patterns with other skills
- Smooth Transitions or reusable modules

**L4 (≤3200 tokens):** Technical Spec
- SSOT schema requirements
- Output format specifications (YAML/XML/Markdown structures)
- MMA evaluation hooks (specific validation logic)
- Automation packaging rules
- CBM (Context Budget Manager) integration

**3. Token Budget Enforcement**
- Write first draft of each layer
- Count tokens (use estimation: ~4 characters per token)
- If over budget:
  - Cut non-essential details
  - Move advanced details to higher layer
  - Split into sub-frameworks
  - Use references instead of duplication

**Validation:**
- L1 is self-sufficient for common cases
- L2 provides complete procedure without requiring L3
- L3 adds depth, not core functionality
- L4 is for builders/debuggers, not operators

**Output:**
- Layer content drafts (L1-L4)
- Token counts per layer

---

### Framework 2: SSOT Contract Design

**Purpose:** Define explicit input/output contracts with SSOT integration.

**Steps:**

**1. Identify Required Inputs**
- What SSOT objects does this skill *must* have? (PROJECT_BRIEF, MESSAGE_SPINE, etc.)
- What non-SSOT inputs are required? (domain-specific data)
- Mark each input:
  ```xml
  <Input name="PROJECT_BRIEF" ssot="true">
    <Notes>Specific fields required: audience, offer, constraints</Notes>
  </Input>
  ```

**2. Identify Optional Inputs**
- What inputs enhance the skill but aren't required?
- What happens if optional input is missing? (graceful degradation)
- Example:
  ```xml
  <Input name="EVIDENCE_PACK" ssot="true">
    <Notes>Required if claims are made; if missing, label claims as UNKNOWN</Notes>
  </Input>
  ```

**3. Define Outputs (Primary and Secondary)**
- **Primary outputs:** Core deliverables (always produced)
- **Secondary outputs:** Coordination notes, handoff packets, validation reports

**4. Specify Output Formats**
- Markdown (for human-readable content)
- YAML (for structured data)
- XML (for IADP handoff packets)

**Example:**
```xml
<Outputs>
  <PrimaryOutputs>
    <Output id="sales_page_draft" format="markdown">
      Long-form sales page with headline, subheads, CTA
    </Output>
  </PrimaryOutputs>
  <SecondaryOutputs>
    <Output id="handoff_packet" format="xml">
      IADP for Email Campaign Genius (objections, proof pillars, CTA)
    </Output>
  </SecondaryOutputs>
</Outputs>
```

**Validation:**
- Every required input has clear purpose
- Every output has format specification
- SSOT inputs are flagged `ssot="true"`

**Output:**
- Complete `<Inputs>` section
- Complete `<Outputs>` section

---

### Framework 3: MOD Integration (Routing & Awakening)

**Purpose:** Configure how MOD routes tasks to this skill and which skills it awakens.

**Steps:**

**1. Define Routing Triggers**
- What task descriptions should route to this skill?
- Use natural language patterns:
  ```xml
  <Trigger>Write a sales page for [product]</Trigger>
  <Trigger>Create long-form sales copy</Trigger>
  <Trigger>Need a conversion-optimized landing page</Trigger>
  ```

**2. Define Awakening Protocol**
- **High priority:** Skills that are almost always needed downstream
- **Medium priority:** Skills that are often needed
- **Low priority:** Skills rarely needed but relevant

Example:
```xml
<RecommendedAwakenings>
  <High>
    <SkillRef>skill.email_campaign_genius.v2_x_x</SkillRef>
    <SkillRef>skill.human_persuasion_editor.v2_x_x</SkillRef>
  </High>
  <Medium>
    <SkillRef>skill.testimonial_library_agent.v2_x_x</SkillRef>
  </Medium>
</RecommendedAwakenings>
```

**3. Define Layer Load Conditions**
- When should L3 be loaded? (complexity thresholds, edge cases)
- When should L4 be loaded? (debugging, schema work)

Example:
```xml
<LayerLoadConditions>
  <Condition layer="L3">
    complexity >= 4 OR compliance_heavy OR MMA_score_below_7
  </Condition>
  <Condition layer="L4">
    building_skills OR schema_debugging OR automation_design
  </Condition>
</LayerLoadConditions>
```

**Validation:**
- At least 2 routing triggers defined
- Awakening protocol identifies downstream skills
- Layer load conditions are testable

**Output:**
- Complete `<Routing>` section

---

### Framework 4: MMA Validation Specification

**Purpose:** Define quality gates and scoring criteria for this skill's outputs.

**Steps:**

**1. Define Quality Gates**
- What are the non-negotiable requirements for this skill's output?
- Use domain-specific gates (not generic)

Example for Sales Page skill:
```xml
<QualityGates>
  <Gate name="SSOT_Aligned">
    <PassCriteria>No contradictions with PROJECT_BRIEF / MESSAGE_SPINE / VOICE_GUIDE</PassCriteria>
  </Gate>
  <Gate name="Proof_Discipline">
    <PassCriteria>All claims map to EVIDENCE_PACK or are downgraded to hypothesis language</PassCriteria>
  </Gate>
  <Gate name="CTA_Integrity">
    <PassCriteria>CTA matches MESSAGE_SPINE canonical phrase exactly</PassCriteria>
  </Gate>
</QualityGates>
```

**2. Define MMA Evaluation Dimensions**
- Which of the 7 MMA dimensions apply to this skill?
  - strategy_alignment
  - clarity_structure
  - voice_consistency
  - proof_discipline
  - resonance_impact
  - cta_integrity
  - ethical_guardrails

Example:
```xml
<MMAIntegration>
  <EvaluateWith>
    <Dimension>strategy_alignment</Dimension>
    <Dimension>voice_consistency</Dimension>
    <Dimension>proof_discipline</Dimension>
    <Dimension>cta_integrity</Dimension>
  </EvaluateWith>
  <PassThreshold>&gt;=7 on all dimensions</PassThreshold>
</MMAIntegration>
```

**3. Define Pass Threshold**
- What's the minimum MMA score required? (typically >=7 for production)
- Are there hard-gate violations that auto-fail regardless of score?

**Validation:**
- At least 3 quality gates defined
- Quality gates are specific to the skill's domain
- Pass threshold is realistic

**Output:**
- Complete `<QualityGates>` section
- Complete `<MMAIntegration>` section

---

### Framework 5: Failure Mode Playbook Generation

**Purpose:** Identify common failure patterns and document recovery procedures.

**Steps:**

**1. Identify Common Failures**
- Review MASTERCLASS_TRANSCRIPT for mentioned pitfalls
- Consider domain-specific anti-patterns
- Typical categories:
  - Input validation failures (missing SSOT, incomplete data)
  - Process failures (skipped steps, wrong order)
  - Output quality failures (voice drift, proof violations)
  - Integration failures (handoff packet incomplete)

**2. Document Each Failure Mode (FM)**
- **Name:** Short descriptive name
- **Detection:** How to recognize this failure (symptoms, signals)
- **Recovery:** Step-by-step fix procedure
- **Prevention:** How to avoid this failure in the first place

Example:
```xml
<FM1>
  <Name>Voice Drift (Generic Corporate Tone)</Name>
  <Detection>
    - Jargon density &gt; 3 per paragraph
    - No personality markers
    - Passive voice &gt; 20%
  </Detection>
  <Recovery>
    - Re-read VOICE_GUIDE tone targets
    - Apply signature phrases from VG
    - Convert passive to active voice
    - Replace jargon with conversational language
  </Recovery>
  <Prevention>
    - Load VOICE_GUIDE in L1
    - Check voice every 3 paragraphs during writing
    - Use MMA voice_consistency check before finalizing
  </Prevention>
</FM1>
```

**3. Prioritize Top 5-7 Failure Modes**
- Most common failures first
- Highest-impact failures prioritized
- Domain-specific failures over generic

**Validation:**
- At least 3 failure modes documented
- Each FM has detection + recovery + prevention
- FMs are specific to this skill's domain

**Output:**
- Complete `<FailureModePlaybook>` section (in L3)

---

### Framework 6: Golden Run Scaffolding

**Purpose:** Create regression test cases with known-good inputs and expected outputs.

**Steps:**

**1. Define Test Case Structure**
```yaml
golden_run_id: GR-[SKILL_ID]-001
description: "Brief description of what this test validates"
inputs:
  PROJECT_BRIEF: "path/to/test_PB.xml"
  MESSAGE_SPINE: "path/to/test_MS.xml"
  # ... other inputs
expected_outputs:
  primary_output:
    format: "markdown"
    validation_criteria:
      - "Headline contains mechanism language"
      - "CTA matches MESSAGE_SPINE"
      - "No claims beyond EVIDENCE_PACK"
  mma_score_expectations:
    strategy_alignment: ">= 8"
    voice_consistency: ">= 7"
    proof_discipline: ">= 9"
```

**2. Create At Least 1 Golden Run**
- Use real project data if available (anonymized)
- Or create synthetic test data
- Document expected behavior clearly

**3. Link to Test Harness**
- Ensure golden run can be executed by test_harness.md
- Provide regression testing instructions

**Validation:**
- At least 1 golden run documented
- Expected outputs are measurable
- Test case can be executed without ambiguity

**Output:**
- GOLDEN_RUN_TEST_CASES file or section

---

### Step Final — Assembly & Validation

**1. Assemble Complete XML Skill**
- Combine all sections:
  - Metadata (skill_id, version, tier, status)
  - Meta (owner, domain, tags)
  - Purpose
  - Scope (WhenToUse, NotFor)
  - SSOT (Required, Optional)
  - Identity (Role, NonNegotiables)
  - Routing (Awakenings, LayerLoad)
  - Inputs, Outputs
  - QualityGates
  - TokenBudget
  - MMAIntegration
  - Layer1_Core
  - Layer2_DetailedProcedure
  - Layer3_EdgeCases
  - Layer4_TechnicalSpec

**2. Run Self-Validation**
- [ ] All token budgets respected?
- [ ] All SSOT contracts defined?
- [ ] MOD routing complete (triggers, awakening, layer conditions)?
- [ ] MMA hooks defined (quality gates, dimensions, threshold)?
- [ ] Failure Mode Playbook has ≥3 FMs?
- [ ] Golden Run has ≥1 test case?

**3. Generate Supporting Files**
- SKILL_MARKDOWN_REFERENCE (human-readable backup)
- MOD_ROUTING_CONFIG (routing table entry)
- MMA_VALIDATION_SPEC (quality gates summary)

**4. Output Complete Package**
- SKILL_XML (production-ready)
- SKILL_MARKDOWN_REFERENCE
- MOD_ROUTING_CONFIG
- MMA_VALIDATION_SPEC
- GOLDEN_RUN_TEST_CASES
- FAILURE_MODE_PLAYBOOK

---

## L3 — Advanced Usage (Edge Cases & Failure Modes)

### Advanced Technique: Reusable Module Extraction

**When to Use:** When a pattern appears in multiple skills (e.g., Smooth Transitions, LEARN→DO→SHARE→TEACH)

**Steps:**
1. Identify the reusable pattern in MASTERCLASS_TRANSCRIPT
2. Extract as standalone module with:
   - Module name
   - Purpose (1 sentence)
   - When to use
   - Steps (concise)
   - Validation checks
3. Reference the module in multiple skills instead of duplicating
4. Store reusable modules in `/ultramind/modules/`

**Example:**
```xml
<ReusableModule id="learn_do_share_teach">
  <Purpose>Prevent content consumption; force action + feedback loop</Purpose>
  <Steps>
    <Step>LEARN (concept)</Step>
    <Step>DO (assignment with success criteria)</Step>
    <Step>SHARE (community check-in / proof)</Step>
    <Step>TEACH (explain it back)</Step>
  </Steps>
  <Validation>Every LEARN must produce a DO with pass/fail definition</Validation>
</ReusableModule>
```

---

### FAILURE MODE PLAYBOOK

#### FM1: Token Budget Exceeded
**Detection:**
- Layer exceeds token limit during assembly
- Content feels bloated or repetitive

**Recovery:**
- Identify lowest-value content in the layer
- Move advanced details to higher layer (L2 → L3, L3 → L4)
- Use references instead of duplication (e.g., "See Framework 2 in L2")
- Split into sub-frameworks if necessary
- Cut ruthlessly: if it's not essential for 80% of use cases, move it up

**Prevention:**
- Estimate tokens during writing (~4 chars per token)
- Write L1 first and ensure it's self-sufficient
- Review token counts before finalizing each layer

---

#### FM2: SSOT Contracts Unclear
**Detection:**
- Input/output requirements are vague
- Unclear which SSOT objects are required vs optional
- Missing format specifications for outputs

**Recovery:**
- Review MASTERCLASS_TRANSCRIPT for explicit input/output mentions
- If still unclear: flag for clarification (don't guess)
- Default to marking inputs as "optional" if unsure (better than blocking)
- Document assumptions clearly in `<Notes>` sections

**Prevention:**
- Start with Framework 2 (SSOT Contract Design) early
- Review existing skills in same domain for contract patterns
- Ask clarifying questions during intake (Step 0)

---

#### FM3: Generic / Weak Quality Gates
**Detection:**
- Quality gates apply to any skill (not domain-specific)
- Examples: "Output is clear", "No errors", "Follows best practices"
- MMA dimensions selected without rationale

**Recovery:**
- Review skill's domain and identify specific risks
  - Sales page → proof discipline, CTA integrity
  - Email sequence → deliverability, consent
  - Program design → validation before build, timeline realism
- Replace generic gates with domain-specific gates
- Ensure each gate has measurable pass criteria

**Prevention:**
- Study quality gates in existing production skills
- Ask: "What could go *very wrong* with this skill's output?"
- Tie quality gates to SSOT objects (e.g., "Must match VOICE_GUIDE tone targets")

---

#### FM4: Missing Failure Modes
**Detection:**
- Failure Mode Playbook has <3 FMs
- FMs are generic ("Something went wrong")
- No recovery procedures documented

**Recovery:**
- Review MASTERCLASS_TRANSCRIPT for mentioned pitfalls
- Interview domain experts for common mistakes
- Study past project failures in this domain
- Document top 3-5 failure patterns with detection + recovery

**Prevention:**
- Include "Common Pitfalls" section in masterclass intake
- Review failure modes from related skills
- Build Failure Mode Playbook in parallel with core procedure (not as afterthought)

---

#### FM5: Awakening Protocol Incomplete
**Detection:**
- No downstream skills identified
- Awakening priorities unclear (everything marked "high")
- Skills awaken in wrong order (downstream before upstream)

**Recovery:**
- Map skill's outputs to other skills' inputs
  - Sales Page → Email Campaign (needs objections, proof, CTA)
  - Offer Architect → Product Creation Genius (needs positioning, mechanism)
- Prioritize:
  - High: Skills that consume this skill's primary outputs
  - Medium: Skills that benefit from coordination notes
  - Low: Skills that share context but don't depend on outputs
- Document awakening rationale in comments

**Prevention:**
- Review skill dependency graph (`/ultramind/registry/registry.yaml`)
- Map outputs to downstream skills during contract design (Framework 2)
- Test awakening protocol with example task flows

---

#### FM6: Layer Progressive Disclosure Violated
**Detection:**
- L1 references L2/L3/L4 content ("See Framework X in L3")
- L2 requires L3 knowledge to execute
- Operator must load L4 to complete common tasks

**Recovery:**
- Ensure L1 is self-sufficient for 80% of use cases
- Move essential content down to lower layers
- Reserve higher layers for:
  - L3: Edge cases, failure recovery, advanced optimization
  - L4: Builders, debuggers, schema designers

**Prevention:**
- Write and test L1 first in isolation
- Validate L2 can be executed without referencing L3/L4
- Progressive disclosure is about *loading* order, not *reading* order

---

#### FM7: Version Upgrade Breaking Changes Undocumented
**Detection:**
- Upgrading from v1 to v2, but changes not clearly documented
- Downstream skills break after upgrade
- Golden runs fail without clear reason

**Recovery:**
- Document all breaking changes in changelog
- Update affected golden runs
- Notify downstream skill maintainers
- Consider deprecation period for major changes

**Prevention:**
- Use semantic versioning strictly:
  - MAJOR: Breaking changes (input/output contracts change)
  - MINOR: New features (backward compatible)
  - PATCH: Bug fixes, clarifications
- Maintain CHANGELOG.md for each skill
- Run regression tests before version bump

---

## L4 — Technical Specification

### SSOT Schema Requirements (for Skill Builder Output)

```xml
<Skill
  skill_id="skill.[domain].[name].v[MAJOR_MINOR_PATCH]"
  name="Human-Readable Skill Name"
  version="MAJOR.MINOR.PATCH"
  tier="production|meta|experimental"
  status="active|draft|deprecated"
  model="sonnet|opus|haiku"
>
  <Meta>
    <Owner>[owner_agent_or_team]</Owner>
    <PrimaryDomain>[domain]</PrimaryDomain>
    <SecondaryDomain>[optional_secondary_domain]</SecondaryDomain>
    <LastUpdated>[YYYY-MM-DD]</LastUpdated>
    <Tags>
      <Tag>[tag1]</Tag>
      <Tag>[tag2]</Tag>
    </Tags>
  </Meta>

  <Purpose>[1-2 sentence purpose statement]</Purpose>

  <Scope>
    <WhenToUse>
      <Trigger>[natural language trigger 1]</Trigger>
      <Trigger>[natural language trigger 2]</Trigger>
    </WhenToUse>
    <NotFor>
      <Item>[explicit exclusion 1]</Item>
      <Item>[explicit exclusion 2]</Item>
    </NotFor>
  </Scope>

  <SSOT>
    <Required>
      <Object schema_id="[SSOT_OBJECT_ID]"/>
    </Required>
    <Optional>
      <Object schema_id="[OPTIONAL_SSOT_OBJECT_ID]"/>
    </Optional>
  </SSOT>

  <Identity>
    <Role>[persona/role statement]</Role>
    <NonNegotiables>
      <Item>[hard constraint 1]</Item>
      <Item>[hard constraint 2]</Item>
    </NonNegotiables>
  </Identity>

  <Routing>
    <RecommendedAwakenings>
      <High>
        <SkillRef>skill.[downstream_skill].v[X_x_x]</SkillRef>
      </High>
      <Medium>
        <SkillRef>skill.[related_skill].v[X_x_x]</SkillRef>
      </Medium>
    </RecommendedAwakenings>
    <LayerLoadDefault>L1+L2</LayerLoadDefault>
    <LayerLoadConditions>
      <Condition layer="L3">[condition_expression]</Condition>
      <Condition layer="L4">[condition_expression]</Condition>
    </LayerLoadConditions>
  </Routing>

  <Inputs>
    <Required>
      <Input name="[INPUT_NAME]" ssot="true|false">
        <Notes>[description]</Notes>
      </Input>
    </Required>
    <Optional>
      <Input name="[INPUT_NAME]" ssot="true|false">
        <Notes>[description]</Notes>
      </Input>
    </Optional>
  </Inputs>

  <Outputs>
    <PrimaryOutputs>
      <Output id="[output_id]" format="markdown|yaml|xml">
        [description]
      </Output>
    </PrimaryOutputs>
    <SecondaryOutputs>
      <Output id="[output_id]" format="markdown|yaml|xml">
        [description]
      </Output>
    </SecondaryOutputs>
  </Outputs>

  <QualityGates>
    <Gate name="[GATE_NAME]">
      <PassCriteria>[measurable criteria]</PassCriteria>
    </Gate>
  </QualityGates>

  <TokenBudget>
    <L1>[max_tokens]</L1>
    <L2>[max_tokens]</L2>
    <L3>[max_tokens]</L3>
    <L4>[max_tokens]</L4>
  </TokenBudget>

  <MMAIntegration>
    <EvaluateWith>
      <Dimension>[dimension_name]</Dimension>
    </EvaluateWith>
    <PassThreshold>[threshold_expression]</PassThreshold>
  </MMAIntegration>

  <Layer1_Core>
    [L1 content - Quick Reference]
  </Layer1_Core>

  <Layer2_DetailedProcedure>
    [L2 content - Core Procedure]
  </Layer2_DetailedProcedure>

  <Layer3_EdgeCases>
    [L3 content - Advanced Usage / Failure Modes]
  </Layer3_EdgeCases>

  <Layer4_TechnicalSpec>
    [L4 content - Technical Spec / Schemas / Automation]
  </Layer4_TechnicalSpec>

</Skill>
```

---

### Output Format Specifications

**SKILL_XML:**
- Format: XML (UTF-8 encoding)
- Schema: As defined above
- File naming: `[skill_id]_v[version].xml`
- Location: `/ultramind/skills/xml/`

**SKILL_MARKDOWN_REFERENCE:**
- Format: Markdown with YAML frontmatter
- Frontmatter includes: skill_id, version, owner, tier, last_updated, inputs, outputs, dependencies, quality_gates, guardrails, token_budget, mod_integration, mma_integration
- Body structure: L1 → L2 → L3 → L4 with clear headings
- File naming: `[skill_id]_v[version].md`
- Location: `/ultramind/skills/markdown/`

**MOD_ROUTING_CONFIG:**
- Format: YAML
- Add entry to `/ultramind/registry/registry.yaml`
- Include: skill_id, triggers, awakens (high/medium/low), layer_load_conditions

**MMA_VALIDATION_SPEC:**
- Format: YAML
- Include: quality_gates, mma_dimensions, pass_threshold
- Can be embedded in skill XML or separate file for test harness

**GOLDEN_RUN_TEST_CASES:**
- Format: YAML
- Location: `/ultramind/tests/golden_runs/[skill_id]/`
- Include: inputs (file paths or inline data), expected_outputs (validation criteria), mma_score_expectations

**FAILURE_MODE_PLAYBOOK:**
- Embedded in L3 of skill XML
- Also extractable as standalone markdown for training/debugging

---

### MMA Evaluation Hooks (Technical Implementation)

```python
# Pseudocode for MMA validation hook integration

def validate_skill_output(skill_id, output, ssot_context):
    """
    MMA validation entry point for any skill output.
    """
    # Load skill's MMA spec
    mma_spec = load_mma_spec(skill_id)

    # Initialize scoring
    scores = {}

    # Evaluate each dimension
    for dimension in mma_spec.dimensions:
        scores[dimension] = evaluate_dimension(
            dimension=dimension,
            output=output,
            ssot_context=ssot_context,
            skill_spec=mma_spec
        )

    # Check quality gates
    gate_results = {}
    for gate in mma_spec.quality_gates:
        gate_results[gate.name] = check_quality_gate(
            gate=gate,
            output=output,
            ssot_context=ssot_context
        )

    # Determine pass/fail
    passed = all(
        scores[dim] >= mma_spec.pass_threshold for dim in scores
    ) and all(gate_results.values())

    # Generate Delta Log
    delta_log = generate_delta_log(
        scores=scores,
        gate_results=gate_results,
        threshold=mma_spec.pass_threshold
    )

    return {
        "passed": passed,
        "scores": scores,
        "gate_results": gate_results,
        "delta_log": delta_log
    }
```

---

### Context Budget Manager (CBM) Integration

**CBM Policy for Skill Builder:**
- Skill Builder is a meta-skill; can load up to L4 when building skills
- When generating skills for others:
  - Assume MOD will enforce "Rule of 3" (max 3 active skills)
  - Design skills to be self-sufficient at L1+L2 (don't require L3/L4 for common cases)
  - Token budgets ensure skills fit within CBM constraints

**Token Allocation Example:**
```
Total Context Budget: 100k tokens (typical Claude sonnet limit)
Allocated:
  - SSOT objects (PB + MS + VG + EP): ~15k tokens
  - MOD orchestration: ~5k tokens
  - MMA validation: ~5k tokens
  - Active Skill 1 (L1+L2): ~3k tokens
  - Active Skill 2 (L1+L2): ~3k tokens
  - Working memory (output generation): ~40k tokens
  - Buffer: ~29k tokens
```

---

### Conflict Resolution Protocol Integration

**When Skill Builder encounters conflicts:**

**Priority Hierarchy:**
1. **SSOT objects** (PB, MS, VG, EP) override all creative decisions
2. **Skill Intent** (from user) overrides Skill Builder's interpretation
3. **Domain best practices** (from masterclass) override generic patterns
4. **Token budget constraints** override completeness desires (cut ruthlessly)

**Example Conflict:**
- **Conflict:** Masterclass describes 12 frameworks, but L2 budget only fits 4
- **Resolution:**
  1. Prioritize frameworks by frequency of use (per masterclass)
  2. Move less-common frameworks to L3
  3. Reference advanced frameworks in L2 without full detail
  4. Document decision in L4 (why these 4 were chosen)

---

### Versioning & Upgrade Path

**Semantic Versioning:**
- **MAJOR.MINOR.PATCH** (e.g., 2.1.0)
- **MAJOR:** Breaking changes (input/output contracts change, SSOT requirements change)
- **MINOR:** New features (new frameworks, new failure modes, backward compatible)
- **PATCH:** Bug fixes, clarifications, typo corrections

**Upgrade Checklist:**
1. Document all changes in CHANGELOG.md
2. Update version in skill_id and version attributes
3. Run golden runs (regression tests)
4. Update affected downstream skills
5. Notify MOD (update routing table if triggers changed)
6. Notify MMA (update quality gates if validation changed)

**Deprecation Policy:**
- Mark old version as `status="deprecated"`
- Provide migration guide in CHANGELOG
- Maintain old version for 1 minor version cycle (e.g., v2.0.x supported through v2.1.x lifetime)

---

### Automation Packaging (Future: Skill Builder as Autonomous Agent)

**Vision:** Skill Builder can be invoked autonomously by MOD when masterclass content is detected.

**Automation Hooks:**
```yaml
automation_trigger:
  - file_created: "/ultramind/masterclasses/*.md"
  - file_created: "/ultramind/masterclasses/*.txt"
  - manual_invoke: "/create-skill [masterclass_path]"

automation_workflow:
  1. Extract SKILL_INTENT from masterclass (first paragraph or user prompt)
  2. Run Skill Builder L1+L2 (generate draft)
  3. Request human review (before finalizing)
  4. If approved: generate XML, update registry, create golden run
  5. If rejected: capture feedback, iterate

human_in_loop:
  - required_for: version bump MAJOR
  - optional_for: version bump MINOR, PATCH
  - review_points: [SSOT contracts, MMA quality gates, token budgets]
```

---

### Golden Run Template (L4 Specification)

```yaml
golden_run_id: GR-SKILL-BUILDER-001
description: "Generate Sales Page Copywriter skill from masterclass"

inputs:
  MASTERCLASS_TRANSCRIPT: "/ultramind/masterclasses/sales_page_masterclass.md"
  SKILL_INTENT: "Create long-form sales pages with proof-driven copy and SSOT alignment"
  RELATED_SKILLS_CONTEXT:
    - skill.email_campaign_genius.v2_0_0
    - skill.offer_architect.v2_0_0
    - skill.human_persuasion_editor.v2_0_0

expected_outputs:
  SKILL_XML:
    format: "xml"
    validation_criteria:
      - "skill_id matches pattern: skill.sales_page_copywriter.v[X_Y_Z]"
      - "L1 token count <= 250"
      - "L2 token count <= 2800"
      - "L3 token count <= 5500"
      - "L4 token count <= 3200"
      - "At least 3 quality gates defined"
      - "At least 2 routing triggers defined"
      - "Awakening protocol includes email_campaign_genius (high priority)"
      - "At least 3 failure modes documented"

  GOLDEN_RUN_TEST_CASES:
    format: "yaml"
    validation_criteria:
      - "At least 1 golden run created"
      - "Golden run includes expected MMA scores"

  mma_score_expectations:
    contract_clarity: ">= 8"
    layer_compliance: ">= 9"
    integration_completeness: ">= 8"
    documentation_quality: ">= 7"

test_execution:
  command: "pytest ultramind/tests/test_skill_builder.py::test_golden_run_001"
  expected_result: "PASS"
```

---

### End of Skill Builder v1.1.0 Specification

**Next Steps After Using This Skill:**
1. Save generated SKILL_XML to `/ultramind/skills/xml/`
2. Save SKILL_MARKDOWN_REFERENCE to `/ultramind/skills/markdown/`
3. Update `/ultramind/registry/registry.yaml` with MOD routing config
4. Create golden run in `/ultramind/tests/golden_runs/[skill_id]/`
5. Run test harness to validate skill
6. If tests pass: mark skill as `status="active"`
7. If tests fail: review Failure Mode Playbook, iterate

**Maintenance:**
- Review skill quarterly for updates
- Collect user feedback (what's unclear? what's missing?)
- Increment version when improvements are made
- Maintain backward compatibility when possible
