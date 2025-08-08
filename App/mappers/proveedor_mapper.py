from entities.proveedor import Proveedor
from models.proveedor import ProveedorModel

def to_entity(model: ProveedorModel) -> Proveedor:
    return Proveedor(
        id_proveedor=getattr(model, 'id_proveedor', None),
        documento=getattr(model, 'documento', None),
        razon_social=getattr(model, 'razon_social', None),
        correo=getattr(model, 'correo', None),
        telefono=getattr(model, 'telefono', None),
        estado=getattr(model, 'estado', None)
    )

def to_dto(entity: Proveedor) -> ProveedorModel:
    return ProveedorModel(
        id_proveedor=getattr(entity, 'id_proveedor', None),
        documento=getattr(entity, 'documento', None),
        razon_social=getattr(entity, 'razon_social', None),
        correo=getattr(entity, 'correo', None),
        telefono=getattr(entity, 'telefono', None),
        estado=getattr(entity, 'estado', None)
    )
