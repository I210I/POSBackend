from marshmallow import Schema, fields

class ClienteModel(Schema):
    id_cliente = fields.Int()
    nombre = fields.Str(required=True)
    direccion = fields.Str()
    telefono = fields.Str()
    correo = fields.Str()
    estado = fields.Bool()
