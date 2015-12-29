Manifest
========

This document is an auto-generated summary of the studies available. The title
of each section corresponds to the directory within this repo.



``hou-2012``
============
Physical domain boundaries from Hou et al 2012 in Kc cells. Table S2 contains
an excel file of physical domains. These are contiguous domains, so it's
probably more useful to look at them as boundaries. The 1-bp boundaries between
domains were calculated from Table S2 and a new BED file created.


:genome: dm3

Tracks
------

* Physical domains

* Physical domain boundaries


``jain-2015``
=============
Phantom peaks from Table S3, parsed from Excel and converted to bigBed format.


:genome: dm3

Tracks
------

* Phantom peaks


``lieberman-2009-hg19``
=======================
Hi-C data in K562 cells. *Note: only selected regions included*
Data were lifted over from hg18 to hg19


:genome: hg19

Tracks
------

* HiC chr11_5200000-5299999: K562 HiC contacts within beta globin locus

* Anchor bin


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


``wood-2011``
=============
Data are available as BED and WIG format files from GEO accession GSE30740. BED
files were minimally processed, by prepending "chr" to chromosome names,
converting negative coordinates to zero, and truncating peaks outside of
chromosome boundaries to the max length of the chromosome.


:genome: dm3

Tracks
------

* CP190 0hrs peaks

* SUHW 0hrs peaks

* BEAF 0hrs peaks

* CTCF 0hrs peaks

