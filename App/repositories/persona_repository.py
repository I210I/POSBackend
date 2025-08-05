from entities.persona import Persona as PersonaEntity
from entities.tipo_persona import TipoPersona as TipoPersonaEntity
from entities.registros import Registros as RegistrosEntity
from models import db

class PersonaRepository:
    @staticmethod
    def encontrar_persona_id(id_persona):
        return PersonaEntity.query.get(id_persona)

    @staticmethod
    def encontrar_administradores(clave):
        return PersonaEntity.query.filter_by(tipo_persona=1).filter_by(clave=clave).count() > 0

    @staticmethod
    def encontrar_persona_por_usuario_clave(usuario, clave):
        return PersonaEntity.query.filter_by(usuario=usuario, clave=clave).first()

    @staticmethod
    def obtener_tipo_persona(persona: PersonaEntity):
        return TipoPersonaEntity.query.get(persona.tipo_persona)

    @staticmethod
    def listar_activos():
        return PersonaEntity.query.filter_by(estado=True).all()

    @staticmethod
    def listar():
        return PersonaEntity.query.all()

    @staticmethod
    def eliminar(id_persona):
        persona = PersonaEntity.query.get(id_persona)
        if persona:
            coincidencias_en_ventas = db.session.query(db.exists().where(db.text(f"ventas.id_usuario = {id_persona}"))).scalar()
            if not coincidencias_en_ventas:
                coincidencias_en_registros = RegistrosEntity.query.filter_by(id_usuario=id_persona).all()
                for reg in coincidencias_en_registros:
                    db.session.delete(reg)
                db.session.delete(persona)
                db.session.commit()
                return True
        return False

    @staticmethod
    def agregar(new_persona: PersonaEntity):
        db.session.add(new_persona)
        db.session.commit()
        return True

    @staticmethod
    def modificar(new_persona: PersonaEntity):
        persona = PersonaEntity.query.get(new_persona.id_persona)
        if persona:
            persona.nombre = new_persona.nombre
            persona.documento = new_persona.documento
            persona.direccion = new_persona.direccion
            persona.telefono = new_persona.telefono
            persona.clave = new_persona.clave
            persona.tipo_persona = new_persona.tipo_persona
            persona.estado = new_persona.estado
            persona.usuario = new_persona.usuario
            db.session.commit()
            return True
        return False
