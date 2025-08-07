from flask import Blueprint

configuraciones_bp = Blueprint('configuraciones', __name__)

@configuraciones_bp.route('/configuraciones')
def configuraciones_home():
    return 'Configuraciones controller'
