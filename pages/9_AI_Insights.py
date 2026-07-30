import streamlit as st
import pandas as pd
import ast
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    page_header,
    section_title,
    kpi_card,
    footer
)
 
 
st.set_page_config(
    page_title="AI Generated Insights",
    page_icon="🤖",
    layout="wide"
)
 
apply_theme()
 
summary = pd.read_csv(
    "business_insights.csv"
)
 
show_brand_header()
 
page_header(
    "AI Business Intelligence",
    "Gemini-generated interpretation of customer conversations and potential actions for Tata Motors."
)
 
 
# ============================================================
# THEME SELECTOR
# ============================================================
 
theme = st.selectbox(
    "Select a Business Theme",
    sorted(summary["short_theme"].dropna().unique())
)
 
 
row = summary[
    summary["short_theme"] == theme
].iloc[0]
 
 
# ============================================================
# THEME OVERVIEW
# ============================================================
 
st.markdown(
    f"""
    <div class="section-card">
 
        <h2>
            {row['short_theme']}
        </h2>
 
        <p style="
            color:#486581;
            line-height:1.7;
            font-size:15px;
        ">
            {row['executive_summary']}
        </p>
 
    </div>
    """,
    unsafe_allow_html=True
)
 
 
# ============================================================
# KPIs
# ============================================================
 
c1, c2 = st.columns(2)
 
with c1:
 
    kpi_card(
        "Messages",
        f"{int(row['Count']):,}",
        "Conversation volume"
    )
 
with c2:
 
    kpi_card(
        "Customer Sentiment",
        str(row["dashboard_sentiment"]),
        "AI-classified overall sentiment"
    )
 
 
# ============================================================
# PAIN POINTS
# ============================================================
 
section_title(
    "Customer Pain Points",
    "Problems and friction areas identified from the conversations."
)
 
for p in ast.literal_eval(row["customer_pain_points"]):
 
    st.markdown(
        f"""
        <div class="insight-card">
 
            <div class="insight-title">
                ⚠️
            </div>
 
            <div class="insight-text">
                {p}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# ============================================================
# REQUESTED FEATURES
# ============================================================
 
section_title(
    "Requested Features",
    "Product or service improvements customers are asking for."
)
 
for f in ast.literal_eval(row["requested_features"]):
 
    st.markdown(
        f"""
        <div class="insight-card"
             style="border-left-color:#527A9D;">
 
            <div class="insight-title">
                💡
            </div>
 
            <div class="insight-text">
                {f}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# ============================================================
# BUSINESS OPPORTUNITIES
# ============================================================
 
section_title(
    "Business Opportunities",
    "Potential actions Tata Motors can consider based on customer demand."
)
 
for o in ast.literal_eval(row["business_opportunities"]):
 
    st.markdown(
        f"""
        <div class="insight-card"
             style="border-left-color:#E31837;">
 
            <div class="insight-title">
                🚀
            </div>
 
            <div class="insight-text">
                {o}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
# ============================================================
# SUBTOPICS
# ============================================================
 
section_title(
    "Top Subtopics"
)
 
subtopics = ast.literal_eval(row["top_subtopics"])
 
cols = st.columns(3)
 
for i, topic in enumerate(subtopics):
 
    with cols[i % 3]:
 
        st.markdown(
            f"""
            <div style="
                background:#EAF2F8;
                border-radius:10px;
                padding:13px;
                margin-bottom:10px;
                color:#1F3A5F;
                font-weight:600;
                font-size:13px;
            ">
                {topic}
            </div>
            """,
            unsafe_allow_html=True
        )
 
 
footer()
 
