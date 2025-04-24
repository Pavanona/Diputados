
import streamlit as st
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Función para generar el PDF
def generar_pdf(fila):
    nombre_archivo = f"{fila['Nombre completo'].replace(' ', '_')}.pdf"
    ruta_pdf = f"/tmp/{nombre_archivo}"
    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    ancho, alto = letter

    y = alto - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Ficha de: {fila['Nombre completo']}")
    y -= 30

    if pd.notna(fila["Foto"]):
        ruta_foto = f"Fotos/{fila['Foto']}"
        if os.path.exists(ruta_foto):
            c.drawImage(ruta_foto, 400, y - 100, width=120, height=120)

    c.setFont("Helvetica", 10)
    for columna, valor in fila.items():
        if columna != "Foto":
            texto = f"{columna}: {valor}"
            c.drawString(50, y, texto[:110])
            y -= 15
            if y < 100:
                c.showPage()
                y = alto - 50

    c.save()
    return ruta_pdf, nombre_archivo

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
        for _, fila in resultados.iterrows():
            st.markdown("---")
            if pd.notna(fila["Foto"]):
                ruta_foto = f"Fotos/{fila['Foto']}"
                if os.path.exists(ruta_foto):
                    st.image(ruta_foto, width=200)
                else:
                    st.warning(f"No se encontró la imagen: {ruta_foto}")
            for columna, valor in fila.items():
                if columna != "Foto":
                    st.markdown(f"**{columna}:** {valor}")
            if st.button(f"📄 Descargar ficha PDF de {fila['Nombre completo']}", key=fila['Nombre completo']):
                ruta_pdf, nombre_archivo = generar_pdf(fila)
                with open(ruta_pdf, "rb") as f:
                    st.download_button(
                        label="⬇️ Descargar PDF",
                        data=f,
                        file_name=nombre_archivo,
                        mime="application/pdf"
                    )
    else:
        st.warning("No se encontraron resultados.")
else:
    st.info("Escribe un nombre para comenzar la búsqueda.")
