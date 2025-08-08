from entities.categoria import Categoria as CategoriaEntity

from models import db

class CategoriaRepository:
    @staticmethod
    def listar_categorias():
        return CategoriaEntity.query.all()


    @staticmethod
    def eliminar(id_categoria):
        try:
            categoria = CategoriaEntity.query.get(id_categoria)
            if categoria:
                db.session.delete(categoria)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Opcional: loggear el error e
            return False


    @staticmethod
    def agregar(new_categoria: CategoriaEntity):
        try:
            db.session.add(new_categoria)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # Opcional: loggear el error e
            return False


    @staticmethod
    def modificar(new_categoria: CategoriaEntity):
        try:
            categoria = CategoriaEntity.query.get(new_categoria.id_categoria)
            if categoria:
                categoria.descripcion_categoria = new_categoria.descripcion_categoria
                categoria.estado = new_categoria.estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Opcional: loggear el error e
            return False
