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
