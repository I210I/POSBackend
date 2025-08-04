from datetime import datetime

class Venta:
    def __init__(self, id_venta: int = None, tipo_documento: str = None, numero_documento: str = None,
                 id_usuario: int = None, documento_cliente: str = None, nombre_cliente: str = None,
                 total_pagar: float = None, pago_con: float = None, cambio: float = None,
                 fecha_registro: datetime = None):
        self.id_venta = id_venta
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.id_usuario = id_usuario
        self.documento_cliente = documento_cliente
        self.nombre_cliente = nombre_cliente
        self.total_pagar = total_pagar
        self.pago_con = pago_con
        self.cambio = cambio
        self.fecha_registro = fecha_registro
