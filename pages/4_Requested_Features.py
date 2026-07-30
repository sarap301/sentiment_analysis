import streamlit as st
import pandas as pd

features = pd.read_csv("requested_features.csv")

st.title("Requested Features")

theme = st.selectbox(
    "Theme",
    features["Theme"].unique()
)

filtered = features[
    features["Theme"] == theme
]

feature_counts = (
    filtered
    .groupby("Requested_Feature")
    .size()
    .reset_index(name="Frequency")
    .sort_values(
        "Frequency",
        ascending=False
    )
)

fig = px.bar(
    feature_counts.head(20),
    x="Frequency",
    y="Requested_Feature",
    orientation="h",
    color="Frequency"
)

st.plotly_chart(
    fig,
    use_container_width=True
)