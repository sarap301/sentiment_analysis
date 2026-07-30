import streamlit as st
import pandas as pd
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    page_header,
    section_title,
    footer
)
 
 
st.set_page_config(
    page_title="Business Opportunities",
    page_icon="🚀",
    layout="wide"
)
 
apply_theme()
 
opp = pd.read_csv("business_opportunities.csv")
 
show_brand_header()
 
page_header(
    "Business Opportunities",
    "Translate customer conversations into actionable opportunities for Tata Motors."
)
 
 
theme = st.selectbox(
    "Select a Business Theme",
    sorted(opp["Theme"].dropna().unique())
)
 
 
filtered = opp[
    opp["Theme"] == theme
]
 
 
section_title(
    "Opportunity Areas",
    f"Potential business actions identified from {theme}."
)
 
 
for _, row in filtered.iterrows():
 
    st.markdown(
        f"""
        <div class="insight-card"
             style="border-left-color:#E31837;">
 
            <div class="insight-title">
                🚀 Business Opportunity
            </div>
 
            <div class="insight-text">
                {row['Business_Opportunity']}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
footer()
