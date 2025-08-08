from models import db
from datetime import datetime

class Registros(db.Model):
    __tablename__ = 'registros'

    id_registro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False, index=True)
    tipo = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Registros {self.id_registro} {self.tipo}>'
