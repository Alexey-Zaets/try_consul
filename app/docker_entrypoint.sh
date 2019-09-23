#!/bin/bash

sleep 10

# Apply database migrations
echo """
*
Apply database migrations
======================================================================
"""
python consul/manage.py migrate

# Run Main service
echo """
*
Start Gunicorn
======================================================================
"""
gunicorn --config ./gunicorn_config.py consul.wsgi:application
