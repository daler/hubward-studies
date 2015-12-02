#!/usr/bin/env python
import pandas
import sys
import pybedtools
from pybedtools.contrib import bigbed

infile, outfile = sys.argv[1:3]
df = pandas.read_excel(infile, header=2, index_col=0)
tmpfile = pybedtools.BedTool._tmp()
df = df.sort(['chrom', 'start', 'end'])
df['epigenetic class'] = df['epigenetic class'].apply(lambda x: x.replace(' ', '_'))
df.to_csv(tmpfile, header=False, index=False, sep='\t')
bigbed.bigbed(pybedtools.BedTool(tmpfile), 'dm3', outfile)
