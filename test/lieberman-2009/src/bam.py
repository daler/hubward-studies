#!/usr/bin/env python
import sys, pandas, os, pybedtools, subprocess
source, target = sys.argv[1:3]


# creates a paired-end BAM file for the coordinate specified in the filename.

coord = os.path.basename(target).replace('.bam', '')
chrom, start, stop = coord.split('_')
coord = '{0}:{1}-{2}'.format(chrom, start, stop)
x = pandas.read_table(source, sep='\t', comment='#', index_col=0)
row_ind = x.index.to_series().apply(lambda y: coord in y)
row = x[row_ind].T.dropna()
row.columns = ['score']

def to_bed(f):
    """E.g., 'HIC_bin1|hg18|chr11:1-99999' -> ('chr11', 1, 99999)"""
    chrom, startend = f.split('|')[-1].split(':')
    start, end = startend.split('-')
    return chrom, int(start), int(end)


row['chr2'], row['start2'], row['end2'] = zip(*(row.index.to_series().apply(to_bed)))
row['chr1'], row['start1'], row['end1'] = chrom, start, stop
row = row[row['score'] > 0]
row['name'] = (
    row['chr1']
    + row['start1'].astype(str)
    + row['end1'].astype(str)
    + row['chr2']
    + row['start2'].astype(str)
    + row['end2'].astype(str)
)
row['strand1'] = '.'
row['strand2'] = '.'
tmp = target + '.tmp'
row[
    [
        'chr1',
        'start1',
        'end1',
        'chr2',
        'start2',
        'end2',
        'name',
        'score',
        'strand1',
        'strand2'
    ]
].to_csv(tmp, sep='\t', index=False, header=False)

bt = pybedtools.BedTool(tmp)
btbam = bt.bedpe_to_bam(genome='hg18', output=tmp + '.bam')

p = subprocess.check_call([
    'samtools', 'sort', '-O', 'bam', '-T', 'sorting', '-o', target, tmp + '.bam'])
p = subprocess.check_call([
    'samtools', 'index', target])

os.unlink(tmp)
os.unlink(tmp + '.bam')

