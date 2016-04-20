#!/usr/bin/env python
import os
import sys
import pandas
import pybedtools
source, target = sys.argv[1:3]
df = pandas.read_table(source)
protein = os.path.basename(target).split('_')[0]
tmp = pybedtools.BedTool._tmp()
df[['chromosome', 'start', 'end', protein]].to_csv(tmp, sep='\t', index=False, header=False)
pybedtools.contrib.bigwig.bedgraph_to_bigwig(pybedtools.BedTool(tmp), 'dm3', target)
