#!/usr/bin/env python
import pandas
import pybedtools
import sys
import os

source, target = sys.argv[1:3]

# Input file is already BEDPE-like
df = pandas.read_excel(source, sheetname=4, skiprows=2)
tmp = pybedtools.BedTool._tmp()
df.to_csv(tmp, sep='\t', index=False, header=False)
bt = pybedtools.BedTool(tmp)
bt = bt.bedpe_to_bam(genome='mm9')
os.system('samtools sort %s -o %s' % (bt.fn, target))
os.system('samtools index %s' % target)
