# Lecture 4

## Probabilistic Roadmap (PRM)

* Kavraki, et al. '96
* Sample a set of states uniformly at random
  * Vertices in the state graph (called roadmap)

![img](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-visualisation.gif)

![1566602020447](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/c-space-prm.png)

### State graph / Roadmap construction algorithm

1. Loop:

   1. Sample a configuration ![q](https://latex.codecogs.com/gif.latex?q) uniformly at random from the state space

      ![1566602240994](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/roadmap-construct-alg-1.png)

   2. If ![q](https://latex.codecogs.com/gif.latex?q) is not in collision,

      1. Add ![q](https://latex.codecogs.com/gif.latex?q) as a vertex to the state graph

      2. For all vertices ![q%27](https://latex.codecogs.com/gif.latex?q%27) within ![D](https://latex.codecogs.com/gif.latex?D) distance from ![q](https://latex.codecogs.com/gif.latex?q) in the state graph:

         ​	![1566602272435](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/roadmap-construct-alg-2.png)

         1. If the line segment (in C-space) between ![q](https://latex.codecogs.com/gif.latex?q) and ![q%27](https://latex.codecogs.com/gif.latex?q%27) is not in-collision, add an edge ![qq%27](https://latex.codecogs.com/gif.latex?qq%27) to the state graph. Note in the example above, the line segment ![qq%27](https://latex.codecogs.com/gif.latex?qq%27) **is** in-collision, so the image below is the result of continuously iterating this algorithm until another configuration ![q%27%27](https://latex.codecogs.com/gif.latex?q%27%27) was found for which we can connect.

            ![1566602153261](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/roadmap-construct-alg-3.png)


To summarise:

```pseudocode
repeat
	Sample a configuration q with a suitable sampling strategy
	if q is collision-free then
		Add q to the graph G
		Connect q to existing vertices using valid edges
until n new vertices have been added to G.
```



### Once the state graph is constructed

* Given an initial and a goal configuration
  * Find the vertex ![q_i](https://latex.codecogs.com/gif.latex?q_i) nearest to the initial configuration, where the straight line segment between initial configuration and ![q_%7Bi%7D](https://latex.codecogs.com/gif.latex?q_%7Bi%7D) is collision-free
  * Find the vertex ![q_g](https://latex.codecogs.com/gif.latex?q_g) nearest to the goal configuration, where the straight line segment between goal configuration and ![q_g](https://latex.codecogs.com/gif.latex?q_g) is collision-free
  * Find a path in the graph from ![q_i](https://latex.codecogs.com/gif.latex?q_i) to ![q_g](https://latex.codecogs.com/gif.latex?q_g) using the search algorithms already discussed in lectures 1, 2, and 3 (e.g. blind, informed searches like A*).
* When is the state graph construction "done" i.e. what's the stopping criteria?
  * Once we have a path from the initial configuration to the goal configuration! See [the interleave algorithm](#Interleave-algorithm)



### Interleave algorithm

Interleave state graph construction and graph search until all queries are answered, i.e. found a path from each pair of initial and goal configurations.

```pseudocode
while runtime < timelimit and path is not found:
repeat
	Sample a configuration q with a suitable sampling strategy
	if q is collision-free then:
		Add q to the graph G
		Connect q to existing vertices in G using valid edges
until n new vertices have been added to G
Search G for a path
	

```

### PRM Summary

* State space ![%5Cto](https://latex.codecogs.com/gif.latex?%5Cto) state graph ![%5Cto](https://latex.codecogs.com/gif.latex?%5Cto) search in a graph
* Use sampling to construct
* Key components:
  * [Sampling strat](#Sampling-strategies) (adding vertices)
  * [Check if a config is valid or not](#Checking-if-a-configuration-is-valid)
  * [Connection strat](#Connection-strategies) (adding edges)
  * Check a line seg in C-Space is valid or not



### Sampling Strategies

* Original PRM uses uniform distribution. If the C-Space is like the one below, there is a very low chance of sampling vertices with uniform distribution that can provide a path from one side to the other.

  ![1566604469176](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-problem-example-1.png)

  Time taken to find a path from ![q_1](https://latex.codecogs.com/gif.latex?q_1) to ![q_2](https://latex.codecogs.com/gif.latex?q_2) increases exponentially as the corridor width decreases.

  ![1566604608292](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-problem-example-2.png)

  Solution is to sample more frequently near collisions?

  

  **Algorithm to sample more near obstacles**

  Sample a configuration ![q_1](https://latex.codecogs.com/gif.latex?q_1) uniformly at random.

  Sample a configuration ![q_2](https://latex.codecogs.com/gif.latex?q_2) from the set of all configurations within ![D](https://latex.codecogs.com/gif.latex?D) distance from ![q_1](https://latex.codecogs.com/gif.latex?q_1), uniformly at random.

  If ![q_1](https://latex.codecogs.com/gif.latex?q_1) is in-collision and ![q_2](https://latex.codecogs.com/gif.latex?q_2) is collision-free, add ![q_2](https://latex.codecogs.com/gif.latex?q_2) as a vertex in the state graph

  Else if ![q_1](https://latex.codecogs.com/gif.latex?q_1) is collision-free and ![q_2](https://latex.codecogs.com/gif.latex?q_2) is in-collision, add ![q_1](https://latex.codecogs.com/gif.latex?q_1) as a vertex in the state graph

  ![1566604846618](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-problem-solution-1.png)

  **Algorithm to sample more in corridors**

  Sample a configuration ![q_1](https://latex.codecogs.com/gif.latex?q_1) uniformly at random.

  Sample a configuration ![q_2](https://latex.codecogs.com/gif.latex?q_2) from the set of all configurations within ![D](https://latex.codecogs.com/gif.latex?D) distance from ![q_1](https://latex.codecogs.com/gif.latex?q_1), uniformly at random.

  If ![q_1](https://latex.codecogs.com/gif.latex?q_1) and ![q_2](https://latex.codecogs.com/gif.latex?q_2) are in-collision,

  * Check if the middle configuration ![q_m%20%3A%3D%200.5%20%5Ccdot%20%5Cleft%28q_1%20%2B%20q_2%20%5Cright%29](https://latex.codecogs.com/gif.latex?q_m%20%3A%3D%200.5%20%5Ccdot%20%5Cleft%28q_1%20%2B%20q_2%20%5Cright%29) is collision free.
  * If ![q_m](https://latex.codecogs.com/gif.latex?q_m) is collision-free, add ![q_m](https://latex.codecogs.com/gif.latex?q_m) as a vertex in the state graph.

  ![prm-problem-solution-2](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-problem-solution-2.png)

  Shown here:

  ![img](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-visualisation.gif)

**Algorithm to use workspace information**

Narrow passages in C-space are often caused by narrow passages in the workspace

Relax the problem into planning for a point robot.

* Discretise the workspace into uniform grid
* Choose a point ![r](https://latex.codecogs.com/gif.latex?r) on the robot
* Find a path ![%5Cpi](https://latex.codecogs.com/gif.latex?%5Cpi) assuming the robot is the point ![r](https://latex.codecogs.com/gif.latex?r)
  * ![%5Cpi](https://latex.codecogs.com/gif.latex?%5Cpi) is a sequence of grid cells

![1566613670170](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/prm-problem-solution-3.png)

To sample a configuration:

* Sample a cell ![c](https://latex.codecogs.com/gif.latex?c) in ![%5Cpi](https://latex.codecogs.com/gif.latex?%5Cpi) with equal probability
* Sample a point ![p](https://latex.codecogs.com/gif.latex?p) uniformly at random from ![c](https://latex.codecogs.com/gif.latex?c).
* Sample a configuration uniformly at random from the set of all configurations that place point ![r](https://latex.codecogs.com/gif.latex?r) of the robot at ![p](https://latex.codecogs.com/gif.latex?p).



### Sampling strategies - Combining sampling strategies

Think of sampling strategies as kind of like a heuristic. We can combine sampling strategies:

* Simples way:
  * Assign equal weight to each candidate sampling strat
  * Choose a strat to use randomly based on the weight
  * Use the chosen strat to sample a configuration
  * Repeat the above steps, without changing the weight
* Frame as a [multi-arm bandit problem](#Multi-arm-bandit-problem)



#### Multi-arm bandit problem

Each arm =  a sampling strat

Choose which "arm" would be most helpful in solving the problem

Key: trading off **exploration** vs **exploitation**

* Use the sampling strategy that has been shown to be useful, but may not be the best strat (**exploit**)
  * *Could be in a local minima?*
* Use other sampling that may not have shown good performance yet, but may actually be the best strat (**explore**)
  * Idea behind reinforcement learning
  * *Could be enough to break out of a local minima?*

![1566614090917](C:\Users\tristan\School\COMP3702\Images\Lecture 4\multi-arm-bandit.png)

Many solutions.

**Simplest: epsilon-greedy:**

1. Assign a weight to each sampling strat
2. Start with equal weights for all strats
3. Strat with the highest weight is selected with probability ![1%20-%20%5Cepsilon](https://latex.codecogs.com/gif.latex?1%20-%20%5Cepsilon). The rest are select with ![%5Cepsilon%20/%20N](https://latex.codecogs.com/gif.latex?%5Cepsilon%20/%20N) where ![N](https://latex.codecogs.com/gif.latex?N) is the # of strats available.
4. Suppose strat ![s_1](https://latex.codecogs.com/gif.latex?s_1) is selected, we'll use ![s_1](https://latex.codecogs.com/gif.latex?s_1) to sample and add a vertex and edges to the roadmap
   1. If the addition connects disconnected components of the roadmap **or** adds # of connected components of the roadmap, increment the weight of ![s_1](https://latex.codecogs.com/gif.latex?s_1) by 1.



E.g. let ![s_1](https://latex.codecogs.com/gif.latex?s_1) be uniform random sampling and let ![s_2](https://latex.codecogs.com/gif.latex?s_2) be to sample more in corridors. If our workspace looks like this:

![1566614811422](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/multi-arm-bandit-workspace-example.png)

Then we can start off pretty good by using ![s_1](https://latex.codecogs.com/gif.latex?s_1), so ![s_1](https://latex.codecogs.com/gif.latex?s_1) would get incremented a lot of have a high weight at the start.

When the robot gets closer to the corridor, ![s_1](https://latex.codecogs.com/gif.latex?s_1) won't be connecting as many components any more since it is not ideal. Instead, the multi-arm robot will start trying ![s_2](https://latex.codecogs.com/gif.latex?s_2) and see more and more that it is the optimal strat to use here.



**More complicated: EXP3 (Auer, et al. 2001)** (not covered in this course).



### Checking if a configuration is valid

#### Check if two axis-aligned rectangles are colliding?

* Axis-aligned rectangles: each side of the rectangle is parallel to the ![X](https://latex.codecogs.com/gif.latex?X) axis or to the ![Y](https://latex.codecogs.com/gif.latex?Y) axis.
* Support ![A](https://latex.codecogs.com/gif.latex?A) and ![B](https://latex.codecogs.com/gif.latex?B) are axis-aligned rectangles
* ![A](https://latex.codecogs.com/gif.latex?A) and ![B](https://latex.codecogs.com/gif.latex?B) do **not** collide when all at least one of the following is true:
  * The left edge of ![A](https://latex.codecogs.com/gif.latex?A) is on the right side of the right edge of ![B](https://latex.codecogs.com/gif.latex?B)
  * The right edge of ![A](https://latex.codecogs.com/gif.latex?A) is on the left side of the left edge of ![B](https://latex.codecogs.com/gif.latex?B)
  * The top edge of ![A](https://latex.codecogs.com/gif.latex?A) is below the bottom edge of ![B](https://latex.codecogs.com/gif.latex?B)
  * The bottom edge of ![A](https://latex.codecogs.com/gif.latex?A) is above the top edge of ![B](https://latex.codecogs.com/gif.latex?B)
* If ![A](https://latex.codecogs.com/gif.latex?A) and ![B](https://latex.codecogs.com/gif.latex?B) do not satisfy any of the requirements above, they they are in collision.

```python
class Rectangle:
    def __init__(x1, y1, x2, y2, x3, y3, x4, y4):
        '''
        Defines a rectangle with the following coordinates:
        	Top left:		(x1, y1)
        	Top right:		(x2, y2)
        	Bottom right:	(x3, y3)
        	Bottom left:	(x4, y4)
        '''
        self.left = x1
        self.top = y1
        self.bottom = y3
        self.right = x2
def rects_colliding(A, B):
    return not (A.left > B.right or A.right < B.left or A.top > B.bottom or A.bottom < B.top)
```

#### Check if two general polygons are colliding?

Orientation of a sequence of 3 points ![a](https://latex.codecogs.com/gif.latex?a), ![b](https://latex.codecogs.com/gif.latex?b), ![c](https://latex.codecogs.com/gif.latex?c), based on the determinant of cross product.

![%5Cmathrm%7BArea%7D%28a%2C%20b%2C%20c%29%20%3D%20%5Cleft%7C%5Cbegin%7Bmatrix%7Da_x%26a_y%261%5C%5Cb_x%26b_y%261%5C%5Cc_x%26c_y%261%5Cend%7Bmatrix%7D%5Cright%7C](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BArea%7D%28a%2C%20b%2C%20c%29%20%3D%20%5Cleft%7C%5Cbegin%7Bmatrix%7Da_x%26a_y%261%5C%5Cb_x%26b_y%261%5C%5Cc_x%26c_y%261%5Cend%7Bmatrix%7D%5Cright%7C)

Orientation of ![a%2C%20b%2C%20c](https://latex.codecogs.com/gif.latex?a%2C%20b%2C%20c) test (counter clockwise):

* CCW: ![%5Cmathrm%7BArea%7D%28a%2C%20b%2C%20c%29%20%5Cgt%200](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BArea%7D%28a%2C%20b%2C%20c%29%20%5Cgt%200)
* CW: ![%5Cmathrm%7BArea%7D%28a%2Cb%2Cc%29%20%5Clt%200](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BArea%7D%28a%2Cb%2Cc%29%20%5Clt%200)
* Colinear: ![%5Cmathrm%7BArea%7D%28a%2Cb%2Cc%29%20%3D%200](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BArea%7D%28a%2Cb%2Cc%29%20%3D%200)



**Example:** ![A%3A%3D%284%2C%203%29](https://latex.codecogs.com/gif.latex?A%3A%3D%284%2C%203%29), ![B%3A%3D%282%2C4%29](https://latex.codecogs.com/gif.latex?B%3A%3D%282%2C4%29), and ![C%3A%3D%282%2C2%29](https://latex.codecogs.com/gif.latex?C%3A%3D%282%2C2%29).

![%5Cmathrm%7BArea%7D%28A%2C%20B%2C%20C%29%20%3D%20%5Cleft%7C%5Cbegin%7Bmatrix%7D4%263%261%5C%5C2%264%261%5C%5C2%262%261%5Cend%7Bmatrix%7D%5Cright%7C%20%3D%204%20%3E%200%20%5Cimplies%20](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BArea%7D%28A%2C%20B%2C%20C%29%20%3D%20%5Cleft%7C%5Cbegin%7Bmatrix%7D4%263%261%5C%5C2%264%261%5C%5C2%262%261%5Cend%7Bmatrix%7D%5Cright%7C%20%3D%204%20%3E%200%20%5Cimplies%20) counter clockwise orientation.

Indeed, the orientation is clockwise!

![1566619500434](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/orientation.png)



#### Check if two line segments are intersecting?

Suppose we have two line segments: ![p_1q_1](https://latex.codecogs.com/gif.latex?p_1q_1) and ![p_2q_2](https://latex.codecogs.com/gif.latex?p_2q_2). The line-segments intersect whenever:

* Majority of the cases intersect iff:

  * If ![p_1q_1p_2](https://latex.codecogs.com/gif.latex?p_1q_1p_2) and ![p_1q_1q_2](https://latex.codecogs.com/gif.latex?p_1q_1q_2) have different orientations, **and**
  * ![p_2q_2p_1](https://latex.codecogs.com/gif.latex?p_2q_2p_1) and ![p_1q_1q_2](https://latex.codecogs.com/gif.latex?p_1q_1q_2) have different orientations

  ![1566619619502](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/intersecting-line-segments.png)

* Special cases: All co-linear segments intersect iff

  * The ![x](https://latex.codecogs.com/gif.latex?x)-components of the first segment intersects with that of the second segment, **and**
  * The ![y](https://latex.codecogs.com/gif.latex?y) components of the first segment intersects with that of the second segment.

  ![1566619732999](C:\Users\tristan\School\COMP3702\Images\Lecture 4\intersecting-line-segments-special.png)

#### More efficient way to check if two line segments are intersecting:

* Bound the line segments with axis-aligned rectangles
* Check intersection between rectangles
* Only if the bounding rectangles intersect will we perform the collision check above

![1566619958335](C:\Users\tristan\School\COMP3702\Images\Lecture 4\intersecting-line-segments-efficient.png)

### A more general collision check: hierarchical bounding volume

Suppose we have an object ![O](https://latex.codecogs.com/gif.latex?O), whose boundary is represented by geometric primitives, e.g. 

* The primitives of a polygon are short line segments
* The primitives of a polyhedron (rep. as triangular mesh) are triangles.

![1566620396344](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/geometric-primitives.png)



* Construct a tree of bounding volumes for each object we want to check

  * Each node represents a volume (sphere/box)
  * The root covers the **entire** object. Each leaf node covers a geometric primitive
  * The higher the node (the closer to the root), the corresponding bounding volume covers a larger surface area of the object
  * Construct from the bottom **up**

  ![1566620845166](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%204/tree-of-bounding-volumes.png)

  Idea: Use bounding volumes where collision checks are easy, e.g. sphere/circle. If the bounding volumes are separated, definitely no collision.



Use a search algorithm on the tree to detect if one shape is in collision with another. There will be a path in the tree.



#### Hierarchical bounding volume to calculate the distance between two objects

* Suppose we want to compute the distance between a point ![p](https://latex.codecogs.com/gif.latex?p) and an object ![O](https://latex.codecogs.com/gif.latex?O).
* Construct the tree of hierarchical bounding volume for ![O](https://latex.codecogs.com/gif.latex?O).
  * Recursive DFS to compute distance between ![p](https://latex.codecogs.com/gif.latex?p) and the nodes of the tree
  * Only traverse down a subtree when needed.

We don't need to compute the distance with **all** the geometric leaf nodes (efficiency).



## Connection strategies

### Where should we try adding the edges?

* Naïve approach: connect all pairs of vertices
  * Long edges: expensive and have higher chance of colliding with the forbidden region
* Try inserting edges only when the distance between two verticies are relatively small
  * Too small: requires more samples to solve problem
  * Too large, inefficient, similar to naive approach
  * Need a balance
  * Sometimes, we also limit the number of edges we try to add to each vertex, i.e. limit the **degree** of each vertex.
* Usually need some trial and error
* **Lazy approach**:
  * Add edges to all pairs of vertices located within a certain distance of each other (no collision check)
  * Do collision check only when needed, i.e. when we search for a path and the particular edge may be traversed



## Check if a line segment in C-Space is valid or not

#### Simple method:

* Discretise the line segmement into small segments
* For each small segment:
  * Take the mid-point ![q_m](https://latex.codecogs.com/gif.latex?q_m) to represent the small segment
  * Check if ![q_m](https://latex.codecogs.com/gif.latex?q_m) is in the forbidden region or not (i.e., if a robot at configuration ![q_m](https://latex.codecogs.com/gif.latex?q_m) collides with an obstacle).
  * If ![q_m](https://latex.codecogs.com/gif.latex?q_m) is in the forbidden region, return collision



Problem: if we don't discretise enough, then there could be a small bit of forbidden region that we are crossing that we didn't detect with our samples. Or we might need to do a LOT of collision checks.



#### Better method using distance computation

1. If ![q](https://latex.codecogs.com/gif.latex?q) or ![q%27](https://latex.codecogs.com/gif.latex?q%27) is in collision, return
2. Compute distance ![d_q](https://latex.codecogs.com/gif.latex?d_q) between ![q](https://latex.codecogs.com/gif.latex?q) and its nearest forbidden region. Do this by creating an empty ball ![B_q](https://latex.codecogs.com/gif.latex?B_q) with centre ![q](https://latex.codecogs.com/gif.latex?q) and radius ![d_q](https://latex.codecogs.com/gif.latex?d_q). Similarly for ![q%27](https://latex.codecogs.com/gif.latex?q%27).
3. Let ![q_m%20%3A%3D%20%28q%20%2B%20q%27%29%20/%202](https://latex.codecogs.com/gif.latex?q_m%20%3A%3D%20%28q%20%2B%20q%27%29%20/%202)
4. If ![q_m](https://latex.codecogs.com/gif.latex?q_m) is inside ![B_q](https://latex.codecogs.com/gif.latex?B_q) and ![B_%7Bq%27%7D](https://latex.codecogs.com/gif.latex?B_%7Bq%27%7D),, the entire segment ![qq%27](https://latex.codecogs.com/gif.latex?qq%27) is collision free. Otherwise, repeat from #1 but for segments ![qq_m](https://latex.codecogs.com/gif.latex?qq_m) and ![q_mq%27](https://latex.codecogs.com/gif.latex?q_mq%27).

![1566623577549](C:\Users\tristan\School\COMP3702\Images\Lecture 4\better-method-using-distance-computation.png)



Good stuff: Guarantees that entire path is collision-free. Also more efficient. Use this method if you ever have to!