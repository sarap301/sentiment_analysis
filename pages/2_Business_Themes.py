import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("theme_ranking.csv")

st.title("Business Themes")

fig = px.treemap(
    df,
    path=["short_theme"],
    values="Count",
    color="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(df)