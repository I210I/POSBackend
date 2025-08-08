from marshmallow import Schema, fields

class DetalleVentaModel(Schema):
    id_detalle = fields.Int()
    id_producto = fields.Int()
    cantidad = fields.Int()
    precio_unitario = fields.Decimal(as_string=True)
    subtotal = fields.Decimal(as_string=True)

class VentaModel(Schema):
    id_venta = fields.Int()
    numero_documento = fields.Str()
    fecha_registro = fields.DateTime()
    id_usuario = fields.Int()
    total_pagar = fields.Decimal(as_string=True)
    tipo_documento = fields.Str()
    estado = fields.Bool()
    detalles = fields.List(fields.Nested(DetalleVentaModel))
