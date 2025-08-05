from marshmallow import Schema, fields

class GananciasDiariasModel(Schema):
    fecha = fields.Date()
    total_ventas = fields.Decimal(as_string=True)
    total_ganancia = fields.Decimal(as_string=True)
    # Agrega otros campos según el resultado del SP
