# Golden Run: Outbound Value Fast Track v0.1

## Purpose
This document defines the "golden run" scenario for Outbound Value Fast Track v0.1 — the expected behavior when the system executes correctly end-to-end.

---

## Inputs (Fixtures)

### Required
- **artifact.project_brief.v0_1**: Use `/freedomation/tests/fixtures/artifact.project_brief.v0_1.example.yaml`

### Optional
- **artifact.prospect_snapshot.v0_1**: Use `/freedomation/tests/fixtures/artifact.prospect_snapshot.v0_1.example.yaml`
  - Can also generate from prospect list if using n1 node

---

## Expected Workflow Execution

### Mode: `trial_surface`
Fast iteration mode for testing (3 touchpoints, 5 prospects max)

### Node Sequence:
1. **n1_prospect_research** (KB-002)
   - Input: project_brief + prospect_snapshot
   - Output: persona_map (should identify "Ambitious Builder" archetype)

2. **n2_value_offer_design** (KB-006)
   - Input: persona_map + project_brief
   - Output: value_offer (should map AI expertise → "ship AI features fast" outcome)

3. **n3_asset_selection** (KB-005)
   - Input: value_offer + persona_map
   - Output: asset_choice (likely: "AI Implementation Roadmap" guide)

4. **n4_outreach_sequence** (KB-004)
   - Input: value_offer + asset_choice + persona_map + prospect_snapshot
   - Output: outreach_sequence (3 touchpoints in trial mode)

5. **n5_community_invitation** (KB-009)
   - Input: outreach_sequence + persona_map
   - Output: invitation_script (permission-based community invite)

6. **n6_resonance_dashboard** (KB-010)
   - Input: outreach_sequence + invitation_script
   - Output: resonance_dashboard (metrics structure, no actual data yet)

---

## Expected Outputs

### 1. artifact.outreach_sequence.v0_1

**Structure:**
```yaml
sequence_name: "Series A SaaS AI Implementation - Cold"
touchpoints:
  - touchpoint_number: 1
    channel: "email"
    timing: "Day 0 (immediate)"
    subject_line: "Quick framework for hypergrowth hiring" # ≤60 chars
    body: |
      Hi Sarah,

      I saw TechFlow just raised $15M (congrats). Your post about
      maintaining culture while doubling the team really resonated.

      I put together a 2-page framework on hypergrowth onboarding
      that cuts ramp time by ~40%. It's based on 12 companies that
      went from 20 → 100+ engineers.

      If that sounds helpful, I'd be happy to send it over—no strings attached.

      Either way, best of luck with the scaling!
    cta: "Want me to send it?"
    intent: "Intro + value demo"
```

**Quality Expectations:**
- Subject line ≤ 60 characters
- 2-3 short paragraphs
- Personalization based on observable facts only (LinkedIn post, funding announcement)
- Permission-based CTA (no pressure)
- No fake urgency or scarcity

### 2. artifact.invitation_script.v0_1

**Structure:**
```yaml
invitation_type: "community_join"
invitation_message: |
  I run a small community of SaaS VPs navigating this exact stage
  (Series A-B, 20-100 eng). We share what's working, what's not,
  and occasionally do group problem-solving sessions.

  If that sounds valuable, you're welcome to join—just reply
  "interested" and I'll send the Slack invite.
value_proposition: "Direct Q&A with people 6 months ahead of you + our shared hypergrowth playbook"
opt_in_mechanism: "Reply 'interested'"
```

**Quality Expectations:**
- Warm but professional tone
- Clear value proposition
- Permission-based ("you're welcome", not "you must")
- Easy opt-in mechanism

### 3. artifact.resonance_dashboard.v0_1

**Structure:**
```yaml
campaign_id: "outbound_value_fast_track_v0_1_trial"
tracking_period: "2025-12-13 to 2025-12-31"
metrics:
  outreach_volume:
    total_sent: 0  # not executed yet, just structure
    total_delivered: 0
  resonance_indicators:
    thoughtful_replies: 0
    conversation_threads: 0
```

**Quality Expectations:**
- All metric fields present
- Structure validates against schema
- Ready to receive actual execution data

---

## Gate Validation

### gate.ethics_integrity.v0_1

**MUST PASS for:**
- `artifact.outreach_sequence.v0_1`
- `artifact.invitation_script.v0_1`

**Validation checks:**
- ❌ No fake urgency ("only 3 spots left!")
- ❌ No fake scarcity ("exclusive group of 10")
- ❌ No shame tactics ("if you're still struggling")
- ❌ No pressure CTAs ("claim your spot now")
- ✅ Truth-only personalization (only observable facts)
- ✅ Permission-based CTAs ("if this resonates...")

### gate.deliverability.v0_1

**MUST PASS for:**
- `artifact.outreach_sequence.v0_1`

**Validation checks:**
- ✅ Subject line ≤ 60 characters
- ✅ Short paragraphs (2-3 lines max)
- ✅ Single CTA per message
- ✅ Plain text safe (no excessive caps, punctuation)
- ❌ No spam triggers

---

## PASS Criteria

The golden run **PASSES** if:

1. **All nodes execute without errors**
   - Each node produces expected artifact types
   - No missing inputs or broken references

2. **All gates pass on first attempt**
   - Ethics gate: 0 violations
   - Deliverability gate: 0 violations
   - No FIX loop needed

3. **Output artifacts validate against schemas**
   - All required fields present
   - Types match schema definitions
   - Artifact IDs match expected values

4. **Personalization is truth-only**
   - All prospect details come from fixture (observable facts)
   - No invented assumptions or fabricated details

5. **Tone is on-brand**
   - Direct and technical, but warm
   - No hype or buzzwords
   - Supportive without being clinical

6. **CTAs are permission-based**
   - Every CTA is an invitation, not demand
   - Easy opt-out implicit
   - No guilt or pressure language

---

## FAIL Criteria

The golden run **FAILS** if:

1. **Any gate fails**
   - Ethics violations detected
   - Deliverability issues found
   - QA report generated

2. **Artifacts don't validate**
   - Missing required fields
   - Type mismatches
   - Schema validation errors

3. **Personalization is invented**
   - Details not from fixture
   - Assumptions about prospect

4. **Manipulation detected**
   - Fake urgency/scarcity
   - Shame or fear tactics
   - Pressure CTAs

---

## Future Enhancements

**v0.2 Golden Run will include:**
- Full `full_deep` mode execution (7 touchpoints)
- Multi-prospect scenario (5+ prospects)
- Actual gate failure + FIX loop test
- Performance benchmarks (execution time per node)

---

**Status:** v0.1 (Draft)
**Last Updated:** 2025-12-13
