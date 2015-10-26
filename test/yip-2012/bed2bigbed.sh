#!/bin/bash
set -e
source="$1"; target="$2"
gunzip -c $source | LC_COLLATE=C sort -k1,1 -k2,2n > ${target}.tmp.bed
chromsizes="$(dirname $source)/hg19"
[[ ! -e $chromsizes ]] && fetchChromSizes hg19 > $chromsizes
bedToBigBed -type=bed4 ${target}.tmp.bed $chromsizes $target
rm ${target}.tmp.bed
