#!/usr/bin/env python
import pandas
import sys
import pybedtools
from pybedtools.contrib import bigbed
infile, outfile = sys.argv[1:3]

df = pandas.read_excel(infile, header=2, index_col=0)
tmpfile = pybedtools.BedTool._tmp()
df = df.sort_values(['chrom', 'start', 'end'])
df['epigenetic class'] = df['epigenetic class'].apply(lambda x: x.replace(' ', '_'))

colors = {
    'Active': '153,0,0',
    'Null': '136,136,136',
    'HP1_centromeric': '51,102,0',
    'PcG': '0,51,102',
}
df['itemRgb'] = df['epigenetic class'].apply(lambda x: colors[x])
df['strand'] = '.'
df['thickStart'] = df['start']
df['thickEnd'] = df['end']
df['score'] = 0
order = [
    'chrom',
    'start',
    'end',
    'epigenetic class',
    'score',
    'strand',
    'thickStart',
    'thickEnd',
    'itemRgb']
df[order].to_csv(tmpfile, header=False, index=False, sep='\t')
bigbed.bigbed(pybedtools.BedTool(tmpfile), 'dm3', outfile)
