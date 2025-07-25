from flask import Blueprint, request, jsonify
from dtos.user_dto import UserDTO
from entities.persona import Persona
from mappers import persona_to_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    # Validar datos con DTO
    errors = UserDTO().validate(data)
    if errors:
        return jsonify(errors), 400
    # Crear entidad Persona
    persona = Persona(nombre=data['nombre'], usuario=data['usuario'], contrasena=data['contrasena'])
    # Mapear a DTO de respuesta
    user_dict = persona_to_user(persona)
    return jsonify(user_dict), 201
