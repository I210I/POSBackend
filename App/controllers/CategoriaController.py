from flask import Blueprint, jsonify, request
from repositories.categoria_repository import CategoriaRepository
from models.categoria import CategoriaModel
from mappers.categoria_mapper import to_entity, to_dto

categoria_bp = Blueprint('categoria', __name__)


# Listar categorías
@categoria_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    entidades = CategoriaRepository.listar_categorias()
    modelos = [to_dto(e).to_dict() for e in entidades]
    return jsonify(modelos), 200



# Crear categoría
@categoria_bp.route('/categorias', methods=['POST'])
def agregar_categoria():
    data = request.get_json()
    errors = CategoriaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    entidad = to_entity(data)
    success = CategoriaRepository.agregar(entidad)
    if not success:
        return jsonify({'error': 'No se pudo crear la categoría'}), 500
    return jsonify(to_dto(entidad)), 201



# Modificar categoría
@categoria_bp.route('/categorias/<int:id_categoria>', methods=['PUT'])
def modificar_categoria(id_categoria):
    data = request.get_json()
    errors = CategoriaModel().validate(data)
    if errors:
        return jsonify(errors), 400
    data['id_categoria'] = id_categoria
    entidad = to_entity(data)
    success = CategoriaRepository.modificar(entidad)
    if not success:
        return jsonify({'error': 'No se pudo modificar la categoría'}), 409
    return jsonify({'success': True}), 200


# Eliminar categoría
@categoria_bp.route('/categorias/<int:id_categoria>', methods=['DELETE'])
def eliminar_categoria(id_categoria):
    success = CategoriaRepository.eliminar(id_categoria)
    if not success:
        return jsonify({'error': 'No se pudo eliminar la categoría'}), 409
    return jsonify({'success': True}), 200
