# AI Risk Assessment: Impact and Likelihood Scoring

This methodology is based on the **EDPB Support Pool of Experts (SPE)** report *"AI Privacy Risks & Mitigations – Large Language Models (LLMs)"* (2025). It uses the **FRASP** framework (Functional Rights AI Assessment & Scoring Protocol) to provide a deterministic way to calculate AI risks.

---

## 1. Probability (Likelihood) Assessment

The probability of a risk materializing is evaluated across 7 dimensions. Each dimension is scored from **1 to 4**.

### Probability Levels

| Level | Range | Definition |
| :--- | :--- | :--- |
| **1 (Unlikely)** | 1.0 - 1.5 | No evidence of such a risk materializing in any case. |
| **2 (Low)** | 1.6 - 2.5 | Low probability of an event occurring. |
| **3 (High)** | 2.6 - 3.5 | Substantial probability of an event occurring. |
| **4 (Very High)** | 3.6 - 4.0 | High probability of an event occurring. |

### Evaluation Criteria

| # | Factor | Level 1 | Level 2 | Level 3 | Level 4 |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Frequency of Use** | Rare/infrequent (annual or less) | Occasional (monthly) | Frequent/integrated (weekly) | Continuous/critical (daily) |
| 2 | **Exposure to High-Risk** | Not used in high-risk scenarios | Moderately sensitive; minimal stakes | High-stakes; potential for impact | Highly sensitive/critical (e.g. healthcare) |
| 3 | **Historical Precedents** | No similar failures known | Few similar failures known | Similar failures occurred frequently | Frequent and significant failures |
| 4 | **Environmental Factors** | Stable conditions; no impact | Occasionally affect performance | Often impact performance; vulnerabilities | Severely affect performance; constant risks |
| 5 | **System Robustness** | Highly robust; redundancies | Moderately robust; some gaps | Significant vulnerabilities | Lacks robustness; prone to failure |
| 6 | **Data Quality & Integrity** | High accuracy; unbiased | Mostly accurate; minor biases | Partially accurate; inconsistencies | Significant inaccuracies; biased/incomplete |
| 7 | **Human Oversight** | Highly trained; effective | Moderately trained; occasional errors | Undertrained; regular errors | Untrained; frequent and severe errors |

**Formula:** `Probability Score = (Sum of All 7 Factors) / 7`

---

## 2. Severity (Impact) Assessment

Severity measures the harm to fundamental rights and freedoms. 

### THE "STOPPER" RULE
> **Important:** If any of the criteria **1, 2, 3, 4, 5, 7, or 8** are assessed at **Level 4**, the overall severity for that risk is immediately set to **Level 4 (Very Significant)**.

### Detailed Severity Criteria

| # | Factor | Level 1 (Very Limited) | Level 2 (Limited) | Level 3 (Significant) | Level 4 (Very Significant) |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Nature of the Right** | Highly limited scope; routine interference | Moderately limited; requires justification | Minimally limited; exceptional cases | **Absolute rights** (Dignity, Life) or severe violation |
| 2 | **Nature of Personal Data** | Non-sensitive; public records | Moderately sensitive (e.g. browsing) | Highly sensitive | **Special categories** (Health, Biometrics, Criminal) |
| 3 | **Category of Data Subject** | Non-vulnerable adults | Potential vulnerability (e.g. employees) | Sensitive roles (e.g. journalists) | **Highly vulnerable** (Minors, Persecuted groups) |
| 4 | **Purpose of Processing** | Clearly legitimate; operational | Legitimate; moderate indirect impact | Questionable necessity (e.g. credit scoring) | **Unlawful; Surveillance; Discriminatory profiling** |
| 5 | **Scale of Impact** | Small/Individual (<100) | Specific group (100 - 1k) | Multiple groups (1k - 100k) | **Widespread (>100k subjects)** |
| 6 | **Contextual Sensitivity** | Context does not amplify severity | Context moderately amplifies risk | Context significantly amplifies risk | Context profoundly intensifies harm |
| 7 | **Reversibility** | Fully reversible; minimal effort | Reversible with moderate effort | Difficult to reverse; needs high resources | **Irreversible harm; no means of recovery** |
| 8 | **Duration of Harm** | Minimal; does not persist | Brief; no long-term consequences | Considerable period; affects groups | **Permanent or indefinite effects** |
| 9 | **Velocity to Materialize** | Gradual; time for intervention | Moderate pace for correction | Sudden; limited time to react | **Rapid; no opportunity for intervention** |
| 10 | **Accountability** | Highly transparent; effective mechanisms | Basic accountability; lacks transparency | Weak accountability mechanisms | **Entirely opaque; no accountability** |
| 11 | **Ripple Effects** | No cascading effects; contained | Minimal cascading; mostly contained | Notable effects across domains | **Severe; propagate extensively across systems** |

---

## 3. Risk Evaluation Matrix

Combine the **Probability Level** and the **Highest Severity Score** to find the final Risk Level.

| Prob \ Severity | Very Limited (1) | Limited (2) | Significant (3) | Very Significant (4) |
| :--- | :--- | :--- | :--- | :--- |
| **Very High (4)** | Medium | High | **Very High** | **Very High** |
| **High (3)** | Low | High | **Very High** | **Very High** |
| **Low (2)** | Low | Medium | High | **Very High** |
| **Unlikely (1)** | Low | Low | Medium | **Very High** |

---
*Source: Isabel Barberá, SPE Programme - European Data Protection Board (EDPB), 2025.*  
*Formatted by Ekaterina Kalugina for the AI Governance Toolkit.*
