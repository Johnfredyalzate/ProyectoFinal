import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de emprendimientos en La Estrella (2023 y 2024)
data = {
    "Año": [2023, 2024],
    "Emprendimientos Totales": [432, 415],
    "Personas Naturales": [301, 273],
    "Sociedades": [131, 142],
    "Activos (millones COP)": [8837, 8585]
}

df = pd.DataFrame(data)

st.title("📊 Emprendimientos en La Estrella (Antioquia)")

# Gráfico de barras
st.subheader("Comparación Personas Naturales vs Sociedades")
fig, ax = plt.subplots()
ax.bar(df["Año"] - 0.15, df["Personas Naturales"], width=0.3, label="Personas Naturales")
ax.bar(df["Año"] + 0.15, df["Sociedades"], width=0.3, label="Sociedades")
ax.set_xlabel("Año")
ax.set_ylabel("Cantidad de Emprendimientos")
ax.set_title("Emprendimientos por tipo")
ax.legend()
st.pyplot(fig)

# Gráfico de línea
st.subheader("Evolución de Activos Totales (Millones COP)")
fig2, ax2 = plt.subplots()
ax2.plot(df["Año"], df["Activos (millones COP)"], marker="o", color="blue")
ax2.set_xlabel("Año")
ax2.set_ylabel("Activos (millones COP)")
ax2.set_title("Activos Totales en Emprendimientos")
st.pyplot(fig2)

#streamlit run urlgraficas.py  streamlit run .\Proyecto.v.2\urlgraficas.py