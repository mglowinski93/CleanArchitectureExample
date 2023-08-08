#!/bin/bash
set -e

# Install python packages.
python -m pip install --upgrade --user --disable-pip-version-check pip
pip install -r /app/requirements/development.txt

# Wait for the database to be ready.
/tools/wait-for "${POSTGRES_DB_HOST}":"${POSTGRES_DB_PORT}" -t 60
if [ $? -ne 0 ]; then
    echo Receipt of readiness from database failed. Exiting...
    exit 1
fi
sleep 5 # Wait to be sure, that database is up.

# Run database migrations.
./manage.py migrate

# Load users from fixture.
./manage.py loaddata infrastructures/fixtures/users.json

# Run the development server.
exec ./manage.py runserver 0.0.0.0:8000
