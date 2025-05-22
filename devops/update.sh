#!/bin/bash

set -e  # exit on first error

echo "🛠️ Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "✅ All done!"
