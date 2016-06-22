#!/usr/bin/env python
import sys, pybedtools, hubward
source, target = sys.argv[1:3]
x = pybedtools.BedTool(source)
x = x.cut([0, 1, 2]).sort()
hubward.utils.bigbed(x.fn, genome='dm3', output=target)
