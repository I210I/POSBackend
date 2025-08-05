from models import db
from entities.ganancias_diarias import GananciasDiarias

class GananciasDiariasRepository:
    @staticmethod
    def get_between_dates(start_date, end_date):
        sql = "SELECT * FROM get_ganancias_between_dates(:start_date, :end_date)"
        result = db.session.execute(sql, {"start_date": start_date, "end_date": end_date})
        return [GananciasDiarias(**row) for row in result]

    @staticmethod
    def get_between_dates_and_user(start_date, end_date, id_usuario):
        sql = "SELECT * FROM get_ganancias_between_dates(:start_date, :end_date, :id_usuario)"
        result = db.session.execute(sql, {
            "start_date": start_date,
            "end_date": end_date,
            "id_usuario": id_usuario
        })
        return [GananciasDiarias(**row) for row in result]
