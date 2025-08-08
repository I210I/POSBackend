from App.models import db

class Tienda(db.Model):
    __tablename__ = 'tienda'

    id_tienda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    documento = db.Column(db.String(20), unique=True, nullable=False)
    razon_social = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    def __repr__(self):
        return f'<Tienda {self.id_tienda} {self.razon_social}>'
