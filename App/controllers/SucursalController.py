from flask import Blueprint, request, jsonify
from models.tienda import TiendaModel
from mappers.tienda_mapper import to_entity, to_dto
from repositories.tienda_repository import TiendaRepository

sucursal_bp = Blueprint('sucursal', __name__)

# Listar sucursales (tiendas)
@sucursal_bp.route('/sucursales', methods=['GET'])
def listar_sucursales():
    sucursales = TiendaRepository.listar()
    sucursales_dto = [to_dto(s) for s in sucursales]
    return jsonify(sucursales_dto), 200

# Crear sucursal (tienda)
@sucursal_bp.route('/sucursales', methods=['POST'])
def crear_sucursal():
    data = request.get_json()
    errors = TiendaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    sucursal = to_entity(data)
    success = TiendaRepository.agregar(sucursal)
    if not success:
        return jsonify({'error': 'No se pudo crear la sucursal'}), 500
    return jsonify(to_dto(sucursal)), 201

# Modificar sucursal (tienda)
@sucursal_bp.route('/sucursales/<int:id_sucursal>', methods=['PUT'])
def modificar_sucursal(id_sucursal):
    data = request.get_json()
    errors = TiendaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    sucursal = to_entity(data)
    sucursal.id_tienda = id_sucursal
    success = TiendaRepository.modificar(sucursal)
    if not success:
        return jsonify({'error': 'No se pudo modificar la sucursal'}), 404
    return jsonify({'success': True}), 200

# Eliminar sucursal (tienda)
@sucursal_bp.route('/sucursales/<int:id_sucursal>', methods=['DELETE'])
def eliminar_sucursal(id_sucursal):
    success = TiendaRepository.eliminar(id_sucursal)
    if not success:
        return jsonify({'error': 'No se pudo eliminar la sucursal'}), 404
    return jsonify({'success': True}), 200
