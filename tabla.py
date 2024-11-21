import streamlit as st
import pandas as pd

st.text("PRUEBA DE CSV")

df = pd.read_excel('tabla_final.csv')
st.write(df)
