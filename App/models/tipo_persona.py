from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TipoPersona(db.Model):
    __tablename__ = 'tipo_persona'
    __table_args__ = {'schema': 'public'}

    id_tipo_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TipoPersona {self.id_tipo_persona} {self.descripcion}>'
