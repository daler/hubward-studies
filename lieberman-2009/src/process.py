#!/usr/bin/env python
import sys, pandas, os, hubward
source, target = sys.argv[1:3]

coord = os.path.basename(target).replace('.bigwig', '')
chrom, start, stop = coord.split('_')
coord = '{0}:{1}-{2}'.format(chrom, start, stop)

x = pandas.read_table(source, sep='\t', comment="#", index_col=0)
row_ind = x.index.to_series().apply(lambda y: coord in y)
row = x[row_ind].T.dropna()
row.columns = ['score']

def to_bed(f):
    """E.g., 'HIC_bin1|hg18|chr11:1-99999' -> ('chr11', 1, 99999)"""
    chrom, startend = f.split('|')[-1].split(':')
    start, end = startend.split('-')
    return chrom, int(start), int(end)

row['chr'], row['start'], row['end'] = zip(*(row.index.to_series().apply(to_bed)))
tmp = target + '.tmp'
hubward.utils.makedirs(os.path.dirname(tmp))
row[['chr', 'start', 'end', 'score']].sort(['chr', 'start'])\
    .to_csv(tmp, sep='\t', index=False, header=False)
hubward.utils.bigwig(tmp, genome='hg18', output=target)
os.unlink(tmp)
