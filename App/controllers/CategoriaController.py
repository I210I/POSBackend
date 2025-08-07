from flask import Blueprint, jsonify, request
from repositories.categoria_repository import CategoriaRepository
from models.categoria import CategoriaModel
from mappers.categoria_mapper import to_entity, to_dto

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    entidades = CategoriaRepository.listar_categorias()
    modelos = [to_dto(e).to_dict() for e in entidades]
    return jsonify(modelos)

@categoria_bp.route('/categorias', methods=['POST'])
def agregar_categoria():
    data = request.get_json()
    model = CategoriaModel(**data)
    entidad = to_entity(model)
    CategoriaRepository.agregar(entidad)
    return jsonify({'success': True}), 201

@categoria_bp.route('/categorias/<int:id_categoria>', methods=['PUT'])
def modificar_categoria(id_categoria):
    data = request.get_json()
    model = CategoriaModel(id_categoria=id_categoria, **data)
    entidad = to_entity(model)
    success = CategoriaRepository.modificar(entidad)
    return jsonify({'success': success})

@categoria_bp.route('/categorias/<int:id_categoria>', methods=['DELETE'])
def eliminar_categoria(id_categoria):
    success = CategoriaRepository.eliminar(id_categoria)
    return jsonify({'success': success})
