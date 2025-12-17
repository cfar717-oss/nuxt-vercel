# MARKDOWN TO XML CONVERSION GUIDE
## How to Convert Existing Ultramind Skills

### Conversion Workflow

1. **Read the Markdown skill** - Understand its purpose, inputs, outputs
2. **Use SKILL_TEMPLATE.xml** - Copy the template as starting point
3. **Map Markdown sections to XML nodes**:
   - Skill header/title → `<Metadata>` + `<Description>`
   - Core procedure → `<Layer1_Core><Procedure>`
   - Detailed instructions → `<Layer2_DetailedProcedure>`
   - Edge cases/troubleshooting → `<Layer3_EdgeCases>`
   - Examples → `<Examples>`
4. **Add contracts** - Define inputs, outputs, dependencies
5. **Add validation criteria** - What MMA should check
6. **Test** - Run through sample task request, verify output

---

### Mapping Guide: Markdown → XML

| Markdown Section | XML Node | Notes |
|-----------------|----------|-------|
| # Skill Name | `<Metadata><Name>` | Human-readable title |
| ## Purpose / Description | `<Description><Purpose>` | Why this skill exists |
| ## When to Use | `<Description><WhenToUse>` | Trigger conditions |
| ## Inputs | `<Contract><InputsRequired>` | SSOT objects + user data |
| ## Outputs | `<Contract><Outputs>` | What this produces |
| ## Procedure / Steps | `<Layer1_Core><Procedure>` | High-level workflow |
| ### Detailed Instructions | `<Layer2_DetailedProcedure>` | Tactical how-to |
| ## Edge Cases / Troubleshooting | `<Layer3_EdgeCases>` | Error handling |
| ## Examples | `<Examples>` | Good/bad output examples |
| ## Constitution Rules | `<Layer1_Core><ConstitutionAlignment>` | Which rules enforced |

---

### Example Conversion

#### Markdown (Before):
```markdown
# Sales Page Copywriter

## Purpose
Drafts long-form sales pages using MESSAGE_SPINE, VOICE_GUIDE, and EVIDENCE_PACK.

## Inputs
- PROJECT_BRIEF (required)
- MESSAGE_SPINE (required)
- VOICE_GUIDE (required)
- EVIDENCE_PACK (required)

## Procedure
1. Load MESSAGE_SPINE - extract promise, mechanism, proof pillars
2. Draft headline using promise (CanonicalStatement variation)
3. Write lead (hook + agitate pain)
4. Explain mechanism (use CanonicalParagraph verbatim)
5. Place proof (testimonials by objection order)
6. Address objections (from MESSAGE_SPINE)
7. Close with CTA (CanonicalPhrasing)

## Edge Cases
- If EvidencePack lacks testimonials: use science/authority proof only
- If promise feels weak: check PROJECT_BRIEF for unique angle
```

#### XML (After):
```xml
<Skill version="1.0" id="sales_page_copywriter">
  <Metadata>
    <SkillID>sales_page_copywriter</SkillID>
    <Name>Sales Page Copywriter</Name>
    <Version>2.0</Version>
    <Category>copywriting</Category>
  </Metadata>

  <Description>
    <Summary>Drafts long-form sales pages using MESSAGE_SPINE + VOICE_GUIDE + EVIDENCE_PACK</Summary>
    <Purpose>Creates persuasive, compliant sales copy aligned with SSOT strategy and voice locks</Purpose>
    <WhenToUse>When task request includes "write sales page" or "draft sales letter"</WhenToUse>
  </Description>

  <Contract>
    <InputsRequired>
      <Input id="I1" priority="critical">
        <Name>MESSAGE_SPINE</Name>
        <Type>SSOT object</Type>
        <Description>Promise, mechanism, proof pillars, objections, CTA</Description>
      </Input>
      <Input id="I2" priority="critical">
        <Name>VOICE_GUIDE</Name>
        <Type>SSOT object</Type>
        <Description>Tone dials, forbidden words, POV rules</Description>
      </Input>
      <Input id="I3" priority="critical">
        <Name>EVIDENCE_PACK</Name>
        <Type>SSOT object</Type>
        <Description>Grounded claims, testimonials, studies</Description>
      </Input>
      <Input id="I4" priority="optional">
        <Name>PROJECT_BRIEF</Name>
        <Type>SSOT object</Type>
        <Description>Audience psychographics, offer details</Description>
      </Input>
    </InputsRequired>

    <Outputs>
      <Output id="O1">
        <Name>Sales Page Draft</Name>
        <Format>Structured copy (headline, lead, mechanism, proof, objections, close)</Format>
        <NextSkill>testimonial_library_agent, human_persuasion_editor</NextSkill>
      </Output>
    </Outputs>
  </Contract>

  <Layer1_Core>
    <Objective>Draft compliant, persuasive sales page using SSOT messaging and voice locks</Objective>
    <Procedure>
      <Step id="S1">
        <Action>Load MESSAGE_SPINE - extract Promise CanonicalStatement, Mechanism, Proof Pillars</Action>
        <Reference>MESSAGE_SPINE: Promise/Mechanism/ProofPillars nodes</Reference>
      </Step>
      <Step id="S2">
        <Action>Draft headline using Promise CanonicalStatement variation (headline context)</Action>
        <Reference>MESSAGE_SPINE: Promise/VariationsAllowed[@context='headline']</Reference>
      </Step>
      <Step id="S3">
        <Action>Write lead: hook (empathy) + agitate (current pain)</Action>
        <Reference>PROJECT_BRIEF: Audience/PrimaryFrustration + MESSAGE_SPINE: Promise</Reference>
      </Step>
      <Step id="S4">
        <Action>Explain mechanism using CanonicalParagraph verbatim or adapted</Action>
        <Reference>MESSAGE_SPINE: Mechanism/CanonicalParagraph</Reference>
      </Step>
      <Step id="S5">
        <Action>Place proof pillars in order (Science → Testimonials → Authority → Results)</Action>
        <Reference>MESSAGE_SPINE: ProofPillars + EVIDENCE_PACK IDs</Reference>
      </Step>
      <Step id="S6">
        <Action>Address objections using MESSAGE_SPINE rebuttal language</Action>
        <Reference>MESSAGE_SPINE: Objections[@priority='critical' | 'high']</Reference>
      </Step>
      <Step id="S7">
        <Action>Close with CTA using CanonicalPhrasing</Action>
        <Reference>MESSAGE_SPINE: CallToAction/CanonicalPhrasing</Reference>
      </Step>
      <FinalStep id="S8">
        <Action>Route output to MMA for validation</Action>
      </FinalStep>
    </Procedure>
  </Layer1_Core>

  <Layer2_DetailedProcedure>
    <!-- Expanded instructions would go here -->
  </Layer2_DetailedProcedure>

  <Layer3_EdgeCases>
    <EdgeCase id="EC1" trigger="evidence_pack_no_testimonials">
      <Scenario>EvidencePack lacks testimonials</Scenario>
      <Resolution>
        <Step>Use science (studies) + authority (expert credentials) proof only</Step>
        <Step>Skip testimonial section or note "Customer reviews coming soon"</Step>
      </Resolution>
    </EdgeCase>
  </Layer3_EdgeCases>
</Skill>
```

---

### Quality Checklist (Post-Conversion)

After converting a Markdown skill to XML, verify:

- [ ] All required XML nodes present (Metadata, Description, Contract, Layer1, ValidationCriteria)
- [ ] InputsRequired clearly defined (what SSOT objects + data needed)
- [ ] Outputs defined (what this skill produces)
- [ ] Layer1_Core has clear step-by-step procedure
- [ ] Constitution rules referenced (which rules this skill enforces)
- [ ] Edge cases documented (at least 2-3 common error scenarios)
- [ ] Examples included (at least 1 good output, 1 bad output with corrections)
- [ ] ValidationCriteria defined (what MMA should check, thresholds)
- [ ] XML is valid (well-formed tags, proper nesting)

---

### Batch Conversion Strategy

For converting 7 skills quickly:

1. **Start with highest-priority skill** (sales_page_copywriter)
2. **Convert fully** (all layers, examples, edge cases) - this becomes the reference
3. **Use as template** for similar skills (email_copy_genius follows same structure)
4. **Adapt quickly** for simpler skills (testimonial_library_agent is smaller scope)
5. **Test each** with sample task_request before moving to next

---

### Tips for Clean XML

- **Use consistent IDs**: `S1`, `S2` for steps; `EC1`, `EC2` for edge cases; `EX1`, `EX2` for examples
- **Escape special characters**: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`
- **Use CDATA for long text blocks**: Wrap prose in `<![CDATA[...]]>` if it contains special chars
- **Indent consistently**: 2 spaces per level for readability
- **Comment liberally**: XML comments `<!-- like this -->` help future editors

---

### Validation

After conversion, test the skill:

1. **Parse XML**: Ensure it's valid (no syntax errors)
2. **Run sample task**: Use examples/task_request.yaml
3. **Check SSOT references**: Verify all referenced IDs exist
4. **Simulate MMA scoring**: Would this output pass validation?
5. **Document gaps**: Note any missing examples or edge cases to add later

---

### Next Steps

Once you've converted 5-7 core skills:
- Run test harness (task → skill → MMA → verify scorecard)
- Build skill registry lookup logic (MOD routing)
- Create skill loading system (Kernel + on-demand fetch)
- Iterate based on real usage
