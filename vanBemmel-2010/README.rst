Raw data
--------
The original data is a flat text file in GFF format listing the positions of
all 412 LADs (Drosophila melanogaster genome sequence release 4.3).

Score (column 6) indicates the fraction of array probes inside the LAD with
a positive LAM DamID logratio, after applying a running median filter with
window size 5.

Processing
----------
Features were converted from GFF to BED format. The original data were in dm2
assembly coordinates. Grayscale colors were assigned based on the original
scores, with black being the highest.
