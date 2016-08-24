Manifest
========

This document is an auto-generated summary of the studies available. The title
of each section corresponds to the directory within this repo.



``alvarez-dominguez-2014``
==========================

See `Figure
1 <http://www.bloodjournal.org/content/bloodjournal/123/4/570/F1.large.jpg>_`
from the paper for info on the classes of long non-coding RNAs.

Briefly:

* lincRNA: intergenic lncRNA
* alncRNA: antisense lncRNA
* ilncRNA: intronic overlapping lncRNA
* elncRNA: enhancer lncRNA
* shlncRNA: sRNA host lncRNA


:genome: mm9

Tracks
------

* lincRNA

* alncRNA

* ilncRNA

* shlncRNA

* plncRNA


``dowen-2014-cohesin-chiapet``
==============================
Interactions in mouse ES cells using ChIA-PET to SMC1 (a component of the
cohesin complex).

Merged SMC1 ChIA-PET interactions (Table S1E) were converted to BEDPE format
and then to paired-end BAM files using BEDTools. This allows the BAM file to be
lifted over to other genomes using CrossMap.

Super-enhancer coordinates from Table S4A were converted to BED and then to
bigBed.


:genome: mm9

Tracks
------

* SMC1 interactions

* super-enhancers


``filion-2010``
===============
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



:genome: dm3

Tracks
------

* chromatin colors

* RED chromatin

* BLACK chromatin

* YELLOW chromatin

* GREEN chromatin

* BLUE chromatin


``fuda-2015``
=============
Called peaks from GAF ChIP-seq.

BED file was downloaded from GSE40646 and converted to bigBed. The original BED
file used macs to call peaks. The original experiment included 2 replicates of
GAF ChIP-seq in both mock and GAF knockdown S2 cells; the GEO entry contains
only the mock data (a merge of the two replicates).


:genome: dm3

Tracks
------

* GAF peaks


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


``moshkovich-2011``
===================
AGO2 ChIP-seq peaks from S2 and S3 cells. Data were downloaded from GEO GSE22623.


:genome: dm3

Tracks
------

* AGO2 S2 peaks

* AGO2 S3 peaks


``sahlen-2015-hicap``
=====================
Interactions in mouse ES cells as determined by HiCap (a capture modification
of HiC).

Supplemental tables were downloaded as a zip of Excel files. "Supplementary
Table 5v5.xlsx" contains three worksheets (promoter-enhancer,
promoter-promoter, and enhancer-enhancer interactions). Each of these were
converted to BEDPE format and then to paired-end BAM using BEDTools, which can
be lifted over with CrossMap. Note that the promoter anchor sites are provided
as single-bp TSS locations, so the BEDPE files use TSS and TSS+1 for the start
and stop coords respectively.


:genome: mm9

Tracks
------

* promoter-to-enhancer

* promoter-to-promoter

* enhancer-to-enhancer


``schoenfelder-2015-capture-HiC``
=================================
Interactions in mouse ES and fetal liver cells as determined by
promoter-capture HiC.

Data were downloaded from ArrayExpress, converted to BEDPE, and then to
paired-end BAM for liftover using CrossMap.

To prepare data for a selected set of genes, the promoter bait was first
extracted according to the gene name (4th column in raw data) and colored red.
The rest of the contacts that interact with that promoter are colored according
to their log(obs/exp) (last column in the raw data), where the color range goes
from 7.0 (light gray) to 18 (black). All selected genes for ESC and FLC are
scaled to the same color scale, so their interaction frequencies can be
compared across genes and across cell types.

If no significant interactions were found for a gene in a cell type, then there
will be an empty file in place of the bigBed, which will show up in the genome
browser as a yellow band.


:genome: mm9

Tracks
------

* ESC promoter-other

* ESC promoter-promoter

* FLC promoter-other

* FLC promoter-promoter

* ESC promoter-other bait

* ESC promoter-promoter bait

* FLC promoter-other bait

* FLC promoter-promoter bait

* Runx1, FLC

* Rgs10, FLC

* Cpeb4, FLC

* Myb, FLC

* Plcl2, FLC

* Bcl11a, FLC

* Car2, FLC

* Meis1, FLC

* Tmco1, FLC

* Hbb-b1, FLC

* Hbb-b2, FLC

* Hbb-bh1, FLC

* Hbb-y, FLC

* Hba-a1, FLC

* Hba-x, FLC

* Mgst3, FLC

* Gypa, FLC

* Ppox, FLC

* Add2, FLC

* Pcx, FLC

* Clk3, FLC

* Stx11, FLC

* Cnnm2, FLC

* Galns, FLC

* Klf13, FLC

* Dapk2, FLC

* Add3, FLC

* Foxo3, FLC

* Ifnar2, FLC

* Junb, FLC

* Mylip, FLC

* Bmp2k, FLC

* Abhd16a, FLC

* Rab43, FLC

* Rhbdf1, FLC

* Grina, FLC

* Rhof, FLC

* Fads2, FLC

* Bcl2l1, FLC

* Nfe2l1, FLC

* Ccnb1, FLC

* St3gal5, FLC

* Ube2f, FLC

* Amd1, FLC


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


``soruco-2013``
===============
CLAMP ChIP-seq in Kc and S2 cells, as well as in MSL2 RNAi cells.

Data downloaded from GEO, accession GSE39271.

From the supplemental methods: signal is log2 fold change of IP over input,
after binning reads into 20-bp bins and normalizing by respective library size.


:genome: dm3

Tracks
------

* CLAMP GFP KD, Kc

* CLAMP GFP KD, S2

* CLAMP MSL2 KD, S2


``test/lieberman-2009``
=======================
Hi-C data in K562 cells. *Note: only selected regions included*

:genome: hg18

Tracks
------

* HiC chr11_5200000-5299999: K562 HiC contacts within beta globin locus

* Anchor bin

* Paired interactions: Paired interaction within beta globin locus


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
Lamin-associated domains (LADs) in fly Kc cells as determined by DamID-chip.

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
Insulator peaks in fly Kc cells during the ecdysone response as determined by
ChIP-seq.

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

