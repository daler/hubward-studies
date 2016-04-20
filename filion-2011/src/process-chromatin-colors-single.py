#!/usr/bin/env python
import pybedtools
import gzip
import sys
import os

source, target = sys.argv[1:3]

colors = {
  'YELLOW': '255,204,0',
  'BLACK': '0,0,0',
  'BLUE': '0,102,204',
  'GREEN': '51,153,0',
  'RED': '153,25,0',
}

single_color = os.path.basename(target).split('-')[-1].replace('.bigbed', '')

fin = gzip.open(source)
fin.readline()
with open(pybedtools.BedTool._tmp(), 'w') as fout:
    for line in fin:
        toks = line.strip().split('\t')
        if toks[-1] != single_color:
            continue
        color = colors[toks[-1]]
        fields = toks + ['0', '.'] + toks[1:3] + [color]
        fout.write('\t'.join(fields) + '\n')

pybedtools.contrib.bigbed.bigbed(fout.name, 'dm3', target)
