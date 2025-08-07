from entities.detalle_venta import DetalleVenta
from models.detalle_venta import DetalleVentaModel

def to_entity(model: DetalleVentaModel) -> DetalleVenta:
    return DetalleVenta(
        id_detalle_venta=getattr(model, 'id_detalle_venta', None),
        id_venta=getattr(model, 'id_venta', None),
        id_producto=getattr(model, 'id_producto', None),
        cantidad=getattr(model, 'cantidad', None),
        precio_venta=getattr(model, 'precio_venta', None),
        subtotal=getattr(model, 'subtotal', None)
    )

def to_dto(entity: DetalleVenta) -> DetalleVentaModel:
    return DetalleVentaModel(
        id_detalle_venta=getattr(entity, 'id_detalle_venta', None),
        id_venta=getattr(entity, 'id_venta', None),
        id_producto=getattr(entity, 'id_producto', None),
        cantidad=getattr(entity, 'cantidad', None),
        precio_venta=getattr(entity, 'precio_venta', None),
        subtotal=getattr(entity, 'subtotal', None)
    )
