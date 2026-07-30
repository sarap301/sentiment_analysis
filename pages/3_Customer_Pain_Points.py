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
    page_title="Customer Pain Points",
    page_icon="⚠️",
    layout="wide"
)
 
apply_theme()
 
pain = pd.read_csv("pain_points.csv")
 
show_brand_header()
 
page_header(
    "Customer Pain Points",
    "Understand the friction points customers repeatedly discuss in EV communities."
)
 
 
theme = st.selectbox(
    "Select a Business Theme",
    sorted(pain["Theme"].dropna().unique())
)
 
 
filtered = pain[
    pain["Theme"] == theme
]
 
 
section_title(
    "Identified Customer Friction",
    f"Pain points associated with {theme}."
)
 
 
for _, row in filtered.iterrows():
 
    st.markdown(
        f"""
        <div class="insight-card">
 
            <div class="insight-title">
                ⚠️ Customer Pain Point
            </div>
 
            <div class="insight-text">
                {row['Pain_Point']}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
footer()
 
