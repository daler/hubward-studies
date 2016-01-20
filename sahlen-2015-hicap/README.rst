Interactions in mouse ES cells as determined by HiCap (a capture modification
of HiC).

Supplemental tables were downloaded as a zip of Excel files. "Supplementary
Table 5v5.xlsx" contains three worksheets (promoter-enhancer,
promoter-promoter, and enhancer-enhancer interactions). Each of these were
converted to BEDPE format and then to paired-end BAM using BEDTools, which can
be lifted over with CrossMap. Note that the promoter anchor sites are provided
as single-bp TSS locations, so the BEDPE files use TSS and TSS+1 for the start
and stop coords respectively.
