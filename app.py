
import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_excel("Fichero Diputados.xlsx", sheet_name="Hoja1")

st.set_page_config(page_title="Buscador de Diputados", layout="wide")
st.title("🔍 Buscador por Nombre - Diputados del Estado de México")

# Buscador
nombre = st.text_input("Escribe el nombre del diputado o diputada que deseas consultar:")

# Filtrado por nombre
if nombre:
    resultados = df[df["Nombre completo"].str.contains(nombre, case=False, na=False)]
    if not resultados.empty:
        st.success(f"Se encontraron {len(resultados)} resultado(s).")
        st.dataframe(resultados, use_container_width=True)
    else:
        st.warning("No se encontraron resultados.")
else:
    st.info("Escribe un nombre para comenzar la búsqueda.")
