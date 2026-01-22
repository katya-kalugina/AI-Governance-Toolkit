# AI Governance Toolkit

A collection of practical tools and methodologies designed to operationalize Responsible AI governance.

---

## Interactive Models

### [Balanced Risk-Quality Model](https://ai-governance-toolkit-rgcqpsvbvnfywrrmfa6tv6.streamlit.app)
[**📊 Run Interactive Simulator**](https://ai-governance-toolkit-rgcqpsvbvnfywrrmfa6tv6.streamlit.app)
### [AI Risk Assessment Calculator](ВСТАВЬТЕ_ССЫЛКУ_ОТ_STREAMLIT_ЗДЕСЬ)
An advanced scoring engine based on the **EDPB SPE 2025** guidelines. It features automated "Stopper Rules" for protecting absolute rights and provides a deterministic probability/severity heatmap.

This component operationalizes a socio-technical approach to AI Governance, focusing on the equilibrium between risk mitigation and performance quality.

- **Project Overview:** A computational model designed to visualize and analyze the trade-offs between diverse AI trustworthiness characteristics. In contrast to traditional governance frameworks that focus primarily on harm mitigation, this model incorporates quality dimensions as a prerequisite for ethical AI.
- **Research Motivation:** This project argues that **suboptimal quality itself constitutes a significant systemic risk**. By utilizing a "computational lens," the model identifies the Pareto Frontier where technical reliability, operational safety, and fundamental rights reach a functional equilibrium.
- **Technical Implementation:** Based on the NIST AI RMF and ISO/IEC 25010/25059 frameworks. Developed with Python and Streamlit.

---

## Methodologies 

### [AI Risk Assessment: Impact and Likelihood Scoring](./risk-assessment/impact-and-likelihood-scores.md)

A comprehensive framework for identifying and evaluating AI risks, based on the **EDPB Support Pool of Experts (SPE) 2025** guidelines and **FRASP** protocol.

- **Objective Risk Evaluation:** A structured methodology for assessing the probability and severity of risks in AI systems.
- **Probability Assessment:** Evaluates 7 key factors including frequency of use, system robustness, and data quality.
- **Severity "Stopper" Rules:** Implements automated high-level risk classification for violations of absolute rights (e.g., human dignity, right to life).
- **Compliance Alignment:** Tailored for the specificities of General Purpose AI (GPAI) and LLMs.

--
*Developed by Ekaterina Kalugina. Part of ongoing research into operationalizing Responsible AI.*
