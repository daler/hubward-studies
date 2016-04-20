Chromatin colors are from a 5-state model trained on 53 DamID profiles,
downloaded from GSE22069 and converted to bigBed (along with coloring the
regions according to their "COLOR").

- GREEN: HP1
- YELLOW: Active, have H3K36me3, broad expression
- RED: Active, not H3K36me3, more specifically expressed genes
- BLUE: Polycomb
- BLACK: Repressive


Signal tracks are from downloading tab-delimited txt.gz from GSE22069,
extracting coordinates and values into a begGraph, and converting to bigWig.
The data have already been normalized according to the methods in the
manuscript.

