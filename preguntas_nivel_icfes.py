# ==================== BANCO PROPIO — NIVEL ICFES ====================
# Preguntas ORIGINALES (no son del examen real del ICFES) escritas para
# imitar el formato, la dificultad y los tipos de competencia que evalúa el
# Saber 11: paráfrasis, función de un fragmento, relación entre enunciados,
# inferencia, estrategia argumentativa, identificación de dimensiones/
# conflictos, causa-efecto, diseño experimental, interpretación de datos, etc.
#
# Se distinguen del banco realmente oficial (preguntas_oficiales.py) por el
# valor del campo "fuente": aquí es "Banco IA · nivel ICFES", nunca se debe
# confundir con una fuente real del Icfes.
#
# En Lectura Crítica, varias preguntas comparten el mismo texto de referencia
# (campo "visual" tipo "texto", repetido en cada pregunta del grupo) para
# imitar la estructura real de "Responda las preguntas X a Y de acuerdo con
# la siguiente información".

FUENTE_PROPIA_NIVEL_ICFES = "Banco IA · nivel ICFES"

# ---------- Texto 1: usado por 5 preguntas ----------
TEXTO_MULTITAREA = {
    "tipo": "texto",
    "titulo": "El mito de la multitarea",
    "contenido": (
        "Durante décadas, se promovió la idea de que hacer varias tareas al mismo tiempo —revisar el "
        "correo mientras se escribe un informe, o estudiar con la televisión encendida— era una habilidad "
        "deseable, casi una virtud del mundo moderno. Sin embargo, la investigación en neurociencia "
        "cognitiva ha demostrado que el cerebro humano no procesa dos tareas complejas de manera "
        "simultánea, sino que alterna rápidamente entre ellas. A este fenómeno se le llama 'cambio de "
        "tarea', y cada cambio tiene un costo cognitivo medible: la atención tarda varios segundos en "
        "reajustarse por completo a la nueva actividad.\n\n"
        "Este costo, aunque parezca mínimo, se acumula. Un estudio ampliamente citado encontró que las "
        "personas que alternan constantemente entre tareas cometen más errores y tardan, en promedio, un "
        "40 % más de tiempo en completar el mismo trabajo que quienes se concentran en una sola actividad "
        "a la vez. Además, la calidad del aprendizaje se ve afectada: la información procesada mientras se "
        "hace otra cosa se almacena de forma más superficial y es más difícil de recordar después.\n\n"
        "¿Por qué, entonces, persiste la creencia de que la multitarea es eficiente? Una explicación es que "
        "la sensación subjetiva de estar 'ocupado' se confunde con la de ser productivo. Alternar entre "
        "tareas genera una ilusión de dinamismo que resulta gratificante, aunque el resultado objetivo sea "
        "peor. Frente a esto, cada vez más especialistas recomiendan técnicas de trabajo enfocado, como "
        "bloques de tiempo dedicados a una sola tarea sin interrupciones, como una alternativa más efectiva "
        "—aunque menos estimulante en apariencia— que la multitarea."
    ),
}

# ---------- Texto 2: usado por 3 preguntas ----------
TEXTO_SEMAFORO = {
    "tipo": "texto",
    "titulo": "El semáforo en rojo",
    "contenido": (
        "Llevaba diez minutos frente al mismo semáforo en rojo, sin una sola razón aparente para que no "
        "cambiara. A mi alrededor, los demás conductores tocaban el claxon, sacaban la cabeza por la "
        "ventana, murmuraban maldiciones contra un sistema que, evidentemente, no los estaba escuchando. "
        "Yo, en cambio, apagué la radio y me quedé mirando un árbol al costado de la calle, uno que llevaba "
        "ahí, imagino, mucho más tiempo que el semáforo mismo. Pensé que quizás no era el semáforo el que "
        "estaba fallando, sino nuestra prisa la que había dejado de tener sentido hace rato. Diez minutos no "
        "son nada comparados con los años que ese árbol llevaba plantado sin moverse un centímetro, y sin "
        "embargo a nosotros, dentro de nuestras cajas de metal con ruedas, esos diez minutos nos parecían "
        "una eternidad insoportable. Cuando por fin la luz cambió a verde, casi lamenté que el momento "
        "terminara. Había algo extrañamente reconfortante en detenerse a mirar un árbol, algo que rara vez "
        "me permito hacer cuando tengo prisa por llegar a algún lugar."
    ),
}

LECTURA_CRITICA_NIVEL_ICFES = [
    {
        "tema": "Paráfrasis",
        "pregunta": "¿Cuál de las siguientes opciones es una paráfrasis adecuada de la primera oración del segundo párrafo del texto ('Este costo, aunque parezca mínimo, se acumula.')?",
        "opciones": [
            "El costo cognitivo del cambio de tarea es insignificante y no genera consecuencias notables.",
            "Aunque cada cambio de tarea implique un gasto de atención pequeño, estos gastos se suman con el tiempo.",
            "El costo económico de la multitarea aumenta con cada tarea adicional.",
            "La acumulación de tareas hace que el costo de cada una disminuya.",
        ],
        "correcta": "Aunque cada cambio de tarea implique un gasto de atención pequeño, estos gastos se suman con el tiempo.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_MULTITAREA,
    },
    {
        "tema": "Función de un fragmento",
        "pregunta": "En el texto 'El mito de la multitarea', la pregunta '¿Por qué, entonces, persiste la creencia de que la multitarea es eficiente?' cumple principalmente la función de:",
        "opciones": [
            "Presentar la tesis central del texto.",
            "Introducir una explicación sobre una aparente contradicción entre la evidencia y la creencia popular.",
            "Refutar directamente los datos presentados en el párrafo anterior.",
            "Concluir el texto resumiendo sus ideas principales.",
        ],
        "correcta": "Introducir una explicación sobre una aparente contradicción entre la evidencia y la creencia popular.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_MULTITAREA,
    },
    {
        "tema": "Relación entre enunciados",
        "pregunta": "Considere los siguientes enunciados tomados del texto: 1. 'la investigación en neurociencia cognitiva ha demostrado que el cerebro humano no procesa dos tareas complejas de manera simultánea'; 2. 'cada cambio [de tarea] tiene un costo cognitivo medible'. ¿Qué relación hay entre ambos enunciados?",
        "opciones": [
            "El enunciado 2 es una consecuencia que se deriva del fenómeno descrito en el enunciado 1.",
            "El enunciado 1 contradice lo afirmado en el enunciado 2.",
            "El enunciado 2 es un ejemplo aislado que no se relaciona con el enunciado 1.",
            "El enunciado 1 es una opinión personal del autor y el enunciado 2 es un dato objetivo.",
        ],
        "correcta": "El enunciado 2 es una consecuencia que se deriva del fenómeno descrito en el enunciado 1.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_MULTITAREA,
    },
    {
        "tema": "Propósito del autor",
        "pregunta": "¿Cuál es el propósito principal del autor en el texto 'El mito de la multitarea'?",
        "opciones": [
            "Narrar una anécdota personal sobre sus hábitos de trabajo.",
            "Cuestionar, con evidencia, una creencia popular sobre la productividad y proponer una alternativa.",
            "Describir el funcionamiento biológico del cerebro humano sin tomar postura.",
            "Persuadir al lector de que jamás debe usar la tecnología mientras trabaja.",
        ],
        "correcta": "Cuestionar, con evidencia, una creencia popular sobre la productividad y proponer una alternativa.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_MULTITAREA,
    },
    {
        "tema": "Inferencia",
        "pregunta": "A partir del texto 'El mito de la multitarea', se puede inferir que:",
        "opciones": [
            "La multitarea es más eficiente cuando las tareas son sencillas y no requieren atención.",
            "La sensación de estar ocupado no siempre coincide con un desempeño realmente productivo.",
            "El trabajo enfocado es una técnica reciente sin respaldo científico.",
            "El cerebro humano puede procesar cualquier cantidad de tareas sin costo alguno.",
        ],
        "correcta": "La sensación de estar ocupado no siempre coincide con un desempeño realmente productivo.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_MULTITAREA,
    },
    {
        "tema": "Idea principal",
        "pregunta": "¿Cuál es la idea principal que transmite el texto 'El semáforo en rojo'?",
        "opciones": [
            "Los semáforos en rojo son un problema de diseño urbano que debería corregirse.",
            "Una pausa forzada puede convertirse en una oportunidad para observar y reflexionar, algo que la prisa cotidiana suele impedir.",
            "Los árboles son más resistentes al paso del tiempo que los seres humanos.",
            "Es recomendable apagar la radio siempre que se conduce un vehículo.",
        ],
        "correcta": "Una pausa forzada puede convertirse en una oportunidad para observar y reflexionar, algo que la prisa cotidiana suele impedir.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_SEMAFORO,
    },
    {
        "tema": "Tono y actitud del narrador",
        "pregunta": "La actitud del narrador frente a la espera en el semáforo, en contraste con la de los demás conductores, puede describirse como:",
        "opciones": [
            "Igual de impaciente, pero más silenciosa.",
            "Indiferente, pues no le presta atención a lo que ocurre a su alrededor.",
            "Contemplativa, encontrando valor en un momento que los demás viven con frustración.",
            "Resignada, porque considera que no hay nada que hacer frente a la situación.",
        ],
        "correcta": "Contemplativa, encontrando valor en un momento que los demás viven con frustración.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_SEMAFORO,
    },
    {
        "tema": "Inferencia",
        "pregunta": "Del texto 'El semáforo en rojo' se puede inferir que el narrador:",
        "opciones": [
            "Suele detenerse a observar su entorno con frecuencia en su vida diaria.",
            "Vive generalmente apurado y pocas veces se permite momentos de pausa como el descrito.",
            "Considera que los árboles deberían reemplazar a los semáforos.",
            "Está enojado porque el semáforo tardó demasiado en cambiar.",
        ],
        "correcta": "Vive generalmente apurado y pocas veces se permite momentos de pausa como el descrito.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": TEXTO_SEMAFORO,
    },
]

SOCIALES_NIVEL_ICFES = [
    {
        "tema": "Identificación de conflictos de interés",
        "pregunta": "En un municipio costero, una empresa pesquera industrial solicitó permisos para ampliar sus operaciones en una zona donde pescadores artesanales han trabajado durante generaciones. La empresa argumenta que la ampliación generará más empleo formal y aumentará las exportaciones del municipio. Los pescadores artesanales sostienen que la pesca industrial a gran escala agotará los bancos de peces de los que depende su sustento diario. ¿Entre quiénes es más probable que se genere un conflicto según la situación descrita?",
        "opciones": [
            "Entre la empresa pesquera y el gobierno municipal.",
            "Entre la empresa pesquera y los pescadores artesanales.",
            "Entre los pescadores artesanales y los consumidores de pescado.",
            "Entre el gobierno municipal y los consumidores de pescado.",
        ],
        "correcta": "Entre la empresa pesquera y los pescadores artesanales.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Dimensiones en conflicto",
        "pregunta": "Un alcalde decide destinar los recursos previstos para la construcción de un parque público a la pavimentación de una vía que conecta con una zona industrial, argumentando que esto atraerá más inversión y empleo al municipio. Un grupo de ciudadanos protesta porque el parque era el único espacio verde disponible para las familias del sector. ¿Cuáles dimensiones están en conflicto en esta situación?",
        "opciones": ["La económica y la cultural.", "La económica y la social.", "La ambiental y la política.", "La cultural y la comercial."],
        "correcta": "La económica y la social.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Ramas del poder público (Colombia)",
        "pregunta": "Según la Constitución Política de Colombia, ¿cuál de las siguientes funciones corresponde a la rama legislativa del poder público?",
        "opciones": [
            "Administrar justicia en los procesos penales.",
            "Expedir las leyes que rigen al país.",
            "Ejecutar las políticas públicas del gobierno nacional.",
            "Vigilar el manejo de los recursos públicos.",
        ],
        "correcta": "Expedir las leyes que rigen al país.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Evaluación de argumentos",
        "pregunta": "Un funcionario público afirma que no es necesario declarar públicamente sus bienes porque eso hace parte de su vida privada y no afecta el ejercicio de su cargo. ¿Cuál de las siguientes opciones representa un argumento que contradice la postura del funcionario?",
        "opciones": [
            "La transparencia en el manejo de bienes por parte de funcionarios públicos previene conflictos de interés y actos de corrupción.",
            "La vida privada de los funcionarios públicos debe ser respetada en todo momento.",
            "Los funcionarios públicos tienen derecho a la intimidad como cualquier ciudadano.",
            "Declarar bienes públicamente puede exponer a los funcionarios a riesgos de seguridad.",
        ],
        "correcta": "La transparencia en el manejo de bienes por parte de funcionarios públicos previene conflictos de interés y actos de corrupción.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Modelos económicos",
        "pregunta": "El comercio justo es un modelo que busca garantizar condiciones de compra más equitativas para los pequeños productores de países en desarrollo, pagándoles un precio mínimo que no depende únicamente de las fluctuaciones del mercado internacional. ¿Cuál de las siguientes situaciones se ajusta a este modelo?",
        "opciones": [
            "Una empresa exportadora reduce el precio que paga a los caficultores cuando el precio internacional del café baja.",
            "Una cooperativa de agricultores negocia con una empresa un precio fijo por su cosecha, independiente de las variaciones del mercado mundial.",
            "Un intermediario compra la cosecha a bajo precio y la revende a mayor precio en mercados internacionales.",
            "Un gobierno subsidia únicamente a las grandes empresas exportadoras de su país.",
        ],
        "correcta": "Una cooperativa de agricultores negocia con una empresa un precio fijo por su cosecha, independiente de las variaciones del mercado mundial.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Desarrollo sostenible",
        "pregunta": "Un municipio planea construir viviendas de interés social. ¿Cuál de las siguientes decisiones reflejaría mejor un enfoque de desarrollo sostenible en este proyecto?",
        "opciones": [
            "Priorizar la construcción del mayor número de viviendas posible, sin importar el impacto ambiental de la zona.",
            "Diseñar las viviendas considerando tanto las necesidades habitacionales de las familias como la protección de las fuentes de agua cercanas.",
            "Destinar todo el presupuesto a la protección ambiental, posponiendo indefinidamente la construcción de viviendas.",
            "Construir las viviendas en la zona más barata disponible, sin consultar a la comunidad afectada.",
        ],
        "correcta": "Diseñar las viviendas considerando tanto las necesidades habitacionales de las familias como la protección de las fuentes de agua cercanas.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Mecanismos de participación ciudadana",
        "pregunta": "Un grupo de estudiantes universitarios, inconformes con una decisión administrativa de su universidad, decide recolectar firmas para solicitar que las directivas reconsideren la medida, sin que ninguno de ellos ocupe un cargo de representación estudiantil formal. Teniendo en cuenta los mecanismos de participación ciudadana, ¿pueden los estudiantes continuar con esta iniciativa?",
        "opciones": [
            "No, pues solo los representantes estudiantiles elegidos pueden dirigirse a las directivas.",
            "No, pues los estudiantes sin cargo formal no tienen derecho a manifestar su desacuerdo.",
            "Sí, pues la participación ciudadana no depende de ocupar un cargo de representación formal.",
            "Sí, pero solo si cuentan con la autorización previa de las directivas.",
        ],
        "correcta": "Sí, pues la participación ciudadana no depende de ocupar un cargo de representación formal.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Clientelismo y democracia",
        "pregunta": "En un municipio, un concejal promete gestionar un subsidio de vivienda a cambio de que los beneficiarios voten por su partido en las próximas elecciones. ¿Por qué esta práctica es problemática para el sistema democrático?",
        "opciones": [
            "Porque condiciona el acceso a un derecho social al apoyo político, distorsionando la libre decisión electoral de los ciudadanos.",
            "Porque los subsidios de vivienda no deberían existir en ningún caso.",
            "Porque los concejales no tienen la capacidad legal de gestionar subsidios.",
            "Porque las elecciones municipales no deberían realizarse con tanta frecuencia.",
        ],
        "correcta": "Porque condiciona el acceso a un derecho social al apoyo político, distorsionando la libre decisión electoral de los ciudadanos.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
]

CIENCIAS_NATURALES_NIVEL_ICFES = [
    {
        "tema": "Relaciones causa-efecto en ecosistemas",
        "pregunta": "En un lago, la introducción de una especie de pez no nativa provocó una disminución notable en la población de anfibios, ya que el pez se alimenta de los huevos y renacuajos que estos depositan en el agua. ¿Cuál de las siguientes es la causa directa de la disminución de anfibios en el lago?",
        "opciones": [
            "El aumento de la temperatura del agua del lago.",
            "La depredación de huevos y renacuajos por parte del pez introducido.",
            "La disminución de las plantas acuáticas del lago.",
            "La contaminación del agua por actividades humanas cercanas.",
        ],
        "correcta": "La depredación de huevos y renacuajos por parte del pez introducido.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Interpretación de datos poblacionales",
        "pregunta": "En una reserva natural se hizo seguimiento a la población de una especie de ave durante 5 años, después de la llegada de un patógeno que afecta su sistema respiratorio (tabla). ¿Cuál de las siguientes opciones describe mejor la tendencia de la población en ese periodo?",
        "opciones": [
            "La población se mantiene constante durante los 5 años.",
            "La población aumenta de forma constante durante los 5 años.",
            "La población disminuye progresivamente año a año.",
            "La población disminuye y luego se recupera por completo al quinto año.",
        ],
        "correcta": "La población disminuye progresivamente año a año.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": [
            {
                "tipo": "tabla",
                "columnas": ["Año", "Población de aves"],
                "datos": [[2020, 500], [2021, 420], [2022, 300], [2023, 150], [2024, 80]],
            },
            {
                "tipo": "grafico_lineas",
                "categorias": ["2020", "2021", "2022", "2023", "2024"],
                "valores": [500, 420, 300, 150, 80],
            },
        ],
    },
    {
        "tema": "Diseño experimental (variables)",
        "pregunta": "Un estudiante quiere comprobar que, entre más pequeños sean los trozos de una tableta antiácida, más rápido se disuelve en agua debido a la mayor superficie de contacto. Para esto, sumerge tres trozos de tamaños distintos (grande, mediano, pequeño) en vasos con la misma cantidad de agua a la misma temperatura, y mide el tiempo que tarda cada uno en disolverse por completo. ¿Cuál de las siguientes sería la variable dependiente en este experimento?",
        "opciones": [
            "El tamaño del trozo de tableta.",
            "La temperatura del agua.",
            "El tiempo que tarda cada trozo en disolverse.",
            "La cantidad de agua usada en cada vaso.",
        ],
        "correcta": "El tiempo que tarda cada trozo en disolverse.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Genética (cruces monohíbridos)",
        "pregunta": "En una especie de planta, el color morado de la flor (M) es dominante sobre el color blanco (m). Se cruza una planta homocigota morada (MM) con una planta blanca (mm). ¿Cuál sería el genotipo de toda la descendencia de la primera generación (F1)?",
        "opciones": [
            "MM (todas moradas homocigotas).",
            "Mm (todas moradas heterocigotas).",
            "mm (todas blancas).",
            "La mitad MM y la mitad mm.",
        ],
        "correcta": "Mm (todas moradas heterocigotas).",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Propiedades de sustancias",
        "pregunta": "Un estudiante tiene cuatro sustancias con las propiedades que se muestran en la tabla. Necesita usar una sustancia que hierva a menos de 100 °C, que no sea soluble en agua y que no conduzca electricidad. ¿Cuál sustancia debe elegir?",
        "opciones": ["Sustancia 1.", "Sustancia 2.", "Sustancia 3.", "Sustancia 4."],
        "correcta": "Sustancia 2.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
        "visual": {
            "tipo": "tabla",
            "columnas": ["Propiedad", "Sustancia 1", "Sustancia 2", "Sustancia 3", "Sustancia 4"],
            "datos": [
                ["Punto de ebullición (°C)", 120, 78, 350, 56],
                ["¿Es soluble en agua?", "Sí", "No", "No", "Sí"],
                ["¿Es conductora?", "No", "No", "No", "Sí"],
            ],
        },
    },
    {
        "tema": "Ley del inverso al cuadrado",
        "pregunta": "Un foco emite luz en todas direcciones. Se sabe que la intensidad de la luz que llega a una superficie es inversamente proporcional al cuadrado de la distancia entre el foco y la superficie. Si a 2 metros de distancia la intensidad es de 40 lux, ¿cuál sería aproximadamente la intensidad a 4 metros de distancia?",
        "opciones": ["80 lux.", "20 lux.", "10 lux.", "5 lux."],
        "correcta": "10 lux.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Ecología aplicada (objetivos de investigación)",
        "pregunta": "Investigadores estudian el efecto de una plaga de insectos que ataca los cultivos de café en una región. El insecto no tiene depredadores naturales en la zona y se ha extendido rápidamente afectando la producción de varios municipios. ¿Para cuál de los siguientes objetivos de investigación sería útil esta información?",
        "opciones": [
            "Determinar los factores que han causado la reducción de la producción cafetera en la región.",
            "Promover el uso de la plaga como método de control de otros cultivos.",
            "Establecer la cantidad de café que se exportaba antes de la llegada del insecto.",
            "Determinar el origen geográfico exacto del insecto invasor.",
        ],
        "correcta": "Determinar los factores que han causado la reducción de la producción cafetera en la región.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
    {
        "tema": "Fisiología del ejercicio (rangos de tolerancia)",
        "pregunta": "Un fisiólogo indica que, durante el ejercicio aeróbico, la frecuencia cardíaca de una persona debe mantenerse entre el 60 % y el 80 % de su frecuencia cardíaca máxima para obtener beneficios cardiovasculares óptimos, sin poner en riesgo su salud. La frecuencia cardíaca máxima se calcula, aproximadamente, restando la edad de la persona a 220. Un hombre de 40 años, mientras corre, alcanza una frecuencia cardíaca de 190 latidos por minuto. Considerando esta información, ¿su frecuencia cardíaca durante el ejercicio está dentro del rango recomendado?",
        "opciones": [
            "Sí, porque 190 está dentro del rango recomendado para su edad.",
            "No, porque 190 supera el rango recomendado (108 a 144 latidos por minuto) para su edad.",
            "Sí, porque cualquier frecuencia cardíaca durante el ejercicio es beneficiosa.",
            "No, porque su frecuencia cardíaca máxima debería ser de 220 latidos por minuto.",
        ],
        "correcta": "No, porque 190 supera el rango recomendado (108 a 144 latidos por minuto) para su edad.",
        "fuente": FUENTE_PROPIA_NIVEL_ICFES,
    },
]
