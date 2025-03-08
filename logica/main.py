class GestorUsuarios:
    def registrar_usuario(self, id: int, nombre: str, correo: str, contrasena: str, rol: bool):
        pass

    def modificar_cuenta(self):
        pass

    def cambiar_contrasena(self):
        pass


class Usuarios:
    def _init_(self, nombre: str, correo: str, contrasena: str, rol: bool):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol


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


class GestorEstacion:
    def alquilar_bicicleta(self):
        pass

    def añadir_bicicleta(self):
        pass


class Estacion:
    def _init_(self, id: int, numero_bicicletas: int):
        self.id = id
        self.numero_bicicletas = numero_bicicletas


class Bicicleta:
    def _init_(self, estado: bool):
        self.estado = estado

    def cambiar_estado(self):
        pass


class Notificacion:
    def _init_(self, reserva: int, devolucion: int, mantenimiento: int):
        self.reserva = reserva
        self.devolucion = devolucion
        self.mantenimiento = mantenimiento


class Cliente(Usuarios):
    def _init_(self, id: int, historial: list):
        self.id = id
        self.historial = historial


class Quejas:
    def _init_(self, cliente: Cliente, razon: str, estado: bool):
        self.cliente = cliente
        self.razon = razon
        self.estado = estado


class GestorCliente:
    def crear_queja(self):
        pass

    def consultar_historial(self):
        pass


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