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

# Visualizaciones
st.subheader("📊 Visualizaciones Generales")
col1, col2 = st.columns(2)

with col1:
    if not filtered_df.empty:
        df_bar = (
            filtered_df["Grupo parlamentario"]
            .value_counts()
            .reset_index()
            .rename(columns={"index": "Grupo Parlamentario", "Grupo parlamentario": "Cantidad"})
        )
        fig1 = px.bar(
            df_bar,
            x="Grupo Parlamentario",
            y="Cantidad",
            title="Diputados por Grupo Parlamentario"
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No hay datos disponibles para graficar en este filtro.")

with col2:
    if not filtered_df.empty:
        fig2 = px.pie(
            filtered_df,
            names="Experiencia legislativa",
            title="Distribución por Experiencia Legislativa"
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No hay datos disponibles para graficar en este filtro.")

# Tabla detallada
st.subheader("📋 Tabla Detallada")
st.dataframe(filtered_df, use_container_width=True)
