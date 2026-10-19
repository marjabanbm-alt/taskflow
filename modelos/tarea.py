class Tarea:
    def init(self, id_tarea, titulo, id_proyecto):
        self._id_tarea = id_tarea
        self._titulo = titulo
        self._id_proyecto = id_proyecto

    def get_id_tarea(self):
        return self._id_tarea

    def get_titulo(self):
        return self._titulo

    def get_id_proyecto(self):
        return self._id_proyecto

    def calcular_prioridad(self):
        return "Normal"

    def obtener_resumen(self, incluir_proyecto=False):
        if incluir_proyecto:
            return f"ID: {self._id_tarea} | Título: {self._titulo} | Proyecto ID: {self._id_proyecto}"
        return f"ID: {self._id_tarea} | Título: {self._titulo}"


class TareaSimple(Tarea):
    def init(self, id_tarea, titulo, id_proyecto, horas_estimadas):
        super().init(id_tarea, titulo, id_proyecto)
        self.horas_estimadas = horas_estimadas

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def calcular_prioridad(self):
        if self.horas_estimadas > 10:
            return "Alta"
        return "Media"


class TareaUrgente(Tarea):
    def init(self, id_tarea, titulo, id_proyecto, dias_retraso):
        super().init(id_tarea, titulo, id_proyecto)
        self.dias_retraso = dias_retraso

    def get_dias_retraso(self):
        return self.dias_retraso

    def calcular_prioridad(self):
        if self.dias_retraso > 3:
            return "CRÍTICA"
        return "Alta" 