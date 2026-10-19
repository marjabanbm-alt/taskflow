class Proyecto:
    def init(self, id_proyecto, nombre, descripcion=""):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas = []
        self.miembros = []

    def get_id_proyecto(self):
        return self.id_proyecto

    def get_nombre(self):
        return self.nombre

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def agregar_miembro(self, usuario):
        self.miembros.append(usuario)

    def get_tareas(self):
        return self.tareas