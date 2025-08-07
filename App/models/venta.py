from marshmallow import Schema, fields

class VentaModel(Schema):
    id_venta = fields.Int()
    numero_documento = fields.Str()
    fecha_registro = fields.DateTime()
    id_usuario = fields.Int()
    total_pagar = fields.Decimal(as_string=True)
    tipo_documento = fields.Str()
    estado = fields.Bool()
