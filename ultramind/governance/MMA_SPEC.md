# MMA SPECIFICATION v1.0
## Master Monitoring Agent

### Purpose
MMA is the quality assurance and validation layer of Ultramind. It evaluates all skill outputs against Constitution standards, scores quality dimensions, flags compliance issues, and generates Delta Logs (patch recommendations).

---

## Core Responsibilities

### 1. Output Validation
Evaluate every skill output across 4 quality dimensions:
- **Voice Adherence**: Matches VoiceGuide specifications
- **Clarity**: Second-person, direct, no jargon or ambiguity
- **Compliance**: All claims grounded in EvidencePack
- **Coherence**: Internally consistent logic and flow

### 2. Scoring System
Each dimension scored 0-100:
- **90-100**: Excellent, ship-ready
- **75-89**: Good, minor refinements recommended
- **50-74**: Acceptable, significant improvements needed
- **0-49**: Failed, requires rework

**Minimum pass threshold**: All dimensions ≥75, overall average ≥80

### 3. Compliance Checking
**Evidence Grounding**:
- Every factual claim must map to EvidencePack entry
- If claim lacks evidence: FLAG and recommend softening language or removal

**Forbidden Patterns**:
- Fabricated statistics
- Unattributed testimonials
- Fake urgency/scarcity
- Income claims (where prohibited)
- Medical diagnosis language (for supplements)

**Required Elements** (task-dependent):
- Disclaimers (supplement/health claims)
- Privacy policy links (opt-in forms)
- Refund policy clarity (e-commerce)

### 4. Delta Log Generation
For every output, produce a patch recommendation list:
- **Critical**: Must fix before shipping (compliance violations)
- **High**: Strongly recommended (voice drift, clarity issues)
- **Medium**: Suggested improvements (flow, word choice)
- **Low**: Optional polish (stylistic preferences)

---

## Input Contract

### Skill Output to Validate
```yaml
validation_request:
  task_id: "TR-2025-001"
  skill_id: "sales_page_copywriter"
  skill_version: "v2.0"
  output_type: "long-form sales page"
  ssot_references:
    message_spine: "MS_Supplement_Core_v1.xml"
    voice_guide: "VG_Health_Authority_v1.xml"
    evidence_pack: "EP_Supplement_Claims_v3.xml"
  output_content: |
    [The actual copywriter output text...]
```

---

## Output Contract

### MMA Scorecard
```yaml
mma_scorecard:
  task_id: "TR-2025-001"
  skill_id: "sales_page_copywriter"
  validation_timestamp: "2025-12-17T14:23:00Z"

  scores:
    voice_adherence: 88
    clarity: 92
    compliance: 78
    coherence: 85
    overall: 85.75

  status: "passed" | "failed"

  findings:
    critical: []
    high:
      - "Line 47: Claim 'reduces inflammation by 60%' not found in EvidencePack. Soften to 'may help reduce inflammation' or add supporting evidence."
    medium:
      - "Headline uses 'discover' (VG forbidden word list). Replace with 'learn' or 'see'."
    low:
      - "Paragraph 3: Consider breaking into 2 shorter paragraphs for readability."

  compliance_flags:
    evidence_gaps:
      - claim: "60% inflammation reduction"
        location: "line 47"
        severity: "high"
        recommendation: "Add study EP:E14 or soften claim"
    forbidden_patterns: []
    missing_required_elements: []

  delta_log:
    - priority: "high"
      location: "line 47"
      current: "reduces inflammation by 60%"
      recommended: "may help reduce inflammation based on preliminary research"
      reason: "Claim not grounded in EvidencePack"

    - priority: "medium"
      location: "headline"
      current: "Discover the Secret to..."
      recommended: "Learn the Science-Backed Method to..."
      reason: "'Discover' on VG forbidden word list"
```

---

## Validation Logic

### Voice Adherence Check
1. Load VoiceGuide tone dials (sophistication, urgency, empathy, authority)
2. Scan output for:
   - Forbidden words (auto-flag)
   - Tone violations (too casual/formal, too hype/flat)
   - POV errors (first-person instead of second-person)
3. Compare against VG examples (on-voice vs off-voice)
4. Score based on violations density

### Clarity Check
1. Sentence length analysis (flag >30 words)
2. Jargon detection (flag unexplained technical terms)
3. Passive voice density (flag >10%)
4. Ambiguity detection (vague pronouns, unclear antecedents)
5. Readability score (target: 8th-10th grade)

### Compliance Check
**Evidence Grounding**:
1. Extract all factual claims from output
2. Cross-reference against EvidencePack IDs
3. Flag ungrounded claims:
   - Critical: Health/safety claims, efficacy percentages
   - High: Specific statistics, study results
   - Medium: General benefits, mechanism descriptions

**Pattern Matching**:
1. Scan for forbidden patterns (regex + semantic)
2. Verify required elements present (disclaimers, policies)
3. Check claim language against allowed/forbidden lists (EP)

### Coherence Check
1. **Logical flow**: Does each section lead naturally to the next?
2. **Consistency**: Do promise/mechanism/proof align?
3. **CTA alignment**: Does the close match the open?
4. **Proof order**: Are objections addressed before CTA?

---

## Scoring Methodology

### Voice Adherence (0-100)
- Start at 100
- -5 per forbidden word used
- -10 per major tone violation (too hype/flat)
- -3 per POV error
- Floor at 0

### Clarity (0-100)
- Start at 100
- -2 per sentence >30 words
- -5 per unexplained jargon term
- -10 per paragraph lacking clear topic sentence
- Floor at 0

### Compliance (0-100)
- Start at 100
- -25 per critical ungrounded claim (health/efficacy)
- -10 per high-priority ungrounded claim (stats)
- -5 per medium ungrounded claim (general benefits)
- -15 per forbidden pattern detected
- Floor at 0

### Coherence (0-100)
- Start at 100
- -10 per major logical gap
- -5 per promise/proof misalignment
- -3 per weak transition
- Floor at 0

---

## Delta Log Priority System

### Critical (Must Fix)
- Compliance violations (ungrounded health claims)
- Legal issues (missing disclaimers)
- Fabricated data
- Forbidden patterns (fake urgency)

### High (Strongly Recommended)
- Voice drift (forbidden words, tone violations)
- Evidence gaps (important claims lacking support)
- Major clarity issues (confusing logic)

### Medium (Suggested)
- Minor voice tweaks (word choice)
- Flow improvements (transitions)
- Readability enhancements (sentence length)

### Low (Optional Polish)
- Stylistic preferences
- Minor wording variations
- Formatting suggestions

---

## Pass/Fail Criteria

### Automatic Fail Conditions
- Any critical compliance violation
- Compliance score <50
- 3+ high-priority evidence gaps
- Fabricated testimonials/data detected

### Pass Requirements
- All scores ≥75
- Overall average ≥80
- Zero critical violations
- All required elements present

### Conditional Pass
- Scores 75-79 (pass with recommended improvements)
- Output ships but Delta Log should be addressed in next revision

---

## Integration with MOD

1. **MOD routes output to MMA** (always final step)
2. **MMA validates and scores**
3. **If passed**: Return output + scorecard + Delta Log to user
4. **If failed**: Return to skill for rework (max 2 iterations)
5. **If still failed after 2 iterations**: Escalate to human review

---

## Performance Metrics
- **Validation speed**: target <2min per output
- **False positive rate**: <5% (flagging valid outputs)
- **False negative rate**: <1% (missing real issues)
- **Delta Log actionability**: >90% of recommendations implemented

---

## Version History
- v1.0 (2025-12-17): Initial MMA specification
