import streamlit as st
import pandas as pd

summary = pd.read_csv("business_insights.csv")

st.title("AI Generated Insights")

theme = st.selectbox(
    "Theme",
    summary["short_theme"]
)

row = summary[
    summary["short_theme"] == theme
].iloc[0]

import ast

st.subheader(row["short_theme"])

st.write(row["executive_summary"])

st.markdown("### Customer Pain Points")

for p in ast.literal_eval(row["customer_pain_points"]):
    st.write("•", p)

st.markdown("### Requested Features")

for f in ast.literal_eval(row["requested_features"]):
    st.write("•", f)

st.markdown("### Business Opportunities")

for o in ast.literal_eval(row["business_opportunities"]):
    st.write("•", o)

st.metric(
    "Messages",
    row["Count"]
)

st.success(
    row["dashboard_sentiment"]
)