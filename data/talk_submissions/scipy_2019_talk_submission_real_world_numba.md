# Real-world Numba: creating a skeleton analysis library

Contributors:

- Juan Nunez-Iglesias

# Short summary

Skan is a Python library to analyze skeleton images, such as images o

branching neurons, or of the molecular skeleton of a cell. It is written using
NumPy, SciPy, and pandas, with key functions compiled by Numba for speed. I'll
briefly describe the library and application, but then spend most of the time
discussing Skan's gritty innards, including: how to write n-dimensional image
analysis code instead of baking in 2D- or 3D-only logic; examples of using Numba
to speed up real-world array-based code; why you should know about memory
layout; and the versatility of SciPy's sparse matrix formats.

# Abstract

Skeletons are single-pixel thick representations of networks within an image,
and have wide application to understanding the structural properties o

objects. For example, skeletons have been used to model human poses, neuronal
morphology, nanofiber structure, road networks, kidney development, and vascular
networks, among others. These applications include both 2D and 3D images, and
even 3D images collected over time, underscoring the need for skeleton analysis
software to support multiple imaging modalities and dimensionality.

In collaboration with colleagues at the University of Melbourne, over the past
year I've been developing a software tool to analyze the membrane skeleton of
red blood cells infected by the malaria parasite. The paper describing this
software's application to malaria research is published in PeerJ [1]\_. In this
talk, I'll briefly describe the software and its application, including the what
skeletons are, why we would want to measure them, and the algorithms involved in
doing so. Then I will dive into parts of the code that should be o

broad interest to the SciPy community, especially those involved in image
analysis. Specifically, I will describe:

- how to "think in n-dimensions" when working with NumPy arrays, rather than
  write algorithms specifically for 2D or 3D arrays.
- how Skan uses standard scientific Python data structures, such as SciPy sparse
  matrices and pandas DataFrames, to represent intermediate and final outputs of
  the program, maximizing interoperability with the SciPy ecosystem,
- my experiences with Numba, a just-in-time compiler (JIT) for Python code
  manipulating NumPy arrays [2]\_,
- the importance of memory access order when dealing with compiled array
  operations.

Skan is open source [3]\_, available under a 3-clause BSD license,
well-documented, and installable from PyPI, conda-forge, as well as the GitHub
master branch.

.. [1] https://peerj.com/articles/4312/
.. [2] I wrote a blog post about this [4]\_, which shows the flavor of what I
want to show, though I would rely less on hyperlinks in the talk! I would also
talk about other issues such as testing and measuring test coverage for Numba
code.
.. [3] https://github.com/jni/skan and https://jni.github.io/skan
.. [4]
https://ilovesymposia.com/2016/12/20/numba-in-the-real-world/
