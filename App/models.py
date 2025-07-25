from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PersonaModel(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), unique=True)
    contrasena = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    def __repr__(self):
        return f'<PersonaModel nombre={self.nombre} usuario={self.usuario}>'
