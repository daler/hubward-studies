#!/usr/bin/env python
import sys
import pybedtools
from pybedtools import featurefuncs
from hubward.utils import singlecolormap, bigbed
source, target = sys.argv[1:3]

# Raw data are in GFF-like format. Convert them, add leading "chr" to chrom
# names, and retain score in both score field as well as name field.
def fix(x):
    x = featurefuncs.gff2bed(x, name_field=5)
    x[4] = x.name
    x.chrom = 'chr' + x.chrom
    return x

x = pybedtools.BedTool(source)\
    .each(fix)\
    .saveas()

# Normalize the colormap based on the scores.
norm = x.colormap_normalize()
color = '#000000'
cm = singlecolormap(color)

# Since we've constructed a separate colormap, we disable the score by setting
# to '0'. Keep the names as scores though so we can check in the browser.
def zero_score(f):
    f.name = '%.4f' % float(f.score)
    f.score = '0'
    return f

x = x.each(featurefuncs.add_color, cm, norm)\
    .each(zero_score)\
    .sort()

bigbed(x.fn, 'dm2', target)
