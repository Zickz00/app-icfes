"""
Módulo de persistencia con SQLite.

Guarda cada intento del test diagnóstico (nombre, puntaje, falencias, respuestas)
para poder mostrar historial y evolución del estudiante en el tiempo.

Nota para despliegue en Streamlit Cloud: el archivo .db vive en el disco del
contenedor. Persiste entre sesiones de usuarios mientras la app siga corriendo,
pero puede reiniciarse si la app se redespliega o duerme por inactividad
prolongada. Para un proyecto académico esto es suficiente; si luego quieres
persistencia 100% garantizada, se puede migrar a una base externa (Supabase,
Postgres, etc.) sin cambiar la forma en que el resto de la app llama a estas
funciones.
"""

import sqlite3
import json
from datetime import datetime

DB_PATH = "icfes_app.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    """Crea la tabla de resultados si no existe. Llamar una vez al inicio de app.py."""
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha TEXT NOT NULL,
            puntaje REAL NOT NULL,
            puntaje_icfes_estimado INTEGER,
            falencias_json TEXT,
            respuestas_json TEXT
        )
    """)
    conn.commit()
    conn.close()


def guardar_resultado(nombre, puntaje, puntaje_icfes, falencias, respuestas):
    """
    Guarda un intento del test diagnóstico.

    - nombre: str
    - puntaje: float (0-100)
    - puntaje_icfes: int (0-500 estimado)
    - falencias: list[dict] -> preguntas falladas (con area, tema, pregunta, etc.)
    - respuestas: dict -> {id_pregunta: respuesta_seleccionada}
    """
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO resultados (nombre, fecha, puntaje, puntaje_icfes_estimado, falencias_json, respuestas_json)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            nombre,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            puntaje,
            puntaje_icfes,
            json.dumps(falencias, ensure_ascii=False),
            json.dumps(respuestas, ensure_ascii=False),
        ),
    )
    conn.commit()
    conn.close()


def obtener_historial(nombre):
    """Devuelve todos los intentos de un estudiante, ordenados del más antiguo al más reciente."""
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        """
        SELECT id, fecha, puntaje, puntaje_icfes_estimado, falencias_json
        FROM resultados
        WHERE nombre = ?
        ORDER BY fecha ASC
        """,
        (nombre,),
    )
    rows = c.fetchall()
    conn.close()

    historial = []
    for row in rows:
        historial.append({
            "id": row[0],
            "fecha": row[1],
            "puntaje": row[2],
            "puntaje_icfes": row[3],
            "falencias": json.loads(row[4]) if row[4] else [],
        })
    return historial


def obtener_ultimo_resultado(nombre):
    """Devuelve el intento más reciente de un estudiante, o None si no tiene ninguno."""
    historial = obtener_historial(nombre)
    return historial[-1] if historial else None


def obtener_nombres_registrados():
    """Devuelve la lista de nombres distintos que ya han hecho el test (útil para un selector)."""
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT DISTINCT nombre FROM resultados ORDER BY nombre ASC")
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows]
