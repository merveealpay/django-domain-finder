#!/usr/bin/env bash

echo "Changes are being investigated on models."
#python manage.py makemigrations finder --settings=config.settings.docker --name created_domain_and_provider

echo "Created migration files are running."
python manage.py migrate --settings=config.settings.docker

echo "Starting Django project"
python manage.py runserver --settings=config.settings.docker 0.0.0.0:8000
