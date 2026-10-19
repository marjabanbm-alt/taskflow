import sqlite3
import os

class ConexionDB:
    def __init__(self, nombre_db="taskflow.db"):
        self.nombre_db = nombre_db

    def obtener_conexion(self):
        conn = sqlite3.connect(self.nombre_db)
        conn.row_factory = sqlite3.Row
        return conn

    def inicializar_tablas(self):
        ruta_sql = os.path.join(os.path.dirname(__file__), '..', 'sql', 'esquema.sql')
        if os.path.exists(ruta_sql):
            with open(ruta_sql, 'r', encoding='utf-8') as f:
                script_sql = f.read()
            
            with self.obtener_conexion() as conn:
                cursor = conn.cursor()
                cursor.executescript(script_sql)
                conn.commit()