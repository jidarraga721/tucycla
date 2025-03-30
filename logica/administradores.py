from usuarios import Usuarios


class Administrador(Usuarios):
    def _init_(self, id: int, estacion):
        self.id = id
        self.estacion = estacion

    def agregar_estacion(self):
        pass

    def editar_estacion(self, id: int):
        pass

    def eliminar_estacion(self, id: int):
        pass

