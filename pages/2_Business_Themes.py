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
    page_title="Business Themes",
    page_icon="🧩",
    layout="wide"
)
 
apply_theme()
 
df = pd.read_csv("theme_ranking.csv")
 
show_brand_header()
 
page_header(
    "Business Themes",
    "Explore the major themes emerging from EV customer conversations."
)
 
 
# ============================================================
# TREEMAP
# ============================================================
 
section_title(
    "Customer Discussion Landscape",
    "Larger areas represent themes with greater conversation volume."
)
 
fig = px.treemap(
    df,
    path=["short_theme"],
    values="Count"
)
 
fig.update_traces(
    marker_colorscale=[
        [0, "#DCE8F2"],
        [0.5, "#527A9D"],
        [1, "#102A43"]
    ]
)
 
fig.update_layout(
    height=600,
    margin=dict(l=10, r=10, t=20, b=20)
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
# ============================================================
# TABLE
# ============================================================
 
section_title(
    "Theme Ranking",
    "Conversation volume across identified business themes."
)
 
display_df = df.copy()
 
display_df.columns = [
    "Business Theme",
    "Messages",
    "Sentiment"
]
 
st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)
 
footer()
