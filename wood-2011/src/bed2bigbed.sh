#!/bin/bash
set -e
source=$1
target=$2
CHROMSIZES=$(dirname "${target}")/dm3.chromsizes

if [ ! -e $CHROMSIZES ]; then
    fetchChromSizes dm3 > $CHROMSIZES
    awk -F "\t" '{OFS="\t"; print $1, "0", $2}' $CHROMSIZES > ${CHROMSIZES}.bed
fi


zcat ${source} \
    | awk -F "\t" '{OFS="\t"; print "chr"$1,($2<0?0:$2),$3}' \
    | sort -k1,1 -k2,2n \
    > "${target}.tmp"
bedtools intersect -a "${target}.tmp" -b ${CHROMSIZES}.bed > "${target}.tmp.clipped"
bedToBigBed "${target}.tmp.clipped" dm3.chromsizes "${target}"
