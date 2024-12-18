import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración inicial
st.title("Simulación de Ondas en una Cuerda Tensa")
st.sidebar.header("Ajusta los Parámetros")

# Parámetros ajustables
tension = st.sidebar.slider("Tensión (N)", 1.0, 100.0, 50.0)
densidad_lineal = st.sidebar.number_input("Densidad Lineal (kg/m)", 0.01, 0.2, 0.05)
frecuencia = st.sidebar.slider("Frecuencia (Hz)", 1.0, 20.0, 5.0)
amplitud = st.sidebar.slider("Amplitud (m)", 0.1, 2.0, 1.0)
tipo_onda = st.sidebar.selectbox("Tipo de Onda", ["Progresiva", "Estacionaria"])

# Cálculos derivados
velocidad = np.sqrt(tension / densidad_lineal)
longitud_onda = velocidad / frecuencia

st.sidebar.write(f"Rapidez de onda: {velocidad:.2f} m/s")
st.sidebar.write(f"Longitud de onda: {longitud_onda:.2f} m")

# Simulación de la onda
x = np.linspace(0, 10, 500)  # Longitud de la cuerda
fig, ax = plt.subplots()

t = st.slider("Tiempo (s)", 0.0, 10.0, 0.0, step=0.1)

if tipo_onda == "Progresiva":
    y = amplitud * np.sin(2 * np.pi * (x / longitud_onda - frecuencia * t))
else:  # Estacionaria
    y = 2 * amplitud * np.sin(2 * np.pi * x / longitud_onda) * np.cos(2 * np.pi * frecuencia * t)

ax.plot(x, y, label=f"t = {t:.2f} s")
ax.set_ylim(-2 * amplitud, 2 * amplitud)
ax.set_xlabel("Posición (m)")
ax.set_ylabel("Desplazamiento (m)")
ax.legend()
st.pyplot(fig)

# Información adicional
st.write("### Información")
st.write("""
La rapidez de la onda depende de la tensión y la densidad lineal de la cuerda.
Esta simulación permite observar cómo las ondas progresivas y estacionarias
cambian al variar los parámetros.
""")
