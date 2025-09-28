#!/usr/bin/env bash
set -o errexit

# instalar deps (si render no lo hace)
pip install -r requirements.txt

# recopila archivos estaticos
python manage.py collectstatic --no-input

# aplicar migraciones
python manage.py migrate

