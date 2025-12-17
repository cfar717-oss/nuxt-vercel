# ULTRAMIND Architecture
## Agentic Operating System for High-Stakes Copywriting + Strategy

### Overview
Ultramind is a production-grade agentic system for creating consistent, compliant, high-quality marketing copy and strategy work. Built on Single Sources of Truth (SSOT) architecture with dynamic skill orchestration.

---

## Directory Structure

```
/ultramind/
├── governance/              # Core system specifications
│   ├── CONSTITUTION.md     # 10 core rules + 4 pillars model
│   ├── MOD_SPEC.md         # Master Orchestration Director
│   └── MMA_SPEC.md         # Master Monitoring Agent
│
├── ssot/                    # Single Sources of Truth
│   ├── schemas/            # XML schema templates
│   │   ├── PROJECT_BRIEF_SCHEMA.xml
│   │   ├── MESSAGE_SPINE_SCHEMA.xml
│   │   ├── VOICE_GUIDE_SCHEMA.xml
│   │   └── EVIDENCE_PACK_SCHEMA.xml
│   └── instances/          # Actual project SSOT files (create per project)
│
├── skills/                  # Execution layer
│   ├── xml/                # Production XML skills
│   ├── markdown/           # Original Markdown skills (for conversion)
│   ├── SKILL_TEMPLATE.xml  # Template for new skills
│   └── MARKDOWN_TO_XML_GUIDE.md
│
├── registry/               # Skill catalog + routing
│   └── registry.yaml       # Central skill index
│
├── examples/               # Sample usage
│   └── task_request.yaml   # Task request examples
│
└── tests/                  # Quality assurance
    ├── test_harness.md     # Testing framework spec
    ├── fixtures/           # Test SSOT files + sample outputs
    ├── golden_tasks/       # Known-good task requests
    └── results/            # Test outputs + scorecards
```

---

## Core Concepts

### The 4 Pillars (SSOT Model)

1. **PROJECT_BRIEF (PB)** - Strategy Lock
   - WHO (audience), WHAT (offer), WHY (promise), HOW (mechanism)
   - Constraints, budget, timeline, compliance
   - Authority: Overrides all strategic decisions

2. **MESSAGE_SPINE (MS)** - Messaging Lock
   - Canonical promise/mechanism/proof pillars/objections/CTA
   - Ensures consistency across all assets
   - Authority: Overrides all messaging decisions

3. **VOICE_GUIDE (VG)** - Voice Lock
   - Tone dials, do/don't rules, forbidden words, POV rules
   - Examples of on-voice vs off-voice
   - Authority: Overrides all style/voice decisions

4. **EVIDENCE_PACK (EP)** - Proof Lock
   - Grounded claims library (studies, testimonials, data)
   - Allowed vs forbidden claim language
   - Authority: Overrides all factual claims

### Orchestration Model

- **MOD (Master Orchestration Director)**: Routes tasks, manages context budget, validates SSOT readiness
- **MMA (Master Monitoring Agent)**: Validates outputs, scores quality, generates Delta Logs
- **Skills**: Modular execution capabilities (copywriting, strategy, editing, etc.)

### Dynamic Skill Cycling

**Never load all 30 skills at once** (causes context collapse).

**Kernel (always loaded):**
- Constitution summary
- MOD + MMA specs
- SSOT objects (PB/MS/VG/EP)
- Skill registry

**On-demand fetch:**
- Specific skill L2 procedures
- Relevant L3 edge cases
- Task-matched examples

**Rule of 3:** Max 3 active skills per run (strategy + execution + MMA)

---

## Quick Start

### 1. Create Your First Project SSOT

```bash
# Copy schemas to create your project SSOT files
cp ssot/schemas/PROJECT_BRIEF_SCHEMA.xml ssot/instances/PB_MyProject_v1.xml
cp ssot/schemas/MESSAGE_SPINE_SCHEMA.xml ssot/instances/MS_MyProject_v1.xml
cp ssot/schemas/VOICE_GUIDE_SCHEMA.xml ssot/instances/VG_MyProject_v1.xml
cp ssot/schemas/EVIDENCE_PACK_SCHEMA.xml ssot/instances/EP_MyProject_v1.xml

# Edit each file to fill in your project details
# Replace all [PLACEHOLDER] markers with real content
```

### 2. Create a Task Request

```yaml
# my_task.yaml
task_request:
  id: "TR-001"
  objective: "Create sales page for my offer"
  output_format: "long-form sales page"

  ssot_references:
    project_brief: "ssot/instances/PB_MyProject_v1.xml"
    message_spine: "ssot/instances/MS_MyProject_v1.xml"
    voice_guide: "ssot/instances/VG_MyProject_v1.xml"
    evidence_pack: "ssot/instances/EP_MyProject_v1.xml"
```

### 3. Route Through MOD

MOD will:
1. Verify SSOT files exist and are complete (RITES gate)
2. Select appropriate skill (sales_page_copywriter)
3. Execute skill with SSOT references
4. Route output to MMA for validation
5. Return validated output + Delta Log

---

## Skill Development

### Converting Markdown Skills to XML

See `skills/MARKDOWN_TO_XML_GUIDE.md` for detailed conversion workflow.

**Quick process:**
1. Copy `skills/SKILL_TEMPLATE.xml`
2. Map Markdown sections to XML nodes
3. Fill in metadata, contract (inputs/outputs), procedures
4. Add edge cases and examples
5. Test with sample task request

### Priority Skills to Convert First

1. **sales_page_copywriter** - Core copywriting skill
2. **email_copy_genius** - Email sequences
3. **offer_architect** - Strategy/positioning
4. **human_persuasion_editor** - Copy refinement
5. **market_intel_synth** - Research synthesis
6. **testimonial_library_agent** - Proof placement
7. **strategic_copy_director** - High-level coordination

---

## Quality Assurance

### MMA Validation

Every skill output is scored across 4 dimensions:
- **Voice Adherence** (75+ required)
- **Clarity** (75+ required)
- **Compliance** (80+ required)
- **Coherence** (75+ required)

**Overall minimum**: 80 average to pass

### Delta Logs

MMA generates patch recommendations:
- **Critical**: Must fix (compliance violations)
- **High**: Strongly recommended (voice drift, evidence gaps)
- **Medium**: Suggested improvements
- **Low**: Optional polish

---

## Constitution Rules (The 10 Commandments)

1. **Truth > Persuasion** - Never sacrifice accuracy for impact
2. **No Fabrication Ever** - Zero tolerance for invented facts
3. **Claims Must Be Grounded** - Every claim maps to EvidencePack
4. **SSOT Overrides Creative Drift** - Respect the locks
5. **Lean Context by Default** - Load only what's needed
6. **Second-Person Clarity** - Direct, clear, no guru tone
7. **No Fake Urgency/Scarcity** - Urgency must be real
8. **Audit Trail** - All edits logged, sources traced
9. **MMA is Final Gate** - No output ships without validation
10. **Everything is Patchable** - Small deltas, versioned changes

---

## Current Status

### ✅ Built (Foundation)
- Governance specs (Constitution, MOD, MMA)
- SSOT schemas (PB, MS, VG, EP)
- Skill registry
- Skill template + conversion guide
- Test harness spec
- Example task requests

### ⏳ In Progress
- Converting 7 core skills from Markdown → XML
- Creating test fixtures (SSOT instances + golden tasks)
- Building skill execution engine

### 📋 TODO
- Remaining 23 skills (convert to XML)
- Automated test runner
- MOD routing logic implementation
- MMA scoring engine
- Skill loading/unloading system (Kernel + on-demand fetch)

---

## Integration with Freedomation/Flowgrams

Once Ultramind core is stable (5-10 converted skills + test harness passing):

1. **Wrap as Nuxt Module** - Ultramind becomes a module in `/modules/ultramind`
2. **UI Layer** - Nuxt provides interface for task requests, SSOT editing
3. **Flowgrams** - Visual workflow builder (maps to Ultramind skill chains)
4. **Storage** - Nuxt handles persistence (database for SSOT + outputs)

Ultramind stays **pure + testable**, Nuxt is **integration surface**.

---

## Contributing

### Adding a New Skill

1. Copy `skills/SKILL_TEMPLATE.xml`
2. Fill in all required sections
3. Add to `registry/registry.yaml`
4. Create test case in `tests/golden_tasks/`
5. Run test harness to validate
6. Document in skill's `<Description>` section

### Updating SSOT Schemas

1. Version the schema (v2.0, v2.1, etc.)
2. Document changes in schema comments
3. Update existing instances (or create migration script)
4. Test with all dependent skills

---

## Support

For questions or issues with Ultramind architecture:
- Review `governance/CONSTITUTION.md` for foundational principles
- Check `registry/registry.yaml` for available skills
- See `examples/task_request.yaml` for usage patterns
- Consult skill specs in `skills/xml/` for detailed procedures

---

## Version History

- **v1.0** (2025-12-17): Initial architecture scaffold
  - Governance specs
  - SSOT schemas
  - Skill template + registry
  - Test harness design
  - 7 skills registered (pending XML conversion)
