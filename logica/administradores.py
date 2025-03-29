from usuarios import Usuarios
class GestorAdministrador:
    def agregar_estacion(self):
        pass

    def editar_estacion(self, id: int):
        pass

    def eliminar_estacion(self, id: int):
        pass


class Administrador(Usuarios):
    def _init_(self, id: int, estacion):
        self.id = id
        self.estacion = estacion
