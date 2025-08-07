from entities.persona import Persona
from models.user import UserModel

def to_entity(model_data) -> Persona:
    return Persona(
        id_persona=model_data.get('id_persona'),
        nombre=model_data.get('nombre'),
        usuario=model_data.get('usuario'),
        clave=model_data.get('clave'),
        estado=model_data.get('estado')
    )

def to_dto(entity: Persona) -> dict:
    return {
        'id_persona': entity.id_persona,
        'nombre': entity.nombre,
        'usuario': entity.usuario,
        'estado': entity.estado
    }
