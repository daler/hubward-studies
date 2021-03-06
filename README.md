# Overview
This repository holds directories of config files for published studies that
can be processed locally with [hubward](https://github.com/daler/hubward).

The goal is for users to mix-and-match (and contribute!) studies from this
repository to build their own custom track hubs, enabling easy visualization of
published data alongside their own data.

The [manifest](manifest.rst) lists what tracks are currently available in the
repo.

# Getting started
This first section will get you set up and running a small test data set to
confirm that everything is set up correctly.

Install required software. It's all available in
[`bioconda`](https://bioconda.github.io). There are two versions: just the
Python package, or Python package plus all outside dependencies like UCSC
utilities, BEDTools, and more.  If you're unsure, choose the second option:

```bash
# option 1: just the Python package
conda install -c bioconda hubward

# option 2: Python package plus extras
conda install -c bioconda hubward-all
```


Clone the github repo:

```bash
git clone https://github.com/daler/hubward-studies.git
```

Go to that directory, and install any additional requirements:

```bash
conda install -c r -c bioconda --file requirements.txt
```

and process the test studies:

```bash
cd hubward-studies
hubward process test/lieberman-2009 test/yip-2012
```

You should get a lot of log output something like this:

```
[2015-12-03 14:03:54,666] hubward INFO Study: lieberman-2009, in "test/lieberman-2009"
[2015-12-03 14:03:54,667] hubward INFO     test/lieberman-2009/processed-data/chr11_5200000_5299999.bigwig does not exist
[2015-12-03 14:03:56,454] hubward INFO     test/lieberman-2009/processed-data/chr11_5200000_5299999.bigwig is up to date
[2015-12-03 14:03:56,455] hubward INFO     test/lieberman-2009/processed-data/chr11_5200000_5299999.bigbed does not exist
[2015-12-03 14:03:57,713] hubward INFO     test/lieberman-2009/processed-data/chr11_5200000_5299999.bigbed is up to date
[2015-12-03 14:03:57,760] hubward INFO Study: yip-2012, in "test/yip-2012"
[2015-12-03 14:03:57,761] hubward INFO     test/yip-2012/processed-data/drm_k562_enhancers.bigbed does not exist
pass1 - making usageList (23 chroms): 2 millis
pass2 - checking and writing primary data (12046 records, 4 fields): 14 millis
[2015-12-03 14:03:57,816] hubward INFO     test/yip-2012/processed-data/drm_k562_enhancers.bigbed is up to date
[2015-12-03 14:03:57,816] hubward INFO     test/yip-2012/processed-data/drm_k562_weak-enhancers.bigbed does not exist
pass1 - making usageList (23 chroms): 2 millis
pass2 - checking and writing primary data (10787 records, 4 fields): 13 millis
[2015-12-03 14:03:57,872] hubward INFO     test/yip-2012/processed-data/drm_k562_weak-enhancers.bigbed is up to date

```

If you get errors saying that a program can't be found (like `fetchChromSizes`
or `bedToBigBed`), then try installing all the external dependencies as in
option 2 above.

The Lieberman et al data are in hg18 coordinates, so lift them over:

```bash
hubward liftover \
    --from_assembly hg18 \
    --to_assembly hg19 \
    test/lieberman-2009 \
    lieberman-2009-hg19
```

You can now use the processed data for downstream analysis, or if you have
a server available you can upload the data to a trackhub to visualize in the
UCSC Genome Browser.  To do so, edit the `example-group.yaml` file to reflect
your server information.  The `studies` section is already filled in to include
the two test studies. When you're ready, upload:

```bash
hubward upload example-group.yaml
```


# Preparing all configured studies

Run the preprocessing script `metaprocess.py`. This will:

* look for all directories containing a `metadata.yaml` file
* exclude those that have been lifted over so that only the original studies are documented
* create a `manifest.rst` file
* add the directory, study description, and configured tracks to the `manifest.rst` file as documentation
* add a line to `to_process.sh` for each original study
* add a final line to `to_process.sh` that will perform the liftovers as needed.

Then edit the `liftovers.tsv` file to indicate which studies should be lifted
over. Note that this file is processed sequentially, so studies that need to be
incrementally lifted over are handled properly.

Then run the `to_process.sh` script to process and update all studies as needed.

Finally, re-run `metaprocess.py` to get an updated list of which studies to
upload. If a study was lifted over to another assembly, only the lifted-over
version will be included.

A summary:

```bash

# initial run to find all configured studies
python metaprocess.py

# then edit liftovers.tsv to add any liftovers

# process all configured studies and then perform liftovers. May take a while.
bash to_process.sh

# re-run to get an updated `to_upload.txt`
python metaprocess.py
```

