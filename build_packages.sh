#!/bin/bash

#clean up cached files

rm -rf dist build
find . -type d \( -name "*cache*" -o -name "*.dist-info" -o -name "*.egg-info" \) -not -path "./setupenv/*"  -exec rm -rf {} \;

#rebuild packages
python -m build --sdist --wheel ./
cd dist
unzip *.whl
cd ..