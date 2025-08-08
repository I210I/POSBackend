from models import db
from datetime import datetime

class Corte(db.Model):
    __tablename__ = 'corte'

    id_corte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False, index=True)
    _1 = db.Column(db.Integer, default=0)
    _2 = db.Column(db.Integer, default=0)
    _5 = db.Column(db.Integer, default=0)
    _10 = db.Column(db.Integer, default=0)
    _20 = db.Column(db.Integer, default=0)
    _50 = db.Column(db.Integer, default=0)
    _100 = db.Column(db.Integer, default=0)
    _200 = db.Column(db.Integer, default=0)
    _500 = db.Column(db.Integer, default=0)
    _1000 = db.Column(db.Integer, default=0)
    tarjeta_cantidad = db.Column(db.Integer, default=0)
    tarjeta_monto = db.Column(db.Numeric(10, 2), default=0)
    fecha_corte = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Corte {self.id_corte}>'
