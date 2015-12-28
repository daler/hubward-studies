#!/usr/bin/env python

import pandas
import sys
import pybedtools

source, target = sys.argv[1:3]
df = pandas.read_excel(source, header=None, skiprows=5)
df = df[[1, 3, 4]]
tmp = pybedtools.BedTool._tmp()
df.to_csv(tmp, header=False, index=False, sep='\t')

if 'boundaries' not in target:

    pybedtools.contrib.bigbed.bigbed(tmp, 'dm3', target)

else:
    def gen():
        last = None
        for i in pybedtools.BedTool(tmp):
            if last is not None:
                if i.chrom == last.chrom:
                    yield pybedtools.create_interval_from_list([
                        i.chrom,
                        str(last.stop),
                        str(i.start),
                    ])
            last = i

    x = pybedtools.BedTool(gen()).saveas('/data/dalerr/asdf')
    pybedtools.contrib.bigbed.bigbed(x, 'dm3', target)
