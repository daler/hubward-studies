#!/usr/bin/env python
import sys, pandas, os, hubward
source, target = sys.argv[1:3]
# extract anchor bin coords from output filename:
coord = os.path.basename(target).replace('.bigbed', '')
chrom, start, stop = coord.split('_')

# write to BED file, then to bigBed
tmp = target + '.tmp'
with open(tmp, 'w') as fout:
    fout.write('{0}\t{1}\t{2}\n'.format(chrom, start, stop))
hubward.utils.bigbed(tmp, genome='hg18', output=target)
os.unlink(tmp)
