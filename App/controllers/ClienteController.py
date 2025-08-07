from flask import Blueprint, request, jsonify
from dtos.cliente_dto import ClienteDTO
from entities.persona import Persona
from mappers import persona_to_cliente

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/cliente', methods=['POST'])
def create_cliente():
    data = request.get_json()
    # Validar datos con DTO
    errors = ClienteDTO().validate(data)
    if errors:
        return jsonify(errors), 400
    # Crear entidad Persona (sin usuario ni contraseña)
    persona = Persona(nombre=data['nombre'], telefono=data.get('telefono'))
    # Mapear a DTO de respuesta
    cliente_dict = persona_to_cliente(persona)
    return jsonify(cliente_dict), 201
