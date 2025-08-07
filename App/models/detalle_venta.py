from marshmallow import Schema, fields

class DetalleVentaModel(Schema):
    id_detalle_venta = fields.Int()
    id_venta = fields.Int()
    id_producto = fields.Int()
    cantidad = fields.Decimal(as_string=True)
    precio_venta = fields.Decimal(as_string=True)
    subtotal = fields.Decimal(as_string=True)
