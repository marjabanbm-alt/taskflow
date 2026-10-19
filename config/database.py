import sqlite3


class ConexionDB:
    def init(self, nombre_db="taskflow.db"):
        self.nombre_db = nombre_db

    def obtener_conexion(self):
        conn = sqlite3.connect(self.nombre_db)
        conn.row_factory = sqlite3.Row
        return conn

    def inicializar_tablas(self):
        with self.obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyectos (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tareas (
                    id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    id_proyecto INTEGER,
                    horas_estimadas REAL,
                    dias_retraso INTEGER,
                    FOREIGN KEY (id_proyecto) REFERENCES proyectos (id_proyecto)
                )
            """)
            conn.commit()