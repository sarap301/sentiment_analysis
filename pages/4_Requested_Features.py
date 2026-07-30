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
    page_title="Requested Features",
    page_icon="💡",
    layout="wide"
)
 
apply_theme()
 
features = pd.read_csv("requested_features.csv")
 
show_brand_header()
 
page_header(
    "Requested Features",
    "Product and service improvements customers would like to see."
)
 
 
theme = st.selectbox(
    "Select a Business Theme",
    sorted(features["Theme"].dropna().unique())
)
 
 
filtered = features[
    features["Theme"] == theme
]
 
 
feature_counts = (
    filtered
    .groupby("Requested_Feature")
    .size()
    .reset_index(name="Frequency")
    .sort_values("Frequency", ascending=False)
)
 
 
section_title(
    "Feature Demand",
    f"Most frequently mentioned requests within {theme}."
)
 
 
fig = px.bar(
    feature_counts.head(15),
    x="Frequency",
    y="Requested_Feature",
    orientation="h"
)
 
fig.update_traces(
    marker_color="#1F3A5F"
)
 
fig.update_layout(
    template="plotly_white",
    height=500,
    margin=dict(l=10, r=20, t=20, b=20),
    xaxis_title="Mention Frequency",
    yaxis_title=""
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
footer()
 
