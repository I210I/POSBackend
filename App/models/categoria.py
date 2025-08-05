class CategoriaModel:
    def __init__(self, id_categoria=None, descripcion_categoria=None, estado=None, fecha_creacion=None):
        self.id_categoria = id_categoria
        self.descripcion_categoria = descripcion_categoria
        self.estado = estado
        self.fecha_creacion = fecha_creacion

    def to_dict(self):
        return {
            'id_categoria': self.id_categoria,
            'descripcion_categoria': self.descripcion_categoria,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion
        }
