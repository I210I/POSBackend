from models import db
from datetime import datetime

class TipoPersona(db.Model):
    __tablename__ = 'tipo_persona'

    id_tipo_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TipoPersona {self.id_tipo_persona} {self.descripcion}>'
