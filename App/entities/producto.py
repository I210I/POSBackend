
from models import db
from sqlalchemy.orm import relationship
from datetime import datetime

class Producto(db.Model):
    __tablename__ = 'producto'

    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False, index=True)
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    mayoreo = db.Column(db.Boolean, default=False)
    pieza_mayoreo = db.Column(db.Integer, default=0)
    precio_mayoreo = db.Column(db.Numeric(10, 2), default=0)
    stock = db.Column(db.Integer, default=0)
    estado = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con DetalleCompra
    detalles_compra = relationship('DetalleCompra', back_populates='producto', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Producto {self.id_producto} {self.nombre}>'
