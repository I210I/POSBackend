from flask import Blueprint

sucursal_bp = Blueprint('sucursal', __name__)

@sucursal_bp.route('/sucursal')
def sucursal_home():
    return 'Sucursal controller'
