from usuarios import Usuarios

class GestorCliente:
    def crear_queja(self):
        pass

    def consultar_historial(self):
        pass

class Cliente(Usuarios):
    def _init_(self, id: int, historial: list):
        self.id = id
        self.historial = historial
