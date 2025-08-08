from entities.venta import Venta
from entities.detalle_venta import DetalleVenta
from mappers.detalle_venta_mapper import to_entity as detalle_to_entity, to_dto as detalle_to_dto
from models.venta import VentaModel

def to_entity(model: VentaModel) -> Venta:
    detalles = []
    detalles_data = getattr(model, 'detalles', None)
    if detalles_data:
        for d in detalles_data:
            detalles.append(detalle_to_entity(d))
    return Venta(
        id_venta=getattr(model, 'id_venta', None),
        numero_documento=getattr(model, 'numero_documento', None),
        fecha_registro=getattr(model, 'fecha_registro', None),
        id_usuario=getattr(model, 'id_usuario', None),
        total_pagar=getattr(model, 'total_pagar', None),
        tipo_documento=getattr(model, 'tipo_documento', None),
        estado=getattr(model, 'estado', None),
        detalles_venta=detalles
    )

def to_dto(entity: Venta) -> VentaModel:
    detalles = []
    if hasattr(entity, 'detalles_venta') and entity.detalles_venta:
        for d in entity.detalles_venta:
            detalles.append(detalle_to_dto(d))
    return VentaModel(
        id_venta=getattr(entity, 'id_venta', None),
        numero_documento=getattr(entity, 'numero_documento', None),
        fecha_registro=getattr(entity, 'fecha_registro', None),
        id_usuario=getattr(entity, 'id_usuario', None),
        total_pagar=getattr(entity, 'total_pagar', None),
        tipo_documento=getattr(entity, 'tipo_documento', None),
        estado=getattr(entity, 'estado', None),
        detalles=detalles
    )
