import streamlit as st
import pandas as pd
import plotly.express as px

sentiment = pd.read_csv(
    "sentiment_distribution.csv"
)

st.title("Sentiment Analysis")

fig = px.pie(
    sentiment,
    values="Count",
    names="Dashboard_Sentiment"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(sentiment)