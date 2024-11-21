import streamlit as st
import pandas as pd

st.text("hola")

df = pd.read_excel('tabla_final.csv')
st.write(df)
