# Trust Tiers & Certification (v0.1)

## Why Trust Tiers?

In an ecosystem of AI-generated workflows and content, **trust** is the foundation. Users need to know:
- Is this KB reliable?
- Has this flowgram been tested?
- Can I trust this SNAPP for production use?

**Trust Tiers** provide a standardized framework for evaluating and certifying Freedomation components (KBs, Flowgrams, SNAPPS, Runtimes).

**Core Principle:** Trust is earned through testing, validation, and independent review — not claimed.

---

## 1) Trust Tier Levels

### Tier 0: Draft
**Status:** Experimental, work in progress
**Testing:** Minimal or none
**Use Case:** Personal experimentation, early development

**Characteristics:**
- No formal review
- May contain errors or incomplete sections
- Status: `draft` in metadata

**Label:** 🟡 Draft

**Example:**
- A newly created KB that hasn't been tested yet
- A flowgram sketch with placeholder nodes

### Tier 1: Stable
**Status:** Functional, tested internally
**Testing:** Author has tested in realistic scenarios
**Use Case:** Internal use, team workflows, low-risk applications

**Characteristics:**
- Basic quality checks passed
- Works as documented in standard scenarios
- Status: `stable` in metadata

**Label:** 🟢 Stable

**Example:**
- A KB that's been used successfully in 5+ runs
- A flowgram that produces expected outputs consistently

### Tier 2: Verified
**Status:** Independently reviewed
**Testing:** Peer review + automated validation
**Use Case:** Production use, client-facing work

**Characteristics:**
- Reviewed by someone other than the author
- Passes automated compliance checks
- Documented edge cases and limitations
- Credibility: `verified` in metadata

**Label:** 🔵 Verified

**Example:**
- A KB reviewed by a domain expert
- A flowgram that passes the Freedomation test suite

### Tier 3: Certified
**Status:** Meets Freedomation certification standards
**Testing:** Formal certification process, rigorous testing
**Use Case:** Mission-critical workflows, regulated industries, high-stakes applications

**Characteristics:**
- Passes Freedomation Certification Suite
- Security audit (if applicable)
- Performance benchmarks documented
- Maintenance commitment (versioning, support)
- Credibility: `certified` in metadata

**Label:** ⭐ Certified

**Example:**
- A SNAPP certified for healthcare compliance
- A runtime certified as Freedomation-compliant

---

## 2) Trust Progression Path

Components should progress through tiers sequentially:

```
Draft (0) → Stable (1) → Verified (2) → Certified (3)
```

**You cannot skip tiers.** A component must be Stable before it can be Verified.

### Promotion Criteria

**Draft → Stable:**
- Component is feature-complete
- Author has tested in realistic scenarios
- Documentation is complete (inputs, outputs, process, examples)
- No known critical bugs

**Stable → Verified:**
- Independent peer review completed
- Passes automated validation (schema checks, gate compliance)
- Edge cases documented
- At least 10 successful production runs (for flowgrams)

**Verified → Certified:**
- Formal certification application submitted
- Passes Freedomation Certification Suite
- Security/compliance audit (if applicable)
- Maintenance commitment established

### Demotion
Components can be demoted if:
- Critical bugs discovered
- Doctrine violations found (e.g., manipulation tactics)
- Dependencies break
- Maintenance abandoned

**Example:** A Certified KB is found to contain fabricated claims → demoted to Draft → removed from registry

---

## 3) CSI Credibility Score (v0.1 Placeholder)

**CSI** = **Credibility, Safety, Integrity**

The CSI score is a **future enhancement** for quantifying component trustworthiness. In v0.1, it's a placeholder concept.

### Proposed Dimensions (v0.2+)

**Credibility (0-100):**
- Author reputation
- Number of successful runs
- Peer review scores
- Community feedback

**Safety (0-100):**
- Security audit results
- Error rate in production
- Rollback frequency
- Incident count

**Integrity (0-100):**
- Doctrine compliance (Agentic Resonance)
- Gate pass rate
- Transparency (open source, documented)

### CSI Calculation (Placeholder)
```
CSI = (Credibility × 0.4) + (Safety × 0.3) + (Integrity × 0.3)
```

**Example:**
- Credibility: 85 (author has 50+ certified components)
- Safety: 90 (zero incidents in 1000 runs)
- Integrity: 95 (100% gate pass rate, open source)
- **CSI = 89** (High trust)

### CSI Thresholds (Proposed)
- **CSI < 40:** ❌ Not recommended
- **CSI 40-69:** 🟡 Use with caution
- **CSI 70-84:** 🟢 Reliable
- **CSI 85-100:** ⭐ Highly trusted

**Note:** CSI is aspirational in v0.1. Current trust system uses tiers only.

---

## 4) Component-Specific Certification

### Knowledge Blocks (KBs)
**Certification Criteria:**
- Follows KB template exactly (`02_KB_SPEC_GOVERNANCE.md`)
- All required metadata present
- At least 3 concrete examples
- Tested in 10+ real-world scenarios
- Peer-reviewed by domain expert
- No doctrine violations

### Flowgrams
**Certification Criteria:**
- All nodes reference Stable+ KBs
- All artifact schemas defined
- All mandatory gates included (ethics, deliverability)
- Tested in both trial and full modes
- Passes Freedomation test suite
- Documented failure modes and recovery procedures

### SNAPPS
**Certification Criteria:**
- All flowgrams are Verified+
- User interface (if any) passes accessibility standards
- Security audit completed (if handles user data)
- Performance benchmarks documented
- Support/maintenance plan established

### Runtimes
**Certification Criteria:**
- Implements all MUST requirements in `04_RUNTIME_CONTRACT.md`
- Passes Runtime Compliance Test Suite
- Observability features functional
- Error handling tested
- Performance benchmarks documented

---

## 5) Certification Process (Future)

**Step 1: Self-Assessment**
- Author completes certification checklist
- Runs automated validation tools
- Fixes any issues

**Step 2: Submission**
- Submit component to Freedomation Registry
- Provide test results, documentation, code (if applicable)

**Step 3: Automated Testing**
- Registry runs compliance tests
- Schema validation
- Doctrine checks (automated gate validation)

**Step 4: Peer Review**
- Assign to qualified reviewer (based on domain expertise)
- Reviewer validates claims, tests edge cases, checks documentation

**Step 5: Certification Decision**
- If passed → Certified ✅
- If failed → Feedback provided, component can be resubmitted

**Step 6: Ongoing Monitoring**
- Certified components monitored for issues
- Periodic re-certification (annually)

---

## 6) Trust Metadata

Every component should declare trust metadata:

### KB Example
```markdown
# KB-001: Draft Email Content

**Version:** 1.0.0
**Status:** stable
**Credibility:** verified
**Risk:** low
**CSI Score:** N/A (v0.1)
```

### Flowgram Example
```yaml
fg_id: "outbound_value_fast_track"
version: "1.0.0"
trust_tier: "verified"
certification_date: "2025-12-13"
certified_by: "Freedomation Registry"
csi_score: null  # v0.1 placeholder
```

### SNAPP Example
```yaml
snapp_id: "outbound_value_engine"
version: "2.1.0"
trust_tier: "certified"
certification_level: "production"
security_audit: "passed"
compliance: ["GDPR", "CAN-SPAM"]
```

---

## 7) Public Registry (Future)

The **Freedomation Registry** will host:
- Certified KBs, Flowgrams, SNAPPS, Runtimes
- Trust tier badges
- CSI scores
- User reviews and ratings
- Security advisories

**Think:** npm for AI workflows + Docker Hub for SNAPPS

**URL (placeholder):** `registry.freedomation.ai`

---

## 8) Trust Badges

Components display trust badges in documentation:

**Draft:**
```markdown
![Trust Tier: Draft](https://img.shields.io/badge/trust-draft-yellow)
```

**Stable:**
```markdown
![Trust Tier: Stable](https://img.shields.io/badge/trust-stable-green)
```

**Verified:**
```markdown
![Trust Tier: Verified](https://img.shields.io/badge/trust-verified-blue)
```

**Certified:**
```markdown
![Trust Tier: Certified](https://img.shields.io/badge/trust-certified-gold)
```

---

## 9) Risk Assessment

All components must declare risk level:

### Low Risk
- Failure has minimal impact
- Easy to rollback
- No user data involved
- **Example:** KB for drafting blog post titles

### Medium Risk
- Failure causes rework or delays
- Requires manual intervention to fix
- Handles non-sensitive data
- **Example:** Flowgram for email campaigns

### High Risk
- Failure could harm users or brand
- Handles sensitive data (PII, financial)
- Regulatory compliance required
- **Example:** SNAPP for medical advice generation

**Rule:** High-risk components MUST be at least Verified tier before production use.

---

## 10) Certification Costs (Future)

**v0.1:** Certification is free (community-driven)

**v0.2+ (proposed):**
- **Draft/Stable:** Free
- **Verified:** Free (peer review volunteer-based)
- **Certified:** $99-$999 depending on complexity and risk level

**Revenue funds:**
- Registry infrastructure
- Security audits
- Certification reviewers
- Compliance tooling

---

## 11) Enforcement

**Automated:**
- Registry validates metadata
- CI/CD pipelines check trust tier requirements
- Gates flag components below minimum trust tier

**Manual:**
- Reviewers verify claims
- Community reports violations
- Freedomation team investigates complaints

**Consequences for violations:**
- Demotion to lower tier
- Removal from registry
- Author reputation penalty

---

## 12) Example: KB Trust Progression

**KB-001: Draft Email Content**

**Day 1:** Created as Draft
- Metadata: `status: draft, credibility: low, risk: low`
- Label: 🟡 Draft

**Week 2:** Tested in 5 runs, works well
- Author promotes to Stable
- Metadata: `status: stable, credibility: medium, risk: low`
- Label: 🟢 Stable

**Month 3:** Peer reviewed, 50+ successful runs
- Reviewed by content strategist, passes all checks
- Promoted to Verified
- Metadata: `status: stable, credibility: verified, risk: low`
- Label: 🔵 Verified

**Year 1:** Submitted for Certification
- Passes Freedomation test suite
- Security audit (none required, low risk)
- Promoted to Certified
- Metadata: `status: stable, credibility: certified, risk: low`
- Label: ⭐ Certified

---

## Summary

**Trust Tiers:**
- 🟡 Draft (0): Experimental
- 🟢 Stable (1): Functional, tested internally
- 🔵 Verified (2): Peer-reviewed, production-ready
- ⭐ Certified (3): Formally certified, mission-critical ready

**Progression:** Draft → Stable → Verified → Certified (no skipping)

**CSI Score:** Future enhancement (Credibility + Safety + Integrity)

**Certification:** Formal process with testing, review, and ongoing monitoring

**Registry:** Public repository of certified components (future)

**Risk:** All components must declare Low/Medium/High risk

**Enforcement:** Automated + manual, violations = demotion/removal

**Goal:** Build a trustworthy ecosystem where users can confidently adopt AI workflows.

---

**Version:** 0.1.0
**Status:** stable
**Last Updated:** 2025-12-13
