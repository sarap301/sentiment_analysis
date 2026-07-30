import streamlit as st
import pandas as pd

business = pd.read_csv("business_categories.csv")

st.title("Message Explorer")

theme = st.selectbox(
    "Business Category",
    business["Business_Category"]
)

messages = business[
    business["Business_Category"] == theme
]["Sample"].iloc[0]

import ast

messages = ast.literal_eval(messages)

for msg in messages:

    with st.chat_message("user"):

        st.write(msg)