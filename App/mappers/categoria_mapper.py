from entities.categoria import Categoria as CategoriaEntity
from models.categoria import CategoriaModel

def to_entity(model: CategoriaModel) -> CategoriaEntity:
    return CategoriaEntity(
        id_categoria=model.id_categoria,
        descripcion_categoria=model.descripcion_categoria,
        estado=model.estado,
        fecha_creacion=model.fecha_creacion
    )

def to_dto(entity: CategoriaEntity) -> CategoriaModel:
    return CategoriaModel(
        id_categoria=entity.id_categoria,
        descripcion_categoria=entity.descripcion_categoria,
        estado=entity.estado,
        fecha_creacion=entity.fecha_creacion
    )
