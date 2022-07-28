#!/usr/bin/env bash

source "scripts/common/activate-virtualenv.sh"
src_dir="./src"

PYTHONPATH="$(realpath "${src_dir}")${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONPATH

echo "Running linters..."
pylama --verbose "$src_dir" || exit 1
echo "Finished running linters."
