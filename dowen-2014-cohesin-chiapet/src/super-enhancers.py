#!/usr/bin/env python
import pandas, sys, os, hubward
source, target = sys.argv[1:3]
df = (pandas.read_excel(source, sheetname=0, skiprows=2)
      .sort_values(['Chr', 'Start', 'End'])
      .to_csv(target + '.tmp', sep='\t', header=False, index=False))
hubward.utils.bigbed(target + '.tmp', genome='mm9', output=target)
os.unlink(target + '.tmp')
