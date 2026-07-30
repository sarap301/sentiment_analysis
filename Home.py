import streamlit as st
import pandas as pd
import plotly.express as px
 
from utils.theme import (
    apply_theme,
    brand_header,
    source_badges,
    section_header,
    kpi_card
)
 
 
# =========================================================
# PAGE CONFIG
# =========================================================
 
st.set_page_config(
    page_title="Tata Motors EV Customer Intelligence",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
 
# =========================================================
# THEME
# =========================================================
 
apply_theme()
 
 
# =========================================================
# LOAD DATA
# =========================================================
 
kpis = pd.read_csv("kpis.csv")
theme_ranking = pd.read_csv("theme_ranking.csv")
summary = pd.read_csv("dashboard_summary.csv")
 
 
# =========================================================
# SIDEBAR
# =========================================================
 
with st.sidebar:
 
    st.markdown(
        """
        <div style="
            font-size:22px;
            font-weight:800;
            margin-bottom:5px;
        ">
        🚗 Tata Motors EV
        </div>
 
        <div style="
            font-size:12px;
            margin-bottom:25px;
        ">
        Customer Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )
 
    st.divider()
 
    st.markdown("### Dashboard Navigation")
 
    st.markdown(
        """
        Explore customer discussions through:
 
        • Executive Summary  
        • Business Themes  
        • Customer Pain Points  
        • Requested Features  
        • Business Opportunities  
        • Sentiment Analysis  
        • Subtopic Explorer  
        • Message Explorer  
        • AI Insights
        """
    )
 
    st.divider()
 
    st.markdown("### Analytics Engine")
 
    st.markdown(
        """
        🧠 BERTopic
 
        🔵 Sentence Transformers
 
        ✨ Gemini AI
        """
    )
 
    st.divider()
 
    st.caption(
        "Digital.AI Labs\n"
        "Tata Motors EV Customer Intelligence"
    )
 
 
# =========================================================
# BRANDING
# =========================================================
 
brand_header()
 
source_badges()
 
 
st.markdown(
    """
    <div style="
        font-size:16px;
        color:#526b7c;
        margin-bottom:20px;
    ">
        An AI-powered analysis of EV customer conversations
        designed to uncover customer needs, emerging themes,
        product expectations and business opportunities.
    </div>
    """,
    unsafe_allow_html=True
)
 
 
# =========================================================
# KPI SECTION
# =========================================================
 
section_header("Dashboard Overview")
 
c1, c2, c3 = st.columns(3)
 
with c1:
 
    kpi_card(
        "Customer Messages Analysed",
        f"{int(kpis.iloc[0]['Value']):,}"
    )
 
with c2:
 
    kpi_card(
        "Business Categories",
        f"{int(kpis.iloc[1]['Value']):,}"
    )
 
with c3:
 
    kpi_card(
        "Major Business Themes",
        f"{int(kpis.iloc[2]['Value']):,}"
    )
 
 
# =========================================================
# TOP BUSINESS THEMES
# =========================================================
 
section_header("What Are Customers Talking About?")
 
theme_plot = theme_ranking[
    ["short_theme", "Count"]
].copy()
 
theme_plot["short_theme"] = (
    theme_plot["short_theme"]
    .fillna("Unknown Theme")
    .astype(str)
)
 
theme_plot["Count"] = pd.to_numeric(
    theme_plot["Count"],
    errors="coerce"
)
 
theme_plot = (
    theme_plot
    .dropna(subset=["Count"])
    .sort_values("Count", ascending=False)
    .head(10)
)
 
fig = px.bar(
    theme_plot,
    x="Count",
    y="short_theme",
    orientation="h",
    text="Count"
)
 
fig.update_traces(
    marker_color="#003b67",
    textposition="outside"
)
 
fig.update_layout(
    height=500,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Customer Messages",
    yaxis_title="",
    showlegend=False,
    margin=dict(l=10, r=40, t=20, b=20)
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
# =========================================================
# EXECUTIVE SUMMARY
# =========================================================
 
section_header("Executive Summary")
 
for _, row in summary.head(5).iterrows():
 
    with st.container(border=True):
 
        c1, c2 = st.columns([5, 1])
 
        with c1:
 
            st.markdown(
                f"### {row['short_theme']}"
            )
 
            st.write(
                row["executive_summary"]
            )
 
        with c2:
 
            st.metric(
                "Messages",
                f"{int(row['Count']):,}"
            )
 
            st.caption(
                row["dashboard_sentiment"]
            )
 
 
# =========================================================
# AI TAKEAWAYS
# =========================================================
 
section_header("Key Customer Intelligence Takeaways")
 
c1, c2, c3 = st.columns(3)
 
with c1:
 
    st.info(
        "**Customer Needs**\n\n"
        "Charging reliability and charging "
        "availability are major discussion areas."
    )
 
with c2:
 
    st.warning(
        "**Product Expectations**\n\n"
        "Customers frequently discuss infrastructure, "
        "pricing and connected EV experiences."
    )
 
with c3:
 
    st.success(
        "**Business Opportunity**\n\n"
        "Community conversations reveal opportunities "
        "for infrastructure, service and digital improvements."
    )
