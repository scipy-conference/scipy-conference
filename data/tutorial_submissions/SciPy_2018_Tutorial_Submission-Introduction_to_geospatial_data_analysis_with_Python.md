# SciPy 2018 Tutorial Submissions: Introduction to geospatial data analysis with Python

Contributors:

- Joris Van den Bossche
- Dani Arribas-Bel
- Sergio Rey
- Levi Wolf

## Short Description

This tutorial is an introduction to geospatial data analysis in Python, with a focus on tabular vector data. 
It is the first part in a series of two tutorials; this part focuses on introducing the participants to the different libraries to work with geospatial data and will cover munging geo-data and exploring relations over space. This includes importing data in different formats (e.g. shapefile, GeoJSON), visualizing, combining and tidying them up for analysis, and will use libraries such as `pandas`, `geopandas`, `shapely`, `PySAL`, or `rasterio`. The second part will built upon this and focus on more more advanced geographic data science and statistical methods to gain insight from the data.

No previous experience with those geospatial python libraries is needed, but basic familiarity with geospatial data and concepts (shapefiles, vector vs raster data) and pandas will be helpful.

The tutorial will cover the following topics, each of them using Jupyter notebooks and hands-on exercises with real-world data:

1. Introduction to the open source geospatial ecosystem in Python
2. Introduction to vector data and GeoPandas
3. Spatial relationships and operations
4. Advanced visualization
5. Spatial joins and overlays
6. Spatial weights
7. Short intro to parallel/distributed geospatial analysis with Dask


## Long Description

This tutorial is an introduction to geospatial data analysis in Python, with a focus on tabular vector data. 
It is the first part in a series of two tutorials; this part focuses on introducing the participants to the different libraries to work with geospatial data and will cover munging geo-data and exploring relations over space. This includes importing data in different formats (e.g. shapefile, GeoJSON), visualizing, combining and tidying them up for analysis, and will use libraries such as `pandas`, `geopandas`, `shapely`, `PySAL`, or `rasterio`. The second part will built upon this and focus on more more advanced geographic data science and statistical methods to gain insight from the data.

No previous experience with those geospatial python libraries is needed, but basic familiarity with geospatial data and concepts (shapefiles, vector vs raster data) and pandas will be helpful.

The tutorial will cover the following topics, each of them using Jupyter notebooks and hands-on exercises with real-world data:

### 1. Environment set-up (10 min)

Before the tutorial, attendees will be provided with a link to a GitHub repository containing all the datasets, Jupyter notebooks, and a conda environment.yaml file and pip requirements file. 

### 2. Introduction to the open source geospatial ecosystem (15 min)

An overview is given of the important OSGeo projects (GDAL/OGR, GEOS) on which the geospatial ecosystem in python is built, and a brief introduction is given about the python wrappers for those libraries (fiona, shapely, pyproj, rasterio, ...)

### 3. Introduction to vector data and GeoPandas (40min)

The idea of raster data and its attributes is explained, differentiating it from raster data, and how it maps to GeoPandas GeoDataFrames. Then the GeoSeries and GeoDataFrame objects and it capabilities will be further introduced. Further basic topics will be used: working with individual Shapely geometry points, importing and exporting GIS file formats, basic visualization with GeoPandas, changing coordinate transformation systems.

### 4. Spatial relationships and operations (40 min)

In this part we will introduce the spatial predicates (intersects, contains, within, ..) and operation (intersection, distance, buffer), and apply those methods on some practical example cases (calculation of closest points, intersection with buffers, ..).

### 5. Advanced visualization (30 min)

We already used the basic plot method of GeoPandas, but in this part we will use some other libraries to make more advanced visualizations: combine with cartopy for projections, using geoplot for more high-level plotting functionality, interactive figures with leaflet or bokeh.

### 6. Spatial joins and overlays (30 min)

Here we will see how the geopandas sjoin and overlay functions can be used to combine data of different datasets based on their spatial relationship.

### 7. Spatial weights (50 min)

In this part, the basic concepts and roles of weights in spatial analysis is explained, and shown how those weights can be constructed in different ways. Further, some analyses and visualization of the spatial weights are performed.

### 8. Parallel/distributed geospatial analysis with Dask (15 min)

This last part will shortly showcase how much of the previous functionality we have seen in this tutorial can be used on big data or parallellized by combining geopandas with Dask.

---

In the above outline and timings we did not explicitly include time for the exercises because each part will have exercises woven into the explanations (each time after introducing some new concepts, the participants will have to do some exercises on this, after which we briefly show the solutions and clarify where needed). As an example, see eg [https://github.com/jorisvandenbossche/DS-python-data-analysis/blob/master/notebooks/pandas_02_basic_operations.ipynb](https://github.com/jorisvandenbossche/DS-python-data-analysis/blob/master/notebooks/pandas_02_basic_operations.ipynb) and other notebooks in this repo.

## Setup Instructions

The materials for the workshop and all software packages have been tested on
Python 2 and 3 on the following three platforms:

- Linux (Ubuntu-Mate x64)
- Windows 10 (x64)
- Mac OS X (10.11.5 x64).

The workshop depends on the following libraries/versions:

* `numpy>=1.11`
* `pandas>=0.18.1`
* `matplotlib>=1.5.1`
* `jupyter>=1.0`
* `seaborn>=0.7.0`
* `pip>=8.1.2`
* `geopandas>=0.2`
* `pysal>=1.11.1`
* `cartopy>=0.14.2`
* `pyproj>=1.9.5`
* `shapely>=1.5.18`
* `geopy>=1.10.0`
* `scikit-learn>=0.17.1`
* `bokeh>0.11.1`
* `mplleaflet>=0.0.5`
* `datashader>=0.2.0`
* `geojson>=1.3.2`
* `folium>=0.2.1`
* `statsmodels>=0.6.1`
* `xlrd>=1.0.0`
* `xlsxwriter>=0.9.2`

### Linux/Mac OS X

1. Install Anaconda
2. Get the most up to date version:

`> conda update conda`

4. Create an environment named `gds-scipy18`:

`> conda create --name gds-scipy18 python=3 pandas numpy matplotlib bokeh seaborn scikit-learn jupyter statsmodels xlrd xlsxwriter`

5. Install additional dependencies:

`> conda install -c conda-forge --name gds-scipy18 geojson geopandas mplleaflet==0.0.5 datashader==0.2.0 cartopy==0.14.2 folium==0.2.1`

6. To activate and launch the notebook:

```
> source activate gds-scipy18

> jupyter notebook
```

### Windows

1. Install
[Anaconda3-4.0.0-Windows-x86-64](http://repo.continuum.io/archive/Anaconda3-4.0.0-Windows-x86_64.exe)
2. open a cmd window
3. Get the most up to date version:

`> conda update conda`

4. Add the `conda-forge` channel:

`> conda config --add channels conda-forge`

5. Create an environment named `gds-scipy18`:

`> conda create --name gds-scipy18 pandas numpy matplotlib bokeh seaborn statsmodels scikit-learn jupyter xlrd xlsxwriter geopandas==0.2 mplleaflet==0.0.5 datashader==0.2.0 geojson cartopy==0.14.2 folium==0.2.1`

6. To activate and launch the notebook:

```
> activate gds-scipy18

> jupyter notebook
```

### Testing

Once installed, you can run the notebook `test.ipynb` placed under
`content/infrastructure/test.ipynb` to make sure everything is correctly
installed. Follow the instructions in the notebook and, if you do not get any
error, you are good to go.
