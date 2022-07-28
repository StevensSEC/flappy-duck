#!/usr/bin/env bash

# if not currently within a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
  venv_dir="${PWD}/venv"
  # if a virtual environment folder does not exist
  if [! -d "$venv_dir "]; then
    echo "Virtual environment does not exist. Creating in \"{venv_dir}\"..."
    {
      python3.10 -m venv "$venv_dir"
    } || {
      python -m venv "$venv_dir"
    } || exit 1
  fi

  venv_bin_dir="${venv_dir}/bin"

  source "${venv_bin_dir}/activate" || exit 1
  echo "Activated virtual environment!"
fi
