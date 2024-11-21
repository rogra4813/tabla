import streamlit as st
import pandas as pd

st.title('EJERCICIO PRÁCTICO ETL')
st.text("*************************************************************************************************************")

# ---------------------------------#
# Información 
expander_bar = st.expander("**Más sobre este trabajo**")
expander_bar.markdown("""
*:orange[Información:]* Este ejercicio práctico permite consolidar lo aprendido en Diseños de procesos ETL en Data Science, para ello, se realizó un web scrapping a la URL https://es.investing.com/crypto/bitcoin, para extraer la información de las cryptos.

*:orange[Integrantes:]* :blue[GRUPO 6] Robert Granda, Francisco García, Fabián Quito y Gabriel Salazar.   

""")


csv_url = "https://raw.githubusercontent.com/rogra4813/tabla/main/tabla_final.csv"  # Reemplaza con la URL de tu archivo CSV

# Leer el archivo CSV desde la URL
df = pd.read_csv(csv_url)

# Mostrar el DataFrame en la aplicación
st.dataframe(df)


