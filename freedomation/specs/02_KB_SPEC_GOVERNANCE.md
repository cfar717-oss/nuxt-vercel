# KB Spec & Governance (v0.1)

## What is a Knowledge Block (KB)?

A **Knowledge Block (KB)** is an atomic, versioned, reusable unit of procedural knowledge. Each KB describes **how to do one specific thing** with clear inputs, outputs, and step-by-step instructions.

**Think of KBs as:**
- Executable documentation
- Recipes for AI agents
- Modular building blocks for flowgrams
- Self-contained units of expertise

**KBs are NOT:**
- Raw data dumps
- Theoretical essays
- Multi-purpose Swiss Army knives
- Vague guidelines without structure

---

## 1) File Naming & Location

### File Path
All KBs live in `/freedomation/kbs/`

### File Name Format
```
KB-###.md
```

**Rules:**
- Use zero-padded numbers: `KB-001`, `KB-042`, `KB-123` (not `KB-1` or `KB42`)
- Start at `KB-001` and increment sequentially
- File name must match KB ID inside the file

**Examples:**
- `/freedomation/kbs/KB-001.md` ✅
- `/freedomation/kbs/KB-042.md` ✅
- `/freedomation/kbs/kb-5.md` ❌ (wrong format)

---

## 2) Required KB Template

Every KB must follow this structure exactly:

```markdown
# KB-###: [Title in Title Case]

**Version:** 0.1.0
**Status:** draft | stable | deprecated
**Layer:** L1 | L2 | L3 | L4
**Type:** procedural | reference | diagnostic
**Category:** [domain-specific category]
**Credibility:** [low | medium | high | verified]
**Risk:** [low | medium | high]

## Purpose
[1-2 sentence description of what this KB does and why it exists]

## Inputs
List all required and optional inputs:
- **Input Name 1** (required): Description, type, format
- **Input Name 2** (optional): Description, type, format

## Outputs
List all outputs this KB produces:
- **Output Name 1**: Description, type, format
- **Output Name 2**: Description, type, format

## Process
Step-by-step instructions:

1. **[Step Name]**: Clear action to take
   - Sub-detail if needed
   - Expected outcome

2. **[Step Name]**: Next action
   - Sub-detail
   - Expected outcome

3. **[Step Name]**: Final action
   - Sub-detail
   - Expected outcome

## Examples
Concrete, real-world examples demonstrating the KB in action.

### Example 1: [Scenario Name]
**Inputs:**
- Input 1: [actual value]
- Input 2: [actual value]

**Process:**
[Walk through the steps with actual data]

**Outputs:**
- Output 1: [actual result]

## Edge Cases & Warnings
What can go wrong? When should you NOT use this KB?

- **Edge Case 1:** Description and how to handle
- **Edge Case 2:** Description and how to handle
- **Warning 1:** What to avoid

## Quality Checks
How to verify this KB was executed correctly:

- [ ] Check 1: What to verify
- [ ] Check 2: What to verify
- [ ] Check 3: What to verify

## Related KBs
- **KB-XXX**: [Relationship description - prerequisite, alternative, next step]
- **KB-YYY**: [Relationship description]

---

**Change Log:**
- 0.1.0 (YYYY-MM-DD): Initial creation
```

---

## 3) Required Metadata Fields

### Version
Use semantic versioning: `MAJOR.MINOR.PATCH`
- `0.1.0`: Initial draft
- `0.1.1`: Small fix/clarification
- `0.2.0`: Significant change to process or structure
- `1.0.0`: Stable, verified, production-ready

### Status
- **draft**: Work in progress, not ready for production use
- **stable**: Ready for use, has been tested
- **deprecated**: No longer recommended, use alternative

### Layer (Progressive Disclosure)
- **L1**: Quick reference (1-page cheat sheet)
- **L2**: Core execution (the main KB format)
- **L3**: Edge cases & diagnostics (troubleshooting)
- **L4**: Technical specs (schemas, algorithms, deep implementation)

Most KBs should be **L2**.

### Type
- **procedural**: Step-by-step process to accomplish a task
- **reference**: Look-up information, definitions, tables
- **diagnostic**: How to identify and fix problems

Most KBs should be **procedural**.

### Category
Domain-specific categorization:
- `content-creation`
- `data-processing`
- `quality-assurance`
- `personalization`
- `delivery`
- `analytics`
- etc.

Choose categories that make sense for your domain.

### Credibility
How trustworthy is this KB?
- **low**: Experimental, unproven
- **medium**: Tested in limited scenarios
- **high**: Battle-tested, widely used
- **verified**: Independently verified by external review

### Risk
What's the impact if this KB fails?
- **low**: Minor inconvenience, easy to fix
- **medium**: Noticeable problem, requires rework
- **high**: Major failure, potential user harm or brand damage

---

## 4) KB Design Principles

### Atomic & Focused
Each KB should do **one thing** well. If a KB tries to do multiple unrelated tasks, split it into multiple KBs.

**Example:**
- ❌ Bad: `KB-001: Content Creation and Quality Assurance`
- ✅ Good: `KB-001: Draft Email Content` + `KB-002: Review Email for Quality`

### Self-Contained
A KB should be understandable on its own. Don't assume the reader has read other KBs (though you can reference them).

### Executable
An AI agent (or human) should be able to follow the KB and produce the expected output. Be specific, not vague.

**Example:**
- ❌ Vague: "Write engaging content"
- ✅ Specific: "Write a 3-paragraph email with a clear value proposition in paragraph 1, supporting details in paragraph 2, and a permission-based CTA in paragraph 3"

### Testable
The "Quality Checks" section should provide clear criteria to determine if the KB was executed correctly.

---

## 5) KB Lifecycle

1. **Draft** → Author creates KB, assigns `status: draft`
2. **Review** → KB is reviewed for clarity, completeness, adherence to template
3. **Stable** → KB passes review, status changes to `status: stable`
4. **Iterate** → As KBs are used, they're refined (version bumps)
5. **Verify** → High-impact KBs undergo formal verification (credibility: verified)
6. **Deprecate** → If a KB is no longer useful, mark `status: deprecated` and point to replacement

---

## 6) Versioning Rules

### When to Bump Versions

**Patch (0.1.0 → 0.1.1):**
- Fix typos
- Clarify wording
- Add examples
- Minor edge case documentation

**Minor (0.1.0 → 0.2.0):**
- Add/remove inputs or outputs
- Change process steps significantly
- Update quality checks
- Change category or layer

**Major (0.9.0 → 1.0.0):**
- KB is verified and production-ready
- Breaking changes to interface

### Version History
Always maintain a change log at the bottom of each KB:

```markdown
---

**Change Log:**
- 0.1.0 (2025-12-13): Initial creation
- 0.1.1 (2025-12-15): Added example 2, clarified step 3
- 0.2.0 (2025-12-20): Added optional input "tone preference"
```

---

## 7) KB Validation Checklist

Before marking a KB as `stable`, verify:

- [ ] File name matches KB ID inside file
- [ ] All required metadata fields present and valid
- [ ] Purpose is clear and concise (1-2 sentences)
- [ ] Inputs are well-defined with types
- [ ] Outputs are well-defined with types
- [ ] Process steps are numbered and actionable
- [ ] At least one concrete example included
- [ ] Edge cases and warnings documented
- [ ] Quality checks are testable
- [ ] Related KBs are cross-referenced
- [ ] Change log is present
- [ ] No violations of Agentic Resonance doctrine (see `01_DOCTRINE_AGENTIC_RESONANCE.md`)

---

## 8) Common Mistakes to Avoid

### Mistake 1: Vague Process Steps
❌ "Create compelling content"
✅ "Write a 3-paragraph email following the structure: value prop, supporting details, CTA"

### Mistake 2: Missing Inputs/Outputs
❌ Process assumes you know what inputs are needed
✅ Explicitly list all required and optional inputs

### Mistake 3: No Examples
❌ Only abstract instructions
✅ At least one concrete example with real inputs/outputs

### Mistake 4: Skipping Edge Cases
❌ Only describe the happy path
✅ Document what can go wrong and how to handle it

### Mistake 5: Untestable Quality Checks
❌ "Content should be good"
✅ "Content passes Ethics & Integrity Gate (no manipulation, no fabricated claims)"

---

## 9) KB Naming Conventions

### KB ID
Sequential numbers, zero-padded to 3 digits:
- `KB-001`
- `KB-042`
- `KB-123`

### KB Title
Use descriptive, action-oriented titles:
- ✅ `KB-001: Draft Outbound Email Content`
- ✅ `KB-002: Validate Email Against Ethics Gate`
- ❌ `KB-001: Email` (too vague)
- ❌ `KB-002: Stuff` (useless)

---

## 10) Integration with Flowgrams

Flowgrams reference KBs by ID. Each node in a flowgram typically maps to one KB:

```yaml
nodes:
  - node_id: "n1_draft_content"
    kb_ref: "KB-001"
    inputs_required:
      - artifact.brand_kit.v0_1
    outputs_primary:
      - artifact.email_draft.v0_1
```

The KB defines **how** the work is done. The flowgram defines **when** and **in what order** KBs are executed.

---

## 11) Governance Authority

KB governance is enforced by:
- **Manual review** (for status promotion)
- **Automated validation** (schema checks, naming conventions)
- **Gate validation** (ethics, deliverability checks on KB outputs)

The **Knowledge Governance Committee** (future) will oversee KB certification and verification.

---

## Summary

KBs are the building blocks of Freedomation workflows. They must be:
- Atomic and focused
- Self-contained and executable
- Well-documented with examples
- Versioned and status-tracked
- Testable and verifiable
- Compliant with Agentic Resonance doctrine

Follow this spec rigorously to maintain system integrity.

---

**Version:** 0.1.0
**Status:** stable
**Last Updated:** 2025-12-13
