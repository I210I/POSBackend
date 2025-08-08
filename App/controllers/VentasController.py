from flask import Blueprint, request, jsonify
from models.venta import VentaModel
from mappers.venta_mapper import to_entity, to_dto
from repositories.venta_repository import VentaRepository

ventas_bp = Blueprint('ventas', __name__)

# Listar ventas
@ventas_bp.route('/ventas', methods=['GET'])
def listar_ventas():
    ventas = VentaRepository.listar()
    ventas_dto = [to_dto(v) for v in ventas]
    return jsonify(ventas_dto), 200

# Crear venta
@ventas_bp.route('/ventas', methods=['POST'])
def crear_venta():
    data = request.get_json()
    errors = VentaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    venta = to_entity(data)
    success = VentaRepository.agregar(venta)
    if not success:
        return jsonify({'error': 'No se pudo crear la venta'}), 500
    return jsonify(to_dto(venta)), 201

# Modificar venta
@ventas_bp.route('/ventas/<int:id_venta>', methods=['PUT'])
def modificar_venta(id_venta):
    data = request.get_json()
    errors = VentaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    venta = to_entity(data)
    venta.id_venta = id_venta
    success = VentaRepository.modificar(venta)
    if not success:
        return jsonify({'error': 'No se pudo modificar la venta'}), 404
    return jsonify({'success': True}), 200

# Eliminar venta
@ventas_bp.route('/ventas/<int:id_venta>', methods=['DELETE'])
def eliminar_venta(id_venta):
    success = VentaRepository.eliminar(id_venta)
    if not success:
        return jsonify({'error': 'No se pudo eliminar la venta'}), 404
    return jsonify({'success': True}), 200
