#!/bin/bash

rm -rf docs/jaxl
pdoc3 -o docs jaxl

rm -rf docs/examples
pdoc3 -o docs examples