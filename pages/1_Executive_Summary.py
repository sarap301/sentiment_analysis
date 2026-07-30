import streamlit as st
import pandas as pd
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    page_header,
    footer
)
 
 
st.set_page_config(
    page_title="Executive Summary",
    page_icon="📊",
    layout="wide"
)
 
apply_theme()
 
summary = pd.read_csv("dashboard_summary.csv")
 
 
show_brand_header()
 
page_header(
    "Executive Summary",
    "A consolidated view of the most important customer themes and their business relevance."
)
 
 
for _, row in summary.head(10).iterrows():
 
    c1, c2 = st.columns([5, 1])
 
    with c1:
 
        st.markdown(
            f"""
            <div class="section-card">
 
                <h3>
                    {row['short_theme']}
                </h3>
 
                <p style="
                    color:#486581;
                    line-height:1.6;
                ">
                    {row['executive_summary']}
                </p>
 
                <div style="
                    margin-top:12px;
                    color:#627D98;
                    font-size:13px;
                ">
                    Customer discussion sentiment:
                    <b>{row['dashboard_sentiment']}</b>
                </div>
 
            </div>
            """,
            unsafe_allow_html=True
        )
 
    with c2:
 
        st.markdown(
            f"""
            <div class="kpi-card">
 
                <div class="kpi-label">
                    Messages
                </div>
 
                <div class="kpi-value">
                    {int(row['Count']):,}
                </div>
 
                <div class="kpi-description">
                    Conversation volume
                </div>
 
            </div>
            """,
            unsafe_allow_html=True
        )
 
 
footer()
 
