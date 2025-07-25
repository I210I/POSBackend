from flask import Blueprint

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
def productos_home():
    return 'Productos controller'
