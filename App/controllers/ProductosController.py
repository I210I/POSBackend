from flask import Blueprint, request, jsonify
from models.producto import ProductoModel
from mappers.producto_mapper import to_entity, to_dto
from repositories.producto_repository import ProductoRepository

productos_bp = Blueprint('productos', __name__)

# Listar productos
@productos_bp.route('/productos', methods=['GET'])
def listar_productos():
    productos = ProductoRepository.listar_productos()
    productos_dto = [to_dto(p) for p in productos]
    return jsonify(productos_dto), 200

# Crear producto
@productos_bp.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    errors = ProductoModel().validate(data)
    if errors:
        return jsonify(errors), 400
    producto = to_entity(data)
    success = ProductoRepository.agregar(producto)
    if not success:
        return jsonify({'error': 'No se pudo crear el producto'}), 500
    return jsonify(to_dto(producto)), 201

# Modificar producto
@productos_bp.route('/productos/<int:id_producto>', methods=['PUT'])
def modificar_producto(id_producto):
    data = request.get_json()
    errors = ProductoModel().validate(data)
    if errors:
        return jsonify(errors), 400
    producto = to_entity(data)
    producto.id_producto = id_producto
    success = ProductoRepository.modificar(producto)
    if not success:
        return jsonify({'error': 'No se pudo modificar el producto'}), 404
    return jsonify({'success': True}), 200

# Eliminar producto
@productos_bp.route('/productos/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    success = ProductoRepository.eliminar(id_producto)
    if not success:
        return jsonify({'error': 'No se pudo eliminar el producto'}), 404
    return jsonify({'success': True}), 200
