from flask import Blueprint

procesos_bp = Blueprint('procesos', __name__)

@procesos_bp.route('/procesos')
def procesos_home():
    return 'Procesos controller'
