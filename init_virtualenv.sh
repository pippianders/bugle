#!/usr/bin/env bash

set -e

if [[ -e 'ENV' ]]; then
    echo "Looks like you've already got a virtualenv here."
    echo "I'm not going to mess with it."
    exit 1
fi

echo "Setting up virtualenv"
virtualenv ENV
echo "Installing requirements"
ENV/bin/pip install -r requirements.txt
