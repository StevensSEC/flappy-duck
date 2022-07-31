#!/usr/bin/env bash

source "scripts/common/activate-virtualenv.sh"
src_dir="./src"
test_dir="./tests"

PYTHONPATH="$(realpath "${src_dir}")${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONPATH

echo "Running linters..."
pylama --verbose "$src_dir" "$test_dir" || exit 1
echo "Finished running linters."
