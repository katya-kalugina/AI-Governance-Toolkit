# AI Risk Assessment: Impact and Likelihood Scoring

This scoring methodology is designed to operationalize the EDPB SPE Programme guidelines (2025) and the FRASP framework for LLMs.

---

## 1. Probability (Likelihood)

The probability of a risk materializing is calculated as the average of **7 key criteria**. Each criterion is scored on a scale of **1 to 4**.

### Probability Levels Definitions

| Level | Score Range | Label | Definition |
| :--- | :--- | :--- | :--- |
| **1** | 1.0 - 1.5 | **Unlikely** | No evidence of such a risk materializing. |
| **2** | 1.6 - 2.5 | **Low** | Low probability; typically occasional or non-critical use. |
| **3** | 2.6 - 3.5 | **High** | Substantial probability; frequent or important operations. |
| **4** | 3.6 - 4.0 | **Very High** | High probability; continuous or critical real-time operations. |

### Probability Evaluation Table

| # | Criterion | Score 1 (Unlikely) | Score 2 (Low) | Score 3 (High) | Score 4 (Very High) |
| :-- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Frequency of Use** | Rare/infrequent (annual or less) | Occasional interactions (monthly) | Frequent use (weekly) | Continuous/Critical (daily) |
| **2** | **Exposure to High-Risk** | Not used in high-risk scenarios | Moderately sensitive; minimal stakes | High-stakes; significant impact | Highly sensitive (e.g. healthcare) |
| **3** | **Historical Precedents** | No known failures | Few instances of failure | Frequent failures in comparable systems | Frequent and significant failures |
| **4** | **Environmental Factors** | Stable conditions | Manageable occasional shifts | Vulnerable to external conditions | Constant high-risk conditions |
| **5** | **System Robustness** | Highly robust; redundancies | Moderately robust; some gaps | Significant vulnerabilities | Lacks robustness; prone to failure |
| **6** | **Data Quality & Integrity** | High accuracy; unbiased | Mostly accurate; minor biases | Partially accurate; inconsistencies | Significant inaccuracies/bias |
| **7** | **Human Oversight** | Highly trained; effective | Moderately trained; some errors | Undertrained; regular errors | Untrained; frequent severe errors |

**Formula:** `Probability Level = Round ( Sum of Scores / 7 )`

---

## 2. Severity (Impact)

Severity measures the impact on the rights and freedoms of natural persons.

### THE STOPPER RULE
> **Important:** According to the EDPB methodology, if any of the criteria **1, 2, 3, 4, 5, 7, or 8** are assessed at **Level 4**, the final severity score is immediately set to **Level 4 (Very Significant)** regardless of other scores.

### Severity Levels Definitions

| Level | Label | Description |
| :--- | :--- | :--- |
| **1** | **Very Limited** | Moderate or minor prejudices. Effects are reversible and temporary. |
| **2** | **Limited** | Serious harm. Temporary degradation of dignity or integrity. Reversible. |
| **3** | **Significant** | Critical harm. Significant degradation of rights. Difficult to reverse. |
| **4** | **Very Significant** | **Catastrophic harm.** Irreversible consequences; deprivation of life or dignity. |

### Detailed Severity Evaluation Table

| # | Criterion | Level 1 (Very Limited) | Level 2 (Limited) | Level 3 (Significant) | Level 4 (Very Significant) |
| :-- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Nature of the Right** | Limited scope; routine | Requires justification | Exceptional cases | **Absolute rights (Life, Dignity)** |
| **2** | **Nature of Data** | Non-sensitive; public | Moderately sensitive | Highly sensitive | **Special Categories (Health, Bio)** |
| **3** | **Data Subject Category** | Non-vulnerable adults | Potential vulnerability | Sensitive roles (Journalists) | **Highly vulnerable (Minors)** |
| **4** | **Purpose of Processing** | Clearly legitimate | Legitimate; indirect risk | Questionable necessity | **Unlawful / Surveillance** |
| **5** | **Scale of Impact** | Individual (<100) | Small group (100 - 1k) | Multiple groups (1k - 100k) | **Widespread (>100,000 subjects)** |
| **6** | **Contextual Sensitivity** | No amplification | Moderate amplification | Significant amplification | Profoundly intensifies harm |
| **7** | **Reversibility** | Fully reversible | Reversible with effort | Difficult to reverse | **Irreversible harm** |
| **8** | **Duration of Harm** | Transient; minimal | Brief | Long-term; affects groups | **Permanent or Indefinite** |
| **9** | **Velocity** | Gradual; time to react | Moderate pace | Sudden; limited reaction | Rapid; no opportunity to stop |
| **10** | **Accountability** | Transparent; clear | Lacks full transparency | Weak mechanisms | Entirely opaque; no accountability |
| **11** | **Ripple Effects** | Isolated; contained | Minimal cascading | Notable cross-domain impact | Severe propagation across systems |

---

## 3. Risk Classification Matrix

Final Risk Level is determined by the intersection of Probability and the Highest Severity Level.

| Prob \ Sev | Very Limited (1) | Limited (2) | Significant (3) | Very Significant (4) |
| :--- | :--- | :--- | :--- | :--- |
| **Very High (4)** | Medium | High | **Very High** | **Very High** |
| **High (3)** | Low | High | **Very High** | **Very High** |
| **Low (2)** | Low | Medium | High | **Very High** |
| **Unlikely (1)** | Low | Low | Medium | **Very High** |

### Risk Treatment Requirements
- **Very High:** Deployment prohibited. Immediate fundamental redesign required.
- **High:** Substantial technical and organizational mitigations required before use.
- **Medium:** Risks must be reduced to ALARP (As Low As Reasonably Practicable).
- **Low:** Acceptable risk. Maintain documentation and regular monitoring.

---
*Source: Regulation (EU) 2024/1689 & EDPB SPE Programme (2025).*
*Formatted by Ekaterina Kalugina.*
