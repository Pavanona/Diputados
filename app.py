st.subheader("📊 Visualizaciones Generales")
col1, col2 = st.columns(2)

with col1:
    if not filtered_df.empty:
        fig1 = px.bar(
            filtered_df["Grupo parlamentario"].value_counts().reset_index(),
            x="index",
            y="Grupo parlamentario",
            labels={"index": "Grupo Parlamentario", "Grupo parlamentario": "Número de Diputados"},
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

