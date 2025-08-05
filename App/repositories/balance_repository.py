from models import db
from entities.balance import Balance

class BalanceRepository:
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
        return [Balance(**row) for row in result]
