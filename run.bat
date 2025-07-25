@echo off

REM Crear entorno virtual si no existe
if not exist venv (
    python -m venv venv
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Ejecutar la aplicación
python App/main.py
