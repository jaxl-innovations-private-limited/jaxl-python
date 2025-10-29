#!/bin/bash

rm -rf docs site
pdoc3 -o docs jaxl
pdoc3 -o docs examples
cp index.md docs
PYTHONPATH=. mkdocs build
# open site/index.html