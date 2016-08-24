#!/usr/bin/env python
import pybedtools
from pybedtools.contrib.bigbed import bigbed
from pybedtools import featurefuncs
import sys
import os
import itertools
from hubward import utils

source, target = sys.argv[1:3]

def get_bait():
    f = open(source)
    f.readline()
    for line in f:
        toks = line.split()
        gene = list(set([i.split('-')[0] for i in toks[3].split('|')]))
        gene = '|'.join(gene)
        bait = pybedtools.create_interval_from_list([
            toks[0],
            toks[1],
            toks[2],
            gene,
            '0',
            '.',
            toks[1],
            toks[2],
            '128,0,0',])

        yield bait

bt = pybedtools.BedTool(get_bait()).sort()
bigbed(bt, genome='mm9', output=target)
