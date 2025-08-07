from models import db

class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(15))
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    clave = db.Column(db.String(50))
    id_tipo_persona = db.Column(db.Integer, db.ForeignKey('tipo_persona.id_tipo_persona'))
    estado = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime)
    usuario = db.Column(db.String(15))
