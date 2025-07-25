from models import PersonaModel

def find_persona_by_credentials(usuario, contrasena):
    return PersonaModel.query.filter_by(usuario=usuario, contrasena=contrasena).first()
