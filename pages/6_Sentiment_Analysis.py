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
    page_title="Sentiment Analysis",
    page_icon="❤️",
    layout="wide"
)
 
apply_theme()
 
sentiment = pd.read_csv(
    "sentiment_distribution.csv"
)
 
show_brand_header()
 
page_header(
    "Customer Sentiment",
    "Understand the overall tone of conversations across EV customer communities."
)
 
 
section_title(
    "Sentiment Distribution",
    "Conversation volume grouped by AI-classified sentiment."
)
 
 
fig = px.pie(
    sentiment,
    values="Count",
    names="Dashboard_Sentiment",
    hole=0.55
)
 
fig.update_layout(
    height=520,
    margin=dict(l=10, r=10, t=20, b=20),
    legend_title="Sentiment"
)
 
st.plotly_chart(
    fig,
    use_container_width=True
)
 
 
# ============================================================
# SENTIMENT TABLE
# ============================================================
 
section_title(
    "Sentiment Breakdown"
)
 
display_df = sentiment.copy()
 
display_df.columns = [
    "Sentiment",
    "Messages"
]
 
st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)
 
 
footer()
