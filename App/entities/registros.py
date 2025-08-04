from datetime import datetime

class Registros:
    def __init__(self, id_registro: int = None, id_usuario: int = None, tipo: str = None, fecha: datetime = None):
        self.id_registro = id_registro
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.fecha = fecha

    def __repr__(self):
        return f'<Registros {self.id_registro} {self.tipo}>'
