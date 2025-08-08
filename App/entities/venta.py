from models import db
from sqlalchemy.orm import relationship
from datetime import datetime

class Venta(db.Model):
    __tablename__ = 'venta'

    id_venta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_documento = db.Column(db.String(50), default='Boleta')
    numero_documento = db.Column(db.String(50))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False, index=True)
    documento_cliente = db.Column(db.String(20))
    nombre_cliente = db.Column(db.String(100))
    total_pagar = db.Column(db.Numeric(10, 2), nullable=False)
    pago_con = db.Column(db.Numeric(10, 2), nullable=False)
    cambio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con DetalleVenta
    detalles_venta = relationship('DetalleVenta', back_populates='venta', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Venta {self.id_venta}>'
