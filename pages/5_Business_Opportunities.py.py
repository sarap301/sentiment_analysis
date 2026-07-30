import streamlit as st
import pandas as pd

opp = pd.read_csv("business_opportunities.csv")

st.title("Business Opportunities")

theme = st.selectbox(
    "Theme",
    opp["Theme"].unique()
)

filtered = opp[
    opp["Theme"] == theme
]

for _, row in filtered.iterrows():

    with st.container(border=True):

        st.info(
            row["Business_Opportunity"]
        )