from datetime import datetime

class Producto:
    def __init__(self, id_producto: int = None, codigo: str = None, nombre: str = None, descripcion: str = None,
                 categoria: int = None, precio_compra: float = None, precio_venta: float = None,
                 mayoreo: bool = None, pieza_mayoreo: int = None, precio_mayoreo: float = None,
                 stock: float = None, estado: bool = None, fecha_creacion: datetime = None):
        self.id_producto = id_producto
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.mayoreo = mayoreo
        self.pieza_mayoreo = pieza_mayoreo
        self.precio_mayoreo = precio_mayoreo
        self.stock = stock
        self.estado = estado
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'<Producto {self.id_producto} {self.nombre}>'
