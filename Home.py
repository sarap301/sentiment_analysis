import streamlit as st
import pandas as pd
import plotly.express as px
 
from utils.theme import (
    apply_theme,
    brand_header,
    source_badges,
    section_header,
    kpi_card,
    footer
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
            font-size:13px;
            opacity:0.8;
            margin-bottom:20px;
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
        **Explore**
 
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
 
    st.markdown(
        """
        **Analytics Engine**
 
        🧠 BERTopic  
        🔎 Sentence Transformers  
        ✨ Gemini AI
        """
    )
 
 
# =========================================================
# HEADER
# =========================================================
 
brand_header()
 
source_badges()
 
st.markdown(
    """
    <div style="
        color:#4b5563;
        font-size:16px;
        line-height:1.7;
        margin-bottom:25px;
    ">
        An AI-powered analysis of EV customer conversations
        to uncover <b>customer needs, emerging themes,
        product expectations and business opportunities.</b>
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
        "CUSTOMER MESSAGES ANALYSED",
        f"{int(kpis.iloc[0]['Value']):,}"
    )
 
with c2:
 
    kpi_card(
        "BUSINESS CATEGORIES",
        f"{int(kpis.iloc[1]['Value']):,}"
    )
 
with c3:
 
    kpi_card(
        "MAJOR BUSINESS THEMES",
        f"{int(kpis.iloc[2]['Value']):,}"
    )
 
 
# =========================================================
# TOP THEMES
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
    orientation="h"
)
 
fig.update_layout(
    height=500,
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Number of Messages",
    yaxis_title="",
    showlegend=False,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
# =========================================================
# EXECUTIVE SUMMARY
# =========================================================
 
section_header("Executive Business Summary")
 
for _, row in summary.head(5).iterrows():
 
    st.markdown(
        f"""
        <div class="info-card">
 
            <div class="info-title">
                {row['short_theme']}
            </div>
 
            <div class="info-text">
                {row['executive_summary']}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# =========================================================
# WHAT THE DASHBOARD DELIVERS
# =========================================================
 
section_header("What This Dashboard Identifies")
 
c1, c2, c3, c4 = st.columns(4)
 
with c1:
 
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">Customer Needs</div>
            <div class="info-text">
                Identifies recurring customer pain points
                and unmet expectations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
 
with c2:
 
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">Product Requests</div>
            <div class="info-text">
                Surfaces features and improvements
                customers are asking for.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
 
with c3:
 
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">Business Opportunities</div>
            <div class="info-text">
                Converts customer discussions into
                actionable business opportunities.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
 
with c4:
 
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">Customer Sentiment</div>
            <div class="info-text">
                Measures the overall tone of conversations
                across major themes.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# =========================================================
# FOOTER
# =========================================================
 
footer()
