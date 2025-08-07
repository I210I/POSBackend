from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from repositories.persona_repository import PersonaRepository
from repositories.persona_repository import PersonaRepository

autenticacion_bp = Blueprint('autenticacion', __name__)

@autenticacion_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')
    if not usuario or not contrasena:
        return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400
    persona = PersonaRepository.encontrar_persona_por_usuario_clave(usuario, contrasena)
    if not persona:
        return jsonify({'error': 'Credenciales inválidas'}), 401
    return jsonify({'nombre': persona.nombre}), 200
