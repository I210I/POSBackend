
# Endpoint temporal para probar conexión y obtener usuarios
from flask import Blueprint, jsonify
from entities.persona import Persona as PersonaEntity

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/test/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = PersonaEntity.query.all()
    result = [
        {
            'id_persona': u.id_persona,
            'nombre': u.nombre,
            'usuario': u.usuario,
            'estado': u.estado
        } for u in usuarios
    ]
    return jsonify(result)
