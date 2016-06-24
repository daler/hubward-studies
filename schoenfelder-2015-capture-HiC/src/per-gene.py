#!/usr/bin/env python
import pybedtools
from pybedtools.contrib.bigbed import bigbed
from pybedtools import featurefuncs
import sys
import os
import itertools
from hubward import utils

source, target = sys.argv[1:3]

gene = os.path.basename(target).split('_for_')[-1].replace('.bigbed', '').replace('_', '|')

def get_bait():
    f = open(source)
    f.readline()
    for line in f:
        toks = line.split()
        if toks[3].startswith(gene):
            bait = pybedtools.create_interval_from_list([
                toks[0],
                toks[1],
                toks[2],
                gene,
                '0',
                '.',
                toks[1],
                toks[2],
                '255,0,0',])

            return bait

def get_contacts():
    f = open(source)
    f.readline()
    for line in f:
        toks = line.strip().split()
        if toks[3].startswith(gene):
            contact = pybedtools.create_interval_from_list([
                toks[6],
                toks[7],
                toks[8],
                '.',
                toks[-1],
                '.',
                toks[7],
                toks[8],
                '0,0,0',
            ]
            )

            yield contact
bt = pybedtools.BedTool(get_contacts()).saveas()
if len(bt) == 0:
    with open(target, 'w') as fout:
        pass

else:
    norm = bt.colormap_normalize(vmin=7.0, vmax=18.0)
    bt = pybedtools.BedTool(itertools.chain(bt, [get_bait()])).saveas()
    cmap = utils.singlecolormap('k')

    def recolor(f):
        if f.name == '.':
            f = featurefuncs.add_color(f, cmap, norm)
        f.score = '0'
        return f


    bt = bt.each(recolor).sort()
    bigbed(bt, genome='mm9', output=target)
