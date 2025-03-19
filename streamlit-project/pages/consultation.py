import streamlit as st
import pandas as pd


data = pd.read_csv("../clients.csv")

st.title("Clientes cadastrados")
st.divider()
st.dataframe(data)