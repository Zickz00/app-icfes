# ==================== BANCO DE PREGUNTAS ICFES ====================
# Organizado por las 5 áreas evaluadas en el Saber 11.
# Cada pregunta tiene: tema, pregunta, opciones (4) y correcta.
#
# Para agregar más preguntas en el futuro, solo añade un nuevo diccionario
# a la lista del área correspondiente, siguiendo el mismo formato.

BANCO_PREGUNTAS = {
    "Matemáticas": [
        {
            "tema": "Porcentajes",
            "pregunta": "¿Cuánto es el 15% de 200?",
            "opciones": ["20", "30", "40", "50"],
            "correcta": "30",
        },
        {
            "tema": "Ecuaciones lineales",
            "pregunta": "Si 2x + 5 = 15, ¿cuál es el valor de x?",
            "opciones": ["3", "5", "10", "7"],
            "correcta": "5",
        },
        {
            "tema": "Proporcionalidad",
            "pregunta": "Si 4 obreros construyen un muro en 6 días, ¿cuántos días tardarán 8 obreros trabajando al mismo ritmo?",
            "opciones": ["12", "3", "6", "2"],
            "correcta": "3",
        },
        {
            "tema": "Estadística",
            "pregunta": "¿Cuál es la media aritmética de los números 4, 8, 6, 10?",
            "opciones": ["6", "7", "8", "9"],
            "correcta": "7",
        },
        {
            "tema": "Geometría",
            "pregunta": "¿Cuál es el área de un rectángulo de base 5 cm y altura 4 cm?",
            "opciones": ["9 cm²", "20 cm²", "18 cm²", "10 cm²"],
            "correcta": "20 cm²",
        },
        {
            "tema": "Probabilidad",
            "pregunta": "Al lanzar un dado, ¿cuál es la probabilidad de obtener un número par?",
            "opciones": ["1/6", "1/3", "1/2", "2/3"],
            "correcta": "1/2",
        },
        {
            "tema": "Funciones",
            "pregunta": "En la función f(x) = 2x + 3, ¿cuál es el valor de f(4)?",
            "opciones": ["7", "8", "11", "14"],
            "correcta": "11",
        },
        {
            "tema": "Razones y proporciones",
            "pregunta": "La razón entre 15 y 5 es:",
            "opciones": ["1/3", "3", "5", "15"],
            "correcta": "3",
        },
        {
            "tema": "Lectura de tablas",
            "pregunta": "La tabla muestra las ventas (en millones de pesos) de una tienda durante el primer semestre. ¿En qué mes se registraron las mayores ventas?",
            "opciones": ["Enero", "Marzo", "Mayo", "Junio"],
            "correcta": "Mayo",
            "visual": {
                "tipo": "tabla",
                "columnas": ["Mes", "Ventas (millones)"],
                "datos": [
                    ["Enero", 12],
                    ["Febrero", 15],
                    ["Marzo", 14],
                    ["Abril", 18],
                    ["Mayo", 22],
                    ["Junio", 19],
                ],
            },
        },
        {
            "tema": "Figuras geométricas",
            "pregunta": "Observa el triángulo rectángulo. Si su base mide 8 cm y su altura mide 6 cm, ¿cuál es su área?",
            "opciones": ["14 cm²", "24 cm²", "48 cm²", "28 cm²"],
            "correcta": "24 cm²",
            "visual": {
                "tipo": "figura_geometrica",
                "svg": "<svg viewBox='0 0 220 160' xmlns='http://www.w3.org/2000/svg'><polygon points='20,140 180,140 20,20' fill='rgba(217,119,87,0.15)' stroke='#D97757' stroke-width='3'/><line x1='20' y1='140' x2='180' y2='140' stroke='#ECECE7' stroke-width='2'/><line x1='20' y1='140' x2='20' y2='20' stroke='#ECECE7' stroke-width='2'/><text x='85' y='158' fill='#ECECE7' font-size='14'>8 cm</text><text x='-25' y='85' fill='#ECECE7' font-size='14' transform='rotate(-90 30,85)'>6 cm</text></svg>",
            },
        },
    ],
    "Lectura Crítica": [
        {
            "tema": "Propósito del texto",
            "pregunta": "El propósito principal de un texto argumentativo es:",
            "opciones": ["Narrar", "Convencer", "Describir", "Informar"],
            "correcta": "Convencer",
        },
        {
            "tema": "Idea principal",
            "pregunta": "La idea principal de un párrafo generalmente se encuentra en:",
            "opciones": [
                "Siempre al final",
                "La oración temática, en cualquier parte del párrafo",
                "Solo en el título",
                "Nunca es explícita",
            ],
            "correcta": "La oración temática, en cualquier parte del párrafo",
        },
        {
            "tema": "Inferencia",
            "pregunta": "Cuando un lector deduce información que no está explícita en el texto, está haciendo:",
            "opciones": ["Una copia", "Una inferencia", "Una cita", "Un resumen"],
            "correcta": "Una inferencia",
        },
        {
            "tema": "Tipos de texto",
            "pregunta": "Un texto que narra hechos reales o ficticios en orden cronológico es de tipo:",
            "opciones": ["Narrativo", "Argumentativo", "Expositivo", "Instructivo"],
            "correcta": "Narrativo",
        },
        {
            "tema": "Conectores",
            "pregunta": "El conector 'sin embargo' se usa para expresar:",
            "opciones": ["Causa", "Consecuencia", "Contraste u oposición", "Adición"],
            "correcta": "Contraste u oposición",
        },
        {
            "tema": "Figuras literarias",
            "pregunta": "La comparación explícita entre dos elementos usando 'como' se llama:",
            "opciones": ["Metáfora", "Símil o comparación", "Hipérbole", "Personificación"],
            "correcta": "Símil o comparación",
        },
        {
            "tema": "Punto de vista del autor",
            "pregunta": "Identificar la postura o intención del autor frente a un tema requiere analizar principalmente:",
            "opciones": [
                "Solo el título",
                "El tono y los argumentos usados",
                "La extensión del texto",
                "El número de párrafos",
            ],
            "correcta": "El tono y los argumentos usados",
        },
        {
            "tema": "Coherencia textual",
            "pregunta": "Un texto es coherente cuando:",
            "opciones": [
                "Tiene muchas palabras",
                "Sus ideas se relacionan lógicamente entre sí",
                "Usa solo oraciones cortas",
                "No tiene conectores",
            ],
            "correcta": "Sus ideas se relacionan lógicamente entre sí",
        },
    ],
    "Ciencias Naturales": [
        {
            "tema": "Fotosíntesis",
            "pregunta": "¿Qué proceso permite a las plantas producir su alimento?",
            "opciones": ["Respiración", "Fotosíntesis", "Digestión", "Evaporación"],
            "correcta": "Fotosíntesis",
        },
        {
            "tema": "Sistema circulatorio",
            "pregunta": "¿Cuál es la función principal del corazón en el sistema circulatorio?",
            "opciones": ["Filtrar el aire", "Bombear la sangre", "Producir glóbulos blancos", "Digerir alimentos"],
            "correcta": "Bombear la sangre",
        },
        {
            "tema": "Leyes de Newton",
            "pregunta": "La ley que establece que 'para toda acción hay una reacción igual y opuesta' es la:",
            "opciones": ["Primera ley de Newton", "Segunda ley de Newton", "Tercera ley de Newton", "Ley de gravitación"],
            "correcta": "Tercera ley de Newton",
        },
        {
            "tema": "Tabla periódica",
            "pregunta": "Los elementos de un mismo grupo (columna) en la tabla periódica comparten:",
            "opciones": [
                "El mismo número de neutrones",
                "Propiedades químicas similares",
                "La misma masa atómica",
                "El mismo color",
            ],
            "correcta": "Propiedades químicas similares",
        },
        {
            "tema": "Ecosistemas",
            "pregunta": "Los organismos que producen su propio alimento a partir de energía solar se llaman:",
            "opciones": ["Consumidores", "Descomponedores", "Productores", "Depredadores"],
            "correcta": "Productores",
        },
        {
            "tema": "Estados de la materia",
            "pregunta": "El proceso de pasar de estado líquido a gaseoso se llama:",
            "opciones": ["Condensación", "Evaporación", "Sublimación", "Fusión"],
            "correcta": "Evaporación",
        },
        {
            "tema": "ADN",
            "pregunta": "La molécula que contiene la información genética de los seres vivos es:",
            "opciones": ["ARN", "ATP", "ADN", "Proteína"],
            "correcta": "ADN",
        },
        {
            "tema": "Reacciones químicas",
            "pregunta": "En una reacción química, la masa total de los reactivos es ______ a la masa total de los productos.",
            "opciones": ["Mayor", "Menor", "Igual", "No relacionada"],
            "correcta": "Igual",
        },
        {
            "tema": "Interpretación de gráficos",
            "pregunta": "El gráfico muestra la temperatura registrada (°C) durante una semana. ¿En qué día se registró la temperatura más alta?",
            "opciones": ["Lunes", "Miércoles", "Viernes", "Domingo"],
            "correcta": "Viernes",
            "visual": {
                "tipo": "grafico_lineas",
                "categorias": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                "valores": [22, 24, 23, 26, 29, 27, 25],
            },
        },
    ],
    "Sociales y Ciudadanas": [
        {
            "tema": "Constitución Política",
            "pregunta": "¿En qué año fue promulgada la actual Constitución Política de Colombia?",
            "opciones": ["1886", "1991", "2001", "1970"],
            "correcta": "1991",
        },
        {
            "tema": "Poderes públicos",
            "pregunta": "En Colombia, ¿cuál rama del poder público se encarga de administrar justicia?",
            "opciones": ["Rama legislativa", "Rama ejecutiva", "Rama judicial", "Órganos de control"],
            "correcta": "Rama judicial",
        },
        {
            "tema": "Globalización",
            "pregunta": "La globalización se refiere principalmente a:",
            "opciones": [
                "El aislamiento económico de los países",
                "La interconexión económica, cultural y social entre países",
                "El fin del comercio internacional",
                "La eliminación de las fronteras políticas",
            ],
            "correcta": "La interconexión económica, cultural y social entre países",
        },
        {
            "tema": "Derechos humanos",
            "pregunta": "Los derechos humanos se caracterizan por ser:",
            "opciones": [
                "Exclusivos de algunos países",
                "Universales, inalienables e indivisibles",
                "Otorgados solo por el Estado",
                "Aplicables solo a adultos",
            ],
            "correcta": "Universales, inalienables e indivisibles",
        },
        {
            "tema": "Revolución Industrial",
            "pregunta": "La Revolución Industrial, iniciada en Inglaterra en el siglo XVIII, se caracterizó principalmente por:",
            "opciones": [
                "El auge del comercio esclavista",
                "La mecanización de la producción y el uso de nuevas fuentes de energía",
                "El fin del feudalismo en Europa",
                "La independencia de las colonias americanas",
            ],
            "correcta": "La mecanización de la producción y el uso de nuevas fuentes de energía",
        },
        {
            "tema": "Geografía de Colombia",
            "pregunta": "¿Cuál es la cordillera que se divide en tres ramales al entrar a Colombia?",
            "opciones": ["Cordillera de los Andes", "Sierra Nevada de Santa Marta", "Cordillera Central únicamente", "Macizo Colombiano"],
            "correcta": "Cordillera de los Andes",
        },
        {
            "tema": "Democracia",
            "pregunta": "La participación ciudadana a través del voto para elegir representantes es un ejemplo de democracia:",
            "opciones": ["Directa", "Representativa", "Autoritaria", "Monárquica"],
            "correcta": "Representativa",
        },
        {
            "tema": "Diversidad cultural",
            "pregunta": "Colombia es reconocida constitucionalmente como una nación:",
            "opciones": ["Monocultural", "Pluriétnica y multicultural", "Sin diversidad regional", "Homogénea lingüísticamente"],
            "correcta": "Pluriétnica y multicultural",
        },
        {
            "tema": "Análisis de datos poblacionales",
            "pregunta": "El gráfico muestra la población (en millones) de cuatro regiones de un país. ¿Cuál región tiene menor población?",
            "opciones": ["Región A", "Región B", "Región C", "Región D"],
            "correcta": "Región D",
            "visual": {
                "tipo": "grafico_barras",
                "categorias": ["Región A", "Región B", "Región C", "Región D"],
                "valores": [8.2, 5.6, 4.1, 2.3],
            },
        },
    ],
    "Inglés": [
        {
            "tema": "Present Simple",
            "pregunta": "Choose the correct sentence: She ___ to school every day.",
            "opciones": ["go", "goes", "going", "gone"],
            "correcta": "goes",
        },
        {
            "tema": "Vocabulary",
            "pregunta": "Choose the synonym of 'happy':",
            "opciones": ["Sad", "Angry", "Joyful", "Tired"],
            "correcta": "Joyful",
        },
        {
            "tema": "Reading Comprehension",
            "pregunta": "'The dog ran quickly because it was scared.' Why did the dog run?",
            "opciones": ["Because it was hungry", "Because it was scared", "Because it was happy", "Because it was tired"],
            "correcta": "Because it was scared",
        },
        {
            "tema": "Prepositions",
            "pregunta": "The book is ___ the table.",
            "opciones": ["in", "on", "at", "under"],
            "correcta": "on",
        },
        {
            "tema": "Past Tense",
            "pregunta": "Yesterday, I ___ to the park.",
            "opciones": ["go", "went", "goes", "going"],
            "correcta": "went",
        },
        {
            "tema": "Comparatives",
            "pregunta": "This car is ___ than that one.",
            "opciones": ["fast", "faster", "fastest", "more fast"],
            "correcta": "faster",
        },
        {
            "tema": "False Cognates",
            "pregunta": "The word 'embarrassed' in English means:",
            "opciones": ["Embarazada", "Avergonzado", "Embarazoso (situación)", "Enojado"],
            "correcta": "Avergonzado",
        },
        {
            "tema": "Question Words",
            "pregunta": "___ is your name?",
            "opciones": ["What", "Where", "When", "Why"],
            "correcta": "What",
        },
    ],
}

# ==================== FUSIÓN CON EL BANCO OFICIAL ICFES ====================
# Se agregan al banco propio las preguntas reales de cuadernillos oficiales
# del ICFES (ver preguntas_oficiales.py). Así, el test diagnóstico puede
# sacar tanto preguntas propias como preguntas oficiales verificadas, cada
# una identificable por su campo "fuente".
from preguntas_oficiales import MATEMATICAS_OFICIALES  # noqa: E402
from preguntas_nivel_icfes import (  # noqa: E402
    LECTURA_CRITICA_NIVEL_ICFES,
    SOCIALES_NIVEL_ICFES,
    CIENCIAS_NATURALES_NIVEL_ICFES,
)

BANCO_PREGUNTAS["Matemáticas"].extend(MATEMATICAS_OFICIALES)
BANCO_PREGUNTAS["Lectura Crítica"].extend(LECTURA_CRITICA_NIVEL_ICFES)
BANCO_PREGUNTAS["Sociales y Ciudadanas"].extend(SOCIALES_NIVEL_ICFES)
BANCO_PREGUNTAS["Ciencias Naturales"].extend(CIENCIAS_NATURALES_NIVEL_ICFES)
# A medida que se agreguen más preguntas oficiales reales del cuadernillo
# (Lectura Crítica, Sociales, Ciencias Naturales), se importan y extienden
# aquí de la misma manera que Matemáticas.
