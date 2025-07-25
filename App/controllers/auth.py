from flask import Blueprint, request, jsonify
from dtos.login_dto import LoginDTO
from mappers import login_dto_to_persona
from repositories.persona_repository import find_persona_by_credentials

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    errors = LoginDTO().validate(data)
    if errors:
        return jsonify(errors), 400
    credenciales = login_dto_to_persona(data)
    persona = find_persona_by_credentials(**credenciales)
    if not persona:
        return jsonify({'error': 'Credenciales inválidas'}), 401
    return jsonify({'nombre': persona.nombre}), 200
