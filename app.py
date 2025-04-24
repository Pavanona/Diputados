
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_excel("Fichero Diputados.xlsx", sheet_name="Hoja1")

st.set_page_config(page_title="Dashboard de Diputados", layout="wide")
st.title("📈 Dashboard Interactivo - Diputados Estado de México")

# Filtros
st.sidebar.header("🔍 Filtros")
grupo = st.sidebar.multiselect("Grupo Parlamentario:", sorted(df["Grupo parlamentario"].dropna().unique()))
experiencia_leg = st.sidebar.multiselect("Experiencia Legislativa:", sorted(df["Experiencia legislativa"].dropna().unique()))

# Aplicar filtros
filtered_df = df.copy()
if grupo:
    filtered_df = filtered_df[filtered_df["Grupo parlamentario"].isin(grupo)]
if experiencia_leg:
    filtered_df = filtered_df[filtered_df["Experiencia legislativa"].isin(experiencia_leg)]

# Columnas para gráficas
st.subheader("📊 Visualizaciones Generales")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df["Grupo parlamentario"].value_counts().reset_index(),
        x="index",
        y="Grupo parlamentario",
        labels={"index": "Grupo Parlamentario", "Grupo parlamentario": "Número de Diputados"},
        title="Diputados por Grupo Parlamentario"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(
        filtered_df,
        names="Experiencia legislativa",
        title="Distribución por Experiencia Legislativa"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Mostrar tabla
st.subheader("📋 Tabla Detallada")
st.dataframe(filtered_df, use_container_width=True)
