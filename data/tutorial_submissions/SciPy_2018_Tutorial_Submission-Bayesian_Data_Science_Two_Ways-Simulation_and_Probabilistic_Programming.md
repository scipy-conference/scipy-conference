# SciPy 2018 Tutorial Submissions: Bayesian Data Science Two Ways: Simulation and Probabilistic Programming

Contributors:

- Eric Ma
- Hugo Bowne-Anderson

## Short Description

In this tutorial, Hugo and Eric will build participants’ knowledge of Bayesian inference, workflows and decision making under uncertainty. We will start with the basics of probability via simulation and analysis of real-world datasets, building up to an understanding of Bayes’ theorem. We will then introduce the use of probabilistic programming to do statistical modelling. Throughout this tutorial, we will use a mixture of instructional time and hands-on time. During instructional time, we will use a variety of datasets to anchor our instruction; during hands-on time, which immediately follow instructional time, our participants will apply the concepts learned to the Darwin’s finches dataset, which will permeate the entire tutorial.

For maximal benefit, participants are expected to have experience writing for-loops and working with numpy arrays. The necessary syntax will be introduced during the tutorial, but familiarity will help. No knowledge of statistics is necessary. However, the most important and beneficial prerequisite is a will to learn new things. If you have this quality, you'll definitely get something out of this tutorial!

## Long Description

In this tutorial, Hugo and Eric will build participants’ knowledge of Bayesian inference, workflows and decision making under uncertainty. We will start with the basics of probability via simulation and analysis of real-world datasets, building up to an understanding of Bayes’ theorem. We will then introduce the use of probabilistic programming to do statistical modelling. Throughout this tutorial, we will use a mixture of instructional time and hands-on time. During instructional time, we will use a variety of datasets to anchor our instruction; during hands-on time, which immediately follow instructional time, our participants will apply the concepts learned to the Darwin’s finches dataset, which will permeate the entire tutorial.

The summarized outline is shown below; a more detailed outline is available after the summarized outline.

#### Probability through to Bayes’ Theorem: 1 hr

- Use `numpy`’s random number generators and real-world datasets to introduce probability from computational perspective.
- Instruction: Estimate probability of a finch having a beak length greater than X.
- Hands-on: Estimate probability of baseball player having a batting average greater than Y.
- Explore joint probability (P(A, B)) and conditional probability (P(A|B)).
- Instruction: What is probability of finch beak having beak length greater than X, given that it is a particular species.
- Hands-on: use baseball dataset.
- Deduce Bayes’ theorem as a direct consequence of joint and conditional probability.
- Instruction: given that finch beak is some length, what is the probability that it is a given species?
- Hands-on: use baseball dataset: given batting average, probability of team?

#### Break: 10 min.

#### Parameter estimation & hypothesis testing: 1 hr

- Parameter estimation: simulate disease incidence rate.
- Explore effect of varying amounts of data on posterior distribution estimate of incidence rate.
- Explore effect of different priors on posterior distribution.
- Explore effect of large amounts of data swamping the priors.
- This section will use ipywidgets to aid learners. We will develop `numpy`-based to solidify core computation concepts.
- Hypothesis testing (better called “Bayesian comparison of groups)
- Instruction: Explore comparison of two species of finches. Plot posterior distribution of two finch species’ beak lengths and the posterior distribution of differences.
- Hands-on: Explore comparison of two baseball teams.

#### Break: 10 min

#### Probabilistic Programming and multivariable parameter estimate (45 min)

- Instruction: PyMC3 introduction, provides statistical distribution library and sampling algorithms, allows us to think about statistical problems at a higher level of abstraction.
- Instruction: modified drug IQ dataset, implementing same concepts from numpy but now in PyMC3 code. Discover that we can have significant p-value but meaningless effect size. Highlight idioms, abstractions, and necessary data transformations to feed into PyMC3.
- Hands-on: Analyze sterilization method dataset. Discover that we can have zero uncertainty in an estimate, given the data.
- Hands-on: build on Darwin’s finches dataset.

#### Break: 10 min

#### Hierarchical modelling (45 min)

- Introduce hierarchical modelling and concepts; justify use of hierarchical modelling, based on the problem on hand, to pool information from related groups.
- Instruction: batting average of baseball players.
- Hands-on: Darwin’s finches. Related by common descent.

Total time: 4 hours, including breaks.

### TUTORIAL DETAILS

#### What is probability? A simulated introduction (1 hr)

We’ll introduce attendees to probability using numpy’s random number generators and real-world datasets (Darwin’s Finch beak data, baseball batting average data, disease incidence data).

Attendees will use these datasets to explore, for example, the probability of a finch having a beak length greater than a certain length or a baseball player having a particular batting average.

INSTRUCTION: 10 MINUTES (we’ll do one data set)
HANDS ON: 10 MINUTES (they’ll do another)

We’ll then explore joint probabilities P(A|B) and conditional probabilities P(A|B) and attendees will code up how to calculate such probabilities, for example, the probability of a particular finch beak length, given that the finch is of a particular species.

INSTRUCTION: 10 MINUTES (we’ll do one data set)
HANDS ON: 10 MINUTES (they’ll do another)

We’ll then deduce Bayes’ Theorem and attendees will code up an example using Finch beak data and see that both sides of Bayes’ Theorem are indeed equal.

INSTRUCTION: 10 MINUTES (we’ll do one data set)
HANDS ON: 10 MINUTES (they’ll do another)

#### BREAK 10 min

#### 2. Parameter estimation and hypothesis testing (1 hr)

##### Parameter Estimation

Often we want to estimate parameters, such as the rate of disease incidence. One way of doing so is by modeling the process as a biased coin flip (explain this further). The question then is: given a bunch of data, the results of the set of coin flips, how do we estimate the probability of heads for the coin flip?

We’ll first get the attendees to simulate the process of flipping a coin using numpy and then to compute and plot the posterior distribution.

We’ll get them to utilize the awesomeness of ipywidgets to see how the variance of the posterior gets smaller the more data you have.

We’ll get them to do this for a bunch of priors in order to see that, when you have enough data, the likelihood dominates the prior and the prior is not really that important!

They’ll also see that you need more data to get narrow distributions when p(heads) is close to 0.5!

INSTRUCTION: 10 MINUTES (we’ll do one data set)
HANDS ON: 20 MINUTES (they’ll do another)

##### Hypothesis Testing

Given two species of finches, we can ask the question: “do these species have the same mean beak length?”

Get attendees to plot posterior of mean beaks lengths \mu_A, \mu_B and posterior of the difference \delta !

INSTRUCTION: 10 MINUTES (we’ll do one data set)
HANDS ON: 20 MINUTES (they’ll do another)

#### BREAK 10 min

#### 3. Multi-variable parameter estimation using probabilistic programming (45 min)

In this section, we will introduce PyMC3 and its application in solving statistical inference problems.

Firstly, we will use a modified version of the “drug IQ” dataset from Kruschke (2013) (testing the effect of a drug on IQ). This dataset was used in Eric’s PyCon 2017 talk on Bayesian statistical analysis. In this example, we will show how even a frequentist p-value of less than 0.05 can still arise in a situation where the posterior uncertainty in effect size is so large as to be useless for interpretation. (15 minutes)

As a semi-hands-on activity, we will explore measurements of sterilization methods’ antibacterial efficacy, from a research laboratory at MIT. Here, participants will be progressively guided towards answering the question, “Which antibacterial method performs best, given the data?” (An delightfully unexpected inference we arrive at is that there is zero uncertainty surrounding one method’s 100% efficacy, given the data.) All necessary syntax for handling this section will be introduced in the Finches example. (15 min)

Finally, the class will use the Darwin’s finches, and use it to show how to implement the same test using PyMC3. This will introduce the necessary syntax and data format for two- and multi-group comparisons. (15 min)

#### BREAK 10 min

#### 4. Hierarchical Modelling (45 min)

In this section, participants will be introduced to the notion of hierarchical modelling, which when properly justified (whether by qualitative or quantitative methods), allows us to pool information from related groups of measurements.

We will highlight how to do this, again using the baseball batting average dataset. Experienced players will have tons of data, but new players (rookies) will have very little data available.

In the hands-on section, participants will use the Darwin’s finches dataset. We will investigate how common ancestry (a justifiable assumption) can be incorporated into the model by using a shared prior. This will allow us to show how the imposition of prior information can help deal with groups which have few samples.

## Setup Instructions

A conda environment.yml file is available on the GitHub repository https://github.com/ericmjl/bayesian-stats-modelling-tutorial. We will provide initialization scripts for both conda and virtualenv environments.
