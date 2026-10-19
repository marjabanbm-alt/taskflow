from datos.conexion import ConexionDB
from datos.models import TareaSimple, TareaUrgente

class GestorTareas:
    def __init__(self):
        self.db = ConexionDB()

    def crear_tarea(self, tarea):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()

        if isinstance(tarea, TareaSimple):
            cursor.execute(
                "INSERT INTO tareas (titulo, tipo, id_proyecto, horas_estimadas) VALUES (?, ?, ?, ?)",
                (tarea.get_titulo(), "SIMPLE", tarea.get_id_proyecto(), tarea.get_horas_estimadas())
            )
        elif isinstance(tarea, TareaUrgente):
            cursor.execute(
                "INSERT INTO tareas (titulo, tipo, id_proyecto, dias_retraso) VALUES (?, ?, ?, ?)",
                (tarea.get_titulo(), "URGENTE", tarea.get_id_proyecto(), tarea.get_dias_retraso())
            )

        conn.commit()
        id_generado = cursor.lastrowid
        conn.close()
        return id_generado

    def listar_todas(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas")
        registros = cursor.fetchall()
        conn.close()

        lista_objetos = []
        for reg in registros:
            if reg["tipo"] == "SIMPLE":
                obj = TareaSimple(reg["id_tarea"], reg["titulo"], reg["id_proyecto"], reg["horas_estimadas"])
            else:
                obj = TareaUrgente(reg["id_tarea"], reg["titulo"], reg["id_proyecto"], reg["dias_retraso"])
            lista_objetos.append(obj)
        return lista_objetos

    def actualizar_titulo(self, id_tarea, nuevo_titulo):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET titulo = ? WHERE id_tarea = ?", (nuevo_titulo, id_tarea))
        conn.commit()
        filas = cursor.rowcount
        conn.close()
        return filas > 0

    def eliminar_tarea(self, id_tarea):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id_tarea = ?", (id_tarea,))
        conn.commit()
        filas = cursor.rowcount
        conn.close()
        return filas > 0