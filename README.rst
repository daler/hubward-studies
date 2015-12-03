Overview
--------
This repository holds directories of config files for published studies that
can be processed locally with `hubward <https://github.com/daler/hubward>`_.

The goal is for users to mix-and-match (and contribute!) studies from this
repository to build their own custom track hubs, enabling easy visualization of
published data alongside their own data.

Usage
-----
Install required software. It's all available in `bioconda
<https://bioconda.github.io/>`_. There are two versions: just the Python
package, or Python package plus all outside dependencies like UCSC utilities,
BEDTools, and more.  If you're unsure, choose the second option::

    # option 1: just the Python package
    conda install -c bioconda hubward

    # option 2: Python package plus extras
    conda install -c bioconda hubward-all


Clone the github repo::

    git clone https://github.com/daler/hubward-studies.git

Go to that directory and process the test studies::

    cd hubward-studies
    hubward process test/lieberman-2009 test/yip-2012

You should get a lot of log output something like this::

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

If you get errors saying that a program can't be found (like `fetchChromSizes`
or `bedToBigBed`), then try installing all the external dependencies as in
option 2 above.

The Lieberman et al data are in hg18 coordinates, so lift them over::

    hubward liftover \
        --from_assembly hg18 \
        --to_assembly hg19 \
        test/lieberman-2009 \
        lieberman-2009-hg19

Now edit the `example-group.yaml` to reflect your server information.  The
`studies` section is already filled in to include the two test studies. When
you're ready, upload::

    hubward upload example-group.yaml


