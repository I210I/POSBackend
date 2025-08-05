from marshmallow import Schema, fields

class GananciasDiariasPorProductoModel(Schema):
    id_producto = fields.Int()
    nombre_producto = fields.Str()
    fecha = fields.Date()
    total_ventas = fields.Decimal(as_string=True)
    total_ganancia = fields.Decimal(as_string=True)
    # Agrega otros campos según el resultado del SP
