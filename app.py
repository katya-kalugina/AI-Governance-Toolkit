import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Quality Visualizer", layout="wide")

st.title("Balanced AI Governance: Risk-Quality Model")
st.markdown("""
### Operationalizing the AI Quality Matrix
This simulator demonstrates how trade-offs between **Data Quality**, **Product Quality**, and **Safety Guardrails** impact overall system trustworthiness. 
*Concept based on research by Ekaterina Kalugina, aligning with ISO/IEC 25010 and NIST AI RMF.*
""")

# --- SIDEBAR / CONTROLS ---
st.sidebar.header("🎛️ Governance & Technical Controls")

st.sidebar.subheader("1. Data Governance (ISO 25012)")
privacy_noise = st.sidebar.slider("Privacy Anonymization (Epsilon Noise)", 0.0, 1.0, 0.2, 
                                 help="Stronger privacy (noise) often reduces Data Quality/Utility.")

st.sidebar.subheader("2. Product Requirements (ISO 25059)")
robustness_opt = st.sidebar.slider("Robustness Optimization", 0.0, 1.0, 0.7, 
                                 help="Investment in technical reliability and error-handling.")

st.sidebar.subheader("3. Safety Alignment")
safety_guardrails = st.sidebar.slider("Safety Filter Strictness", 0.0, 1.0, 0.4, 
                                     help="Strict filters improve ethics but can limit 'Quality in Use' (Effectiveness).")

# --- SIMULATION LOGIC (Based on Slide 15: Interconnectivity) ---
def calculate_metrics(p_noise, robust, safe):
    # Data Quality: Noise reduces accuracy
    data_quality = max(20, 100 - (p_noise * 45))
    
    # Product Quality: Depends on robustness and data foundation
    product_quality = (robust * 60) + (data_quality * 0.4)
    
    # Quality in Use (Effectiveness): Heavily strict safety can cause 'over-alignment' and lower utility
    quality_in_use = product_quality * (1 - (safe * 0.35))
    
    # Risk Mitigation Index (The 'Safety' score)
    risk_mitigation = (p_noise * 35 + safe * 65)
    
    return data_quality, product_quality, quality_in_use, risk_mitigation

dq, pq, qiu, rm = calculate_metrics(privacy_noise, robustness_opt, safety_guardrails)

# --- DASHBOARD DISPLAY ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Data Quality", f"{dq:.0f}%")
col2.metric("Product Quality", f"{pq:.0f}%")
col3.metric("Quality in Use", f"{qiu:.0f}%")
col4.metric("Risk Mitigation", f"{rm:.0f}%", delta_color="normal")

# --- VISUALIZATION: THE PARETO FRONTIER ---
st.subheader("The Trustworthy AI Frontier (Quality vs. Risk)")
st.info("The red dot represents your current system configuration. Suboptimal quality itself constitutes a systemic risk.")

# Generate frontier curve
points = np.linspace(0.01, 1, 100)
frontier_df = pd.DataFrame({
    'RiskControl': points * 100,
    'Performance': (1 - points**1.8) * 100
})

fig = px.line(frontier_df, x='RiskControl', y='Performance', 
              labels={'RiskControl': 'Risk Mitigation (Safety) %', 'Performance': 'Performance Quality %'},
              title="Equilibrium Model: Risk-Oriented vs. Quality-Oriented Approach")

# Add current state
fig.add_scatter(x=[rm], y=[qiu], mode='markers+text', 
                marker=dict(size=20, color='red', symbol='diamond'),
                text=["Current System Balance"], textposition="top center")

st.plotly_chart(fig, use_container_width=True)

# --- RESEARCH CONTEXT ---
with st.expander("🎓 See Research Context (Socio-Technical Lens)"):
    st.write("""
    Achieving trustworthy AI requires a balance between risk-based and quality-based approaches. 
    As systems evolve, 'Quality in Use' depends on 'Product Quality', but continuous learning 
    loops create a dynamic feedback effect.
    
    **Key Dimensions Addressed:**
    - **Data Quality:** Reliability and representativeness vs. Privacy constraints.
    - **Product Quality:** Functional suitability vs. Safety-alignment trade-offs.
    - **Quality in Use:** Real-world effectiveness and human-centric outcomes.
    """)
