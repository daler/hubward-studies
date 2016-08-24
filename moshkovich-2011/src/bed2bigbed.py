#!/usr/bin/env python
import pybedtools
from pybedtools.contrib.bigbed import bigbed
import sys
source, dest = sys.argv[1:3]
bigbed(pybedtools.BedTool(source).cut([0, 1, 2]).sort(), 'dm3', dest)
