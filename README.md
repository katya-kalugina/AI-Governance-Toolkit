# AI Governance Toolkit

A collection of practical tools and methodologies designed to operationalize Responsible AI governance.

---

## Interactive Models

### [Risk-Quality Model v.2](https://ai-governance-toolkit-v2-rgcqpsvbvnfywrrmfa6tv6.streamlit.app)
An advanced socio-technical assessment tool that models the trade-offs between technical quality metrics (Art. 15 AI Act) and systemic safety. It identifies the "Reliability Gap" where performance degradation itself becomes a driver of systemic risk.

### [AI System Classifier](https://ai-act-compliance-navigator-g7js7fwafmpct3dwk4qtjv.streamlit.app/)
A deterministic decision-support tool for classifying AI systems under Regulation (EU) 2024/1689. It navigates through Prohibited Practices (Art. 5), High-Risk categories (Art. 6 & Annex III), and GPAI systemic risk thresholds.

### [AI Role Navigator](https://ai-role-navigator-zjcqute523oxsv6hicsnrj.streamlit.app/)
An algorithmic tool to determine the specific legal status of an entity within the AI lifecycle (Provider, Deployer, Importer, or Distributor). Includes logic for Article 25 regarding substantial modifications and branding of existing systems.

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
