from flask import Blueprint

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.route('/ventas')
def ventas_home():
    return 'Ventas controller'
