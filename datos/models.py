class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._email = email

    def get_id_usuario(self):
        return self._id_usuario

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email


class Tarea:
    def __init__(self, id_tarea, titulo, id_proyecto):
        self._id_tarea = id_tarea
        self._titulo = titulo
        self._id_proyecto = id_proyecto

    def get_id_tarea(self):
        return self._id_tarea

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_id_proyecto(self):
        return self._id_proyecto

    def calcular_prioridad(self):
        return "Normal"

    def obtener_resumen(self, incluir_proyecto=False):
        if incluir_proyecto:
            return f"ID: {self._id_tarea} | Título: {self._titulo} | Proyecto ID: {self._id_proyecto}"
        return f"ID: {self._id_tarea} | Título: {self._titulo}"


class TareaSimple(Tarea):
    def __init__(self, id_tarea, titulo, id_proyecto, horas_estimadas):
        super().__init__(id_tarea, titulo, id_proyecto)
        self._horas_estimadas = horas_estimadas

    def get_horas_estimadas(self):
        return self._horas_estimadas

    def calcular_prioridad(self):
        if self._horas_estimadas and self._horas_estimadas > 10:
            return "Alta"
        return "Media"


class TareaUrgente(Tarea):
    def __init__(self, id_tarea, titulo, id_proyecto, dias_retraso):
        super().__init__(id_tarea, titulo, id_proyecto)
        self._dias_retraso = dias_retraso

    def get_dias_retraso(self):
        return self._dias_retraso

    def calcular_prioridad(self):
        if self._dias_retraso and self._dias_retraso > 3:
            return "CRÍTICA"
        return "Alta"