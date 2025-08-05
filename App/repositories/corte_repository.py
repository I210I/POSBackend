from entities.corte import Corte as CorteEntity
from models import db
from datetime import datetime

class CorteRepository:
    @staticmethod
    def consultar_corte_del_dia(fecha: datetime):
        # Filtrar cortes por fecha y obtener el último corte por usuario
        cortes = CorteEntity.query.filter(
            db.extract('year', CorteEntity.fecha_corte) == fecha.year,
            db.extract('month', CorteEntity.fecha_corte) == fecha.month,
            db.extract('day', CorteEntity.fecha_corte) == fecha.day
        ).all()
        # Agrupar por usuario y obtener el último corte por usuario
        cortes_por_usuario = {}
        for corte in cortes:
            uid = corte.id_usuario
            if uid not in cortes_por_usuario or corte.id_corte > cortes_por_usuario[uid].id_corte:
                cortes_por_usuario[uid] = corte
        return list(cortes_por_usuario.values())

    @staticmethod
    def agregar_nuevo_corte(nuevo_corte: CorteEntity):
        db.session.add(nuevo_corte)
        db.session.commit()
        return True
