import matplotlib.pyplot as plt
import pandas as pd

# Datos de emprendimientos en La Estrella (2023 y 2024)
data = {
    "Año": [2023, 2024],
    "Emprendimientos Totales": [432, 415],
    "Personas Naturales": [301, 273],
    "Sociedades": [131, 142],
    "Activos (millones COP)": [8837, 8585]  # Suma de personas naturales + sociedades
}

# Crear DataFrame
df = pd.DataFrame(data)

# -------------------------------
# Gráfico de barras comparativo
# -------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df["Año"] - 0.15, df["Personas Naturales"], width=0.3, label="Personas Naturales")
plt.bar(df["Año"] + 0.15, df["Sociedades"], width=0.3, label="Sociedades")

plt.title("Emprendimientos en La Estrella (Antioquia) - 2023 vs 2024")
plt.xlabel("Año")
plt.ylabel("Cantidad de Emprendimientos")
plt.xticks(df["Año"])
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

# -------------------------------
# Gráfico de línea de activos
# -------------------------------
plt.figure(figsize=(10, 6))
plt.plot(df["Año"], df["Activos (millones COP)"], marker="o", linestyle="-", color="blue", label="Activos Totales (millones COP)")

plt.title("Evolución de Activos de Emprendimientos en La Estrella (2023-2024)")
plt.xlabel("Año")
plt.ylabel("Activos (millones COP)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()