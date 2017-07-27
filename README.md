# GAIP

Geoscience Australia Image Processor

## Instructions (quickstart)

Note this is an older branch of gaip, which is preserved as an interim solution for maintaining a downstream product (WOfS).

These instructioned are tailored to NCI/Raijin system.

First, open terminal (ssh raijin).

Obtain and prepare gaip software. E.g., git checkout and make, and configure as a loadable module. Prepare the environment by loading modules containing dependencies:

``` 
module use /g/data/v10/private/modules/modulefiles
module load gcc/5.2.0 core
```

If there are multiple versions of gaip installed, ensure that the correct scripts will be invoked. For example, work in a directory containing `pq_script_generator.py` and `run_PQ.pbs`, checking that the latter pbs script contains lines which load *the wofs pq variant of* the gaip module (on the worker nodes). Avoid actually loading the gaip module in the interactive terminal to ensure no ambiguity between script versions.

`cd /g/data/v10/testing_ground/4.2.5-pq-wofs`

The necessary inputs are the level1 and NBAR scenes (both are necessary). There is also one ancillary product, the land-sea rasters, and its configuration is hard-coded.

The python pq_script_generator.py will produce a bash script to kick off the job, and will immediately source (execute) that script unless the `--test` argument is supplied (e.g., permitting modification of PBS settings for just one job). 

At the conclusion of the job, the .stderr log should contain a message such as 'progress looks :)', signalling whether any issues were encountered. This is worth checking for.

Certain naming conventions are expected by gaip. If the input folders contain exceptions, then a staging area should be used as input and be populated with a cleaned set of symbolic links. For example, applying a rule of only processing definitive (not predictive) datasets:

`for file in /g/data/v10/reprocess_interim/ls7/level1/2016/12/L*OTH*; do ln -s $file $(basename $file); done && rm *PREDICT*`

Any job will result in log files and, for each scene, a .completed file (small), a packaged pqa output (e.g. roughly 8 gig), and a folder of intermediate outputs (e.g. >100gig; presumably uncompressed rasters). The latter should be cleaned up for sake of storage space.
