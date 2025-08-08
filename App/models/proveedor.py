from marshmallow import Schema, fields

class ProveedorModel(Schema):
    id_proveedor = fields.Int()
    documento = fields.Str()
    razon_social = fields.Str(required=True)
    correo = fields.Str()
    telefono = fields.Str()
    estado = fields.Bool()
    fecha_creacion = fields.DateTime()
