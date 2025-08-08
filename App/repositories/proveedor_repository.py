from entities.proveedor import Proveedor
from models import db
from sqlalchemy.exc import SQLAlchemyError

class ProveedorRepository:
    @staticmethod
    def listar():
        try:
            # Suponiendo que tipo_persona=2 es proveedor
            return Proveedor.query.filter_by(estado=True).all()
        except SQLAlchemyError:
            return []

    @staticmethod
    def agregar(proveedor: Proveedor):
        try:
            db.session.add(proveedor)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    @staticmethod
    def modificar(proveedor: Proveedor):
        try:
            proveedor_db = Proveedor.query.get(proveedor.id_proveedor)
            if not proveedor_db:
                return False
            proveedor_db.documento = proveedor.documento
            proveedor_db.razon_social = proveedor.razon_social
            proveedor_db.correo = proveedor.correo
            proveedor_db.telefono = proveedor.telefono
            proveedor_db.estado = proveedor.estado
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    @staticmethod
    def eliminar(id_proveedor):
        try:
            proveedor = Proveedor.query.get(id_proveedor)
            if not proveedor:
                return False
            proveedor.estado = False
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False
