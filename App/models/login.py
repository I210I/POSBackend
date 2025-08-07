from marshmallow import Schema, fields

class LoginModel(Schema):
    usuario = fields.Str(required=True)
    clave = fields.Str(required=True, load_only=True)
