#!/usr/bin/env python

import sys
import pandas as pd
from hubward import utils
import os
import pybedtools

source, target = sys.argv[1:]
df = pd.read_excel(source)
# note space in "chr "
TMP = target + '.tmp'
df[['chr ', 'start', 'end']].to_csv(
    TMP,
    sep='\t',
    index=False,
    header=False
)

utils.bigbed(pybedtools.BedTool(TMP).sort(), genome='dm3', output=target)
os.unlink(TMP)
