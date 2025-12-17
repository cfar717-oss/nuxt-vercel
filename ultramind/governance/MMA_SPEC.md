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
- v1.1 (2025-12-17): Added 6-Axis Neuro-Validation (RESONANCE_CONSTITUTION.xml integration)

---

## NEURO-VALIDATION INTEGRATION (v1.1+)
**PATCH BLOCK: Integrated 2025-12-17 | 6-Axis Resonance Scoring**

### Enhanced Quality Dimensions (7 Total)

**Original 4 Dimensions (v1.0):**
1. Voice Adherence
2. Clarity
3. Compliance
4. Coherence

**NEW 5th-7th Dimensions (v1.1+):**
5. **Neuro-Resonance Score** (6-axis activation + balance)
6. **Manipulation Detection** (dark pattern identification)
7. **Transformation Clarity** (Radical Simplicity test)

**Reference**: All neuro-validation rules defined in `RESONANCE_CONSTITUTION.xml`.

---

### 6-Axis Neuro-Resonance Scoring

**What MMA Now Evaluates:**

For every output, MMA scores activation of each neurochemical axis (0-10 scale):

#### AXIS 1: BOTTOM (GABA - Safety/Trust)
**Question**: *"Will this hurt me?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: No safety signals, feels risky, lacks trust-building
- **4-6 (Moderate)**: Some safety signals but inconsistent
- **7-8 (Strong)**: Clear safety/trust foundation (guarantees, proof, risk reversal)
- **9-10 (Exceptional)**: Multi-layered safety architecture (testimonials + guarantees + third-party validation + transparent process)

**Copy Indicators:**
- Guarantees (money-back, satisfaction)
- Risk reversal language ("no obligation", "cancel anytime")
- Testimonials (social proof = safety in numbers)
- Transparency (clear ingredients, process, pricing)
- Third-party validation (certifications, studies)

**Rule**: BOTTOM must be established FIRST for cold audiences (score ≥7/10).

---

#### AXIS 2: TOP (Serotonin - Status/Elevation)
**Question**: *"Will this elevate me?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: Generic benefits, no status differentiation
- **4-6 (Moderate)**: Some status signals but not compelling
- **7-8 (Strong)**: Clear elevation (join elite group, insider access, premium positioning)
- **9-10 (Exceptional)**: Transformational identity shift (become the kind of person who...)

**Copy Indicators:**
- Exclusivity language ("select few", "insider", "VIP")
- Identity transformation (before/after states)
- Social status markers (what others will notice/admire)
- Achievement framing (reach new level, join top performers)
- Premium positioning (not for everyone)

**Balance Rule**: TOP score cannot exceed BOTTOM by 3+ points (elevation requires foundation).

---

#### AXIS 3: LEFT (Dopamine - Emotion/Desire)
**Question**: *"Do I want this?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: Flat, no emotional resonance
- **4-6 (Moderate)**: Some desire but not compelling
- **7-8 (Strong)**: Clear emotional hooks (pain/desire vividly painted)
- **9-10 (Exceptional)**: Visceral desire (can taste/feel/see the outcome)

**Copy Indicators:**
- Sensory language (vivid imagery)
- Emotional pain points (frustration, fear, desire)
- Future pacing (imagine when...)
- Contrast (before vs after emotional states)
- Storytelling (relatable struggle → victory)

---

#### AXIS 4: RIGHT (Acetylcholine - Logic/Reason)
**Question**: *"Does this make sense?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: No logical explanation, feels like magic/hype
- **4-6 (Moderate)**: Some reasoning but gaps in logic
- **7-8 (Strong)**: Clear mechanism explanation (UMP/UMS), logical proof
- **9-10 (Exceptional)**: Airtight reasoning (mechanism + studies + expert validation + FAQs preempt all logical objections)

**Copy Indicators:**
- Mechanism explanation (HOW it works, not just THAT it works)
- Scientific backing (studies, research, citations)
- Expert endorsements (authority validation)
- Logical flow (cause → effect clearly explained)
- FAQ/objection handling (addresses "why" questions)

**Balance Rule**: LEFT/RIGHT must balance within 2-3 points (emotion without logic = hype; logic without emotion = boring).

---

#### AXIS 5: FRONT (Adrenaline - Action/Urgency)
**Question**: *"Should I act now?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: No urgency, passive, easy to delay
- **4-6 (Moderate)**: Some urgency but not compelling
- **7-8 (Strong)**: Clear genuine urgency (limited spots, deadline, problem worsening)
- **9-10 (Exceptional)**: Irresistible momentum (opportunity cost vivid + FOMO + genuine scarcity + time-bound consequences)

**Copy Indicators:**
- Genuine scarcity (limited inventory, enrollment cap)
- Time-bound offers (expiring bonus, price increase)
- Opportunity cost (what you lose by waiting)
- Consequence stacking (problem worsens over time)
- Clear CTA (specific action, deadline, easy next step)

**CRITICAL**: Urgency MUST be genuine (Rule #7 of Constitution).

**Manipulation Penalty**: -3.0 per fake countdown timer, manufactured scarcity, or fear-mongering tactic.

---

#### AXIS 6: BACK (Oxytocin - Harmony/Identity)
**Question**: *"Does this fit who I am?"*

**Scoring Criteria (0-10):**
- **0-3 (Weak)**: No identity alignment, feels foreign
- **4-6 (Moderate)**: Some alignment but not integrated
- **7-8 (Strong)**: Clear identity match (this is for people like you)
- **9-10 (Exceptional)**: Deep tribal belonging (you're already one of us, we see you, this completes your identity)

**Copy Indicators:**
- Tribe language ("people like us", "if you're the kind of person who...")
- Values alignment (what you believe/stand for)
- Identity affirmation (we see you, we get you)
- Shared enemy (us vs the broken system)
- Belonging signals (join the community, you're not alone)

**Balance Rule**: FRONT (urgency) without BACK (identity) = manipulation red flag.

---

### 6-Axis Balance Rules (Auto-Enforced)

**Opposing Pairs Must Harmonize:**

1. **BOTTOM ↔ TOP (Foundation ↔ Elevation)**
   - Rule: TOP cannot exceed BOTTOM by 3+ points
   - Why: Promising elevation without safety = manipulation
   - Example Violation: TOP=9, BOTTOM=5 (promising status without trust)

2. **LEFT ↔ RIGHT (Emotion ↔ Logic)**
   - Rule: Must balance within 2-3 points
   - Why: Pure emotion = hype; pure logic = boring
   - Example Balance: LEFT=8, RIGHT=7 (emotion-led with logical backing)

3. **FRONT ↔ BACK (Action ↔ Harmony)**
   - Rule: FRONT without BACK (score differential >3) = manipulation flag
   - Why: Urgency without identity alignment = pressure tactics
   - Example Violation: FRONT=9, BACK=3 (pushing action without belonging)

**MMA Enforcement**: Balance violations trigger automatic score penalties and Delta Log entries.

---

### Overall Neuro-Resonance Score (0-10)

**Calculation:**
```
Overall_Resonance = (
  (BOTTOM + TOP + LEFT + RIGHT + FRONT + BACK) / 6
) - Balance_Penalties - Manipulation_Penalties
```

**Balance Penalties:**
- -1.0 per balance rule violation (opposing pairs out of sync)

**Manipulation Penalties:**
- -3.0 per manipulation pattern detected (fake urgency, manufactured scarcity, fear-mongering, hidden costs)

**Rating Bands:**
- **9.0-10.0**: Exceptional (publish immediately)
- **7.5-8.9**: Strong (minor polish recommended)
- **6.0-7.4**: Good (refinements needed)
- **4.0-5.9**: Weak (significant rework required)
- **0-3.9**: Poor (redesign from strategy layer)

---

### Manipulation Detection (Automatic Penalties)

**Prohibited Patterns (from RESONANCE_CONSTITUTION.xml):**

1. **Fake Countdown Timers**
   - Detection: Timer resets on page reload, no real inventory tracking
   - Penalty: -3.0 to FRONT axis + critical compliance flag
   - Remediation: Remove timer or implement genuine deadline

2. **Manufactured Scarcity**
   - Detection: "Only 3 spots left" with no backend verification
   - Penalty: -3.0 to FRONT axis + critical compliance flag
   - Remediation: Remove scarcity claim or provide genuine inventory limits

3. **Fear-Mongering**
   - Detection: Excessive negative consequences without balanced hope
   - Penalty: -2.0 to BOTTOM axis (erodes safety)
   - Remediation: Balance problem awareness with solution confidence

4. **Hidden Costs**
   - Detection: Pricing not transparent, surprise fees mentioned later
   - Penalty: -3.0 to BOTTOM axis (destroys trust) + critical compliance flag
   - Remediation: Full price transparency upfront

5. **Bait-and-Switch**
   - Detection: Promise doesn't match offer, misleading headlines
   - Penalty: -3.0 to RIGHT axis (logic violation) + critical compliance flag
   - Remediation: Align promise with actual offer

**Auto-Fail**: 2+ manipulation patterns detected = automatic validation failure (requires rework from strategy layer).

---

### Radical Simplicity Test (Pass/Fail Gate)

**Before any output passes MMA, it must answer these 4 questions:**

1. **THE PROMISE**: Can the transformation be stated in ONE sentence?
   - **Pass**: Single, clear transformation
   - **Fail**: Compound claims, vague outcomes, requires paragraphs to explain

2. **THE PROOF**: Can you explain WHY it works + show WHO it worked for?
   - **Pass**: Clear mechanism (UMP/UMS) + specific testimonials/data
   - **Fail**: No mechanism explanation or generic "results may vary"

3. **THE TRUST**: Have you made them feel SAFE (GABA ≥7/10)?
   - **Pass**: BOTTOM axis score ≥7/10
   - **Fail**: BOTTOM axis score <7/10

4. **THE DEAL**: Is the urgency genuine (not manufactured)?
   - **Pass**: Urgency ties to real deadline/scarcity + FRONT score ≤ BACK+3
   - **Fail**: Fake countdown/scarcity or FRONT >> BACK (manipulation flag)

**If any answer is "Fail"**: Output does not pass MMA validation (regardless of other scores).

**Authority**: Radical Simplicity overrides all other quality metrics. Complex ≠ better.

---

### Enhanced MMA Scorecard (v1.1 Format)

```yaml
mma_scorecard:
  task_id: "TR-2025-001"
  skill_id: "sales_page_copywriter"
  validation_timestamp: "2025-12-17T14:23:00Z"

  # Original 4 Dimensions (v1.0)
  scores:
    voice_adherence: 88
    clarity: 92
    compliance: 78
    coherence: 85
    overall_traditional: 85.75

  # NEW: 6-Axis Neuro-Resonance (v1.1+)
  neuro_resonance:
    axis_scores:
      BOTTOM_gaba_safety: 8.5
      TOP_serotonin_status: 7.0
      LEFT_dopamine_emotion: 8.0
      RIGHT_acetylcholine_logic: 7.5
      FRONT_adrenaline_action: 6.0
      BACK_oxytocin_harmony: 7.0

    balance_check:
      BOTTOM_TOP_differential: 1.5  # ✓ Pass (TOP not exceeding BOTTOM by 3+)
      LEFT_RIGHT_differential: 0.5  # ✓ Pass (balanced within 2 points)
      FRONT_BACK_differential: -1.0 # ✓ Pass (FRONT ≤ BACK, no manipulation flag)
      balance_violations: 0
      balance_penalties: 0.0

    manipulation_detection:
      patterns_detected: []
      manipulation_penalties: 0.0

    overall_resonance_score: 7.33  # (8.5+7+8+7.5+6+7)/6 = 7.33
    resonance_rating: "Strong"     # 7.5-8.9 band

  # Radical Simplicity Test (v1.1+)
  radical_simplicity:
    promise_clarity: "pass"  # Single sentence transformation: ✓
    proof_strength: "pass"   # Mechanism + testimonials: ✓
    trust_foundation: "pass" # BOTTOM ≥7: ✓ (8.5)
    urgency_authenticity: "pass" # Genuine urgency + FRONT≤BACK+3: ✓
    overall_test: "PASS"

  # Overall Status
  status: "passed"

  # Findings (Delta Log)
  findings:
    critical: []
    high:
      - "Line 47: Claim 'reduces inflammation by 60%' not found in EvidencePack (Compliance)."
      - "FRONT axis score low (6.0) - consider strengthening CTA urgency or adding genuine deadline (Neuro-Resonance)."
    medium:
      - "Headline uses 'discover' (VG forbidden word). Replace with 'learn'."
      - "LEFT/RIGHT differential optimal (0.5) but could increase emotional resonance by +1 point for stronger impact."
    low:
      - "Paragraph 3: Consider breaking into 2 shorter paragraphs (Clarity)."

  neuro_recommendations:
    - axis: "FRONT"
      current_score: 6.0
      target_score: 7.5
      recommendation: "Add genuine time-bound offer or limited enrollment window to strengthen urgency."
    - axis: "BOTTOM"
      current_score: 8.5
      note: "Strong foundation - maintain this level across all touchpoints."
```

---

### Enhanced Validation Logic (v1.1)

**MMA Validation Sequence:**

1. **Run Original 4 Validations** (v1.0):
   - Voice Adherence
   - Clarity
   - Compliance
   - Coherence

2. **Run 6-Axis Neuro-Scoring** (v1.1+):
   - Score each axis (BOTTOM, TOP, LEFT, RIGHT, FRONT, BACK)
   - Check balance rules (opposing pairs)
   - Detect manipulation patterns
   - Calculate overall resonance score

3. **Run Radical Simplicity Test** (v1.1+):
   - Promise clarity (1 sentence?)
   - Proof strength (WHY + WHO?)
   - Trust foundation (GABA ≥7?)
   - Urgency authenticity (genuine?)

4. **Aggregate Scores**:
   - Traditional overall (4 dimensions average)
   - Neuro-resonance overall (6 axes average - penalties)
   - **Combined Overall** = (Traditional × 0.4) + (Neuro-Resonance × 0.6)
   - Rationale: Neuro-resonance weighted higher (60%) as it predicts conversion + ethical persuasion

5. **Generate Delta Log**:
   - Critical: Compliance violations + manipulation patterns
   - High: Voice drift + evidence gaps + low axis scores (<6)
   - Medium: Balance opportunities + clarity improvements
   - Low: Stylistic polish

6. **Pass/Fail Decision**:
   - Must pass ALL gates (Traditional + Neuro + Radical Simplicity)
   - Single gate failure = overall failure (requires rework)

---

### Enhanced Pass/Fail Criteria (v1.1)

**Automatic Fail Conditions (v1.0 + v1.1):**
- Any critical compliance violation [v1.0]
- Compliance score <50 [v1.0]
- 3+ high-priority evidence gaps [v1.0]
- Fabricated testimonials/data detected [v1.0]
- **2+ manipulation patterns detected** [v1.1+]
- **Radical Simplicity test failure (any of 4 questions = fail)** [v1.1+]
- **Balance violation ≥2 axes (opposing pairs out of sync by 3+ points)** [v1.1+]
- **BOTTOM axis <7 for cold audience** [v1.1+]

**Pass Requirements (v1.0 + v1.1):**
- All traditional scores ≥75 [v1.0]
- Overall traditional average ≥80 [v1.0]
- Zero critical violations [v1.0]
- All required elements present [v1.0]
- **Overall neuro-resonance score ≥7.0** [v1.1+]
- **Zero balance violations (or max 1 minor violation <2 point differential)** [v1.1+]
- **Zero manipulation patterns** [v1.1+]
- **Radical Simplicity test: PASS on all 4 questions** [v1.1+]

**Conditional Pass (v1.0 + v1.1):**
- Traditional scores 75-79 (recommended improvements) [v1.0]
- **Neuro-resonance 6.0-6.9 (refinements recommended)** [v1.1+]
- 1 minor balance violation (differential 2-3 points, not critical pair)
- Output ships but Delta Log must be addressed in next revision

---

### Integration with MOD (v1.1 Updated)

**Enhanced Handoff from MOD:**
MOD now passes to MMA:
- Traditional SSOT objects (PB/MS/VG/EP)
- **RESONANCE_CONSTITUTION.xml reference** [v1.1+]
- **Neuro-targeting requirements** (which axes to prioritize, balance rules, audience temperature) [v1.1+]

**MMA Responsibilities:**
1. Validate traditional quality (v1.0)
2. **Validate neuro-resonance (6-axis scoring + balance + manipulation detection)** [v1.1+]
3. **Run Radical Simplicity test** [v1.1+]
4. Generate comprehensive Delta Log (traditional + neuro recommendations)
5. Return scorecard to MOD

**Failure Routing:**
- If failed due to traditional issues → Return to execution skill (e.g., `sales_page_copywriter`)
- If failed due to neuro-issues (balance/manipulation) → Route back to strategy layer (`offer_architect` or `strategic_copy_director`)
- Rationale: Neuro-failures indicate strategic misalignment, not execution errors

---

### Enhanced Performance Metrics (v1.1)

**Original Metrics (v1.0):**
- Validation speed: target <2min per output
- False positive rate: <5%
- False negative rate: <1%
- Delta Log actionability: >90%

**NEW Neuro-Performance Metrics (v1.1+):**
- **Neuro-scoring accuracy**: target >95% agreement with human neuro-auditors
- **Balance violation detection**: target 100% catch rate (zero false negatives)
- **Manipulation pattern detection**: target >98% accuracy (critical for ethics)
- **Radical Simplicity enforcement**: target 100% (non-negotiable gate)
- **Overall neuro-pass rate**: target >75% first-pass (lower than traditional due to higher bar)

---

### Authority Note

**RESONANCE_CONSTITUTION.xml is now authoritative for all neuro-validation rules.**

MMA does NOT invent neuro-scoring criteria. All rules, penalties, balance thresholds, and manipulation definitions are defined in RESONANCE_CONSTITUTION.xml.

**MMA's role**: Enforce the constitution, score accurately, flag violations, recommend improvements.

**System Note**: The 6-Axis Neuro-Box is the operating system of persuasion. MMA is the quality gate that ensures this operating system runs without corruption (manipulation).
