from marshmallow import Schema, fields

class CategoriaModel(Schema):
    id_categoria = fields.Int()
    descripcion_categoria = fields.Str(required=True)
    estado = fields.Bool()
    fecha_creacion = fields.DateTime()
