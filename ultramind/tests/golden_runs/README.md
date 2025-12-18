# Golden Runs Test Harness

## Purpose

Golden Runs are **regression tests** that prevent quality degradation after skill updates. They ensure that:
- Skill updates maintain or improve quality
- Core functionality remains deterministic
- Output standards don't drift
- Breaking changes are caught before production

---

## How Golden Runs Work

### 1. Baseline Establishment
- Run skill with canonical inputs
- Capture MMA quality scores
- Store outputs as "golden standard"
- Document expected behavior

### 2. Regression Testing
- After skill update, re-run same inputs
- Compare new MMA scores to baseline
- Check for structural/quality changes
- Flag any degradation

### 3. Status Classification
- **IMPROVED** ✅ — Scores increased, all tests pass
- **MAINTAINED** ✅ — Scores within acceptable range (±0.5)
- **DEGRADED** ⚠️ — Scores dropped, flag for review

---

## Golden Run Structure

Each golden run includes:

```yaml
GOLDEN_RUN:
  id: "GR-[SKILL]-[SCENARIO]-[##]"
  name: "[Descriptive Name]"

  # Metadata
  skill_id: "[skill being tested]"
  baseline_version: "[version]"
  baseline_date: "[YYYY-MM-DD]"

  # Inputs (canonical, do not modify)
  inputs:
    PROJECT_BRIEF_ref: "[path or inline]"
    MESSAGE_SPINE_ref: "[path or inline]"
    EVIDENCE_PACK_ref: "[path or inline]"
    task: "[exact task description]"

  # Expected Outputs
  expected_output:
    format: "[output format]"
    structure: []
    key_elements: []
    quality_benchmarks: {}

  # Pass Criteria (non-negotiable)
  pass_criteria:
    - "MMA scores all >= [threshold]"
    - "[specific quality check]"
    - "[specific compliance check]"

  # Baseline Scores
  baseline_scores:
    strategy_alignment: 0-10
    clarity_structure: 0-10
    voice_consistency: 0-10
    proof_discipline: 0-10
    neuro_resonance: 0-10
    cta_integrity: 0-10
    ethical_guardrails: 0-10
    average: 0-10
```

---

## Running Golden Runs

### Manual Execution
1. Load golden run YAML
2. Execute skill with exact inputs
3. Run MMA quality check
4. Compare scores to baseline
5. Document results

### Automated Execution (Future)
```bash
./run_golden_runs.sh [skill_id]
# Runs all golden runs for specified skill
# Outputs regression report
```

---

## When to Create a Golden Run

**Create a golden run when:**
- Launching a new production skill (establish baseline)
- Skill reaches stable quality (score ≥ 8.0 average)
- Common use case identified (represents 20%+ of usage)
- Edge case solved successfully (preserve solution)

**Minimum golden runs per skill:** 2
- One "ideal scenario" (high quality inputs)
- One "challenging scenario" (edge case or constraints)

---

## When to Update a Golden Run

**Update golden runs when:**
- Skill undergoes major version change (2.0, 3.0, etc.)
- Quality expectations change systematically
- Input schemas change (SSOT evolution)

**Do NOT update to:**
- Make failing tests pass
- Hide quality degradation
- Accommodate shortcuts

---

## Golden Run Library

This directory contains canonical test cases for all production skills:

### Email Campaign Genius
- `GR-EMAIL-WELCOME-01.yaml` — Welcome sequence for info product
- `GR-EMAIL-LAUNCH-01.yaml` — Education-first launch sequence

### Sales Page Copywriter
- `GR-SALESPAGE-B2B-01.yaml` — Short B2B SaaS page
- `GR-SALESPAGE-CONSUMER-01.yaml` — Long-form consumer health page

### Product Creation Genius
- `GR-PCG-TRANSFORMATION-01.yaml` — 90-day transformation program
- `GR-PCG-HYBRID-01.yaml` — Physical + digital hybrid offer

### Add more as skills mature...

---

## Regression Report Format

After running golden runs:

```yaml
REGRESSION_REPORT:
  skill_id: ""
  old_version: ""
  new_version: ""
  test_date: ""

  summary:
    total_runs: 0
    improved: 0
    maintained: 0
    degraded: 0

  details:
    - golden_run_id: ""
      status: "IMPROVED|MAINTAINED|DEGRADED"
      baseline_avg: 0-10
      current_avg: 0-10
      delta: +/-X.X
      notes: ""

  recommendation: "ACCEPT_UPDATE|REVIEW_DEGRADATION|ROLLBACK"
```

---

## Best Practices

1. **Deterministic Inputs** — Use the exact same inputs every time
2. **Realistic Scenarios** — Test real use cases, not artificial perfection
3. **Balanced Coverage** — Include both ideal and challenging scenarios
4. **Version Lock** — Pin baseline version clearly
5. **Document Context** — Explain why this scenario matters
6. **Update Carefully** — Only update baselines for good reasons
7. **Review Degradation** — Always investigate score drops
