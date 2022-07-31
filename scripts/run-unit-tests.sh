#!/usr/bin/env bash

./scripts/common/check-venv.sh || exit 1

src_dir="./src"
test_dir="./tests/unit-tests"

PYTHONPATH="$(realpath "${src_dir}")${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONPATH

echo "Running unit tests..."
python3 -m unittest discover --start-directory "$test_dir" \
 --verbose --locals --buffer
