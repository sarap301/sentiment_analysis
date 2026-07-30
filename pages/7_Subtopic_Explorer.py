import streamlit as st
import pandas as pd
import plotly.express as px
 
from utils.theme import (
    apply_theme,
    show_brand_header,
    page_header,
    section_title,
    footer
)
 
 
st.set_page_config(
    page_title="Subtopic Explorer",
    page_icon="🔎",
    layout="wide"
)
 
apply_theme()
 
subtopics = pd.read_csv("subtopics.csv")
 
show_brand_header()
 
page_header(
    "Subtopic Explorer",
    "Drill down from broad business themes into specific customer discussion areas."
)
 
 
theme = st.selectbox(
    "Select a Business Theme",
    sorted(subtopics["Theme"].dropna().unique())
)
 
 
filtered = subtopics[
    subtopics["Theme"] == theme
]
 
 
section_title(
    "Subtopic Landscape",
    f"Detailed discussion areas within {theme}."
)
 
 
fig = px.sunburst(
    filtered,
    path=["Theme", "Subtopic"],
    values="Count"
)
 
fig.update_layout(
    height=600,
    margin=dict(l=10, r=10, t=20, b=20)
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
footer()
