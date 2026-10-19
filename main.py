from config.database import ConexionDB
from models.tarea import TareaSimple, TareaUrgente
from dao.tarea_dao import TareaDAO

if __name__ == "__main__":
    db = ConexionDB()
    db.inicializar_tablas()
    dao = TareaDAO(db)

    t1 = TareaSimple(None, "Diseñar Mockups", 1, 12.5)
    t2 = TareaUrgente(None, "Corregir Bug en Login", 1, 5)

    id1 = dao.crear(t1)
    id2 = dao.crear(t2)

    tareas = dao.listar_todas()
    for t in tareas:
        print(f"{t.obtener_resumen(incluir_proyecto=True)} | Prioridad: {t.calcular_prioridad()}")

    dao.actualizar_titulo(id1, "Diseñar Mockups UI/UX")
    dao.eliminar(id2)

    print("\nEstado final:")
    for t in dao.listar_todas():
        print(t.obtener_resumen())