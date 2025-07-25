def login_dto_to_persona(data):
    # data es un dict validado por Marshmallow
    return {'usuario': data['usuario'], 'contrasena': data['contrasena']}
from entities.persona import Persona

def persona_to_user(persona: Persona):
    """Mapea una entidad Persona a un dict de usuario (UserDTO)"""
    return {
        'nombre': persona.nombre,
        'usuario': persona.usuario,
        'contrasena': persona.contrasena
    }

def persona_to_cliente(persona: Persona):
    """Mapea una entidad Persona a un dict de cliente (ClienteDTO)"""
    return {
        'nombre': persona.nombre,
        'telefono': persona.telefono
    }
