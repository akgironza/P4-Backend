#!/usr/bin/env bash

# exit on error
set -o errexit

# install dependencies
pip install -r dependencies.txt

# run migrations
python manage.py migrate

chmod a+x setup.sh