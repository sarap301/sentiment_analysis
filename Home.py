import streamlit as st
import pandas as pd
import plotly.express as px
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    kpi_card,
    section_title,
    footer
)
 
 
# ============================================================
# CONFIG
# ============================================================
 
st.set_page_config(
    page_title="Tata Motors EV Customer Intelligence",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
apply_theme()
 
 
# ============================================================
# DATA
# ============================================================
 
kpis = pd.read_csv("kpis.csv")
theme_ranking = pd.read_csv("theme_ranking.csv")
summary = pd.read_csv("dashboard_summary.csv")
 
 
# ============================================================
# SIDEBAR
# ============================================================
 
with st.sidebar:
 
    st.markdown(
        """
        <div style="
            font-size:25px;
            font-weight:800;
            margin-bottom:5px;
        ">
            🚗 TATA MOTORS
        </div>
 
        <div style="
            font-size:14px;
            opacity:0.85;
            margin-bottom:25px;
        ">
            EV Customer Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )
 
    st.markdown("---")
 
    st.markdown(
        """
        <div style="
            font-size:13px;
            font-weight:700;
            letter-spacing:0.8px;
            margin-bottom:8px;
        ">
            DASHBOARD
        </div>
        """,
        unsafe_allow_html=True
    )
 
    st.markdown(
        """
        Explore customer conversations across
        WhatsApp and Telegram EV communities.
 
        <br>
 
        <b>Analytics powered by</b>
 
        <br><br>
 
        • BERTopic<br>
        • Sentence Transformers<br>
        • Gemini AI
        """,
        unsafe_allow_html=True
    )
 
    st.markdown("---")
 
    st.markdown(
        """
        <div style="
            font-size:12px;
            opacity:0.75;
            line-height:1.6;
        ">
        Customer Intelligence<br>
        Business Themes<br>
        Pain Points<br>
        Feature Requests<br>
        Opportunities<br>
        Sentiment
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# ============================================================
# BRAND HEADER
# ============================================================
 
show_brand_header()
 
 
# ============================================================
# HERO
# ============================================================
 
st.markdown(
    """
    <div style="
        padding:10px 0px 22px 0px;
    ">
 
        <h1 style="
            font-size:38px;
            margin-bottom:5px;
        ">
            🚗 EV Customer Intelligence
        </h1>
 
        <p style="
            font-size:17px;
            color:#627D98;
            max-width:850px;
        ">
            Turning real-world EV community conversations into
            actionable customer, product and business insights.
        </p>
 
    </div>
    """,
    unsafe_allow_html=True
)
 
 
# ============================================================
# SOURCES
# ============================================================
 
st.markdown(
    """
    <div class="source-row">
 
        <span class="source-badge">
            💬 WhatsApp EV Communities
        </span>
 
        <span class="source-badge">
            ✈️ Telegram EV Communities
        </span>
 
        <span class="source-badge">
            🤖 AI-Powered Analysis
        </span>
 
    </div>
    """,
    unsafe_allow_html=True
)
 
 
# ============================================================
# KPI SECTION
# ============================================================
 
section_title(
    "Customer Intelligence at a Glance",
    "A high-level view of the conversations analysed and business themes identified."
)
 
c1, c2, c3 = st.columns(3)
 
with c1:
 
    kpi_card(
        "Messages Analysed",
        f"{int(kpis.iloc[0]['Value']):,}",
        "Customer conversations processed"
    )
 
with c2:
 
    kpi_card(
        "Business Categories",
        f"{int(kpis.iloc[1]['Value']):,}",
        "Consolidated customer discussion areas"
    )
 
with c3:
 
    kpi_card(
        "Major Business Themes",
        f"{int(kpis.iloc[2]['Value']):,}",
        "Themes surfaced through AI analysis"
    )
 
 
st.markdown("<br>", unsafe_allow_html=True)
 
 
# ============================================================
# TOP THEMES
# ============================================================
 
section_title(
    "What Are Customers Talking About?",
    "The most prominent business themes identified across EV community conversations."
)
 
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
 
fig.update_traces(
    marker_color="#1F3A5F"
)
 
fig.update_layout(
    template="plotly_white",
    height=480,
    margin=dict(l=10, r=20, t=20, b=20),
    xaxis_title="Number of Messages",
    yaxis_title="",
    showlegend=False,
    font=dict(
        family="Arial",
        color="#102A43"
    )
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
# ============================================================
# EXECUTIVE INSIGHTS
# ============================================================
 
section_title(
    "Executive View",
    "AI-generated summaries of the most significant customer discussion areas."
)
 
for _, row in summary.head(5).iterrows():
 
    st.markdown(
        f"""
        <div class="insight-card">
 
            <div class="insight-title">
                {row['short_theme']}
            </div>
 
            <div class="insight-text">
                {row['executive_summary']}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# ============================================================
# FOOTER
# ============================================================
 
footer()
