#!/usr/bin/env bash

set -e

if [[ -e 'bugle_project_ve' ]]; then
    echo "Looks like you've already got a virtualenv here."
    echo "I'm not going to mess with it."
    exit 1
fi

echo "Setting up virtualenv"
virtualenv bugle_project_ve
echo "Installing requirements"
pip install -E bugle_project_ve --use-mirrors --mirrors=http://pypi.fort/ -r requirements.txt

