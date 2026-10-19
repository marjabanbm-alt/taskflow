class Auxiliar:
    @staticmethod
    def validar_texto(texto: str) -> bool:
        return bool(texto and texto.strip())

    @staticmethod
    def validar_opcion(opcion: str, min_val: int, max_val: int) -> bool:
        if opcion.isdigit():
            val = int(opcion)
            return min_val <= val <= max_val
        return False
    