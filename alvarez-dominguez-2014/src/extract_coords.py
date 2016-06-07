#!/usr/bin/env python

import pandas
import pybedtools
import re
import sys
import os
source, target = sys.argv[1:3]
xls = pandas.read_excel(source, sheetname=os.path.basename(target).replace('.bigbed', '').replace('rna', 'RNA'))
regexp = re.compile(r'(?P<chrom>\w*)\[(?P<strand>.)\](?P<start>\d+)-(?P<stop>\d+)')
def coord_to_interval(x):
    m = regexp.search(x).groupdict()
    return pybedtools.create_interval_from_list([
        m['chrom'],
        m['start'],
        m['stop'],
        '.',
        '0',
        m['strand']])

def gen():
    for i in xls['Coordinates (mm9)'].values:
        try:
            yield coord_to_interval(i)
        except AttributeError:
            pass

bt = pybedtools.BedTool(gen()).sort()
pybedtools.contrib.bigbed.bigbed(bt, genome='mm9', output=target)
