import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Configuración del dashboard
# ---------------------------

st.set_page_config(
    page_title="IA en Psicología Clínica",
    layout="wide"
)

# ---------------------------
# Encabezado
# ---------------------------

st.title("Inteligencia Artificial en la Psicología Clínica")
st.subheader("De la Automatización Administrativa a la Eficacia Terapéutica")

st.write("**Autora:** Ligia Fernanda Canul Dorantes")

st.divider()

# ---------------------------
# Resumen
# ---------------------------

st.header("Resumen")

st.write("""
Este artículo analiza la integración de la inteligencia artificial en la práctica de la psicología clínica y su impacto en la eficacia terapéutica y la gestión profesional. 
La investigación se basa en una revisión de literatura fundamentada en la Teoría de la Aceptación y Uso de Tecnología (UTAUT) y el Modelo de Alianza Terapéutica en Salud Digital.

Los hallazgos indican que los agentes conversacionales basados en inteligencia artificial, especialmente aquellos con capacidades generativas y multimodales, 
pueden reducir significativamente síntomas de depresión y distrés psicológico. Sin embargo, existe una brecha entre el potencial clínico de la tecnología 
y su implementación en la práctica profesional, ya que actualmente su uso se concentra principalmente en tareas administrativas.
""")

st.write("**Palabras clave:** Inteligencia artificial, psicología clínica, agentes conversacionales, salud digital, alianza terapéutica")

st.divider()

# ---------------------------
# Introducción
# ---------------------------

st.header("Introducción")

st.write("""
En la última década, la salud mental ha experimentado una creciente integración de tecnologías avanzadas. 
La inteligencia artificial se ha convertido en una herramienta estratégica para mejorar el acceso y la eficacia de las intervenciones psicológicas.

La psicología asistencial digital busca transformar la asistencia tradicional mediante herramientas de soporte, monitoreo y diagnóstico automatizado.

El análisis del uso de la IA en psicología clínica se fundamenta principalmente en dos modelos teóricos:

• Teoría de la Aceptación y Uso de Tecnología (UTAUT)  
• Modelo de Alianza Terapéutica en Salud Digital
""")

# ---------------------------
# Metodología
# ---------------------------

st.header("Metodología")

st.write("""
El estudio se desarrolló mediante una revisión documental de literatura científica reciente publicada entre 2023 y 2025.

El análisis incluyó:

• Meta-análisis de **35 estudios experimentales** sobre agentes conversacionales.  
• Estudios sobre percepción del uso de tecnologías en profesionales de salud mental.  
• Aplicación de modelos teóricos como UTAUT y Alianza Terapéutica Digital para clasificar las variables del estudio.
""")

# ---------------------------
# Resultados
# ---------------------------

st.header("Resultados")

st.subheader("Indicadores principales")

col1, col2, col3 = st.columns(3)

col1.metric("Estudios analizados", "35")
col2.metric("Ensayos controlados", "15")
col3.metric("Herramientas evaluadas", "12")

st.subheader("Impacto reportado en estudios")

data = pd.DataFrame({
    "Indicador": ["Depresión", "Estrés psicológico", "Bienestar general"],
    "Impacto (%)": [70, 65, 20]
})

fig, ax = plt.subplots()
ax.bar(data["Indicador"], data["Impacto (%)"])
ax.set_ylabel("Reducción estimada (%)")
ax.set_title("Impacto de agentes conversacionales en salud mental")

st.pyplot(fig)

st.write("""
Los resultados muestran que los agentes conversacionales basados en inteligencia artificial 
pueden reducir significativamente síntomas de depresión y estrés psicológico, especialmente cuando:

• Utilizan IA generativa  
• Son multimodales (texto, voz e imágenes)  
• Están integrados en aplicaciones móviles  
• Se utilizan en poblaciones clínicas
""")

# ---------------------------
# Discusión
# ---------------------------

st.header("Discusión")

st.write("""
La adopción de la inteligencia artificial en psicología clínica no depende únicamente de la sofisticación tecnológica, 
sino de la calidad de la interacción entre el profesional y el sistema.

Factores como la facilidad de uso, la utilidad percibida y la confianza en la tecnología influyen en la adopción de estas herramientas.

Asimismo, existen desafíos importantes relacionados con la privacidad de los datos, los sesgos algorítmicos y la regulación ética.
""")

st.divider()

# ---------------------------
# Artículos científicos
# ---------------------------

st.header("Artículos científicos analizados")

articulos = {
"Li et al. (2023) – AI conversational agents for mental health":
"""
Revisión sistemática y meta-análisis de estudios sobre chatbots basados en inteligencia artificial.

Resultados principales:
• Reducción significativa de depresión y estrés psicológico.
• Mayor eficacia en sistemas multimodales.
• Mejor desempeño en aplicaciones móviles y poblaciones clínicas.
""",

"Ortega Litardo (2025) – Potencial de la IA en psicología clínica":
"""
Estudio observacional que analizó 12 herramientas de inteligencia artificial utilizadas en psicología clínica.

Conclusiones:
• Muchas herramientas no cumplen estándares de seguridad.
• Algunas aplicaciones apoyan tareas administrativas y seguimiento de pacientes.
• La IA complementa el trabajo del psicólogo.
""",

"Quirós Valverde et al. (2024) – Tecnologías e IA en psicología clínica":
"""
Investigación cualitativa con psicólogos clínicos en Costa Rica.

Resultados principales:
• Uso principal de IA en tareas administrativas.
• Mejora del acceso a servicios psicológicos.
• Riesgos relacionados con privacidad y regulación.
"""
}

seleccion = st.selectbox(
"Selecciona un artículo para ver su resumen",
list(articulos.keys())
)

st.info(articulos[seleccion])

st.divider()

# ---------------------------
# Conclusión
# ---------------------------

st.header("Conclusión")

st.write("""
Los agentes conversacionales basados en inteligencia artificial tienen un gran potencial para apoyar la atención psicológica,
especialmente en la reducción de síntomas de depresión y estrés.

No obstante, estas tecnologías no sustituyen la terapia humana y deben integrarse de manera ética, segura y basada en evidencia científica.
""")
