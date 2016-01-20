#!/usr/bin/env python

import os, sys, pandas, pybedtools
import numpy as np
source, target = sys.argv[1:3]

# NOTE: to speed up iterations while developing this script (e.g., playing
# around with different thresholds or scoring)


# map requested input files to target output files and arguments for importing
# from source.

lookup = {
    'promoter-to-enhancer': {
        'cache': 'p2e.txt',
        'sheet_name': 0,
        'skiprows': 4,
        'dtype': {
            'Gene Name': str,
            'Representative Transcript Name': str,
            'Gene Expression': np.float64,
            'Shared Promoter': str,
            'Number of DpnII sites within core promoter': np.int32,
            'Promoter chr': str,
            'Promoter TSS': np.int64,
            'Promoter Strand': str,
            'Fragment chromosome': str,
            'Fragment start coordinate': np.int64,
            'Fragment end coordinate': np.int64,
            'Read pairs in HiCap replicate 1': np.int64,
            'p-value HiCap replicate 1': np.float64,
            'Adjusted p-value HiCap replicate 1': np.float64,
            'Read pairs in HiCap replicate 2': np.int64,
            'p-value HiCap replicate 2': np.float64,
            'Adjusted p-value HiCap replicate 2': np.float64,
        },
        'bedpe_coord_cols': [
            'Promoter chr',
            'Promoter TSS',
            'Promoter TSS+1',  # will be created once the table is read into memory
            'Fragment chromosome',
            'Fragment start coordinate',
            'Fragment end coordinate'
        ],
    },
    'promoter-to-promoter': {
        'cache': 'p2p.txt',
        'sheet_name': 1,
        'skiprows': 1,
        'dtype':  {
            'Gene Name': str,
            'Gene ID': str,
            'Promoter chr': str,
            'Promoter TSS': np.int64,
            'Expression (RPKM)': np.float64,
            'Number of DpnII sites within core promoter': np.int32,
            'Mappability of core promoter': np.float64,
            'Shared promoter': str,
            'Gene Name.1': str,
            'Gene ID.1': str,
            'Promoter chr.1': str,
            'Promoter TSS.1': np.int64,
            'Expression': np.float64,
            'Number of DpnII sites within core promoter.1': np.int32,
            'Mappability of core promoter.1': np.float64,
            'Read pairs in HiCap replicate 1': np.int64,
            'Read pairs in HiCap replicate 2': np.int64,
        },
        'bedpe_coord_cols': [
            'Promoter chr',
            'Promoter TSS',
            'Promoter TSS+1',  # will be created once the table is read into memory
            'Promoter chr.1',
            'Promoter TSS.1',
            'Promoter TSS.1+1',
        ],
            # note: no pvals or adjusted pvals for p2p.
    },
    'enhancer-to-enhancer': {
        'cache': 'e2e.txt',
        'sheet_name': 2,
        'skiprows': 1,
        'dtype': {
            'Fragment chromosome': str,
            'Fragment start coordinate': np.int64,
            'Fragment end coordinate': np.int64,
            'Fragment mappability': np.float64,
            'Fragment chromosome.1': str,
            'Fragment start coordinate.1': np.int64,
            'Fragment end coordinate.1': np.int64,
            'Fragment mappability.1': np.float64,
            'Read pairs in HiCap replicate 1': np.int64,
            'Read pairs in HiCap replicate 2': np.int64,
        },
        'bedpe_coord_cols': [
            'Fragment chromosome',
            'Fragment start coordinate',
            'Fragment end coordinate',
            'Fragment chromosome.1',
            'Fragment start coordinate.1',
            'Fragment end coordinate.1'
        ],
    },
}

for k, v in lookup.items():
    if not os.path.basename(target).startswith(k):
        continue
    cache = os.path.join(os.path.dirname(source), v['cache'])
    if not os.path.exists(cache):
        pandas.read_excel(source, skiprows=v['skiprows'], sheetname=v['sheet_name']).to_csv(cache, sep='\t', index=False)

    # default read_table fails; need to specify low_memory=False or specify
    # a dtype. I chose dtype to be more explicit.
    df = pandas.read_table(cache, dtype=v['dtype'])
    for col in v['bedpe_coord_cols']:
        if col not in df.columns:
            df[col] = df[col.replace('+1', '')] + 1

    df['default strand'] = '.'
    df['default score'] = 0
    df['name'] = df.index
    bedpe_cols = v['bedpe_coord_cols'] + ['name', 'default score', 'default strand', 'default strand']

    bedpe = df[bedpe_cols].to_csv(target + '.bedpe', sep='\t', index=False, header=False)
    bt = pybedtools.BedTool(target + '.bedpe')
    bt = bt.bedpe_to_bam(genome='mm9')
    os.system('samtools sort %s -o %s' % (bt.fn, target))
    os.system('samtools index %s' % target)
    os.unlink(target + '.bedpe')

