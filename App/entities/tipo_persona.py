from datetime import datetime

class TipoPersona:
    def __init__(self, id_tipo_persona: int = None, descripcion: str = None, estado: bool = None, fecha_creacion: datetime = None):
        self.id_tipo_persona = id_tipo_persona
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'<TipoPersona {self.id_tipo_persona} {self.descripcion}>'
