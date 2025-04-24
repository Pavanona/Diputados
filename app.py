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
