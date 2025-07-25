
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os

from controllers.usuario import usuario_bp
from controllers.auth import auth_bp
from controllers.cliente import cliente_bp
from controllers.productos import productos_bp
from controllers.ventas import ventas_bp
from controllers.procesos import procesos_bp
from controllers.provedores import provedores_bp
from controllers.configuraciones import configuraciones_bp
from controllers.sucursal import sucursal_bp
from controllers.auth import auth_bp

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
API_KEY = os.getenv('API_KEY')
EXEMPT_PATHS = set(['/', '/login'])


app = Flask(__name__)

# Swagger UI config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "POSBackend API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.before_request
def require_api_key():
    # Permitir acceso libre a Swagger UI y archivos estáticos
    if (
        request.path in EXEMPT_PATHS or
        request.path.startswith('/swagger') or
        request.path.startswith('/static/')
    ):
        return
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/')
def hello():
    return "Hola desde app embebida sin venv!"

# Registrar blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(procesos_bp)
app.register_blueprint(provedores_bp)
app.register_blueprint(configuraciones_bp)
app.register_blueprint(sucursal_bp)

import os
if __name__ == '__main__':
    # Asegura que swagger.json esté disponible en /static
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    swagger_json_path = os.path.join(static_dir, 'swagger.json')
    if not os.path.exists(swagger_json_path):
        import shutil
        shutil.copy(os.path.join(os.path.dirname(__file__), 'swagger.json'), swagger_json_path)
    app.run(port=7860)