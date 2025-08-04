from datetime import datetime

class Categoria:
    def __init__(self, id_categoria: int = None, descripcion_categoria: str = None, estado: bool = None, fecha_creacion: datetime = None):
        self.id_categoria = id_categoria
        self.descripcion_categoria = descripcion_categoria
        self.estado = estado
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'<Categoria {self.id_categoria} {self.descripcion_categoria}>'
