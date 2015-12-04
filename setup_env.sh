#!/bin/bash
ENV_NAME=hubward-studies
[[ $(conda env list | grep "^$ENV_NAME") ]] || conda create -n $ENV_NAME python=2
conda install --channel bioconda -n $ENV_NAME --file requirements.txt
