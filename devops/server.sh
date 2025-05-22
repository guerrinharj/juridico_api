#!/bin/zsh

chmod +x ./devops/server.sh

source .venv/bin/activate

python manage.py runserver