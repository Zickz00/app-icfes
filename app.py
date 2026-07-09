import random
import streamlit as st
import pandas as pd
from groq import Groq

from preguntas import BANCO_PREGUNTAS
from database import (
    init_db,
    guardar_resultado,
    obtener_historial,
    obtener_ultimo_resultado,
)

# ==================== CONFIGURACIÓN GROQ ====================
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)

# Inicializa la base de datos (crea la tabla si no existe). Es seguro llamarlo
# en cada rerun: CREATE TABLE IF NOT EXISTS no hace nada si ya existe.
init_db()

# Cuántas preguntas tomar de cada área para armar el diagnóstico
PREGUNTAS_POR_AREA = 3

st.set_page_config(page_title="IA Preparador ICFES", page_icon="🚀", layout="wide")

# ==================== ESTILO MINIMALISTA (solo interfaz, no toca lógica) ====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #262624;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header[data-testid="stHeader"] {
    background-color: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 800px;
}

section[data-testid="stSidebar"] {
    background-color: #1E1E1C;
    border-right: 1px solid #3A3A37;
}
section[data-testid="stSidebar"] label {
    font-weight: 600;
    color: #ECECE7 !important;
}

.stApp, .stApp p, .stApp li, .stApp span, .stApp label,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #ECECE7 !important;
}

h1 { color: #FFFFFF !important; font-weight: 700; }
h2, h3 { color: #ECECE7 !important; font-weight: 600; }

div.stButton > button, div.stButton > button * {
    color: #ECECE7 !important;
}

div.stButton > button {
    border-radius: 999px;
    border: 1px solid #4A4A47;
    background-color: #33322F;
    padding: 0.5rem 1.5rem;
    font-weight: 500;
    transition: all 0.2s ease;
}
div.stButton > button:hover {
    background-color: #3F3E3B;
    border-color: #5A5A56;
    transform: translateY(-1px);
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] textarea {
    border-radius: 12px !important;
    border: 1px solid #4A4A47 !important;
    background-color: #33322F !important;
    color: #ECECE7 !important;
}

div[role="radiogroup"] label {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-radius: 12px;
    padding: 0.6rem 1rem;
    margin-bottom: 0.4rem;
}

details {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-radius: 14px;
    padding: 0.5rem 1rem;
    margin-bottom: 0.6rem;
}
summary {
    color: #ECECE7 !important;
}

[data-testid="stChatMessage"] {
    background-color: #2F2E2B;
    border-radius: 16px;
    border: 1px solid #3F3E3A;
    padding: 0.8rem 1rem;
    margin-bottom: 0.5rem;
}

div[data-testid="stNotification"], .stAlert {
    border-radius: 14px;
}

@media (max-width: 640px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }
    h1 { font-size: 1.6rem; }
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 IA Preparador ICFES")
st.subheader("Tu tutor inteligente para el Saber 11 - con Groq")

menu = st.sidebar.selectbox(
    "Menú",
    ["🏠 Inicio", "📝 Test Diagnóstico", "📊 Mis Resultados", "📚 Plan de Estudio IA", "🃏 Flashcards", "💬 Chat IA"],
)


# ==================== FUNCIONES AUXILIARES ====================
def generar_test():
    """Arma un test tomando PREGUNTAS_POR_AREA preguntas aleatorias de cada área."""
    preguntas = []
    contador_id = 1
    for area, lista_preguntas in BANCO_PREGUNTAS.items():
        seleccionadas = random.sample(lista_preguntas, min(PREGUNTAS_POR_AREA, len(lista_preguntas)))
        for p in seleccionadas:
            preguntas.append({
                "id": contador_id,
                "area": area,
                "tema": p["tema"],
                "pregunta": p["pregunta"],
                "opciones": p["opciones"],
                "correcta": p["correcta"],
            })
            contador_id += 1
    random.shuffle(preguntas)
    return preguntas


def estimar_puntaje_icfes(puntaje_porcentual):
    """
    Aproximación simple: mapea el % de aciertos a la escala global ICFES (0-500).
    Es una estimación educativa, no un cálculo oficial del ICFES.
    """
    return round((puntaje_porcentual / 100) * 500)


# ==================== INICIO ====================
if menu == "🏠 Inicio":
    st.write("Bienvenido a tu IA para prepararte para el ICFES.")
    st.success("Usa el menú de la izquierda para navegar.")
    st.info(f"El test diagnóstico incluye {PREGUNTAS_POR_AREA} preguntas aleatorias de cada una de las 5 áreas del Saber 11.")

# ==================== TEST DIAGNÓSTICO ====================
elif menu == "📝 Test Diagnóstico":
    st.header("📝 Test Diagnóstico Inicial")
    nombre = st.text_input("Tu nombre completo:", value=st.session_state.get("nombre_estudiante", ""))

    if st.button("🚀 Empezar Test"):
        if not nombre.strip():
            st.warning("Por favor escribe tu nombre antes de empezar.")
        else:
            st.session_state.nombre_estudiante = nombre.strip()
            st.session_state.test_iniciado = True
            st.session_state.respuestas = {}
            st.session_state.preguntas = generar_test()

    if st.session_state.get("test_iniciado", False):
        st.caption(f"{len(st.session_state.preguntas)} preguntas · 5 áreas del Saber 11")

        # Agrupar visualmente por área para que se vea más ordenado
        area_actual = None
        for p in st.session_state.preguntas:
            if p["area"] != area_actual:
                area_actual = p["area"]
                st.markdown(f"#### {area_actual}")
            resp = st.radio(p["pregunta"], p["opciones"], key=f"q{p['id']}", index=None)
            st.session_state.respuestas[p["id"]] = resp

        if st.button("✅ Finalizar Test"):
            sin_responder = [p for p in st.session_state.preguntas if st.session_state.respuestas.get(p["id"]) is None]
            if sin_responder:
                st.warning(f"Te faltan {len(sin_responder)} pregunta(s) por responder.")
            else:
                total = len(st.session_state.preguntas)
                aciertos = sum(
                    1 for p in st.session_state.preguntas
                    if st.session_state.respuestas.get(p["id"]) == p["correcta"]
                )
                puntaje = round((aciertos / total) * 100, 1)
                puntaje_icfes = estimar_puntaje_icfes(puntaje)
                falencias = [
                    p for p in st.session_state.preguntas
                    if st.session_state.respuestas.get(p["id"]) != p["correcta"]
                ]

                st.session_state.resultados = {
                    "nombre": nombre,
                    "puntaje": puntaje,
                    "puntaje_icfes": puntaje_icfes,
                    "falencias": falencias,
                }

                # Persistir en SQLite para el historial
                guardar_resultado(
                    nombre=nombre,
                    puntaje=puntaje,
                    puntaje_icfes=puntaje_icfes,
                    falencias=falencias,
                    respuestas=st.session_state.respuestas,
                )

                st.success(f"¡Test completado! Puntaje: {puntaje}% · Estimado ICFES: {puntaje_icfes}/500")
                st.balloons()
                st.session_state.test_iniciado = False

# ==================== RESULTADOS ====================
elif menu == "📊 Mis Resultados":
    st.header("📊 Mis Resultados")
    nombre = st.text_input("Escribe tu nombre para ver tu historial:", value=st.session_state.get("nombre_estudiante", ""))

    if nombre.strip():
        historial = obtener_historial(nombre.strip())

        if historial:
            ultimo = historial[-1]
            col1, col2, col3 = st.columns(3)
            col1.metric("Último puntaje", f"{ultimo['puntaje']}%")
            col2.metric("Estimado ICFES", f"{ultimo['puntaje_icfes']}/500")
            col3.metric("Intentos realizados", len(historial))

            st.subheader("📈 Evolución en el tiempo")
            df = pd.DataFrame(historial)[["fecha", "puntaje_icfes"]].set_index("fecha")
            st.line_chart(df)

            st.subheader("🕓 Historial de intentos")
            for h in reversed(historial):
                with st.expander(f"{h['fecha']} — {h['puntaje']}% ({h['puntaje_icfes']}/500)"):
                    if h["falencias"]:
                        st.write("**Falencias detectadas en este intento:**")
                        for f in h["falencias"]:
                            st.write(f"- **{f['area']}**: {f['tema']}")
                    else:
                        st.write("Sin falencias registradas. ¡Buen resultado!")
        else:
            st.warning("Aún no tienes resultados guardados con ese nombre. Realiza el Test Diagnóstico primero.")
    else:
        st.info("Escribe tu nombre para consultar tu historial.")

# ==================== PLAN DE ESTUDIO ====================
elif menu == "📚 Plan de Estudio IA":
    st.header("📚 Plan de Estudio Personalizado por IA")
    if st.session_state.get("resultados"):
        res = st.session_state.resultados
        falencias = res.get("falencias", [])

        st.write(f"**Estudiante:** {res['nombre']}")
        st.write(f"**Puntaje General:** {res['puntaje']}% · **Estimado ICFES:** {res.get('puntaje_icfes', '—')}/500")

        st.subheader("🎯 Análisis de la IA")
        if falencias:
            st.write("**Tus principales falencias detectadas:**")
            for f in falencias:
                st.write(f"- **{f['area']}**: {f['tema']}")
        else:
            st.success("¡Excelente! Tienes un buen nivel general.")

        st.subheader("📅 Plan de Estudio Personalizado (7 días)")
        plan = []
        for i, f in enumerate(falencias[:3]):
            plan.append({
                "dia": f"Día {i+1}",
                "area": f["area"],
                "tema": f["tema"],
                "actividades": [f"Estudiar teoría de {f['tema']} (30 min)", "Hacer 10 flashcards", "Resolver 5 ejercicios prácticos"],
                "recursos": [f"https://www.khanacademy.org/search?q={f['tema'].lower()}", "Caja de herramientas ICFES", "Quizlet ICFES"],
            })

        for p in plan:
            with st.expander(f"📅 {p['dia']}: {p['area']} - {p['tema']}"):
                st.write("**Actividades recomendadas:**")
                for act in p["actividades"]:
                    st.write(f"- {act}")
                st.write("**Recursos útiles:**")
                for rec in p["recursos"]:
                    st.write(f"- {rec}")

        st.subheader("🃏 Flashcards Generadas por IA")
        if falencias:
            for f in falencias[:2]:
                st.write(f"**Tema:** {f['tema']}")
                st.write("- **Pregunta:** ¿Qué es / Cómo funciona " + f["tema"] + "?")
                st.write("- **Respuesta:** (Repasa el concepto clave en los recursos)")
                st.divider()
    else:
        st.warning("Realiza primero el Test Diagnóstico.")

# ==================== FLASHCARDS MEJORADAS ====================
elif menu == "🃏 Flashcards":
    st.header("🃏 Flashcards Interactivas")

    if st.session_state.get("resultados"):
        falencias = st.session_state.resultados.get("falencias", [])
        if not falencias:
            falencias = [{"area": "Ciencias Naturales", "tema": "Fotosíntesis"}]

        for i, f in enumerate(falencias[:4]):
            st.subheader(f"📌 {f['area']} - {f['tema']}")

            if f"flipped_{i}" not in st.session_state:
                st.session_state[f"flipped_{i}"] = False

            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("🔄 Voltear Tarjeta", key=f"flip_{i}"):
                    st.session_state[f"flipped_{i}"] = not st.session_state[f"flipped_{i}"]

            with col2:
                if st.session_state[f"flipped_{i}"]:
                    st.success("**Respuesta:**")
                    if f["tema"] == "Fotosíntesis":
                        st.write("**Es el proceso por el cual las plantas convierten la luz solar, agua y CO₂ en glucosa y oxígeno.**")
                        st.write("Ecuación: 6CO₂ + 6H₂O + luz → C₆H₁₂O₆ + 6O₂")
                    else:
                        st.write(f"**Explicación clave:** {f['tema']} es un tema fundamental en el ICFES. Repasa definiciones, ejemplos y ejercicios típicos.")
                    st.info("💡 Repite esta respuesta en voz alta 3 veces")
                else:
                    st.info("**Pregunta (Cara frontal)**")
                    st.markdown(f"### ¿Qué es / Cómo funciona **{f['tema']}**?")
                    st.caption("Haz clic en 'Voltear Tarjeta' para ver la respuesta")

            st.divider()
    else:
        st.warning("Realiza el test diagnóstico primero.")

# ==================== CHAT IA CON GROQ ====================
elif menu == "💬 Chat IA":
    st.header("💬 Chat con Tutor IA (Groq)")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Escribe tu duda de ICFES...")
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.spinner("Groq pensando..."):
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt + " Responde como tutor experto para el ICFES en español, claro y útil."}],
                    temperature=0.7,
                    max_tokens=800,
                )
                respuesta = completion.choices[0].message.content
            except Exception as e:
                respuesta = f"Error: {str(e)}"

        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)

st.caption("Proyecto IA para ICFES con Groq")
