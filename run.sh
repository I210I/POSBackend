#!/bin/bash

# Crear entorno virtual si no existe
test -d venv || python3.11 -m venv venv

# Activar entorno virtual
test -f venv/bin/activate && source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar la aplicación
python3.11 App/main.py