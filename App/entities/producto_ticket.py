class ProductoTicket:
    def __init__(self, id_producto: int = None, codigo: str = None, nombre_producto: str = None,
                 venta_caja: bool = None, mayoreo: bool = None, pieza_mayoreo: int = None,
                 precio_mayoreo: float = None, cantidad: float = None, cantidad_caja: float = None,
                 precio_compra: float = None, precio_venta: float = None, subtotal: float = None):
        self.id_producto = id_producto
        self.codigo = codigo
        self.nombre_producto = nombre_producto
        self.venta_caja = venta_caja
        self.mayoreo = mayoreo
        self.pieza_mayoreo = pieza_mayoreo
        self.precio_mayoreo = precio_mayoreo
        self.cantidad = cantidad
        self.cantidad_caja = cantidad_caja
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.subtotal = subtotal

    def __repr__(self):
        return f'<ProductoTicket {self.id_producto} {self.nombre_producto}>'
