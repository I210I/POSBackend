from entities.persona import Persona
from models.cliente import ClienteModel

def to_entity(model: ClienteModel) -> Persona:
    return Persona(
        id_cliente=getattr(model, 'id_cliente', None),
        nombre=getattr(model, 'nombre', None),
        direccion=getattr(model, 'direccion', None),
        telefono=getattr(model, 'telefono', None),
        correo=getattr(model, 'correo', None),
        estado=getattr(model, 'estado', None)
    )

def to_dto(entity: Persona) -> ClienteModel:
    return ClienteModel(
        id_cliente=getattr(entity, 'id_cliente', None),
        nombre=getattr(entity, 'nombre', None),
        direccion=getattr(entity, 'direccion', None),
        telefono=getattr(entity, 'telefono', None),
        correo=getattr(entity, 'correo', None),
        estado=getattr(entity, 'estado', None)
    )
