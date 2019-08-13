#!/bin/bash

export PYTHON_SRC=../figurebot

echo "[Generating Plots and Collecting Data]"
cd "$PYTHON_SRC"
python "Application.py" "-lo"
echo "[Done]"