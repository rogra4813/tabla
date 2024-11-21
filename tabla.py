import streamlit as st
import pandas as pd
import csv

st.text("PRUEBA DE CSV")
csv_url = "https://raw.githubusercontent.com/usuario/repositorio/rama/archivo.csv"  # Reemplaza con la URL de tu archivo CSV

# Leer el archivo CSV desde la URL
df = pd.read_csv(csv_url)

# Mostrar el DataFrame en la aplicación
st.dataframe(df)


