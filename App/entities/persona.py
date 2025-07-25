class Persona:
    def __init__(self, nombre: str, telefono: str = None, usuario: str = None, contrasena: str = None):
        self.nombre = nombre
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena

    def __repr__(self):
        return f"<Persona nombre={self.nombre} telefono={self.telefono} usuario={self.usuario}>"
