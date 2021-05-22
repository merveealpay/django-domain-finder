#!/usr/bin/env bash

echo "Created migration files are running."
python manage.py migrate --settings=config.settings.local

echo "Starting Django project"
python manage.py runserver --settings=config.settings.local 0.0.0.0:8000

