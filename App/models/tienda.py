from marshmallow import Schema, fields

class TiendaModel(Schema):
    id_tienda = fields.Int()
    razon_social = fields.Str()
    documento = fields.Str()
    correo = fields.Str()
    telefono = fields.Str()
