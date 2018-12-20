# SciPy 2018 Tutorial Submissions: Around the world in 80 ways: An introduction to working with geodata and cartopy

Contributors:

- Phil Elson

## Short Description

On the 1st of October 1872, Jules Verne’s character Phileas Fogg embarks on an adventure to circumnavigate the world in just 80 days. Travelling exclusively by sea and rail, Fogg voyages from the misty alleys of Victorian London to the exotic subcontinent and the Wild West in a race against the clock. Despite fastidiously counting each sunrise, he famously neglects the effect of crossing the dateline and thus arrives on a different day to the one he calculated.

The mistreatment of the dateline is far from unique to Phileas Fogg; it is not just the 24hr time discontinuity that we struggle with - the antimeridian is also a longitudinal discontinuity of 360 degrees for coordinate systems centered at the Greenwich Prime meridian. Whilst Cartesian treatment of geospatial data is a reasonable assumption with an appropriately transformed coordinate system and at large scale (small area), the discontinuities of the antimeridian and the poles frequently wreak havoc on our Cartesian tools when we treat larger area (global / small scale) data.

In this tutorial, join Phileas Elson on our own epic adventure by tracking Fogg’s travel log with careful non-Cartesian treatment as we go. Along the way, we will discover how many of the python libraries we may already know and love can be used in conjunction with cartopy to provide a powerful suite of open source geospatial tools.

We will cover many of the core concepts in cartopy, including topics such as: coordinate reference systems and projections; the matplotlib interface; geospatial image, data (NetCDF) and raster treatment; as well as geometry predicates and transformations. The knowledge developed from this tutorial will be applicable to a broad range of geospatial analyses (both raster and vector), and will provide hands-on experience of tools such as numpy, proj.4, matplotlib and shapely to name a few.

The tutorial will be applicable to a broad range of experiences, but familiarity with numpy and matplotlib will be essential to enable progress through the exercises. A prior awareness of tools such as shapely, proj.4, geopandas, and xarray/Iris will help, though are by no means essential. The tutorial will be made up of a number of exercises with each being designed to accommodate a broad range of expertise.

## Long Description

This tutorial will be a broad overview of many of the core concepts found within cartopy. cartopy’s strength comes from its interfaces to the the powerful ecosystem of open source tools that are known and loved, including matplotlib, proj.4 and shapely. The tutorial will be themed around the adventures of Phileas Fogg, giving us an excellent opportunity to explore treatment of geospatial data at all scales.

Each exercise will be time-bound, and will have extensions to ensure more experienced attendees remain engaged. There will also be opportunities for “ringers” (the authors/maintainers of some of the packages we are discussing) to positively contribute should they wish. The data and solutions will be prepared in advance to allow offline completion of the materials after-the-fact.

A draft outline of the tutorial (subject to change and adaptation):

- Introduction, location of tutorial material. (10 min)
- Demonstration of documentation. (10 min)
- CRS & Projections. Introduce the concept, and the implications. (10 min)
	- Glossary of terminology
	- Exercise (paper based): using pre-prepared laminated maps to understand projections (10 min). Extensions available.
- cartopy’s matplotlib interface and terminology (15 min)
	- Exercise: use cartopy to produce a map (15 min). Extensions available.
- -- break --
- Vectors and rasters
	- Exercise (paper based): Post it note bingo on Rasters vs. Vectors. (5 min). Extensions available.
	- Formats and tools that can be used on rasters and vectors. (20 min)
- Vector to vector transformations (30 min)
	- Point transformations
	- General (non-affine) geometry transformation
	- Exercise (paper): Transform a geometry by hand
	- Geometry predicates - intersection
	- Exercise: Processing & visualisation of Phileas Fogg’s travel log (15 min). Extensions available.
	- Demonstration of advanced vector to vector transformations (5 mins)
- Raster to raster transformations (30 min)
	- Clipping in matplotlib
	- Load image with rasterio + show on map
	- OGC webservices
	- Exercise: Plot image from webservice. Extensions available.
	- NetCDF
	- Exercise: Plot data with contour/contourf. Extensions available.
	- Regridding
	- Cartopy wind vector transformation
- Vector to raster (20 min)
	- Probability distribution
	- Shapely (& geopandas) vectorization + rasterization
	- Exercise: Produce a binary land-sea mask. Extensions available.
- Raster to vector (20 min)
	- Contours
	- Exercise: Use contours to produce a geometry for regions exceeding a data threshold. Extensions available.
- Conclusions (10 min)
- Total running time 225 minutes.

## Setup Instructions

Precise environment definitions will be provided closer to the time as part of the tutorial repository. All pre-requisite packages will be readily available through conda-forge on all platforms.
