from models import db
from sqlalchemy.orm import relationship

class DetalleCompra(db.Model):
    __tablename__ = 'detalle_compra'

    id_detalle_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_compra = db.Column(db.Integer, db.ForeignKey('compra.id_compra'), nullable=False, index=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable=False, index=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)

    # Relaciones ORM
    compra = relationship('Compra', back_populates='detalles_compra')
    producto = relationship('Producto', back_populates='detalles_compra')

    def __repr__(self):
        return f"<DetalleCompra(id={self.id_detalle_compra}, compra={self.id_compra}, producto={self.id_producto}, cantidad={self.cantidad})>"
