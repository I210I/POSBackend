from flask import Blueprint

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/cliente')
def cliente_home():
    return 'Cliente controller'
