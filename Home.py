import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tata Motors EV Customer Intelligence",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------

kpis = pd.read_csv("kpis.csv")
theme_ranking = pd.read_csv("theme_ranking.csv")
summary = pd.read_csv("dashboard_summary.csv")

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🚗 Tata Motors EV Dashboard")

st.sidebar.markdown("""
### Navigation

Use the pages in the left sidebar.

This dashboard summarizes customer discussions from
WhatsApp and Telegram EV communities using

- BERTopic
- Sentence Transformers
- Gemini AI
""")

# -----------------------------
# Title
# -----------------------------

st.title("🚗 Tata Motors EV Customer Intelligence Dashboard")

st.markdown("""
### WhatsApp & Telegram EV Community Analytics

This dashboard analyzes discussions collected from

• WhatsApp EV Communities
• Telegram EV Communities

using

✔ BERTopic       
✔ Sentence Transformers           
✔ Gemini AI      

to discover

- Business Themes
- Customer Pain Points
- Requested Features
- Business Opportunities
- Customer Sentiment
""")

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Messages Analysed",
        f"{int(kpis.iloc[0]['Value']):,}"
    )

with c2:
    st.metric(
        "Business Categories",
        int(kpis.iloc[1]["Value"])
    )

with c3:
    st.metric(
        "Major Business Themes",
        int(kpis.iloc[2]["Value"])
    )

st.divider()

# -----------------------------
# Top Themes
# -----------------------------

st.subheader("Top Business Themes")

import plotly.express as px

fig = px.bar(
    theme_ranking.head(10),
    x="Count",
    y="short_theme",
    orientation="h",
    color="Count",
    title="Top Business Themes"
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------
# Executive Summary
# -----------------------------

st.subheader("Executive Summary")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.subheader("Key AI Insights")

st.info("""
• Charging reliability dominates customer discussions.

• Infrastructure expansion is the most requested feature.

• Pricing transparency remains a major concern.

• Customers demand a unified charging experience.

• Highway charging coverage is still inadequate.
""")

st.success(
    "Use the navigation menu on the left to explore Business Themes, Pain Points, Requested Features, Business Opportunities and Sentiment."
)