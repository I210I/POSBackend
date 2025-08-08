from marshmallow import Schema, fields

class UsuarioModel(Schema):
    id_persona = fields.Int()
    id_tipo_persona = fields.Int(required=True)
    nombre = fields.Str(required=True)
    usuario = fields.Str(required=True)
    clave = fields.Str(load_only=True)
    estado = fields.Bool()
