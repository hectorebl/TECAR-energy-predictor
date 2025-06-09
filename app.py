import streamlit as st
import numpy as np
import joblib

# Cargar el modelo entrenado
modelo = joblib.load('modelo_tecar.pkl')

st.title("Predicción de Energía TECAR (KJ)")

st.write("""
Introduce los valores de los parámetros del paciente antes de la sesión:
""")

# Pedimos solo las variables usadas en el modelo
altura = st.number_input('Altura (cm)', min_value=0.0, step=0.01, format="%.2f")
sexo = st.selectbox('Sexo', options=['Hombre', 'Mujer'])
sexo_val = 0 if sexo == 'Hombre' else 1
edad = st.number_input('Edad (años)', min_value=0, max_value=120, step=1)
duracion = st.number_input('Duración de la sesión (minutos)', min_value=0, max_value=200, step=1)
trigliceridos_inicio = st.number_input('Triglicéridos inicio (mg/dL)', min_value=0, step=1)
plicometro_antes = st.number_input('Plicómetro antes (mm)', min_value=0, step=1)
hdl_inicio = st.number_input('HDL-colesterol inicio (mg/dL)', min_value=0, step=1)
trocanter_antes = st.number_input('Trocanter antes (cm)', min_value=0.0, step=0.1, format="%.2f")
imc_antes = st.number_input('IMC antes', min_value=0.0, step=0.01, format="%.2f")




# Cuando el usuario da a predecir
if st.button('Predecir Energía (KJ)'):
    # Ordenar las variables exactamente como en el modelo
    entrada = np.array([[trigliceridos_inicio, edad, plicometro_antes, hdl_inicio,
                         trocanter_antes, imc_antes, altura, duracion, sexo_val]])
    energia_pred = modelo.predict(entrada)[0]
    st.success(f"Energía recomendada a entregar: {energia_pred:.2f} KJ")

st.markdown("""
---
Aplicación desarrollada para la personalización de energía en equipos TECAR mediante IA.  
""")
