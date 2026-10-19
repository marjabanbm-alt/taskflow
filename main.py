from datos.conexion import ConexionDB
from presentacion.menu import MenuConsola

if __name__ == "__main__":
    db = ConexionDB()
    db.inicializar_tablas()
    
    menu = MenuConsola()
    menu.iniciar()