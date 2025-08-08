from flask import Blueprint, request, jsonify
from models.usuario import UsuarioModel
from mappers.user_mapper import to_entity, to_dto
from repositories.persona_repository import PersonaRepository

usuario_bp = Blueprint('usuario', __name__)

# Listar usuarios
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = PersonaRepository.listar_usuarios()
    usuarios_dto = [to_dto(u) for u in usuarios]
    return jsonify(usuarios_dto), 200

# Crear usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    errors = UsuarioModel().validate(data)
    if errors:
        return jsonify(errors), 400
    usuario = to_entity(data)
    usuario.tipo_persona = 3  # Suponiendo 3 = usuario
    success = PersonaRepository.agregar(usuario)
    if not success:
        return jsonify({'error': 'No se pudo crear el usuario'}), 500
    return jsonify(to_dto(usuario)), 201

# Modificar usuario
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    data = request.get_json()
    errors = UsuarioModel().validate(data)
    if errors:
        return jsonify(errors), 400
    usuario = to_entity(data)
    usuario.id_persona = id_usuario
    success = PersonaRepository.modificar(usuario)
    if not success:
        return jsonify({'error': 'No se pudo modificar el usuario'}), 404
    return jsonify({'success': True}), 200

# Eliminar usuario
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    success = PersonaRepository.eliminar(id_usuario)
    if not success:
        return jsonify({'error': 'No se pudo eliminar el usuario'}), 404
    return jsonify({'success': True}), 200
