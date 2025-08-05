from entities.detalle_venta import DetalleVenta as DetalleVentaEntity
from models import db

class DetalleVentaRepository:
    @staticmethod
    def consultar_por_venta(id_venta):
        return DetalleVentaEntity.query.filter_by(id_venta=id_venta).all()

    @staticmethod
    def agregar(detalle: DetalleVentaEntity):
        db.session.add(detalle)
        db.session.commit()
        return True

    @staticmethod
    def eliminar(id_detalle):
        detalle = DetalleVentaEntity.query.get(id_detalle)
        if detalle:
            db.session.delete(detalle)
            db.session.commit()
            return True
        return False
