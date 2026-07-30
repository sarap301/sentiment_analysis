import streamlit as st
import pandas as pd

subtopics = pd.read_csv("subtopics.csv")

st.title("Subtopic Explorer")

theme = st.selectbox(
    "Theme",
    subtopics["Theme"].unique()
)

filtered = subtopics[
    subtopics["Theme"] == theme
]

fig = px.sunburst(
    subtopics,
    path=[
        "Theme",
        "Subtopic"
    ],
    values="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)