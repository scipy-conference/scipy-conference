# SciPy 2018 Tutorial Submissions: pandas .head() to .tail()

Contributors:

- Tom Augspurger
- Joris Van den Bossche
- Dilon Niederhut

## Short Description

This tutorial is an introduction to pandas, a library providing data structures and algorithms for tabular data analysis. It's aimed at scientists and data analysts new to scientific Python. No previous experience with pandas is expected. Familiarity with the basics of Python will be helpful.

We'll work through a series of Jupyter notebooks together, with an emphasis on solving realistic problems as exercises. We'll cover
1. A definition of tabular data and pandas' data structures for tabular data 
2. How pandas' alignment by row and column labels simplifies data analysis 
3. groupby for analyzing subsets of a table grouped by some common factor 
4. Tidy data: how to structure your data to facilitate analysis. 
5. Performance: How to benchmark and profile code, and some common pandas performance pitfalls 
6. pandas' special support for time-series data.

## Long Description

This tutorial is an introduction to pandas, a library providing data structures 
and algorithms for tabular data analysis. 

The tutorial is given as a sequence of Jupyter notebooks. Attendees will work 
through the notebooks. The typical workflow will be 

1. Brief introduction of a concept, like "A `DataFrame` is a container for  heterogenous, tabular data..." 
2. Attendees work through an exercise exploring that concept (Read this CSV into  a `DataFrame` and check its dtypes) 
3. The instructors will demonstrate the provided solution, answering any questions that came up during the exercise 

### Environment Setup (10 minutes) 

Before the tutorial, attendees will be provided with a link to a GitHub repository containing all the datasets, Jupyter notebooks, and a conda `environment.yaml` file. We'll take some time to introduce the instructors while some attendees finish setting up their environment.

### Introduce tabular data and the dataframe (5 minutes) 

We'll introduce the high-level problems that pandas helps solve, beginning with a discussion of heterogenous, tabular data. We'll talk a bit about the dataframe as a container for heterogenous, tabular data. But the goal will be to get to hands-on examples as quickly as possible.

### pandas data IO and Introduction to pandas Data Structures (40 minutes) 

We'll see our first pandas IO function to read in a dataset. But the focus of this section is the data structures pandas provides. 

1. `DataFrame`: container for tabular data with labeled rows and columns. 
2. `Series`: container for 1-D data with labeled rows. 
3. `Index`: container for index and column labels. 

We'll develop a feel for working with these data structures by using some of the methods.

### Operations, Alignment, and Missing Data (45 minutes) 

Introduce pandas' novel *alignment* when doing binary operations between multiple `Series` or `DataFrame`s.

We'll compare pandas automatic alignment to manually aligning multiple `DataFrame`s by joining them together.

We'll emphasize the importance of having *meaningful row labels*, and how they can simplify your analysis.

We'll use pandas' alignment, which creates missing values, as a demonstration of missing values. We'll discuss some of the "strangeness" of `NaN`, pandas' missing value marker, some of the causes of missing data, and how to detect and handle missing data.

### GroupBy (45 minutes) 

We'll introduce *groupby*, a common operation for analyzing subsets of the data as a group. We'll introduce the *split, apply, combine* mental model for how to think about a groupby.

We'll discuss pandas' three types of group-wise functions: 

1. `.agg`: each input *group* forms one output *row* 
2. `.transform`: Each input *row* forms one output *row* 
3. `.apply`: Arbitrary output shape 

### Tidy Data (40 minutes) 

Now that we have some familiarity with manipulating datasets, we'll take a step back to think about *how to structure the data to facilitate analysis*. We'll see how a dataset can be represented in multiple forms. We'll see that *tidy data* is a particularly convenient form for many types of operations.

After introducing the definition of tidy data, we will transform a non-tidy dataset into a tidy one. After tidying the data, we'll go on to perform some interesting analysis.

### Performance (30 minutes) 

We will discuss some common performance pitfalls when using pandas. We'll introduce

1. Data types and conversion functions like `pd.to_datetime` 
2. Categoricals 
3. Vectorizaiton 
4. Efficient algorithms 

We'll also use this as a opportunity to introduce simple benchmarking within IPython with `%timeit` and some basic profiling. The emphasis will be on attendees measuring if a given method is slow, why it might be slow, and potential alternatives.

### Time-Series Data (35 minutes) 

(This section is "time permitting" depending on how much extra time is spent on environment setup, exercises, and questions.)

An exploration of pandas' support for time-series data. We'll introduce 

1. Pandas' formats for storing time-series data (`Timestamp` for moments in time, `Period` for intervals of time) 
2. Basics of working with timezones 
3. Resampling: a time-series-specific version of groupby 
4. Rolling and expanding window operations

## Setup Instructions

1) Install Miniconda for your platform 

- Download: https://conda.io/miniconda.html 
- instructions: https://conda.io/docs/install/quick.html 

If you already have conda, then update conda `conda update conda`; It's also fine to use virtualenv + pip. You should be able to pip install -r requirements.txt to get the same package versions as step 5.

2) Open a new shell after installing, so that conda is on your path 

3) Clone the repository at [https://github.com/tomaugspurger/pandas-head-to-tail](https://github.com/tomaugspurger/pandas-head-to-tail) 

	git clone https://github.com/tomaugspurger/pandas-head-to-tail 

If you don't have git installed, you can download the zip using the green "Clone or download" button, and then "Download ZIP". Note that the filename will be "pandas-head-to-tail-master" 

4) Change directory into the repository 

	cd pandas-head-to-tail 

5) Create the conda environment 

	conda env create 

6) Activate the environment 

	source activate ph2t 
	conda activate ph2t 

7) Run the check environment command 

	python check_environment 

8) Start the Jupyter notebook server 

	jupyter notebook