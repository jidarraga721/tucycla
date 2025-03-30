


class Usuarios:
    def _init_(self, nombre: str, correo: str, contrasena: str, rol: bool):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def registrar_usuario(self, id: int, nombre: str, correo: str, contrasena: str, rol: bool):
        pass

    def modificar_cuenta(self):
        pass

    def cambiar_contrasena(self):
        pass