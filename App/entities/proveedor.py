from models import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id_proveedor = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(15))
    razon_social = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    estado = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime)
