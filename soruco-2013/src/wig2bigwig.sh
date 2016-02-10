#!/bin/bash
fetchChromSizes dm3 > dm3.chromsizes
wigToBigWig $1 dm3.chromsizes $2
rm dm3.chromsizes
