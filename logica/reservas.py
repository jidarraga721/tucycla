class Reserva:
    def _init_(self, fecha: str, distancia: int, duracion: int, hora: int):
        self.fecha = fecha
        self.distancia = distancia
        self.duracion = duracion
        self.hora = hora


class GestorReserva:
    def crear_reserva(self):
        pass

    def eliminar_reserva(self):
        pass
