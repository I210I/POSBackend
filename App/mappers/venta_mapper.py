from entities.venta import Venta
from models.venta import VentaModel

def to_entity(model: VentaModel) -> Venta:
    return Venta(
        id_venta=getattr(model, 'id_venta', None),
        numero_documento=getattr(model, 'numero_documento', None),
        fecha_registro=getattr(model, 'fecha_registro', None),
        id_usuario=getattr(model, 'id_usuario', None),
        total_pagar=getattr(model, 'total_pagar', None),
        tipo_documento=getattr(model, 'tipo_documento', None),
        estado=getattr(model, 'estado', None)
    )

def to_dto(entity: Venta) -> VentaModel:
    return VentaModel(
        id_venta=getattr(entity, 'id_venta', None),
        numero_documento=getattr(entity, 'numero_documento', None),
        fecha_registro=getattr(entity, 'fecha_registro', None),
        id_usuario=getattr(entity, 'id_usuario', None),
        total_pagar=getattr(entity, 'total_pagar', None),
        tipo_documento=getattr(entity, 'tipo_documento', None),
        estado=getattr(entity, 'estado', None)
    )
