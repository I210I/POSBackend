from marshmallow import Schema, fields

class LoginDTO(Schema):
    usuario = fields.Str(required=True)
    contrasena = fields.Str(required=True)
