import streamlit as st
from groq import Groq

# ==================== CONFIGURACIÓN GROQ ====================
API_KEY = ""   # ← Cambia esto

client = Groq(api_key=API_KEY)

st.set_page_config(page_title="IA Preparador ICFES", page_icon="🚀", layout="wide")
st.title("🚀 IA Preparador ICFES")
st.subheader("Tu tutor inteligente para el Saber 11 - con Groq")

menu = st.sidebar.selectbox("Menú", ["🏠 Inicio", "📝 Test Diagnóstico", "📊 Mis Resultados", "📚 Plan de Estudio IA", "🃏 Flashcards", "💬 Chat IA"])
# ==================== INICIO ====================
if menu == "🏠 Inicio":
    st.write("Bienvenido a tu IA para prepararte para el ICFES.")
    st.success("Usa el menú de la izquierda para navegar.")

# ==================== TEST DIAGNÓSTICO ====================
elif menu == "📝 Test Diagnóstico":
    st.header("📝 Test Diagnóstico Inicial")
    nombre = st.text_input("Tu nombre completo:")
    
    if st.button("🚀 Empezar Test"):
        st.session_state.test_iniciado = True
        st.session_state.respuestas = {}
        st.session_state.preguntas = [
            {"id": 1, "area": "Matemáticas", "tema": "Porcentajes", "pregunta": "¿Cuánto es el 15% de 200?", "opciones": ["20", "30", "40", "50"], "correcta": "30"},
            {"id": 2, "area": "Lectura Crítica", "tema": "Propósito del texto", "pregunta": "El propósito principal de un texto argumentativo es:", "opciones": ["Narrar", "Convencer", "Describir", "Informar"], "correcta": "Convencer"},
            {"id": 3, "area": "Ciencias Naturales", "tema": "Fotosíntesis", "pregunta": "¿Qué proceso permite a las plantas producir su alimento?", "opciones": ["Respiración", "Fotosíntesis", "Digestión", "Evaporación"], "correcta": "Fotosíntesis"},
        ]
    
    if st.session_state.get("test_iniciado", False):
        for p in st.session_state.preguntas:
            resp = st.radio(p['pregunta'], p['opciones'], key=f"q{p['id']}")
            st.session_state.respuestas[p['id']] = resp
        
        if st.button("✅ Finalizar Test"):
            aciertos = sum(1 for p in st.session_state.preguntas if st.session_state.respuestas.get(p['id']) == p['correcta'])
            puntaje = round((aciertos / len(st.session_state.preguntas)) * 100, 1)
            
            st.session_state.resultados = {
                "nombre": nombre,
                "puntaje": puntaje,
                "falencias": [p for p in st.session_state.preguntas if st.session_state.respuestas.get(p['id']) != p['correcta']]
            }
            st.success(f"¡Test completado! Puntaje: {puntaje}%")
            st.balloons()

# ==================== RESULTADOS ====================
elif menu == "📊 Mis Resultados":
    if st.session_state.get("resultados"):
        res = st.session_state.resultados
        st.write(f"**Estudiante:** {res['nombre']}")
        st.write(f"**Puntaje General:** {res['puntaje']}%")
    else:
        st.warning("Aún no has realizado el test.")

# ==================== PLAN DE ESTUDIO ====================
elif menu == "📚 Plan de Estudio IA":
    st.header("📚 Plan de Estudio Personalizado por IA")
    if st.session_state.get("resultados"):
        res = st.session_state.resultados
        falencias = res.get("falencias", [])
        
        st.write(f"**Estudiante:** {res['nombre']}")
        st.write(f"**Puntaje General:** {res['puntaje']}%")
        
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
                "area": f['area'],
                "tema": f['tema'],
                "actividades": [f"Estudiar teoría de {f['tema']} (30 min)", "Hacer 10 flashcards", "Resolver 5 ejercicios prácticos"],
                "recursos": [f"https://www.khanacademy.org/search?q={f['tema'].lower()}", "Caja de herramientas ICFES", "Quizlet ICFES"]
            })
        
        for p in plan:
            with st.expander(f"📅 {p['dia']}: {p['area']} - {p['tema']}"):
                st.write("**Actividades recomendadas:**")
                for act in p['actividades']:
                    st.write(f"- {act}")
                st.write("**Recursos útiles:**")
                for rec in p['recursos']:
                    st.write(f"- {rec}")
        
        st.subheader("🃏 Flashcards Generadas por IA")
        if falencias:
            for f in falencias[:2]:
                st.write(f"**Tema:** {f['tema']}")
                st.write("- **Pregunta:** ¿Qué es / Cómo funciona " + f['tema'] + "?")
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
                    # === CARA POSTERIOR (Respuesta) ===
                    st.success("**Respuesta:**")
                    if f['tema'] == "Fotosíntesis":
                        st.write("**Es el proceso por el cual las plantas convierten la luz solar, agua y CO₂ en glucosa y oxígeno.**")
                        st.write("Ecuación: 6CO₂ + 6H₂O + luz → C₆H₁₂O₆ + 6O₂")
                    else:
                        st.write(f"**Explicación clave:** {f['tema']} es un tema fundamental en el ICFES. Repasa definiciones, ejemplos y ejercicios típicos.")
                    st.info("💡 Repite esta respuesta en voz alta 3 veces")
                else:
                    # === CARA FRONTAL (Pregunta) ===
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
                    max_tokens=800
                )
                respuesta = completion.choices[0].message.content
            except Exception as e:
                respuesta = f"Error: {str(e)}"
        
        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)

st.caption("Proyecto IA para ICFES con Groq")
