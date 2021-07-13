# Astar-grid

Motion Planning Algorithms can be broadly categorised into (a) Graph based Planning (b) Sampling based Planning. Through this project I've attempted to discretize a 
map by cell decomposition( Graph based planning) and navigate through this map using A* Search Algorithm.

Given a grid(picture) of a environment, a  starting point and an ending point, this application calculates the shortest path using A* Algorithm.
 
(i)The grid can be sketched using any tool.(Ive used MS Paint to sketch the grid here)
(ii)The obstacles are treated as 1 and free space is treated as 0.( so an inversion is applied on the image.(255 --> 0))

![Grid](https://github.com/nphilip1098/Astar-grid/blob/master/results/grid.jpeg)
![Astar-grid1](https://github.com/nphilip1098/Astar-grid/blob/master/results/Figure_2.png)
![Astar-grid2](https://github.com/nphilip1098/Astar-grid/blob/master/results/Figure_3.png)
