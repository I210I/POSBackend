from models import db
from entities.ganancias_diarias_por_producto import GananciasDiariasPorProducto

class GananciasDiariasPorProductoRepository:
    @staticmethod
    def get_between_dates_per_product(id_producto, start_date, end_date):
        sql = "SELECT * FROM get_detalle_venta_by_date_range(:id_producto, :start_date, :end_date)"
        result = db.session.execute(sql, {
            "id_producto": id_producto,
            "start_date": start_date,
            "end_date": end_date
        })
        return [GananciasDiariasPorProducto(**row) for row in result]
