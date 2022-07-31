#!/usr/bin/env bash

./scripts/common/check-venv.sh || exit 1

src_dir="./src"
test_dir="./tests"

PYTHONPATH="$(realpath "${src_dir}")${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONPATH

echo "Running linters..."
pylama --verbose "$src_dir" "$test_dir" || exit 1
echo "Finished running linters."
