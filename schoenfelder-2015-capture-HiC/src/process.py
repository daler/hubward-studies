#!/usr/bin/env python

import pandas, os, sys, pybedtools
source, target = sys.argv[1:3]

if 'promoter_other' in source:
    bedpe_coord_cols = ['chr bait', 'start bait', 'end bait', 'chr', 'start', 'end']
elif 'promoter_promoter' in source:
    bedpe_coord_cols = ['chr', 'start', 'end', 'chr.1', 'start.1', 'end.1']

df = pandas.read_table(source)
df['strand'] = '.'
df['name'] = df.index
cols = bedpe_coord_cols + ['name', 'log(observed/expected)', 'strand', 'strand']
df[cols].to_csv(target + '.bedpe', sep='\t', index=False, header=False)
bt = pybedtools.BedTool(target + '.bedpe')
bt = bt.bedpe_to_bam(genome='mm9')
os.system('samtools sort %s -o %s' % (bt.fn, target))
os.system('samtools index %s' % target)
os.unlink(target + '.bedpe')
