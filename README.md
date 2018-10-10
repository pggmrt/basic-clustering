# Basic-Clustering

Points are just a two dimensional object, so we can use them to represent numerical features of a data set.  Here we will implement an iterative algorithm  which will be a specific case of the  $k$-means clustering algorithm.  The algorithm will require us to keep track of two clusters, each of which has a list of points and a center (which is another point, not necessarily one of the points we are clustering).  After making an initial guess at the center of the two clusters ($C_1$, $C_2$, the steps proceed as follows

1. Assign each point to $C_1$ or $C_2$ based on whether the point is closer to the center of $C_1$ or $C_2$.
2. Recalculate the center of $C_1$ and $C_2$ based on the contained points.

See [reference](https://en.wikipedia.org/wiki/K-means_clustering#Standard_algorithm) for more information.

The returned values are  the two centers of the clusters ordered by greatest `x` value.  
