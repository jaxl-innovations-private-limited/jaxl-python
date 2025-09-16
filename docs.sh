#!/bin/bash

rm -rf docs
pdoc3 --html -o docs jaxl
pdoc3 --html -o docs examples