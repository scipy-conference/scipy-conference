# SciPy 2018 Tutorial Submissions: Network Analysis Made Simple Part I: Network Fundamentals

Contributors:

- Eric Ma
- Mridul Seth

## Short Description

This tutorial is for Pythonistas who want to understand relationship problems - as in, data problems that involve relationships between entities. Participants should already have a grasp of for loops and basic Python data structures (lists, tuples and dictionaries). By the end of the tutorial, participants will have learned how to use the NetworkX package in the Jupyter environment, and will become comfortable in visualizing large networks using Circos plots. Other plots will be introduced as well. It will also form the grounding knowledge for Part II of the tutorial.


## Long Description

Have you ever wondered about how those data scientists at Facebook and LinkedIn make friend recommendations? Or how epidemiologists track down patient zero in an outbreak? If so, then this tutorial is for you. In this tutorial, which is Part I of a two-part series, we will use a variety of datasets to help you understand the fundamentals of network thinking, with a particular focus on constructing, summarizing, and visualizing complex networks. With this tutorial, you will be well equipped to explore advanced topics (dynamics on graphs, evolving graphs, and network propagation methods) in Part II.

### Part 1: Introduction (30 min)

- Networks of all kinds: biological, transportation.
- Representation of networks, NetworkX data structures
- Basic quick-and-dirty visualizations

### Part 2: Hubs and Paths (40 min)

- Finding important nodes; applications
- Pathfinding algorithms and their applications
- Hands-on: implementing path-finding algorithms
- Visualize degree and betweenness centrality distributions.

### Part 3: Cliques, Triangles & Structures (40 min)

- Definition of cliques
- Triangles as the simplest complex clique, applications
- Using path-finding algorithms to find structures in a graph.
- Open triangles as recommender systems.

### Part 4: Advanced Network Visualizations (40 min)

- Basic concepts in rational layouts: node positioning, node colouring.
- Plots: Circos, Arc, Hive, Matrix, Flow plots

### Part 5: Bipartite Graphs (30 min)

- Definition of bipartite graphs, applications
- Constructing bipartite graphs in NetworkX.
- Summary statistics of bipartite graphs
- Double-Arc plots for visualization

## Setup Instructions

The material can be found online at GitHub: https://github.com/ericmjl/Network-Analysis-Made-Simple. No special materials are required. Two convenience installation scripts are also provided: one for using virtualenv, the other for using conda environments.

This year, the material will be updated to reflect updates in NetworkX (now version 2.0), as well as developments to nxviz (now version 0.3.3). We will highlight practical convenience functions for loading graph data from CSV files into NetworkX, as well as the declarative API for rational complex network visualization.
