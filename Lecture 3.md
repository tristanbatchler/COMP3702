# Lecture 3

## Recall from last lecture...

**BFS** uses a container which is first-in-first-out (FIFO, i.e. Stack).

* In the case of solving the 8-puzzle (at least with the naive implementation, this was fast(ish))

**DFS** uses a container which is first-in-last-out (FILO, i.e. Queue).

* In the case of solving the 8-puzzle this was much slower than BFS.

See Tutorial 2 for more info.

## Informed search

* Informed search: select which node to expand based on a function of the estimated cost from the current node to the goal state
* Cost: ![f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29)
  * ![g%28n%29](https://latex.codecogs.com/gif.latex?g%28n%29): cost from the root node to ![n](https://latex.codecogs.com/gif.latex?n).
  * ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29): estimated cost from ![n](https://latex.codecogs.com/gif.latex?n) to the goal (usually based on heuristics)
  * In informed search, the node is selected based on ![f%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29), and ![f%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29) must contain ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29).

When compared to blind search, informed search uses a "bias" toward the goal; points way from the goal look "worse" to the search as it progresses.

### Examples of informed search algorithms

* [Greedy best first search](#Greedy-best-first-search)
* [A* search](#A*-search)

### Greedy best first search

* Expand fringe node with lowest estimated cost from the current node to the goal
  * ![f%28n%29%20%3D%20h%28n%29%3A](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20h%28n%29%3A) estimated cost from ![n](https://latex.codecogs.com/gif.latex?n) to the goal based on heuristics
  * ![g%28n%29](https://latex.codecogs.com/gif.latex?g%28n%29): ignored
  * Expand fringe node with the lowest ![f%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29).

For example, recall the navigation app environment from Lecture 2.

![Navigation app graph](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%202/navigation-app-graph.png)

In this example, the following estimated costs could be:

* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`UQLake`![%29%20%3A%3D%20100](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%20100)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld78`![%29%20%3A%3D%2050](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2050)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`AEB`![%29%20%3A%3D%2053](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2053)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Wordsmith`![%29%20%3A%3D%209999](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%209999)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld42`![%29%20%3A%3D%2050](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2050)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld50`![%29%20%3A%3D%2038](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2038)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld51`![%29%20%3A%3D%2030](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2030)
* ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld7`![%29%20%3A%3D%200](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%200)

Notice the estimated cost of moving further away from the goal (`Bld7`) is higher (moving to `Wordsmith` which is a deadlock is very high) while moving closer gives a lower cost and moving to the goal is the lowest cost (![0](https://latex.codecogs.com/gif.latex?0)). 

* Almost the same as Uniform Cost search
* Use **priority queue (PQ)** to keep fringe nodes
  * The highest priority in PQ for Greedy Best First is the node with the smallest estimated cost from the current node to the goal (i.e. the heuristic function ![h](https://latex.codecogs.com/gif.latex?h)), rather than the cost from the root to the current node (![g](https://latex.codecogs.com/gif.latex?g)) as in Uniform Cost.

1. Set the initial vertex ![I](https://latex.codecogs.com/gif.latex?I) as the root of the search tree
2. Push ![I](https://latex.codecogs.com/gif.latex?I) to the PQ
3. Loop
   1. Assign ![t%3A%3D](https://latex.codecogs.com/gif.latex?t%3A%3D) the node ![n](https://latex.codecogs.com/gif.latex?n) from the PQ with the lowest ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29)
   2. Remove ![t](https://latex.codecogs.com/gif.latex?t) from PQ and mark ![t](https://latex.codecogs.com/gif.latex?t) as expanded
   3. If ![t](https://latex.codecogs.com/gif.latex?t) is the goal vertex, then return
   4. For each ![v](https://latex.codecogs.com/gif.latex?v) in `successor(`![t](https://latex.codecogs.com/gif.latex?t)`)`:
      * If ![v](https://latex.codecogs.com/gif.latex?v) has not been expanded yet
        * Insert ![v](https://latex.codecogs.com/gif.latex?v) to the PQ
        * Put ![v](https://latex.codecogs.com/gif.latex?v) as a child of ![t](https://latex.codecogs.com/gif.latex?t) in the search tree