from marshmallow import Schema, fields

class BalanceModel(Schema):
    fecha = fields.Date()
    tipo_documento = fields.Str()
    id_producto = fields.Int()
    nombre = fields.Str()
    precio_venta = fields.Decimal(as_string=True)
    precio_compra = fields.Decimal(as_string=True)
    cantidad = fields.Decimal(as_string=True)
    cantidad_caja = fields.Decimal(as_string=True)
    tipo_venta = fields.Str()
    subtotal = fields.Decimal(as_string=True)
    ganancia = fields.Decimal(as_string=True)
    perdida = fields.Decimal(as_string=True)
