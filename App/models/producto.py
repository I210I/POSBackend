from marshmallow import Schema, fields

class ProductoModel(Schema):
    id_producto = fields.Int()
    codigo = fields.Str()
    nombre = fields.Str()
    descripcion = fields.Str()
    stock = fields.Decimal(as_string=True)
    precio_compra = fields.Decimal(as_string=True)
    precio_venta = fields.Decimal(as_string=True)
    cajas = fields.Str()
    piezas_mayoreo = fields.Int()
    precio_mayoreo = fields.Decimal(as_string=True)
    categoria = fields.Int()
    estado = fields.Bool()
