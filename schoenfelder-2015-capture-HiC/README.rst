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
