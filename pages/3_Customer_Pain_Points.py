import streamlit as st
import pandas as pd

pain = pd.read_csv("pain_points.csv")

st.title("Customer Pain Points")

theme = st.selectbox(
    "Choose Theme",
    pain["Theme"].unique()
)

filtered = pain[
    pain["Theme"] == theme
]

for _, row in filtered.iterrows():
    with st.container(border=True):
        st.warning(row["Pain_Point"])