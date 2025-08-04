from datetime import datetime

class Persona:
    def __init__(self, id_persona: int = None, documento: str = None, nombre: str = None, direccion: str = None,
                 telefono: str = None, clave: str = None, tipo_persona: int = None, estado: bool = None,
                 usuario: str = None, fecha_creacion: datetime = None):
        self.id_persona = id_persona
        self.documento = documento
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.clave = clave
        self.tipo_persona = tipo_persona
        self.estado = estado
        self.usuario = usuario
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'<Persona {self.id_persona} {self.nombre}>'
