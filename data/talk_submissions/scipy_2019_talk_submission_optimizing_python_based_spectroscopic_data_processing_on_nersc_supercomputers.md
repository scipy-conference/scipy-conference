# Optimizing Python-based spectroscopic data processing on NERSC supercomputers

Contributors:

- Laurie Stephey
- Rollin Thomas
- Stephen Bailey

# Short summary

This talk is a case study that describes how a Python image processing pipeline
was optimized for increased throughput of 5-7x on a high-performance system.
The workflow of using profiling tools to find candidate kernels for
optimization and the techniques for speeding up these kernels will be
described. The most successful method used to obtain speedup was just-in-time
compiling using Numba; several successful examples will be provided.
Parallelization strategies using MPI and Dask will be compared, and preliminary
considerations for moving the code to GPUs will be discussed.

# Abstract

We present a case study of optimizing a Python-based cosmology data processing
pipeline designed to run in parallel on thousands of cores using supercomputers
at the National Energy Research Scientific Computing Center (NERSC). We hope a
wide audience of Python users can learn how to speed up their code from this
case study.

The goal of the Dark Energy Spectroscopic Instrument (DESI) experiment is to
better understand dark energy by making the most detailed 3D map of the
universe to date. The images (many spectra on a CCD) obtained nightly over a
period of 5 years starting this year (2019) will be sent to the NERSC Cori
supercomputer for processing and scientific analysis.

The DESI spectroscopic pipeline for processing these data is written almost
exclusively in Python. Writing in Python allows the DESI scientists to write
very readable scientific code in a relatively short amount of time, which is
important due to limited DESI developer resources. Even though DESI is
leveraging NumPy and SciPy wherever possible, Python can be substantially
slower than more traditional high performance computing languages like C++ and
Fortran.

The goal of this work is to increase the efficiency of the DESI spectroscopic
data processing at NERSC while satisfying their requirement that the software
remain in Python. Within this space we have obtained throughput improvements of
over 5x and 6x on the Cori Haswell and KNL partitions, respectively. Several
profiling techniques were used to determine potential areas for improvement
including Python's cProfile, line_profiler, Intel Vtune, and Tau. Once we
identified expensive kernels, we used the following techniques: 1)
JIT-compiling hotspots using Numba (the most successful strategy so far) and 2)
re-structuring the code to compute and store important data rather than
repeatedly calling expensive functions. We are now considering Dask as a more
flexible and robust alternative to MPI for parallelism in the DESI extraction
code. We will also explore the requirements for transitioning the DESI image
processing to GPUs (coming in the next NERSC system in 2020).

Supporting links:

DESI code on github (development ongoing):
https://github.com/desihub

DESI/NERSC data processing:
https://www.desi.lbl.gov/data-systems/

Previous presentations on this topic:
Lawrence Berkeley Lab LabTech 2018
https://labtech.lbl.gov/sessions
Intel booth talk Supercomputing 2018
https://docs.google.com/presentation/d/1mBNndC_VDwGO0UbdZtZuqq9jtbqsl86NZX9rFkChqkw/edit?usp=sharing

Presenting author speaking sample:
https://www.youtube.com/watch?v=N0niaVb5WyM&feature=youtu.be
