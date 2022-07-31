#!/usr/bin/env bash

# venv not required in CI
if [ -z "$CI" ]; then
    if [ -z "$VIRTUAL_ENV" ]; then
        printf "No virtual environment detected. Please run:\n\n"
        printf "\tpython3.10 -m venv venv\n\n"
        printf "to make a new virtual environment or:\n\n"
        printf "\tsource venv/bin/activate\n\n"
        printf "to activate one that already exists.\n"
        exit 1
    fi
fi

exit 0