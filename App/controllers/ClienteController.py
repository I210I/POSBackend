from flask import Blueprint, request, jsonify
from models.cliente import ClienteModel
from mappers.cliente_mapper import to_entity, to_dto
from repositories.persona_repository import PersonaRepository

cliente_bp = Blueprint('cliente', __name__)


# Crear cliente
@cliente_bp.route('/cliente', methods=['POST'])
def create_cliente():
    data = request.get_json()
    errors = ClienteModel().validate(data)
    if errors:
        return jsonify(errors), 400
    persona = to_entity(data)
    success = PersonaRepository.agregar(persona)
    if not success:
        return jsonify({'error': 'No se pudo crear el cliente'}), 500
    return jsonify(to_dto(persona)), 201

# Listar clientes
@cliente_bp.route('/cliente', methods=['GET'])
def listar_clientes():
    personas = PersonaRepository.listar()
    clientes = [to_dto(p) for p in personas]
    return jsonify(clientes), 200

# Obtener cliente por ID
@cliente_bp.route('/cliente/<int:id_persona>', methods=['GET'])
def obtener_cliente(id_persona):
    persona = PersonaRepository.encontrar_persona_id(id_persona)
    if not persona:
        return jsonify({'error': 'Cliente no encontrado'}), 404
    return jsonify(to_dto(persona)), 200

# Modificar cliente
@cliente_bp.route('/cliente/<int:id_persona>', methods=['PUT'])
def modificar_cliente(id_persona):
    data = request.get_json()
    errors = ClienteModel().validate(data)
    if errors:
        return jsonify(errors), 400
    persona = to_entity(data)
    persona.id_persona = id_persona
    success = PersonaRepository.modificar(persona)
    if not success:
        return jsonify({'error': 'No se pudo modificar el cliente'}), 404
    return jsonify({'success': True}), 200

# Eliminar cliente
@cliente_bp.route('/cliente/<int:id_persona>', methods=['DELETE'])
def eliminar_cliente(id_persona):
    success = PersonaRepository.eliminar(id_persona)
    if not success:
        return jsonify({'error': 'No se pudo eliminar el cliente'}), 404
    return jsonify({'success': True}), 200
