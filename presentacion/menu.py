from negocio.gestor_tareas import GestorTareas
from datos.models import TareaSimple, TareaUrgente
from datos.auxiliar import Auxiliar

class MenuConsola:
    def __init__(self):
        self.gestor = GestorTareas()

    def iniciar(self):
        while True:
            print("\n==============================")
            print("     SISTEMA TASKFLOW - POO   ")
            print("==============================")
            print("1. Listar tareas")
            print("2. Crear tarea simple")
            print("3. Crear tarea urgente")
            print("4. Actualizar título de tarea")
            print("5. Eliminar tarea")
            print("6. Salir")

            opcion = input("Seleccione una opción (1-6): ")
            if not Auxiliar.validar_opcion(opcion, 1, 6):
                print("Opción inválida. Intente de nuevo.")
                continue

            op = int(opcion)
            if op == 1:
                self.listar()
            elif op == 2:
                self.crear_simple()
            elif op == 3:
                self.crear_urgente()
            elif op == 4:
                self.actualizar()
            elif op == 5:
                self.eliminar()
            elif op == 6:
                print("¡Hasta luego!")
                break

    def listar(self):
        print("\n--- LISTA DE TAREAS ---")
        tareas = self.gestor.listar_todas()
        if not tareas:
            print("No hay tareas registradas.")
        else:
            for t in tareas:
                print(f"{t.obtener_resumen(incluir_proyecto=True)} | Prioridad: {t.calcular_prioridad()}")

    def crear_simple(self):
        titulo = input("Título de la tarea: ")
        if not Auxiliar.validar_texto(titulo):
            print("Título no válido.")
            return
        horas = float(input("Horas estimadas: "))
        t = TareaSimple(None, titulo, 1, horas)
        self.gestor.crear_tarea(t)
        print("Tarea simple creada exitosamente.")

    def crear_urgente(self):
        titulo = input("Título de la tarea: ")
        if not Auxiliar.validar_texto(titulo):
            print("Título no válido.")
            return
        dias = int(input("Días de retraso: "))
        t = TareaUrgente(None, titulo, 1, dias)
        self.gestor.crear_tarea(t)
        print("Tarea urgente creada exitosamente.")

    def actualizar(self):
        self.listar()
        id_t = int(input("\nIngrese ID de la tarea a actualizar: "))
        nuevo_titulo = input("Nuevo título: ")
        if self.gestor.actualizar_titulo(id_t, nuevo_titulo):
            print("Tarea actualizada.")
        else:
            print("No se encontró la tarea.")

    def eliminar(self):
        self.listar()
        id_t = int(input("\nIngrese ID de la tarea a eliminar: "))
        if self.gestor.eliminar_tarea(id_t):
            print("Tarea eliminada.")
        else:
            print("No se encontró la tarea.")