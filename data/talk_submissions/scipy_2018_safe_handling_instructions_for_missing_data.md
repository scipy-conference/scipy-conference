# Safe handling instructions for missing data

Contributors:

- Dillon Niederhut

# Short summary

In machine learning tasks, it is common to handle missing data by simply
removing observations with missing values, or just replacing missing data with
the mean value for its feature. To show why this is problematic, we use
listwise deletion and mean imputing to recover missing values from artificially
created datasets, and we compare those models against ones with full
information. Unless quite strong independence assumptions are met, we observe
large biases in the resulting coefficients and an increase in the model's
prediction error. We conclude by repeating the experiment on a real dataset,
and showing the appropriate diagnostic and correction steps to handle missing
values.

# Abstract

Introduction

It is common in data analytics tasks to encounter incomplete observations, or
records in a database that contain non-attested values. Strategies for how to
handle these missing data points range from removing the entire record, to
estimating what the missing value "should" have been. These strategies largely
ignore the processes which are responsible for the generation of missing data,
and as such can introduce strong biases into models. In particular, the
treatment of missing values which appear truly randomly should differ from the
treatment of missing values whose appearance is related to other observed or
latent features.

Methods

To demonstrate when and how this bias appears, 450 datasets were randomly
generated with linear, quadratic, and sinusoidal relationships between two
features and one target. Fractions of data were removed according to whether
those missing values were related to other variables in the dataset, and these
values were handled according to one of four different strategies (deletion,
mean imputation, median imputation, and expectation maximization). These
datasets were fit to regression models, and their coefficients compared to
baseline models with full information. We repeat the experiment one more time
on an attested dataset as a concrete example of how missing values cause models
to change, and what can be done to safely correct it.

Results

We find that deleting record with missing values is only unbiased when the
distribution of missing values is completely stochastic with respect to the
other variables in the dataset. In all cases where the appearance of missing
values is related to one of the other predictors, or to the target, both
deletion and imputation produce strong biases in model coefficients. We find,
further, that increasing the amount of data collected does not reduce the
magnitude of this bias (so the common injuncture to collect more data is
unhelpful). On our attested dataset, we show that both deletion and mean
imputation cause one or more of the best features to drop from the model
entirely. Expectation maximization preserves the most important features (with
roughly similar coefficients).

We conclude with a set of recommendations for handing missing values. The first
step is to attempt to fix the acquisition to avoid absent or illegal values in
the first place. In the event that this is not possible, it is good practice to
collect several covariates, or variables related to the one with missing data,
during acquisition, to later facilitate the estimation of reasonable
replacement values. Finally, it is important to check for correlations between
the absence of data and both the features and target of the experiment. If
missing values appear truly stochastically, it is safe to remove those
observations. If they are correlated with your covariates, it should be
possible to estimate replacement values using full information models.

About

I am a Python developer and technical instructor at Enthought. I presented two
tutorials at SciPy 2017 (NumPy and Cython), and have published on the use of
information models in language. You can see those videos here
(http://dillon.niederhut.us/media), a list of publications here
(http://dillon.niederhut.us/products), and publicly available source code here
(https://github.com/deniederhut).
