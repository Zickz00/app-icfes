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
