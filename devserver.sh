#!/bin/sh
source .venv/bin/activate
python backend_bodega17/manage.py runserver $PORT
