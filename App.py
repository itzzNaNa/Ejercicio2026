import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IA en Psicología Clínica",
    page_icon="🧠",
    layout="wide"
)

# Estilo minimalista personalizado
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stMarkdown {
        text-align: justify;
    }
    h1 {
        text-align: center;
        color: #1E1E1E;
    }
    .author-text {
        text-align: left;
        color: #555555;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO Y AUTOR ---
st.title("Inteligencia Artificial en la Psicología Clínica: De la Automatización Administrativa a la Eficacia Terapéutica")
st.markdown('<p class="author-text">Ligia Fernanda Canul Dorantes</p>', unsafe_allow_html=True)

st.divider()

# --- CUERPO DEL ARTÍCULO (DISEÑO MINIMALISTA) ---
col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    # Resumen
    st.subheader("Resumen")
    st.write("""
    El presente artículo analiza la integración de la inteligencia artificial (IA) en la práctica de la psicología clínica, 
    examinando su impacto en la eficacia terapéutica y la gestión profesional. Se realizó una revisión de literatura 
    fundamentada en la Teoría de la Aceptación y Uso de Tecnología (UTAUT) y el Modelo de Alianza Terapéutica en Salud Digital.
    """)

    # Introducción
    st.subheader("Introducción")
    st.write("""
    En la última década, la salud mental ha experimentado un crecimiento exponencial en la integración de tecnologías avanzadas. 
    La IA se ha consolidado como una herramienta estratégica para optimizar el acceso y la eficacia de las intervenciones. 
    Este fenómeno se manifiesta principalmente a través de la psicología asistencial digital, sustentada en la expectativa de 
    desempeño del profesional y la capacidad del algoritmo para replicar componentes de empatía.
    """)

    # Metodología
    st.subheader("Metodología")
    st.write("""
    Se empleó un diseño de investigación documental y descriptivo (2023-2025). El corpus incluyó:
    * **Análisis de meta-análisis:** Evaluación de 35 estudios sobre agentes conversacionales.
    * **Revisión de campo:** Análisis de percepción en profesionales de salud mental (Costa Rica).
    * **Marco Conceptual:** Aplicación de modelos UTAUT y Alianza Terapéutica Digital.
    """)

    # Resultados
    st.subheader("Resultados")
    
    tab1, tab2, tab3 = st.tabs(["Eficacia (CAs)", "Adopción Profesional", "Calidad Asistencial"])
    
    with tab1:
        st.write("**Eficacia de Agentes Conversacionales (CAs):**")
        st.write("""
        Los sistemas con IA generativa y multimodalidad (texto, voz e imagen) reducen significativamente síntomas 
        de depresión y distrés, especialmente en entornos móviles.
        """)
        
    with tab2:
        st.write("**Adopción y Uso:**")
        st.write("""
        Existe una brecha entre potencial y práctica. En contextos como Costa Rica, el uso se limita a:
        * Tareas administrativas y gestión.
        * Comunicación básica con el paciente.
        * Automatización de notas de progreso clínico.
        """)
        
    with tab3:
        st.write("**Impacto en Calidad:**")
        st.write("""
        La IA reduce la carga laboral administrativa, permitiendo teóricamente que el profesional incremente 
        la calidad del tiempo dedicado a la interacción humana directa.
        """)

    # Discusión y Conclusión
    st.subheader("Discusión")
    st.write("""
    La transición digital depende de la interacción “humano-agente”. Para ser terapéutica, la IA debe replicar 
    empatía y comunicación efectiva. La adopción está condicionada por la facilidad de uso percibida (UTAUT) 
    y enfrenta desafíos éticos críticos en privacidad de datos.
    """)

    st.info("**Palabras clave:** Inteligencia artificial, psicología clínica, agentes conversacionales, salud digital, alianza terapéutica.")

st.divider()

# --- SECCIÓN DE REFERENCIAS Y BOTÓN DESPLEGABLE ---
st.header("📚 Referencias y Resúmenes")

# Diccionario de datos de las fuentes
referencias = {
    "Li et al. (2023) - Systematic review and meta-analysis of AI-based conversational agents": {
        "resumen": "Analiza la efectividad de chatbots en salud mental mediante 35 estudios. Concluye que reducen significativamente síntomas de depresión y estrés, siendo más efectivos los modelos multimodales y generativos.",
        "puntos_clave": ["Reducción de depresión/estrés", "Eficacia en poblaciones clínicas", "Riesgos de privacidad y sesgos"]
    },
    "Ortega Litardo (2025) - El potencial de la IA en la psicología clínica": {
        "resumen": "Explora herramientas disponibles y su impacto. Indica que muchas apps carecen de respaldo científico, pero las consolidadas apoyan eficazmente tareas administrativas y seguimiento sin reemplazar al psicólogo.",
        "puntos_clave": ["Complemento al trabajo humano", "Transformación ética", "Análisis de 12 aplicaciones"]
    },
    "Quirós Valverde et al. (2024) - Análisis de aportes, riesgos y necesidades en Costa Rica": {
        "resumen": "Estudio cualitativo con profesionales costarricenses. Destaca que la IA se usa mayormente en telepsicología y administración, con barreras de capacitación y preocupaciones por la pérdida de lenguaje no verbal.",
        "puntos_clave": ["Aumento de acceso", "Necesidad de regulación", "Falta de formación tecnológica"]
    }
}

# Botón desplegable (Selectbox) para mostrar resúmenes
seleccion = st.selectbox("Seleccione un artículo para ver su resumen:", ["Seleccione una opción..."] + list(referencias.keys()))

if seleccion != "Seleccione una opción...":
    with st.expander("Ver detalles del artículo", expanded=True):
        st.write(f"**Resumen:** {referencias[seleccion]['resumen']}")
        st.write("**Puntos destacados:**")
        for punto in referencias[seleccion]['puntos_clave']:
            st.write(f"- {punto}")

st.sidebar.markdown("### Sobre este Dashboard")
st.sidebar.info("Este dashboard presenta una síntesis de la investigación actual sobre la integración de la IA en la práctica clínica psicológica.")
