# MOD SPECIFICATION v1.0
## Master Orchestration Director

### Purpose
MOD is the routing and coordination layer of Ultramind. It receives task requests, validates SSOT readiness, selects appropriate skills, manages context budget, and orchestrates skill execution.

---

## Core Responsibilities

### 1. Task Request Intake
- Receive structured task requests (YAML or natural language)
- Parse request into: objective, constraints, required outputs, deadline
- Validate request completeness

### 2. SSOT Readiness Check (RITES Gate)
Before executing any skill, verify:
- **PROJECT_BRIEF exists** and required fields are filled (not [PLACEHOLDER])
- **MESSAGE_SPINE exists** and core pillars are defined
- **VOICE_GUIDE exists** and tone dials are set
- **EVIDENCE_PACK exists** if claims are expected in output

If SSOT objects incomplete: HALT and request missing information.

### 3. Skill Selection
Based on task request, select the appropriate skill(s) from registry:
- Match task objective to skill capabilities
- Check skill dependencies (some skills require outputs from others)
- Respect execution order (strategy → execution → validation)

### 4. Context Budget Management (Lean MCP)
**Rule of 3**: Never load more than 3 active skills in a single run:
- 1 strategy skill (if needed)
- 1 execution skill
- MMA (validator, always loaded)

**Kernel (always loaded):**
- Constitution summary (10 rules)
- MOD + MMA specs (short reference)
- SSOT objects (PB/MS/VG/EP instances)
- Skill registry (IDs, triggers, I/O contracts)

**On-demand fetch (only when skill activates):**
- Skill L2 procedure (detailed steps)
- Skill L3 edge cases (only if error occurs)
- Examples relevant to current task

### 5. Orchestration Execution
1. Load Kernel
2. Activate selected skill(s)
3. Pass SSOT objects + task request to skill
4. Collect skill output
5. Route output to MMA for validation
6. Return validated output + Delta Log

---

## Input Contract

### Task Request Format (YAML)
```yaml
task_request:
  id: "TR-2025-001"
  objective: "Draft sales page for new supplement offer"
  audience: "Health-conscious men 45-65"
  output_format: "long-form sales page"
  constraints:
    - "Must use evidence from EvidencePack only"
    - "No income claims"
    - "FDA-compliant language"
  ssot_references:
    project_brief: "PB_Supplement_Launch_v2.xml"
    message_spine: "MS_Supplement_Core_v1.xml"
    voice_guide: "VG_Health_Authority_v1.xml"
    evidence_pack: "EP_Supplement_Claims_v3.xml"
  deadline: "2025-12-20"
```

---

## Output Contract

### MOD Execution Report
```yaml
mod_report:
  task_id: "TR-2025-001"
  status: "complete" | "incomplete" | "error"
  skills_activated:
    - skill_id: "offer_architect"
      version: "v1.2"
      duration: "3min"
    - skill_id: "sales_page_copywriter"
      version: "v2.0"
      duration: "8min"
  ssot_loaded:
    - "PB_Supplement_Launch_v2.xml"
    - "MS_Supplement_Core_v1.xml"
    - "VG_Health_Authority_v1.xml"
    - "EP_Supplement_Claims_v3.xml"
  mma_validation: "passed" | "failed"
  delta_log_generated: true
  next_recommended_skill: "email_copy_genius"
  notes: "Draft passed compliance, minor voice adjustments recommended"
```

---

## Routing Logic

### Skill Selection Algorithm
1. **Parse task objective** → identify required output type
2. **Check skill registry** → match output type to skill capabilities
3. **Check dependencies** → ensure prerequisite skills have run (or outputs exist)
4. **Priority order**:
   - Strategy skills (if PROJECT_BRIEF incomplete)
   - Execution skills (primary task)
   - Refinement skills (polish/edit)
   - MMA (always final step)

### Example Routing Paths

**Task: "Create supplement sales page"**
- Route: `offer_architect` (if PB/MS incomplete) → `sales_page_copywriter` → `testimonial_library_agent` → `human_persuasion_editor` → `MMA`

**Task: "Write 5-email nurture sequence"**
- Route: `email_copy_genius` → `MMA`

**Task: "Audit existing sales page for compliance"**
- Route: `compliance_auditor` → `MMA`

---

## Error Handling

### SSOT Incomplete
- HALT execution
- Return specific missing fields
- Request user input before proceeding

### Skill Failure
- Log error
- Attempt fallback skill (if available)
- If no fallback: return partial output + error report

### Context Budget Exceeded
- Unload non-essential skills
- Paginate large SSOT objects (load only relevant sections)
- Request task simplification if unavoidable

---

## Performance Metrics
- **Task completion time**: target <10min for standard tasks
- **SSOT reference accuracy**: 100% (every output must cite SSOT)
- **Context efficiency**: <50% of max context window used
- **MMA pass rate**: target >85% first-pass validation

---

## Version History
- v1.0 (2025-12-17): Initial MOD specification
- v1.1 (2025-12-17): Added Neuro-Routing Integration (RESONANCE_CONSTITUTION.xml layer)

---

## NEURO-ROUTING INTEGRATION (v1.1+)
**PATCH BLOCK: Integrated 2025-12-17 | Neuro-Persuasion Architecture**

### Enhanced Kernel (Always Loaded)
The MOD Kernel now includes:
- Constitution summary (10 rules) [v1.0]
- **RESONANCE_CONSTITUTION.xml summary** (6-axis Neuro-Box, balance rules, manipulation prohibitions) [v1.1+]
- MOD + MMA specs (short reference)
- SSOT objects (PB/MS/VG/EP instances)
- Skill registry (IDs, triggers, I/O contracts)

**Rationale**: The Neuro-Box architecture is now foundational to all routing decisions. MOD must understand which neurochemical axes a task requires activation for intelligent skill selection.

---

### Enhanced SSOT Readiness Check (RITES Gate v1.1)

**Original RITES Gate checks:**
- PROJECT_BRIEF exists and required fields filled
- MESSAGE_SPINE exists and core pillars defined
- VOICE_GUIDE exists and tone dials set
- EVIDENCE_PACK exists if claims expected

**NEW: Neuro-Readiness Gate (added to RITES):**
- **MESSAGE_SPINE must include 6-axis scoring targets** (which axes to prioritize)
- **VOICE_GUIDE must specify neuro-balance rules** (e.g., "BOTTOM score minimum 7/10", "LEFT/RIGHT balance within 2 points")
- **EVIDENCE_PACK must map proof to axes** (which claims support GABA safety vs Acetylcholine logic vs Serotonin status)

**If neuro-requirements incomplete**: HALT and request neuro-targeting strategy (typically route to `offer_architect` or `strategic_copy_director` first).

---

### Neuro-Aware Skill Selection

**Enhanced Routing Algorithm (v1.1):**

1. **Parse task objective** → identify required output type [v1.0]
2. **Identify neuro-axis requirements** → which axes must be activated? [v1.1+]
   - **Cold audience** (never heard of you): BOTTOM (GABA) must be primary, then LEFT (Dopamine), then RIGHT (Acetylcholine)
   - **Warm audience** (know/like you): Can lead with TOP (Serotonin status) or FRONT (Adrenaline urgency)
   - **Hot audience** (ready to buy): FRONT (Adrenaline action) + BACK (Oxytocin identity) priority
3. **Check skill registry** → match output type + neuro-requirements to skill capabilities [v1.1+]
4. **Check dependencies** → ensure prerequisite skills have run
5. **Priority order** [v1.0 + v1.1 enhancements]:
   - **Neuro-strategy skills** (if MESSAGE_SPINE lacks 6-axis targets) [v1.1+]
   - Strategy skills (if PROJECT_BRIEF incomplete)
   - Execution skills (primary task)
   - Refinement skills (polish/edit)
   - **Neuro-audit skills** (validate 6-axis balance before MMA) [v1.1+]
   - MMA (always final step)

**Skill-to-Axis Mapping (Reference Guide):**
- `offer_architect` → Defines which axes to activate (UMP/UMS/angle selection is neuro-architecture)
- `sales_page_copywriter` → Implements axis activation through copy structure
- `vsl_writer` → Activates axes sequentially (BOTTOM→LEFT→RIGHT→TOP→FRONT)
- `email_copy_genius` → Maintains axis consistency across sequence
- `ad_copy_genius` → Optimizes for specific axis (often LEFT Dopamine or FRONT Adrenaline)
- `human_persuasion_editor` → Balances axes in final polish
- `neuro_resonance_auditor` → Validates 6-axis scores + balance rules [v1.1+]

---

### Enhanced Task Request Format (YAML v1.1)

**New optional fields for neuro-targeting:**

```yaml
task_request:
  id: "TR-2025-001"
  objective: "Draft sales page for new supplement offer"
  audience: "Health-conscious men 45-65"
  audience_temperature: "cold" | "warm" | "hot"  # [v1.1+]
  output_format: "long-form sales page"
  constraints:
    - "Must use evidence from EvidencePack only"
    - "No income claims"
    - "FDA-compliant language"
  neuro_targeting: # [v1.1+]
    primary_axes: ["BOTTOM", "LEFT", "RIGHT"]  # Priority axes to activate
    axis_balance_rules:
      - "BOTTOM minimum 7/10"
      - "TOP cannot exceed BOTTOM by 3+"
      - "LEFT/RIGHT balance within 2 points"
    prohibited_patterns:
      - "fake_urgency"
      - "manufactured_scarcity"
      - "fear_mongering"
  ssot_references:
    project_brief: "PB_Supplement_Launch_v2.xml"
    message_spine: "MS_Supplement_Core_v1.xml"
    voice_guide: "VG_Health_Authority_v1.xml"
    evidence_pack: "EP_Supplement_Claims_v3.xml"
    resonance_constitution: "RESONANCE_CONSTITUTION.xml"  # [v1.1+] Always referenced
  deadline: "2025-12-20"
```

**Default Behavior (if `neuro_targeting` omitted):**
- MOD infers neuro-requirements from `audience_temperature` + `output_format`
- Cold audience → BOTTOM (GABA) priority, conservative axis activation
- Hot audience → FRONT (Adrenaline) + BACK (Oxytocin) priority, aggressive but aligned

---

### Enhanced Routing Paths (v1.1 Examples)

**Task: "Create supplement sales page for COLD audience"**
- **Neuro-Requirement**: BOTTOM (GABA safety) must be primary, TOP (Serotonin status) cannot exceed BOTTOM by 3+
- **Route**: `offer_architect` (defines axis strategy) → `sales_page_copywriter` (implements axis activation) → `testimonial_library_agent` (GABA proof reinforcement) → `human_persuasion_editor` (balance check) → `neuro_resonance_auditor` (6-axis validation) → `MMA` (final compliance)

**Task: "Write urgency-driven launch email for HOT list"**
- **Neuro-Requirement**: FRONT (Adrenaline action) primary, but BACK (Oxytocin identity) must be present to avoid manipulation flag
- **Route**: `email_copy_genius` (implements urgency + identity alignment) → `neuro_resonance_auditor` (verify genuine urgency, not fake scarcity) → `MMA`

**Task: "Audit existing sales page for neuro-resonance"**
- **Route**: `neuro_resonance_auditor` (6-axis scoring + balance check + manipulation detection) → `MMA` (compliance + Delta Log generation)

---

### Neuro-Aware Error Handling (v1.1+)

**NEW: Neuro-Balance Violation**
- **Trigger**: Skill output exceeds balance rule thresholds (e.g., TOP > BOTTOM by 4 points)
- **Action**: Route to `human_persuasion_editor` with specific rebalancing instruction
- **Example**: "Reduce status claims (TOP axis) and strengthen safety/trust signals (BOTTOM axis)"

**NEW: Manipulation Pattern Detected**
- **Trigger**: `neuro_resonance_auditor` flags fake urgency, manufactured scarcity, or fear-mongering
- **Action**: HALT execution, return error report with specific violations
- **Remediation**: Route to `offer_architect` (redesign angle) or `strategic_copy_director` (reframe messaging)

**NEW: Axis Activation Mismatch**
- **Trigger**: Task requires axis activation that MESSAGE_SPINE doesn't support (e.g., cold audience page trying to lead with TOP Serotonin status without BOTTOM GABA foundation)
- **Action**: HALT and request MESSAGE_SPINE revision or route to `offer_architect` to define missing axis strategy

---

### Integration with MMA (Quality Gate)

**MMA Validation now includes (v1.1+):**
- 6-axis scoring (0-10 per axis)
- Balance rule compliance (opposing pairs harmonize)
- Manipulation detection (penalties applied)
- Overall resonance score (Exceptional/Strong/Good/Weak/Poor)

**Handoff from MOD → MMA:**
MOD passes `neuro_targeting` requirements from task request to MMA, so MMA knows which thresholds to enforce.

**Reference**: See `MMA_SPEC.md` v1.1+ for detailed neuro-validation scoring rubric.

---

### Performance Metrics (v1.1 Updated)

**Original Metrics:**
- Task completion time: target <10min
- SSOT reference accuracy: 100%
- Context efficiency: <50% of max context window
- MMA pass rate: target >85% first-pass validation

**NEW Neuro-Performance Metrics:**
- **Neuro-balance accuracy**: target >90% of outputs pass balance rules on first execution
- **Manipulation flag rate**: target <5% (should be rare with proper MESSAGE_SPINE)
- **Axis activation clarity**: target 100% of outputs have explicit axis scores from auditor
- **Fast Track conversion**: target >80% of funnels converted to Fast Track architecture

---

### Authority Note

**RESONANCE_CONSTITUTION.xml is now a first-class SSOT object** (alongside PB/MS/VG/EP).

**Authority Hierarchy for MOD:**
1. CONSTITUTION.md (10 Core Rules + Neuro-Resonance Layer)
2. RESONANCE_CONSTITUTION.xml (6-axis architecture + balance rules)
3. PROJECT_BRIEF (strategic constraints)
4. MESSAGE_SPINE (messaging constraints + neuro-targets)
5. VOICE_GUIDE + EVIDENCE_PACK (execution constraints)

**System Note**: The Neuro-Box is not optional. It is the operating system of persuasion. MOD enforces it at the orchestration layer.
