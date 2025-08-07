from flask import Blueprint

provedores_bp = Blueprint('provedores', __name__)

@provedores_bp.route('/provedores')
def provedores_home():
    return 'Provedores controller'
