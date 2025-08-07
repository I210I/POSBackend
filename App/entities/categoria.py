from models import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    descripcion_categoria = db.Column(db.String(15))
    estado = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime)
