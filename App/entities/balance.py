from models import db

class Balance(db.Model):
    __tablename__ = 'balance_view'
    fecha = db.Column(db.Date)
    tipo_documento = db.Column(db.String)
    id_producto = db.Column(db.Integer)
    nombre = db.Column(db.String)
    precio_venta = db.Column(db.Numeric)
    precio_compra = db.Column(db.Numeric)
    cantidad = db.Column(db.Numeric)
    cantidad_caja = db.Column(db.Numeric)
    tipo_venta = db.Column(db.String)
    subtotal = db.Column(db.Numeric)
    ganancia = db.Column(db.Numeric)
    perdida = db.Column(db.Numeric)
