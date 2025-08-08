from marshmallow import Schema, fields

class TipoPersonaModel(Schema):
    id_tipo_persona = fields.Int()
    descripcion = fields.Str(required=True)
    estado = fields.Bool()
    fecha_creacion = fields.DateTime()
