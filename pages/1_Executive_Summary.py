import streamlit as st
import pandas as pd

summary = pd.read_csv("dashboard_summary.csv")

st.title("Executive Summary")

for _, row in summary.head(10).iterrows():

    with st.container(border=True):

        c1, c2 = st.columns([4,1])

        with c1:

            st.subheader(row["short_theme"])

            st.write(row["executive_summary"])

        with c2:

            st.metric(
                "Messages",
                f"{row['Count']:,}"
            )

            st.success(
                row["dashboard_sentiment"]
            )