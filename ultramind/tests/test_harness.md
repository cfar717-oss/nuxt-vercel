# ULTRAMIND TEST HARNESS
## Automated Testing for Skills + MMA Validation

### Purpose
The test harness validates that skills produce compliant, high-quality outputs that pass MMA scoring thresholds.

---

## Test Structure

### 1. Golden Task Requests
Pre-defined task requests with known expected outputs.

**Location**: `tests/golden_tasks/`

**Format**:
```yaml
golden_task:
  id: "GT-001"
  name: "Supplement Sales Page - Standard Case"
  task_request:
    # Full task_request.yaml structure
  expected_outputs:
    skill_id: "sales_page_copywriter"
    min_word_count: 2000
    required_sections:
      - "headline"
      - "lead"
      - "mechanism"
      - "proof"
      - "objections"
      - "cta"
    ssot_references_required:
      - "MESSAGE_SPINE:Promise/CanonicalStatement"
      - "MESSAGE_SPINE:Mechanism/CanonicalParagraph"
      - "EVIDENCE_PACK:E01 or E02" # At least one study cited
  mma_thresholds:
    voice_adherence: 80
    clarity: 80
    compliance: 85
    coherence: 75
    overall: 80
```

---

### 2. Preflight Checks (RITES Gate)

Before running any skill, validate SSOT completeness.

**Test**: `tests/preflight_test.py` (or shell script)

**Checks**:
- [ ] PROJECT_BRIEF exists at specified path
- [ ] Required PB fields filled (no `[PLACEHOLDER]` markers)
- [ ] MESSAGE_SPINE exists and has Promise + Mechanism
- [ ] VOICE_GUIDE exists and tone dials are set
- [ ] EVIDENCE_PACK exists if task requires claims

**Pass criteria**: All SSOT objects present and complete
**Fail action**: Return missing fields list, HALT execution

---

### 3. Skill Execution Test

Run a skill with a golden task and capture output.

**Test Flow**:
```
1. Load golden task request
2. Verify preflight (RITES gate)
3. Activate skill
4. Capture output
5. Route output to MMA
6. Compare MMA scorecard to thresholds
7. Log results (pass/fail)
```

**Example Test Case**:
```yaml
test_case:
  id: "TC-001"
  skill: "sales_page_copywriter"
  golden_task: "GT-001"
  ssot_files:
    PB: "tests/fixtures/PB_Supplement_v1.xml"
    MS: "tests/fixtures/MS_Supplement_v1.xml"
    VG: "tests/fixtures/VG_Health_Authority_v1.xml"
    EP: "tests/fixtures/EP_Supplement_v1.xml"
  expected_result:
    status: "pass"
    mma_scores_above_threshold: true
    required_sections_present: true
    ssot_references_found: true
```

---

### 4. MMA Validation Test

Test MMA's ability to score outputs accurately.

**Test Fixtures**:
- `tests/fixtures/good_copy.txt` - Should score >80 all dimensions
- `tests/fixtures/voice_drift_copy.txt` - Should flag forbidden words, score <75 voice
- `tests/fixtures/ungrounded_claims_copy.txt` - Should flag compliance <75
- `tests/fixtures/unclear_copy.txt` - Should flag clarity <75

**Test**:
```
For each fixture:
1. Load fixture copy
2. Load SSOT references
3. Run MMA validation
4. Assert expected score ranges
5. Assert expected findings (e.g., "forbidden word 'miracle' detected")
```

**Pass criteria**: MMA scores match expected ranges, findings match known issues

---

### 5. SSOT Reference Validation

Verify that skill outputs reference SSOT objects correctly.

**Test**:
```
1. Run skill (e.g., sales_page_copywriter)
2. Parse output for MESSAGE_SPINE references
   - Should find Promise CanonicalStatement (verbatim or close variation)
   - Should find Mechanism CanonicalParagraph
3. Parse output for EVIDENCE_PACK references
   - Extract all factual claims
   - Match against EP claim IDs (E01, E02, T01, etc.)
   - Flag any claims not found in EP
```

**Pass criteria**:
- Promise language matches MS canonical (90%+ similarity)
- Mechanism explanation references MS canonical
- All claims map to EP IDs (or are softened probabilistic language)

---

### 6. Regression Tests

After updating a skill or SSOT schema, re-run golden tasks to ensure no breakage.

**Test Suite**: `tests/regression/`

**Run**:
```bash
# Run all golden tasks through current skill versions
# Compare outputs to baseline (previous passing outputs)
# Flag any new MMA failures or missing sections
```

**Pass criteria**: All previously passing golden tasks still pass

---

## Test Harness Implementation (Pseudo-code)

### Simple Shell Script Version

```bash
#!/bin/bash
# tests/run_test.sh

TASK_FILE=$1
SKILL_ID=$2

echo "Running test: $TASK_FILE with skill: $SKILL_ID"

# 1. Preflight check
python tests/preflight_check.py $TASK_FILE
if [ $? -ne 0 ]; then
  echo "PREFLIGHT FAILED - SSOT incomplete"
  exit 1
fi

# 2. Run skill (simulated - in real system this would call skill executor)
echo "Activating skill: $SKILL_ID"
# python ultramind/execute_skill.py --skill $SKILL_ID --task $TASK_FILE > output.txt

# 3. Run MMA validation
echo "Running MMA validation"
# python ultramind/mma_validator.py --input output.txt --ssot ssot/instances/ > mma_scorecard.yaml

# 4. Check thresholds
echo "Checking MMA thresholds"
python tests/check_thresholds.py mma_scorecard.yaml golden_tasks/$TASK_FILE

if [ $? -eq 0 ]; then
  echo "TEST PASSED"
else
  echo "TEST FAILED - See mma_scorecard.yaml for details"
  exit 1
fi
```

---

### Python Test Framework Version

```python
# tests/test_skills.py

import pytest
import yaml
from ultramind.executor import execute_skill
from ultramind.mma import validate_output

def load_golden_task(task_id):
    with open(f'tests/golden_tasks/{task_id}.yaml') as f:
        return yaml.safe_load(f)

def load_ssot(file_path):
    # Load and parse SSOT XML
    pass

@pytest.mark.parametrize("task_id", [
    "GT-001",  # Supplement sales page
    "GT-002",  # Email sequence
    "GT-003",  # Offer development
])
def test_golden_tasks(task_id):
    # Load golden task
    golden = load_golden_task(task_id)

    # Preflight check
    assert preflight_check(golden['task_request']['ssot_references'])

    # Execute skill
    output = execute_skill(
        skill_id=golden['expected_outputs']['skill_id'],
        task_request=golden['task_request']
    )

    # MMA validation
    scorecard = validate_output(output, golden['task_request']['ssot_references'])

    # Assert thresholds
    thresholds = golden['mma_thresholds']
    assert scorecard['voice_adherence'] >= thresholds['voice_adherence']
    assert scorecard['clarity'] >= thresholds['clarity']
    assert scorecard['compliance'] >= thresholds['compliance']
    assert scorecard['coherence'] >= thresholds['coherence']
    assert scorecard['overall'] >= thresholds['overall']

    # Assert required sections present
    for section in golden['expected_outputs']['required_sections']:
        assert section in output['sections']

def preflight_check(ssot_refs):
    """Verify SSOT objects exist and are complete"""
    # Implementation
    return True
```

---

## Test Fixtures Needed

Create these sample SSOT files in `tests/fixtures/`:

1. **PB_Supplement_v1.xml** - Complete PROJECT_BRIEF for supplement offer
2. **MS_Supplement_v1.xml** - Complete MESSAGE_SPINE for supplement
3. **VG_Health_Authority_v1.xml** - Complete VOICE_GUIDE (health/authority voice)
4. **EP_Supplement_v1.xml** - Complete EVIDENCE_PACK (10+ testimonials, 3+ studies)

5. **good_copy.txt** - Sales page that should score 85+ on all MMA dimensions
6. **voice_drift_copy.txt** - Copy with forbidden words, hype tone (should score <75 voice)
7. **ungrounded_claims_copy.txt** - Copy with claims not in EP (should score <75 compliance)
8. **unclear_copy.txt** - Copy with long sentences, jargon (should score <75 clarity)

---

## Running Tests

### Initial Setup
```bash
# 1. Create test fixtures
cd /home/user/nuxt-vercel/ultramind/tests
mkdir -p fixtures golden_tasks results

# 2. Add golden tasks (GT-001.yaml, GT-002.yaml, etc.)

# 3. Add SSOT fixtures (PB_Supplement_v1.xml, etc.)
```

### Run Single Test
```bash
# Test one skill with one golden task
./run_test.sh GT-001 sales_page_copywriter
```

### Run Full Suite
```bash
# Test all skills with all golden tasks
pytest tests/test_skills.py -v
```

### Check Results
```bash
# View MMA scorecard
cat tests/results/GT-001_mma_scorecard.yaml

# View Delta Log (patch recommendations)
cat tests/results/GT-001_delta_log.yaml
```

---

## Success Criteria

A skill passes testing if:
- [ ] Preflight check passes (SSOT complete)
- [ ] Output contains all required sections
- [ ] MMA scores meet or exceed thresholds (typically 75-85 per dimension)
- [ ] All factual claims map to EvidencePack IDs
- [ ] No critical compliance violations flagged
- [ ] Regression tests pass (no previously passing tasks now fail)

---

## Continuous Improvement

After each test run:
1. Review failed tests - why did MMA flag issues?
2. Update skill L2/L3 layers to address gaps
3. Add new edge cases discovered
4. Refine MMA scoring logic if false positives/negatives
5. Re-run regression suite
6. Document patterns in skill examples

---

## Next Steps

1. Create 3-5 golden tasks (covering main use cases)
2. Build SSOT fixtures (1 complete set)
3. Implement basic preflight check script
4. Manually run one skill → capture output → manually score with MMA criteria
5. Automate scoring logic
6. Expand test coverage
