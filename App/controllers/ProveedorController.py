from flask import Blueprint, request, jsonify
from models.proveedor import ProveedorModel
from mappers.proveedor_mapper import to_entity, to_dto
from repositories.proveedor_repository import ProveedorRepository

proveedor_bp = Blueprint('proveedor', __name__)

# Listar proveedores
@proveedor_bp.route('/proveedores', methods=['GET'])
def listar_proveedores():
    proveedores = ProveedorRepository.listar() #TODO refactorizar a personas de tipo rpovedor
    proveedores_dto = [to_dto(p) for p in proveedores]
    return jsonify(proveedores_dto), 200

# Crear proveedor
@proveedor_bp.route('/proveedores', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    errors = ProveedorModel().validate(data)
    if errors:
        return jsonify(errors), 400
    proveedor = to_entity(data)
    success = ProveedorRepository.agregar(proveedor)
    if not success:
        return jsonify({'error': 'No se pudo crear el proveedor'}), 500
    return jsonify(to_dto(proveedor)), 201

# Modificar proveedor
@proveedor_bp.route('/proveedores/<int:id_proveedor>', methods=['PUT'])
def modificar_proveedor(id_proveedor):
    data = request.get_json()
    errors = ProveedorModel().validate(data)
    if errors:
        return jsonify(errors), 400
    proveedor = to_entity(data)
    proveedor.id_proveedor = id_proveedor
    success = ProveedorRepository.modificar(proveedor)
    if not success:
        return jsonify({'error': 'No se pudo modificar el proveedor'}), 404
    return jsonify({'success': True}), 200

# Eliminar proveedor
@proveedor_bp.route('/proveedores/<int:id_proveedor>', methods=['DELETE'])
def eliminar_proveedor(id_proveedor):
    success = ProveedorRepository.eliminar(id_proveedor)
    if not success:
        return jsonify({'error': 'No se pudo eliminar el proveedor'}), 404
    return jsonify({'success': True}), 200
