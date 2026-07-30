import streamlit as st
import pandas as pd
import ast
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    page_header,
    section_title,
    footer
)
 
 
st.set_page_config(
    page_title="Message Explorer",
    page_icon="💬",
    layout="wide"
)
 
apply_theme()
 
business = pd.read_csv(
    "business_categories.csv"
)
 
show_brand_header()
 
page_header(
    "Customer Message Explorer",
    "Explore representative EV community conversations behind the identified business themes."
)
 
 
theme = st.selectbox(
    "Select a Business Category",
    sorted(business["Business_Category"].dropna().unique())
)
 
 
row = business[
    business["Business_Category"] == theme
].iloc[0]
 
 
messages = ast.literal_eval(row["Sample"])
 
 
section_title(
    "Representative Conversations",
    f"Showing sample conversations associated with Business Category {theme}."
)
 
 
st.caption(
    f"{len(messages)} representative messages available"
)
 
 
for i, msg in enumerate(messages):
 
    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #D9E2EC;
            border-radius:12px;
            padding:16px 18px;
            margin-bottom:10px;
            box-shadow:0 2px 8px rgba(16,42,67,0.05);
        ">
 
            <div style="
                color:#829AB1;
                font-size:11px;
                margin-bottom:7px;
                font-weight:600;
            ">
                COMMUNITY MESSAGE {i + 1}
            </div>
 
            <div style="
                color:#243B53;
                line-height:1.55;
                font-size:14px;
            ">
                {msg}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
footer()
 
