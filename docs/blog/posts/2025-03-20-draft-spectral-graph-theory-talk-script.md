---
date: 2025-03-20
categories:
  - UNE
  - Master of Scientific Studies
  - CRICOS CODE 000441G
  - Jelena Schmalz
  - MATH503
  - Advanced Topics in Mathematics
  - Graph Theory
  - Spectral Graph Theory
  - Algebraic Graph Theory
  - Spectral and Algebraic Graph Theory
  - Daniel A. Spielman
authors:
  - fishfugu
---

# Draft of Script for Spectral Graph Theory Presentation

## Spectral Graph Theory: A Quick Tour

### Adventures with Complete Graphs, Star Graphs, Hypercubes & More

Hi everyone! Thanks for coming today, and welcome to my talk on Spectral Graph Theory - and what _Daniel A. Spielman_ refers to as "_The Zoo of Graphs_".

<!-- more -->

During this term, many of the examples I've seen of people introducing Spectral Graph Thewory (of just Graph Theory in general) have started with this particular caveat.

    ANIMATION: that's not a graph, this is!

This is not a graph... not in terms of Graph Theory anyway... this is.

Graph Theory is essentially the study of `nodes` (or `vertices` - as _Daniel A. Spielman_ is a fan of saying: "the terms will get used interchangably, sorry"), and `edges`, the connections between each of the `nodes`. Combining this with some of the ideas behind Linear Algebra, gives us Spectral Graph Theory... a field that’s equal parts mind-boggling, beautiful, and surprisingly practical.

    SLIDE: What Is Spectral Graph Theory?

    Basic definition: “Spectral” relates to the eigenvalues/eigenvectors of matrices associated with graphs (e.g. adjacency matrix, Laplacian).
    
    Why it matters: Bridges geometry, linear algebra, and combinatorics.

Spectral Graph Theory focuses on studying the properties of a graph through the `eigenvalues` and `eigenvectors` of matrices, such as the adjacency matrix \( A \) or the Laplacian matrix \( L \).

Why do we do that? Because, somewhat surpsingly, you can figure quite out a lot about a `network` (or a `graph`) by how these `eigenvalues` behave — everything from connectivity, to mixing rates of random walks, to whether the graph is friendly to your favourite algorithms.

If you’re picturing some big, unweildy, massive matrix... good! That's often what the implementation of these ideas requires... but we'll keep it simple for today. Most of these qualities can be understood clearly by looking at smaller examples first.

    ANIMATION - MANIM: Animate a small 3x3 or 4×4 adjacency matrix appearing on the screen, each entry lighting up if there’s an edge, going dark if there isn’t. Or each edge moving over to the matrix (twice) and turning into a 1... an the rest of the matrix being filled with 0s.

References:
- [Lectures on Spectral Graph Theory - Fan R. K. Chung](https://mathweb.ucsd.edu/~fan/research/cbms.pdf)

Also possibly read:
- Chung, F. R. K. (1997) Spectral Graph Theory, CBMS Regional Conference Series in Mathematics, 92, AMS
- [Godsil, C. and Royle, G. (2001) Algebraic Graph Theory, Springer](https://www.researchgate.net/publication/235410068_Algebraic_Graph_Theory)

