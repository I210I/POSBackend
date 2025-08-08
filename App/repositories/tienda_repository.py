from entities.tienda import Tienda as TiendaEntity
from models import db

class TiendaRepository:
    @staticmethod
    def encontrar(id_tienda):
        return TiendaEntity.query.get(id_tienda)

    @staticmethod
    def eliminar(id_tienda):
        try:
            tienda = TiendaEntity.query.get(id_tienda)
            if tienda:
                db.session.delete(tienda)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def agregar(new_tienda: TiendaEntity):
        try:
            db.session.add(new_tienda)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def modificar(new_tienda: TiendaEntity):
        try:
            tienda = TiendaEntity.query.get(new_tienda.id_tienda)
            if tienda:
                tienda.razon_social = new_tienda.razon_social
                tienda.documento = new_tienda.documento
                tienda.correo = new_tienda.correo
                tienda.telefono = new_tienda.telefono
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False
