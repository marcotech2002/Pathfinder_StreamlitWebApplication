import streamlit as st
import pandas as pd

file_path = '../clients.csv'

try:
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline()
except FileNotFoundError:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("Nome,Data de nascimento,Tipo\n")
    
data = pd.read_csv(file_path)

st.title("Clientes cadastrados")
st.divider()
st.dataframe(data)