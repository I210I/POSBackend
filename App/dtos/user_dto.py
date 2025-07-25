from marshmallow import Schema, fields

class UserDTO(Schema):
    nombre = fields.Str(required=True)
    usuario = fields.Str(required=True)
    contrasena = fields.Str(required=True)
