from models import db
from sqlalchemy.orm import relationship

class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id_proveedor'))
    monto_total = db.Column(db.Numeric(10,2), default=0)
    tipo_documento = db.Column(db.String(50), default='Boleta')
    numero_documento = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime)

    # Relación con DetalleCompra
    detalles_compra = relationship('DetalleCompra', back_populates='compra', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Compra {self.id_compra}>'
