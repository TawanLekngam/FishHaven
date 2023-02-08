#!/bin/bash

autopep8 $(git ls-files '**.py*') --in-place