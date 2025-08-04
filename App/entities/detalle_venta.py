from datetime import datetime

class DetalleVenta:
    def __init__(self, id_detalle_venta: int = None, id_venta: int = None, producto: int = None,
                 venta_caja: bool = None, precio_compra: float = None, cantidad: float = None,
                 cantidad_caja: float = None, precio_venta: float = None, subtotal: float = None,
                 fecha_registro: datetime = None):
        self.id_detalle_venta = id_detalle_venta
        self.id_venta = id_venta
        self.producto = producto
        self.venta_caja = venta_caja
        self.precio_compra = precio_compra
        self.cantidad = cantidad
        self.cantidad_caja = cantidad_caja
        self.precio_venta = precio_venta
        self.subtotal = subtotal
        self.fecha_registro = fecha_registro

    def __repr__(self):
        return f'<DetalleVenta {self.id_detalle_venta}>'
