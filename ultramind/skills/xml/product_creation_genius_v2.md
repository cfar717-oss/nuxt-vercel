---
skill_id: product_creation_genius
version: 2.1.0
owner: "Product Creation Genius"
tier: production
last_updated: "2025-12-16"

intent: "Design complete transformation ecosystems—90-day programs, hybrid offers, and tiered architectures that integrate digital + physical + community + AI into one coherent outcome."

inputs_required:
  - PROJECT_BRIEF
  - MESSAGE_SPINE

inputs_optional:
  - EVIDENCE_PACK
  - MARKET_RESEARCH_SYNTHESIS
  - COMPETITIVE_ANALYSIS

outputs_primary:
  - PROGRAM_ARCHITECTURE
  - TIERED_OFFER_STRUCTURE
  - TRANSFORMATION_MAP

outputs_secondary:
  - VALIDATION_PLAN
  - PRICING_STRATEGY
  - COORDINATION_NOTES

dependencies_upstream:
  - market_intelligence_synthesizer: "provides market research synthesis + avatar sophistication signals"
  - offer_architect: "provides positioning framework + canonical mechanism language"

dependencies_downstream:
  - sales_page_copywriter: "receives program structure, proof-ready milestones, and offer tiers"
  - email_campaign_genius: "receives tier logic, launch phases, and objections mapped to stages"
  - vsl_long_form: "receives narrative arc + milestone visuals"

awakens_L1:
  high_priority: [offer_architect, sales_page_copywriter, email_campaign_genius]
  medium_priority: [market_intelligence_synthesizer, vsl_long_form]

quality_gates:
  - transformation_over_information: "Program is a guided identity/behavior shift, not a content library."
  - whole_solution_integration: "Digital + physical + community + AI reinforce the same behaviors."
  - validation_before_build: "Run profit-first validation before heavy production."
  - realistic_timelines: "Timelines match EVIDENCE_PACK or are framed as hypotheses/betas."

guardrails:
  - no_information_dump: "Use LEARN→DO→SHARE→TEACH; every lesson produces action + feedback."
  - no_unsupported_timelines: "No 'X days guaranteed' unless Evidence Pack supports."
  - no_feature_dump_bundles: "Every component must map to a stage + behavior."
  - validate_before_building: "If not validated, build only the minimum viable onboarding + week 1."

token_budget:
  L1: 250
  L2: 2800
  L3: 5500
  L4: 3200

mod_integration:
  routing_triggers:
    - "Design a program, course, coaching offer, membership, or hybrid bundle"
    - "Need a 30/60/90-day transformation map"
    - "Need tiered pricing/packaging architecture"
  default_layers: "L1+L2"
  load_L3_when: ["complexity >= 4", "edge_case_detected", "MMA_score_below_7", "validation_failed"]
  load_L4_when: ["building/upgrading skills", "schema debugging", "SSOT contract design"]

mma_integration:
  evaluate_with: ["strategy_alignment", "clarity_structure", "proof_discipline", "cta_integrity", "ethical_guardrails"]
  pass_threshold: ">=7 on all; no hard-gate violations"
---

# Product Creation Genius

## L1 — Quick Reference

**Check PROJECT_BRIEF for**
- Avatar sophistication (first-time vs proven buyer)
- Transformation complexity (single-phase vs multi-phase)
- Support capacity (self-serve vs high-touch)
- Nonnegotiables (claims, compliance, brand-donts)
- Tone dials (warmth/authority/urgency…)

**Check MESSAGE_SPINE for**
- Core promise + canonical mechanism paragraph
- Proof pillars (must be present in program & marketing)
- Big objections + counters
- CTA frame (exact language)

**Golden Rules**
1. **Transformation > Information** (90-day journey + identity shift)
2. **Breakthrough by Week 1–2** (quick win = momentum)
3. **LEARN→DO→SHARE→TEACH** (retention + behavior change)
4. **Minimum 4-pillar support** (content + community + coaching + resources)
5. **Validate before you build** (profit-first 72-hour sprint)
6. **Whole-solution integration** (physical + digital + community + AI synergy)
7. **Honest timelines** (effort shown; no hype)

**Canonical Examples**
- **90-Day Blueprint:** Breakthrough (1–2) → Milestones (3–8) → Miracle/Integration (9–12)
- **3-Tier Hybrid:** Core (digital) → Premium (+physical kit) → VIP (+1:1 / clinic-grade support)

---

## L2 — Core Procedure (Production)

### Step 0 — Confirm Contracts (No Guessing)
**Inputs required:** PROJECT_BRIEF + MESSAGE_SPINE
**If missing fields:** request them or derive explicitly (label as *ASSUMPTION*).

**Hard checks**
- If any transformation/timeline claim is needed: require EVIDENCE_PACK or label as *beta hypothesis*.
- If compliance constraints exist: copy them into program "language rules".

---

## Framework 1: 90-Day Transformation Blueprint (Design the Journey)
**Purpose:** Build a guided progression that creates real behavior change.
**When to use:** Any program > 2 weeks, any premium offer, any coaching/membership.

**Steps**
1. **Define the Identity Shift**
   - "From ___ to ___" (who they become by day 90)
2. **Set the 3 Stages**
   - Stage A (Weeks 1–2): Breakthrough + quick win
   - Stage B (Weeks 3–8): Capability milestones
   - Stage C (Weeks 9–12): Integration + autonomy
3. **For each stage, define**
   - One core behavior to install
   - One metric of completion
   - One support mechanism (community/coaching/resource)
4. **Write the "Success Path"**
   - The minimum actions required weekly (no fluff)

**Validation**
- Can a beginner follow this without willpower heroics?
- Does each stage produce a measurable win?

**Outputs**
- TRANSFORMATION_MAP (90-day stages + metrics)
- PROGRAM_ARCHITECTURE skeleton

---

## Framework 2: Breakthrough → Milestone → Miracle Map (Proof-Disciplined)
**Before applying**
- Check EVIDENCE_PACK for timeline proof.
- If proof is missing, design as *hypothesis*, then validate via beta cohort.

**Steps**
1. **Quick Win (Week 1–2)**
   - Small, believable, measurable result
2. **3 Milestones (Weeks 3–8)**
   - Each milestone = new capability + proof moment
3. **Integration (Weeks 9–12)**
   - "They can do it without you" plan (maintenance + relapse prevention)

**Validation**
- Any "timeline promise" must be supported or softened.
- If unsupported: "Many people notice early wins in 1–2 weeks" (attribution/hypothesis language).

---

## Framework 3: LEARN → DO → SHARE → TEACH (Retention + Results Engine)
**Purpose:** Prevent "content consumption" and force action + feedback.

**Steps**
1. For each module: **LEARN** (concept)
2. Immediately: **DO** (assignment with clear success criteria)
3. Then: **SHARE** (community check-in / proof of completion)
4. Then: **TEACH** (explain it back; simplifies mastery)

**Validation**
- Every LEARN must produce a DO.
- Every DO must have a pass/fail definition.

---

## Framework 4: Four-Pillar Support System (Minimum Effective Support)
**Pillars**
1. Content (lessons / playbooks)
2. Community (accountability + normalization)
3. Coaching (office hours / group calls / async feedback)
4. Resources (checklists, trackers, templates, AI prompts)

**Steps**
1. Choose the **minimum viable** version of each pillar (per capacity)
2. Bind pillars to stages (Week 1–2 must be highest support)
3. Define "support SLAs" (response windows, coaching cadence)

**Validation**
- If fewer than 3 pillars exist → flag as delivery risk.

---

## Framework 5: Tiered Offer Structure (Core → Premium → VIP)
**Purpose:** Price discrimination without confusion.

**Steps**
1. Core = complete transformation (digital + essential support)
2. Premium = accelerators (physical kit, extra calls, diagnostics)
3. VIP = proximity (1:1, implementation, concierge)

**Validation**
- No random bonuses. Every component must map to a stage + behavior.
- Each tier must clearly answer: *"Why pay more?"*

**Outputs**
- TIERED_OFFER_STRUCTURE
- PRICING_STRATEGY draft

---

## Framework 6: 72-Hour Profit-First Validation (Before You Build)
**Purpose:** Prove demand before months of production.

**Steps**
1. Create **Founding Member Offer** (limited cohort, real start date)
2. Run short demand test:
   - Outreach + waitlist + call booking / checkout
3. Success signals (examples—adjust per market):
   - ≥10% opt-in to waitlist OR
   - ≥3–10 pre-sales / deposits OR
   - ≥10 booked calls with qualified leads
4. If weak signals → refine mechanism/promise/price, retest.

**Output**
- VALIDATION_PLAN

---

## Coordination Notes (Always Produce)
At the end, output **COORDINATION_NOTES** containing:
- Canonical promise (copy-paste from MESSAGE_SPINE)
- Canonical mechanism paragraph usage rules (word-for-word requirement if specified)
- Proof pillars + where they show up in program & marketing
- Objections map (which week/asset handles which objection)
- CTA exact phrase

---

## L3 — Advanced Usage

### Smooth Transitions (Optional Module)
Use when creating program guides, onboarding sequences, or long-form lesson scripts that must "pull" the reader forward.
- End sections with a micro-open-loop ("Here's the part most people miss—")
- Pay it off immediately in the next section
- Don't overuse (feels gimmicky)

---

## FAILURE MODE PLAYBOOK (L3)

### FM1: Information Dump Program
**Detection:** >30 modules or no clear progression
**Recovery:** apply 90-day blueprint → cut to essential path → DO/SHARE/TEACH to every LEARN.

### FM2: No Support System
**Detection:** content-only
**Recovery:** enforce 4 pillars (minimum community + group coaching) → flag if <3 pillars.

### FM3: Unrealistic Timelines
**Detection:** timelines not supported by EVIDENCE_PACK
**Recovery:** soften claims → show effort → add attribution language → compliance check.

### FM4: Feature-Dump Bundle
**Detection:** bundle items don't map to stages
**Recovery:** map each item to a stage/behavior → remove non-serving items → validate synergy.

### FM5: Building Before Validating
**Detection:** heavy build with no sales signal
**Recovery:** STOP → run 72-hour validation → only build Week 1 onboarding until validated.

### FM6: Selling "AI" Instead of Outcomes
**Detection:** AI is positioned as the product
**Recovery:** outcome-first framing → AI as acceleration → mechanism clarity before AI mention.

### FM7: Launch Obsession, Delivery Neglect
**Detection:** weak first-week experience
**Recovery:** build First 7-Day Onboarding Blueprint → daily touchpoints for 7 days → track completion.

---

## L4 — Technical Spec (Schemas + Enforcement)

### SSOT Required Fields
**PROJECT_BRIEF must include**
- project_id, asset_id, version, owner_agent, date
- nonnegotiables (claims_limits, compliance, brand_donts)
- tone_controls (warmth/authority/humor/urgency/mystique)

**MESSAGE_SPINE must include**
- promise_1liner
- mechanism_paragraph_canonical (if locked)
- proof_pillars (max 3)
- objections (max 5) + counters
- CTA frame (primary phrase)

### Output Schemas (Minimal)
```yaml
PROGRAM_ARCHITECTURE:
  format: markdown
  required_sections:
    - program_overview
    - delivery_model
    - weekly_map (weeks 1-12)
    - support_system (4 pillars)
    - onboarding_week_1
    - metrics_and_completion

TIERED_OFFER_STRUCTURE:
  format: yaml_or_markdown
  required_fields:
    - tiers: [core, premium, vip]
    - price_points
    - inclusions_mapped_to_stages
    - tier_differentiators

TRANSFORMATION_MAP:
  format: yaml_or_markdown
  required_fields:
    - identity_shift
    - stages (breakthrough/milestones/integration)
    - metrics_per_stage
    - proof_pillars_placement
```

### MMA Evaluation Hooks
- Proof discipline: any timeline claim must cite EVIDENCE_PACK or be framed as hypothesis.
- CTA integrity: one consistent CTA phrase passed downstream.
- Ethics: no fake urgency; no guaranteed outcomes unless evidence supports.
