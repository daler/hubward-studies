Manifest
========

This document is an auto-generated summary of the studies available. The title
of each section corresponds to the directory within this repo.



``sexton-2012``
===============
"Domain coordinates (from dm3 assembly) of the physical
domains, defined by the distance-scaling model as described in Figure 2C. The
epigenomic class of each physical domain, as defined by the clustering
described in Figure 3, is also identified."

Data are from Table S1 from doi:10.1016/j.cell.2012.01.010, and the above text
is the legend from that table.

The original Table S1 is an Excel spreadsheet in BED-like format. Spaces in
feature names were converted to underscores for conversion to bigBed format.

See git@github.com:daler/hubward-studies.git for details on how to reconstruct
this dataset.


:genome: dm3

Tracks
------

* TADs


``test/lieberman-2009``
=======================
Hi-C data in K562 cells. *Note: only selected regions included*

:genome: hg18

Tracks
------

* HiC chr11_5200000-5299999: K562 HiC contacts within beta globin locus

* Anchor bin


``test/yip-2012``
=================
Distal regulatory modules (DRMS) intersecting ...

:genome: hg19

Tracks
------

* K562 DRM+E

* K562 DRM+WE


``vanBemmel-2010``
==================
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


:genome: dm2

Tracks
------

* LAD domains (Kc)

