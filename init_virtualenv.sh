#!/usr/bin/env bash

set -e

if [[ -e 'bin/activate' ]]; then
    echo "Looks like you've already got a virtualenv here."
    echo "I'm not going to mess with it."
    exit 1
fi

echo "Setting up virtualenv"
virtualenv .
echo "Installing requirements"
pip install --use-mirrors --mirrors=http://pypi.fort/ -r requirements.txt

