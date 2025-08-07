from models.login import LoginModel

def to_entity(model_data) -> dict:
    return {
        'usuario': model_data.get('usuario'),
        'clave': model_data.get('clave')
    }

def to_dto(entity) -> dict:
    return {
        'usuario': entity.get('usuario')
    }
