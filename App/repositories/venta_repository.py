from entities.venta import Venta as VentaEntity
from models import db

class VentaRepository:
    @staticmethod
    def consultar(id_venta):
        return VentaEntity.query.get(id_venta)

    @staticmethod
    def consultar_ticket(numero_documento):
        return VentaEntity.query.filter_by(numero_documento=numero_documento).first()

    @staticmethod
    def agregar(venta: VentaEntity):
        try:
            db.session.add(venta)
            db.session.commit()
            return venta.id_venta
        except Exception as e:
            db.session.rollback()
            return None

    @staticmethod
    def eliminar(id_venta):
        try:
            venta = VentaEntity.query.get(id_venta)
            if venta:
                db.session.delete(venta)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def get_ganancias_between_dates(start_date, end_date):
        sql = "SELECT * FROM get_ganancias_between_dates(:start_date, :end_date)"
        result = db.session.execute(sql, {"start_date": start_date, "end_date": end_date})
        return [dict(row) for row in result]

    @staticmethod
    def get_ganancias_between_dates_and_user(start_date, end_date, id_usuario):
        sql = "SELECT * FROM get_ganancias_between_dates(:start_date, :end_date, :id_usuario)"
        result = db.session.execute(sql, {
            "start_date": start_date,
            "end_date": end_date,
            "id_usuario": id_usuario
        })
        return [dict(row) for row in result]

    @staticmethod
    def get_ganancias_between_dates_per_product(id_producto, start_date, end_date):
        sql = "SELECT * FROM get_detalle_venta_by_date_range(:id_producto, :start_date, :end_date)"
        result = db.session.execute(sql, {
            "id_producto": id_producto,
            "start_date": start_date,
            "end_date": end_date
        })
        return [dict(row) for row in result]

    @staticmethod
    def get_balance(start_date, end_date):
        sql = '''
        SELECT 
            fecha_registro AS fecha,
            tipo_documento AS tipo_documento,
            id_producto AS id_producto,
            nombre AS nombre,
            precio_venta AS precio_venta,
            precio_compra AS precio_compra,
            cantidad AS cantidad,
            cantidad_caja AS cantidad_caja,
            tipo_venta AS tipo_venta,
            subtotal AS subtotal,
            ganancia AS ganancia,
            perdida AS perdida
        FROM obtener_reporte_ventas(:start_date, :end_date)
        '''
        result = db.session.execute(sql, {"start_date": start_date, "end_date": end_date})
        return [dict(row) for row in result]
