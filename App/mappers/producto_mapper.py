from entities.producto import Producto
from models.producto import ProductoModel

def to_entity(model: ProductoModel) -> Producto:
    return Producto(
        id_producto=getattr(model, 'id_producto', None),
        codigo=getattr(model, 'codigo', None),
        nombre=getattr(model, 'nombre', None),
        descripcion=getattr(model, 'descripcion', None),
        stock=getattr(model, 'stock', None),
        precio_compra=getattr(model, 'precio_compra', None),
        precio_venta=getattr(model, 'precio_venta', None),
        cajas=getattr(model, 'cajas', None),
        piezas_mayoreo=getattr(model, 'piezas_mayoreo', None),
        precio_mayoreo=getattr(model, 'precio_mayoreo', None),
        categoria=getattr(model, 'categoria', None),
        estado=getattr(model, 'estado', None)
    )

def to_dto(entity: Producto) -> ProductoModel:
    return ProductoModel(
        id_producto=getattr(entity, 'id_producto', None),
        codigo=getattr(entity, 'codigo', None),
        nombre=getattr(entity, 'nombre', None),
        descripcion=getattr(entity, 'descripcion', None),
        stock=getattr(entity, 'stock', None),
        precio_compra=getattr(entity, 'precio_compra', None),
        precio_venta=getattr(entity, 'precio_venta', None),
        cajas=getattr(entity, 'cajas', None),
        piezas_mayoreo=getattr(entity, 'piezas_mayoreo', None),
        precio_mayoreo=getattr(entity, 'precio_mayoreo', None),
        categoria=getattr(entity, 'categoria', None),
        estado=getattr(entity, 'estado', None)
    )
