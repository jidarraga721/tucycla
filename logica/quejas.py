from clientes import Cliente

class Quejas:
    def _init_(self, cliente: Cliente, razon: str, estado: bool):
        self.cliente = cliente
        self.razon = razon
        self.estado = estado