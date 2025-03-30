from usuarios import Usuarios



class Cliente(Usuarios):
    def _init_(self, id: int, historial: list):
        self.id = id
        self.historial = historial

    def crear_queja(self):
        pass

    def consultar_historial(self):
        pass

