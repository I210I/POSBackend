from flask import Blueprint

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuario')
def usuario_home():
    return 'Usuario controller'
