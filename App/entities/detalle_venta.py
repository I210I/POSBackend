from models import db
from sqlalchemy.orm import relationship
from datetime import datetime

class DetalleVenta(db.Model):
    __tablename__ = 'detalle_venta'

    id_detalle_venta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('venta.id_venta'), nullable=False, index=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable=False, index=True)
    venta_caja = db.Column(db.Boolean, default=False)
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    cantidad_caja = db.Column(db.Float, default=0)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones ORM
    venta = relationship('Venta', back_populates='detalles_venta')
    producto = relationship('Producto')

    def __repr__(self):
        return f'<DetalleVenta {self.id_detalle_venta}>'
