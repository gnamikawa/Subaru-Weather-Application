#!/bin/bash
#
#################################################
# Wrapper for conda environment "webdev"
#################################################

# activate miniconda environment
export CONDAPATH=/home/genzo/miniconda3
export CONDA_EXE=$CONDAPATH/bin/conda
export CONDA_PREFIX=$CONDAPATH/envs/webdev
export CONDA_PYTHON_EXE=$CONDA_PREFIX
export CONDA_DEFAULT_ENV=webdev

export PATH=$CONDA_PREFIX/bin\:$PATH
export SCRIPTPATH=/home/genzo/git/swa/fetch

cd $SCRIPTPATH

bash GenerateScript.sh
bash CopyScript.sh