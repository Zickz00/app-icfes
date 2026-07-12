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
    registrar_visita,
    calcular_racha,
)

# ==================== CONFIGURACIÓN GROQ ====================
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)

# Inicializa la base de datos (crea la tabla si no existe). Es seguro llamarlo
# en cada rerun: CREATE TABLE IF NOT EXISTS no hace nada si ya existe.
init_db()

# Registra la visita de hoy (para la racha de estudio) una sola vez por sesión,
# apenas sepamos el nombre del estudiante (se setea en Inicio o en el Test).
if st.session_state.get("nombre_estudiante") and not st.session_state.get("_visita_registrada"):
    registrar_visita(st.session_state.nombre_estudiante)
    st.session_state["_visita_registrada"] = True

# Cuántas preguntas tomar de cada área para armar el diagnóstico
PREGUNTAS_POR_AREA = 3

# Instrucciones de sistema para el Chat IA: define el rol del tutor y los
# límites de tema. Esto se envía en cada llamada a Groq como mensaje "system",
# separado de lo que escribe el estudiante.
SYSTEM_PROMPT = """Eres un tutor experto en la prueba Saber 11 (ICFES) de Colombia, dentro de una app de preparación para el examen.

Tu rol:
- Ayudas a estudiantes de secundaria a entender temas de Matemáticas, Lectura Crítica, Ciencias Naturales, Sociales y Ciudadanas, e Inglés, tal como se evalúan en el ICFES.
- También puedes orientar sobre técnicas de estudio, manejo del tiempo, manejo de la ansiedad ante exámenes y estrategias para resolver preguntas de selección múltiple.
- Explicas paso a paso, con ejemplos claros y cercanos a la realidad de un estudiante colombiano.
- Tu tono es motivador, paciente y cercano, nunca condescendiente.

Límites importantes:
- Si el estudiante pregunta algo que NO tiene relación con el ICFES, las áreas del examen o la preparación académica (por ejemplo: chismes, temas personales de terceros, contenido para adultos, tareas de otras materias no relacionadas, opiniones políticas no académicas, etc.), respóndele amablemente que solo puedes ayudar con temas de estudio y preparación para el ICFES, y redirígelo a preguntar algo de esas áreas.
- No completes tareas que no tengan fines educativos relacionados con el ICFES (por ejemplo, no escribas código, no redactes mensajes personales, no des consejos ajenos al estudio).
- Responde siempre en español, salvo que el estudiante te pida practicar específicamente en inglés.
- Sé conciso: prioriza explicaciones claras sobre respuestas largas, salvo que el estudiante pida más detalle.
"""

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

/* ==== Decoración adicional: acentos, tarjetas y estados vacíos ==== */

/* Etiqueta pequeña tipo "eyebrow" sobre los títulos de cada sección */
.eyebrow {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #D97757 !important;
    background-color: rgba(217, 119, 87, 0.12);
    border: 1px solid rgba(217, 119, 87, 0.35);
    border-radius: 999px;
    padding: 0.2rem 0.75rem;
    margin-bottom: 0.7rem;
}

/* Grid de tarjetas de funcionalidades (página de Inicio) */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.9rem;
    margin: 1.3rem 0 0.5rem 0;
}
@media (max-width: 640px) {
    .feature-grid { grid-template-columns: 1fr; }
}
.feature-card {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-left: 3px solid #D97757;
    border-radius: 14px;
    padding: 1rem 1.1rem;
    transition: transform 0.15s ease, border-color 0.15s ease;
}
.feature-card:hover {
    transform: translateY(-2px);
    border-color: #D97757;
}
.feature-card .fc-icon {
    font-size: 1.4rem;
    margin-bottom: 0.4rem;
    display: block;
}
.feature-card .fc-title {
    font-weight: 600;
    color: #ECECE7 !important;
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
}
.feature-card .fc-desc {
    color: #A9A89F !important;
    font-size: 0.82rem;
    line-height: 1.4;
}

/* Estado vacío ilustrado, reemplaza los st.warning/st.info sueltos */
.empty-state {
    text-align: center;
    padding: 2.5rem 1.5rem;
    background-color: #2F2E2B;
    border: 1px dashed #4A4A47;
    border-radius: 16px;
    margin-top: 1rem;
}
.empty-state .es-icon {
    font-size: 2.2rem;
    display: block;
    margin-bottom: 0.6rem;
    opacity: 0.85;
}
.empty-state .es-title {
    font-weight: 600;
    color: #ECECE7 !important;
    font-size: 1.05rem;
    margin-bottom: 0.3rem;
}
.empty-state .es-desc {
    color: #A9A89F !important;
    font-size: 0.88rem;
    max-width: 420px;
    margin: 0 auto;
}

/* Métricas nativas de Streamlit con apariencia de tarjeta */
div[data-testid="stMetric"] {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-radius: 14px;
    padding: 0.9rem 1rem 0.7rem 1rem;
    margin-bottom: 0.5rem;
}
div[data-testid="stMetricLabel"] {
    color: #A9A89F !important;
}
div[data-testid="stMetricValue"] {
    color: #ECECE7 !important;
}

/* Footer del sidebar */
.sidebar-footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #3A3A37;
    font-size: 0.75rem;
    color: #8C8B84 !important;
    line-height: 1.6;
}
.sidebar-footer b { color: #ECECE7 !important; }

/* Flashcards generadas por IA */
.flashcard {
    border-radius: 18px;
    padding: 1.4rem 1.3rem;
    margin-top: 0.5rem;
    margin-bottom: 0.6rem;
    min-height: 130px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: background-color 0.2s ease, border-color 0.2s ease;
}
.flashcard.front {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-left: 4px solid #D97757;
}
.flashcard.back {
    background-color: #2A322B;
    border: 1px solid #3D453D;
    border-left: 4px solid #7FB88A;
}
.flashcard .fc-badge {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #A9A89F !important;
    margin-bottom: 0.7rem;
}
.flashcard .fc-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #D97757 !important;
    margin-bottom: 0.4rem;
}
.flashcard.back .fc-label {
    color: #7FB88A !important;
}
.flashcard .fc-content {
    font-size: 1.05rem;
    font-weight: 500;
    color: #ECECE7 !important;
    line-height: 1.5;
}

/* Banner de racha de estudio */
.streak-banner {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    background: linear-gradient(135deg, rgba(217,119,87,0.16), rgba(217,119,87,0.05));
    border: 1px solid rgba(217,119,87,0.35);
    border-radius: 16px;
    padding: 0.9rem 1.1rem;
    margin: 0.8rem 0 1.2rem 0;
}
.streak-banner .streak-flame {
    font-size: 1.8rem;
    line-height: 1;
}
.streak-banner .streak-count {
    font-weight: 700;
    color: #ECECE7 !important;
    font-size: 1rem;
}
.streak-banner .streak-sub {
    color: #B0AFA8 !important;
    font-size: 0.78rem;
    margin-top: 0.15rem;
}

/* Caja de análisis de IA (insight) */
.ai-insight {
    background-color: #2F2E2B;
    border: 1px solid #3F3E3A;
    border-left: 4px solid #D97757;
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    margin: 0.6rem 0 1.1rem 0;
}
.ai-insight .ai-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #D97757 !important;
    margin-bottom: 0.5rem;
}
.ai-insight .ai-text {
    color: #ECECE7 !important;
    font-size: 0.92rem;
    line-height: 1.6;
}

@media (max-width: 640px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }
    h1 { font-size: 1.6rem; }
}

/* ==== Ajustes mobile-first (la app se usa principalmente en celular) ==== */

/* Respeta el "notch"/barra inferior en iPhones cuando la PWA corre a pantalla completa */
.stApp {
    padding-bottom: env(safe-area-inset-bottom);
}

/* Botones y radios con área táctil mínima cómoda (~44px, estándar de accesibilidad táctil) */
div.stButton > button {
    min-height: 44px;
}
div[role="radiogroup"] label {
    min-height: 44px;
    display: flex;
    align-items: center;
}

/* En pantallas muy angostas, un poco menos de padding y texto más compacto */
@media (max-width: 400px) {
    .feature-card { padding: 0.85rem 0.9rem; }
    .flashcard { padding: 1.1rem 1rem; }
    div.stButton > button { padding: 0.5rem 1rem; }
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 IA Preparador ICFES")
st.subheader("Tu tutor inteligente para el Saber 11 - con Groq")

menu = st.sidebar.selectbox(
    "Menú",
    ["🏠 Inicio", "📝 Test Diagnóstico", "📊 Mis Resultados", "📚 Plan de Estudio IA", "🃏 Flashcards", "💬 Chat IA"],
)

if st.session_state.get("nombre_estudiante"):
    st.sidebar.caption(f"👤 Sesión: **{st.session_state.nombre_estudiante}**")
    racha_sidebar = calcular_racha(st.session_state.nombre_estudiante)
    if racha_sidebar > 0:
        st.sidebar.caption(f"🔥 Racha: **{racha_sidebar} día{'s' if racha_sidebar != 1 else ''}**")

st.sidebar.markdown("""
<div class="sidebar-footer">
<b>IA Preparador ICFES</b><br>
Diagnóstico · Plan de estudio · Flashcards · Chat<br>
Hecho con Streamlit + Groq
</div>
""", unsafe_allow_html=True)


# ==================== FUNCIONES AUXILIARES ====================
def generar_test():
    """Arma un test tomando PREGUNTAS_POR_AREA preguntas aleatorias de cada área."""
    preguntas = []
    contador_id = 1
    for area, lista_preguntas in BANCO_PREGUNTAS.items():
        seleccionadas = random.sample(lista_preguntas, min(PREGUNTAS_POR_AREA, len(lista_preguntas)))
        for p in seleccionadas:
            # Se copia el diccionario completo (**p) y luego se sobreescriben/agregan
            # id y area. Así, cualquier campo nuevo que agregues a una pregunta en
            # preguntas.py (visual, dificultad, imagen, etc.) viaja automáticamente
            # sin tener que acordarte de listarlo aquí a mano.
            preguntas.append({**p, "id": contador_id, "area": area})
            contador_id += 1
    random.shuffle(preguntas)
    return preguntas


def estimar_puntaje_icfes(puntaje_porcentual):
    """
    Aproximación simple: mapea el % de aciertos a la escala global ICFES (0-500).
    Es una estimación educativa, no un cálculo oficial del ICFES.
    """
    return round((puntaje_porcentual / 100) * 500)


def empty_state(icon, title, desc):
    """Tarjeta de estado vacío, reemplaza los st.warning/st.info sueltos."""
    st.markdown(f"""
    <div class="empty-state">
        <span class="es-icon">{icon}</span>
        <div class="es-title">{title}</div>
        <div class="es-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)


@st.cache_data(show_spinner=False, ttl=3600)
def generar_flashcard_ia(area, tema):
    """
    Genera (pregunta, respuesta) para una flashcard usando Groq.

    Se cachea por (area, tema) durante 1 hora: si dos estudiantes o dos
    sesiones piden flashcard del mismo tema, no se vuelve a llamar la API.
    Esto ahorra costo/latencia y mantiene el repaso consistente.
    """
    prompt = f"""Genera una flashcard de estudio para el examen ICFES (Saber 11) sobre el tema "{tema}", del área "{area}".

Responde ÚNICAMENTE en este formato exacto, sin texto adicional antes o después:
PREGUNTA: <una pregunta breve y clara sobre el tema>
RESPUESTA: <la respuesta correcta, clara y concisa, máximo 3 líneas>"""

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un generador de flashcards educativas para estudiantes colombianos que se preparan para el ICFES. Sé claro, conciso y pedagógico. Sigue el formato pedido al pie de la letra.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=250,
        )
        texto = completion.choices[0].message.content.strip()

        pregunta_fc, respuesta_fc = "", ""
        for linea in texto.splitlines():
            linea_limpia = linea.strip()
            if linea_limpia.upper().startswith("PREGUNTA:"):
                pregunta_fc = linea_limpia.split(":", 1)[1].strip()
            elif linea_limpia.upper().startswith("RESPUESTA:"):
                respuesta_fc = linea_limpia.split(":", 1)[1].strip()

        # Si el modelo no siguió el formato exacto, se usa un respaldo razonable
        if not pregunta_fc:
            pregunta_fc = f"¿Qué es {tema}?"
        if not respuesta_fc:
            respuesta_fc = texto if texto else "Repasa este tema en tus apuntes o con el Chat IA."

        return pregunta_fc, respuesta_fc

    except Exception:
        return (
            f"¿Qué es / cómo funciona {tema}?",
            "No se pudo generar la respuesta con IA en este momento. Intenta de nuevo o pregúntale al Chat IA.",
        )


def generar_analisis_falencias(nombre, puntaje, falencias):
    """
    Genera un análisis breve y personalizado de las falencias del estudiante
    usando Groq: qué patrón hay, por qué esos temas suelen costar, y qué
    reforzar primero. Devuelve None si falla la llamada (se maneja con un
    respaldo en la interfaz).
    """
    temas_txt = "\n".join(f"- {f['area']}: {f['tema']}" for f in falencias)
    prompt = f"""Un estudiante llamado {nombre} presentó un simulacro tipo ICFES y obtuvo {puntaje}% de aciertos.
Estas son las preguntas que falló, agrupadas por área y tema:
{temas_txt}

Escribe un análisis breve (máximo 120 palabras), en español, cercano y motivador, que explique:
1. Si hay un patrón o conclusión general entre estas falencias.
2. Por qué estos temas suelen costarles a los estudiantes.
3. Cuál debería reforzar primero y por qué.

No repitas la lista de temas tal cual (ya se muestra aparte), intégrala de forma natural en la explicación."""

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un tutor experto en el ICFES que da retroalimentación breve, cálida y accionable a partir de resultados de un diagnóstico.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=350,
        )
        return completion.choices[0].message.content.strip()
    except Exception:
        return None


def construir_system_prompt():
    """
    Arma el system prompt para el Chat IA. Si el estudiante ya tiene un
    diagnóstico en session_state, le añade contexto de sus falencias para que
    el tutor pueda personalizar sus respuestas sin que el estudiante tenga
    que repetir su situación cada vez.
    """
    prompt = SYSTEM_PROMPT
    resultados = st.session_state.get("resultados")
    if resultados and resultados.get("falencias"):
        temas = ", ".join(f"{f['area']} ({f['tema']})" for f in resultados["falencias"])
        prompt += f"""

Contexto del estudiante actual: en su último diagnóstico obtuvo {resultados['puntaje']}% de aciertos (estimado ICFES: {resultados.get('puntaje_icfes', '—')}/500). Sus falencias detectadas fueron: {temas}. Ten esto en cuenta cuando sea relevante: si pregunta algo relacionado con estos temas, profundiza un poco más ya que sabes que le cuestan; si pregunta algo distinto, respóndele con normalidad sin forzar la mención de sus falencias."""
    return prompt


ICONOS_AREA = {
    "Matemáticas": "🧮",
    "Lectura Crítica": "📖",
    "Ciencias Naturales": "🔬",
    "Sociales y Ciudadanas": "🌎",
    "Inglés": "🇬🇧",
}


def render_visual(visual):
    """
    Renderiza el elemento visual de una pregunta (tabla, gráfico de barras,
    gráfico de líneas o figura geométrica), dentro de una tarjeta con borde.
    El campo 'visual' de la pregunta define el 'tipo' y sus datos.

    Los gráficos de barras/líneas admiten dos formatos:
    - Una sola serie: {"categorias": [...], "valores": [...]}
    - Varias series:  {"categorias": [...], "series": {"Nombre A": [...], "Nombre B": [...]}}
    """
    tipo = visual.get("tipo")
    with st.container(border=True):
        if tipo == "tabla":
            st.caption("📋 Tabla de datos")
            df = pd.DataFrame(visual["datos"], columns=visual["columnas"])
            st.dataframe(df, use_container_width=True, hide_index=True)

        elif tipo == "grafico_barras":
            st.caption("📊 Gráfico de barras")
            if "series" in visual:
                df = pd.DataFrame(visual["series"], index=visual["categorias"])
                st.bar_chart(df)
            else:
                df = pd.DataFrame({"valor": visual["valores"]}, index=visual["categorias"])
                st.bar_chart(df, color="#D97757")

        elif tipo == "grafico_lineas":
            st.caption("📈 Gráfico de líneas")
            if "series" in visual:
                df = pd.DataFrame(visual["series"], index=visual["categorias"])
                st.line_chart(df)
            else:
                df = pd.DataFrame({"valor": visual["valores"]}, index=visual["categorias"])
                st.line_chart(df, color="#D97757")

        elif tipo == "figura_geometrica":
            st.caption("📐 Figura geométrica")
            st.markdown(visual["svg"], unsafe_allow_html=True)


def render_visuales(visual):
    """
    Acepta un solo visual (dict) o varios (lista de dicts, ej. una tabla de
    datos junto con el diagrama que la acompaña) y los renderiza en orden.
    """
    if not visual:
        return
    if isinstance(visual, list):
        for v in visual:
            render_visual(v)
    else:
        render_visual(visual)


# ==================== INICIO ====================
if menu == "🏠 Inicio":
    st.markdown('<span class="eyebrow">SABER 11 · ICFES</span>', unsafe_allow_html=True)

    nombre_home = st.text_input(
        "¿Cómo te llamas? (para guardar tu progreso y tu racha)",
        value=st.session_state.get("nombre_estudiante", ""),
    )
    if nombre_home.strip():
        st.session_state.nombre_estudiante = nombre_home.strip()

    if st.session_state.get("nombre_estudiante"):
        racha = calcular_racha(st.session_state.nombre_estudiante)
        if racha > 0:
            plural = "s" if racha != 1 else ""
            st.markdown(f"""
            <div class="streak-banner">
                <span class="streak-flame">🔥</span>
                <div>
                    <div class="streak-count">{racha} día{plural} seguido{plural} estudiando</div>
                    <div class="streak-sub">¡Vas muy bien! Vuelve mañana para no perder la racha.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("Bienvenido a tu preparador con IA. Haz el diagnóstico, descubre tus falencias y sigue un plan de estudio hecho a tu medida.")

    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <span class="fc-icon">📝</span>
            <div class="fc-title">Test Diagnóstico</div>
            <div class="fc-desc">15 preguntas de las 5 áreas del Saber 11 para medir tu nivel actual.</div>
        </div>
        <div class="feature-card">
            <span class="fc-icon">📊</span>
            <div class="fc-title">Mis Resultados</div>
            <div class="fc-desc">Consulta tu historial y la evolución de tu puntaje estimado en el tiempo.</div>
        </div>
        <div class="feature-card">
            <span class="fc-icon">📚</span>
            <div class="fc-title">Plan de Estudio IA</div>
            <div class="fc-desc">Un plan de 7 días enfocado en tus falencias, con recursos recomendados.</div>
        </div>
        <div class="feature-card">
            <span class="fc-icon">🃏</span>
            <div class="fc-title">Flashcards</div>
            <div class="fc-desc">Repasa con tarjetas interactivas los temas donde más lo necesitas.</div>
        </div>
        <div class="feature-card">
            <span class="fc-icon">💬</span>
            <div class="fc-title">Chat IA</div>
            <div class="fc-desc">Resuelve dudas puntuales con un tutor experto disponible 24/7.</div>
        </div>
        <div class="feature-card">
            <span class="fc-icon">🎯</span>
            <div class="fc-title">Enfocado en ti</div>
            <div class="fc-desc">Cada recomendación parte de tus propios resultados, no de un plan genérico.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.get("resultados"):
        res = st.session_state.resultados
        st.write("")
        st.success(f"Tu último diagnóstico: **{res['puntaje']}%** · Estimado ICFES **{res.get('puntaje_icfes', '—')}/500**. Ve a *Plan de Estudio IA* para continuar.")
    else:
        st.write("")
        st.caption(f"💡 El test diagnóstico incluye {PREGUNTAS_POR_AREA} preguntas aleatorias de cada una de las 5 áreas del Saber 11.")

# ==================== TEST DIAGNÓSTICO ====================
elif menu == "📝 Test Diagnóstico":
    st.markdown('<span class="eyebrow">DIAGNÓSTICO</span>', unsafe_allow_html=True)
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
                st.markdown(f"#### {ICONOS_AREA.get(area_actual, '')} {area_actual}")
            if p.get("fuente"):
                st.caption(f"📄 Pregunta oficial · {p['fuente']}")
            render_visuales(p.get("visual"))
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

                analisis_ia = None
                if falencias:
                    with st.spinner("Analizando tus resultados con IA..."):
                        analisis_ia = generar_analisis_falencias(nombre, puntaje, falencias)

                st.session_state.resultados = {
                    "nombre": nombre,
                    "puntaje": puntaje,
                    "puntaje_icfes": puntaje_icfes,
                    "falencias": falencias,
                    "analisis_ia": analisis_ia,
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
    st.markdown('<span class="eyebrow">PROGRESO</span>', unsafe_allow_html=True)
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
            empty_state("📭", "Todavía no hay resultados", "Realiza el Test Diagnóstico para empezar a construir tu historial de progreso.")
    else:
        empty_state("👋", "Ingresa tu nombre", "Escribe tu nombre arriba para consultar tu historial de resultados.")

# ==================== PLAN DE ESTUDIO ====================
elif menu == "📚 Plan de Estudio IA":
    st.markdown('<span class="eyebrow">PLAN PERSONALIZADO</span>', unsafe_allow_html=True)
    st.header("📚 Plan de Estudio Personalizado por IA")
    if st.session_state.get("resultados"):
        res = st.session_state.resultados
        falencias = res.get("falencias", [])

        st.write(f"**Estudiante:** {res['nombre']}")
        st.write(f"**Puntaje General:** {res['puntaje']}% · **Estimado ICFES:** {res.get('puntaje_icfes', '—')}/500")

        st.subheader("🎯 Análisis de la IA")
        if falencias:
            analisis_ia = res.get("analisis_ia")
            if analisis_ia:
                st.markdown(f"""
                <div class="ai-insight">
                    <div class="ai-label">✨ Análisis personalizado</div>
                    <div class="ai-text">{analisis_ia}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info("No fue posible generar el análisis con IA en este momento. Aquí tienes tus falencias de todas formas:")

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
        empty_state("🧭", "Aún no tienes un plan", "Realiza el Test Diagnóstico para que la IA arme un plan de estudio hecho a tu medida.")

# ==================== FLASHCARDS MEJORADAS (generadas con IA) ====================
elif menu == "🃏 Flashcards":
    st.markdown('<span class="eyebrow">REPASO</span>', unsafe_allow_html=True)
    st.header("🃏 Flashcards Interactivas")

    if st.session_state.get("resultados"):
        falencias = st.session_state.resultados.get("falencias", [])
        if not falencias:
            falencias = [{"area": "Ciencias Naturales", "tema": "Fotosíntesis"}]

        st.caption("Generadas con IA a partir de tus falencias del diagnóstico. Toca la tarjeta para voltearla.")

        for i, f in enumerate(falencias[:4]):
            area, tema = f["area"], f["tema"]

            if f"flipped_{i}" not in st.session_state:
                st.session_state[f"flipped_{i}"] = False

            with st.spinner(f"Generando flashcard de {tema}..."):
                pregunta_fc, respuesta_fc = generar_flashcard_ia(area, tema)

            # st.empty() reserva el espacio de la tarjeta ANTES del botón, así
            # la tarjeta queda arriba y el botón de voltear abajo (una sola
            # columna, cómodo para pulgar en celular en vez de dos columnas
            # angostas lado a lado).
            card_slot = st.empty()

            if st.button("🔄 Voltear tarjeta", key=f"flip_{i}", use_container_width=True):
                st.session_state[f"flipped_{i}"] = not st.session_state[f"flipped_{i}"]

            flipped = st.session_state[f"flipped_{i}"]
            cara_clase = "back" if flipped else "front"
            etiqueta = "RESPUESTA" if flipped else "PREGUNTA"
            contenido = respuesta_fc if flipped else pregunta_fc

            card_slot.markdown(f"""
            <div class="flashcard {cara_clase}">
                <div class="fc-badge">{ICONOS_AREA.get(area, '')} {area} · {tema}</div>
                <div class="fc-label">{etiqueta}</div>
                <div class="fc-content">{contenido}</div>
            </div>
            """, unsafe_allow_html=True)

            st.write("")
    else:
        empty_state("🃏", "Sin flashcards todavía", "Completa el Test Diagnóstico y aquí aparecerán tarjetas de repaso para tus temas más débiles.")

# ==================== CHAT IA CON GROQ ====================
elif menu == "💬 Chat IA":
    st.markdown('<span class="eyebrow">TUTOR IA</span>', unsafe_allow_html=True)
    st.header("💬 Chat con Tutor IA (Groq)")
    if not st.session_state.get("chat_history"):
        if st.session_state.get("resultados", {}).get("falencias"):
            st.caption("👋 Ya conozco los temas donde tuviste más dificultad en tu diagnóstico — pregúntame lo que necesites y lo tendré en cuenta.")
        else:
            st.caption("👋 Pregúntame cualquier duda sobre matemáticas, lectura crítica, ciencias, sociales o inglés para el ICFES.")

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
                mensajes_api = [{"role": "system", "content": construir_system_prompt()}] + st.session_state.chat_history
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=mensajes_api,
                    temperature=0.5,
                    max_tokens=800,
                )
                respuesta = completion.choices[0].message.content
            except Exception as e:
                respuesta = f"Error: {str(e)}"

        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)

st.caption("Proyecto IA para ICFES con Groq")
