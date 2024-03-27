# Data analysis of PreTalx data

The notebooks under this repository perform various data scientific tasks across the data that can be pulled out of PreTalx.
These can come in useful to direct resources during the review period.

## Setup

Simply use Conda:

```sh
conda env create
```

This sets up Jupyter Lab, so one can simply activate the environment and start it out.

```sh
conda activate scipy-conference-data-analysis
jupyter lab
```

If one already has a running Jupyter with a kernel that includes the `requests`, `pandas` and `tqdm` packages, they are likely fine to use that, and don't need to set up this environment.
Simply change the kernel of the notebooks so it points at that bespoke environment.
