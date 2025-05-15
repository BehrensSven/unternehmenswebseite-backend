#!/bin/bash
cd /home/ubuntu/backend
source venv/bin/activate
gunicorn unternehmenswebseite.wsgi:application --bind 0.0.0.0:8000
