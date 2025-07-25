from marshmallow import Schema, fields

class ClienteDTO(Schema):
    nombre = fields.Str(required=True)
    telefono = fields.Str(required=False)
