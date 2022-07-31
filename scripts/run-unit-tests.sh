#!/usr/bin/env bash

source "scripts/common/activate-virtualenv.sh"
src_dir="./src"
test_dir="./tests/unit-tests"

PYTHONPATH="$(realpath "${src_dir}")${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONPATH

echo "Running unit tests..."
python3 -m unittest discover --start-directory "$test_dir" \
 --verbose --locals --buffer
