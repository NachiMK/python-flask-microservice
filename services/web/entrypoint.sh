#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    # while ! nc -z $SQL_HOST $SQL_PORT; do
    #   sleep 0.1
    # done
    echo "PostgreSQL started"
fi

if [ "$FLASK_DEBUG" = "1" ]
then
    echo "Running in Debug mode..."
    python manage.py
fi

exec "$@"