from entities.tienda import Tienda
from models.tienda import TiendaModel

def to_entity(model: TiendaModel) -> Tienda:
    return Tienda(
        id_tienda=getattr(model, 'id_tienda', None),
        razon_social=getattr(model, 'razon_social', None),
        documento=getattr(model, 'documento', None),
        correo=getattr(model, 'correo', None),
        telefono=getattr(model, 'telefono', None)
    )

def to_dto(entity: Tienda) -> TiendaModel:
    return TiendaModel(
        id_tienda=getattr(entity, 'id_tienda', None),
        razon_social=getattr(entity, 'razon_social', None),
        documento=getattr(entity, 'documento', None),
        correo=getattr(entity, 'correo', None),
        telefono=getattr(entity, 'telefono', None)
    )
