
import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_excel("Fichero Diputados.xlsx", sheet_name="Hoja1")

# Título
st.title("Fichero de Diputados - Estado de México")

# Filtros
grupo = st.multiselect("Filtrar por Grupo Parlamentario:", sorted(df["Grupo parlamentario"].dropna().unique()))
experiencia_leg = st.multiselect("Filtrar por Experiencia Legislativa:", sorted(df["Experiencia legislativa"].dropna().unique()))
ideologia = st.text_input("Buscar por Posicionamiento Ideológico o Temático:")

# Aplicar filtros
filtered_df = df.copy()

if grupo:
    filtered_df = filtered_df[filtered_df["Grupo parlamentario"].isin(grupo)]

if experiencia_leg:
    filtered_df = filtered_df[filtered_df["Experiencia legislativa"].isin(experiencia_leg)]

if ideologia:
    filtered_df = filtered_df[filtered_df["Posicionamiento ideológico o temático"].str.contains(ideologia, case=False, na=False)]

# Mostrar tabla
st.dataframe(filtered_df, use_container_width=True)
