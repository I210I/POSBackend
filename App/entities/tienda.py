class Tienda:
    def __init__(self, id_tienda: int = None, documento: str = None, razon_social: str = None,
                 correo: str = None, telefono: str = None):
        self.id_tienda = id_tienda
        self.documento = documento
        self.razon_social = razon_social
        self.correo = correo
        self.telefono = telefono

    def __repr__(self):
        return f'<Tienda {self.id_tienda} {self.razon_social}>'
