# Lecture 2

## In the first part of this class

### Assumptions on the class environment

* Discrete or continuous
* Deterministic
* Fully observable
* Static

Therefore, in the first part of this class, designing an agent only needs to set:

* Action space (<img src="https://latex.codecogs.com/gif.latex\?%24A%24" />)
* ~~Percept space (<img src="https://latex.codecogs.com/gif.latex\?%24P%24" />)~~ (<img src="https://latex.codecogs.com/gif.latex\?%24P%20%3D%20S%20%5Cbecause%20%24" /> fully observable environment assumption)
* State space (<img src="https://latex.codecogs.com/gif.latex\?%24S%24" />)
* World dynamics (<img src="https://latex.codecogs.com/gif.latex\?%24T%3AS%5Ctimes%20A%5Cto%20S%24" />)
* ~~Percept function (<img src="https://latex.codecogs.com/gif.latex\?%24Z%3AS%5Cto%20P%24" />)~~ (<img src="https://latex.codecogs.com/gif.latex\?%24Z%20%3D%20I_S%20%5Cbecause%24" /> fully observable)
* Utility function (<img src="https://latex.codecogs.com/gif.latex\?%24U%3AS%5Cto%5Cmathbb%7BR%7D%24" />)



## Recall the problem the agent should solve

Trying to find a mapping from sequences of percepts to an action (<img src="https://latex.codecogs.com/gif.latex\?%24P%5En%20%5Cto%20A%24" />) that maximises the utility function.

* Given the sequences of percepts (or spaces in the first part of this class) that the agent has seen so far, what should the agent do next, so that <img src="https://latex.codecogs.com/gif.latex\?%24U%24" /> is maximised?
  * **Search** is a way to solve this problem

## Introduction to search

### What is search?

Using world dynamics, we can foresee future paths of different actions.

![8 Puzzle Search](.\Images\Lecture 2\8-puzzle-search.png)

The image above represents the possibilities of just one time step, but to find a solution we would need to iterate over all the possibilities at each step until the goal state is found.

**How do we explore this massive search space to find the solution in the least number of steps?**

* If the solution is 10 steps away, and we have 4 branches each step, the number of calculations required is of the order of <img src="https://latex.codecogs.com/gif.latex\?%244%5E%7B10%7D%24" />.

### Types of search

#### Blind search

* Do not use any additional information to "guess" cost of moving from current node to goal

#### Informed search

* Use additional information to "guess" the cost of moving from current node to goal and decide where to explore next using this information.

### Formulating a problem as a search problem

Similar to the formulation of a rational agent but with the addition of the initial and goal state.

* Action space
* ~~Percept space~~
* State space
* World dynamics/transition function
* ~~Percept function~~
* Utility/**cost** function
* **Initial and goal state**

Must find a sequence of actions to move the agent from being in the initial state to being in the goal state, such that the utility is maximised (or **cost** of moving is **minimised**).

### How to search in a discrete space

* Want agent to be able to search for its own solution
* Need a way to embed this definition into a representation that is easy to search

#### Overview

1. [State graph representation](#state-graph-representation)
2. [General structure of search algorithms](#general-structure-of-search-algorithms)
3. [Uninformed (blind) search](#uninformed-search)
4. Informed search (next lecture)

## State graph representation

**Definition**: a weighted directed graph (digraph) is a pair <img src="https://latex.codecogs.com/gif.latex\?%24%28V%2C%20E%29%24" /> of a vertex set <img src="https://latex.codecogs.com/gif.latex\?%24V%24" /> and an edge set <img src="https://latex.codecogs.com/gif.latex\?%24E%24" />.

* Vertices represent states
* Edges represent world dynamics
  * Each edge <img src="https://latex.codecogs.com/gif.latex\?%24%5Coverline%7Bs%20s%27%7D%24" /> is labelled by the cost to move from <img src="https://latex.codecogs.com/gif.latex\?%24s%24" /> to <img src="https://latex.codecogs.com/gif.latex\?%24s%27%24" />. It may also be labelled by the action to move from state <img src="https://latex.codecogs.com/gif.latex\?%24s%24" /> to <img src="https://latex.codecogs.com/gif.latex\?%24s%27%24" /> (i.e. **weighted** graph)
* Initial and goal states -- initial & goal verticies
* The solution is a path from the initial vertex to the goal vertex in the state graph
* The cost is the sum of the cost associated with each edge in the path

### 8-puzzle example

![8 puzzle graph](.\Images\Lecture 2\8-puzzle-graph.png)

**Notes on state graph representation**:

* A way to represent the problem **concretely** in programs
* Also a way of thinking about the problem
* We may or may not explicitly represent the state graph
* In problems with continuous or very large state space, state graph is often used as a compact representation of the state space (e.g. tutorial 1 question on navigation app)



**The state graph may have multiple connected components**

* **Connected component**: sub-graph where there is at least one path in the sub-graph from each vertex in the sub-graph to any other vertex in the sub-graph.

  * Useful for determining if a solution exists from the initial state to the goal state--they can't be in different connected components!

    

    ![Connected components](.\Images\Lecture 2\connected-component.png)

* **Reachability**: if I'm in a particular state, can I reach another state?

  * E.g. see above, also see **Parity Check** in Tutorial 2.

## General structure of search algorithms

1. Put initial vertex in a "container" of states to be expanded
2. Loop:
   * Select a vertex, <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> from the "container"
     * If <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> is the goal vertex, then return
     * Expand <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> (i.e. put the results of `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24v%24" />`)` to the "container")
3. `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24v%24" />`)` is a function that:
   1. Takes a vertex <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> as input
   2. Outputs the set of immediate next vertices that can be visited from <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> (i.e. the endpoints of out-edges from <img src="https://latex.codecogs.com/gif.latex\?%24v%24" />)

### "Container" + expanded nodes <img src="https://latex.codecogs.com/gif.latex\?%24%5Cto%24" /> search tree

To keep track of our visited vertices, we referenced the idea of a "container" and expanded nodes. This is typically represented by a **search tree**.

* An abstract representation of the visited nodes (expanded + container)

  ![State space graph](.\Images\Lecture 2\state-space-graph.png)

* If states can be revisited, the search **tree** may be **infinite**, even though the state graph/space is **finite**.

  * See, e.g. example above, bidirectional arrows can be thought of as a loop.

  ![State space search tree](.\Images\Lecture 2\state-space-search-tree.png)

  Note: the tree above would continue infinitely due to the loops from <img src="https://latex.codecogs.com/gif.latex\?%24s%24" /> to <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> and <img src="https://latex.codecogs.com/gif.latex\?%24c%24" /> -- we only draw the first 3 levels. We assume the initial state is <img src="https://latex.codecogs.com/gif.latex\?%24s%24" />.

* **Container** is what's known as the **fringe** of the tree.

  * A list of nodes in the search tree that have not been expanded yet.

    ![Fringe nodes](.\Images\Lecture 2\fringe-nodes.png)

    ### General structure of a search algorithm with search tree

    1. Put initial vertex as root of the search tree
    2. Loop:
       * Select a fringe node <img src="https://latex.codecogs.com/gif.latex\?%24t%24" />
         * If <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> corresponds to the goal vertex, then return
         * Expand <img src="https://latex.codecogs.com/gif.latex\?%24t%24" />:
           * Suppose <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> corresponds to a vertex <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> of the state graph
           * Put the results of `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24v%24" />`)` as children of <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> in the search tree
    3. Various search methods (e.g. breadth-first search) differ in:
       * Which node to expands next (i.e. retrieval order of the container)
       * How to expand

### Performance measure of search algorithms

* **Completeness**
  * Complete: the algorithm will find the solution whenever one exists
* **Optimality**
  * Optimal: return a minimum cost path whenever one exists
* **Complexity**
  * Time (# steps) and space (memory) complexity
  * How the required time and memory needed to solve the problem increases as the input size increases (big <img src="https://latex.codecogs.com/gif.latex\?%24O%24" /> notation)
  * Input size: size of the **state** and **action spaces** of the search problem
    * In state graph representation, the **size** of the graph
  * Use computational complexity notation (e.g. big-<img src="https://latex.codecogs.com/gif.latex\?%24O%24" />)

### Big-<img src="https://latex.codecogs.com/gif.latex\?%24O%24" /> definition

Suppose <img src="https://latex.codecogs.com/gif.latex\?%24f%28n%29%24" /> is the required time/space required to solve the problem if the input size is <img src="https://latex.codecogs.com/gif.latex\?%24n%24" />. Then we say <img src="https://latex.codecogs.com/gif.latex\?%24f%28n%29%24" /> is of complexity <img src="https://latex.codecogs.com/gif.latex\?%24O%28g%28n%29%29%24" /> whenever:

* There is a constant <img src="https://latex.codecogs.com/gif.latex\?%24k%24" /> and <img src="https://latex.codecogs.com/gif.latex\?%24n_0%24" /> such that:
<img src="https://latex.codecogs.com/gif.latex\?%20%200%20%5Cle%20f%28n%29%20%5Cle%20k%20%5Ccdot%20g%28n%29%20%5Cquad%20%5Cforall%20n%20%5Cge%20n_0%0A" />  

### Branching factor definition

See diagram below: <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> is the branching factor for each tree, <img src="https://latex.codecogs.com/gif.latex\?%24n%24" /> is the size of the tree.

![Branching factor](.\Images\Lecture 2\branching-factor.png)

### Problem example: Navigation app

Given a map, how do I move from point <img src="https://latex.codecogs.com/gif.latex\?%24A%24" /> to <img src="https://latex.codecogs.com/gif.latex\?%24B%24" />? Also see Tutorial 1, problem 2.

![Navigation app](.\Images\Lecture 2\navigation-app.png)

## Uninformed search

We **don't** estimate the cost from the current node to the goal.

Examples:

* [Breadth first search (BFS)](#breadth-first-search)
* [Depth first search (DFS)](#depth-first-search)
* [Iterative deepening DFS (IDDFS)](#iterative-deepening-depth-first-search)
* [Uniform cost search](#uniform-cost-search)



### Breadth first search

* Cost = #steps (ignore cost on the edges, i.e. weights)
* Expand nodes of the search tree level-by-level
  * Select a fringe node in the same level of the search tree before selecting fringe nodes at the next level
  * Use a **queue** to keep the fringe nodes (container)
    * Abstract data structure which is FIFO (first in, first out)



1. Set initial vertex <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> as the root of the search tree

2. Push <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> to the queue

3. Loop

   1. Assign <img src="https://latex.codecogs.com/gif.latex\?%24t%3A%3D%24" /> `front of the queue`

   2. Remove <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> from the queue and mark <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> as expanded
   3. If <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> is the goal vertex, then return

   3. For each <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> in `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24t%24" />`)`:
      * If <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> is not in the tree yet
        * Push <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> to the queue
        * Put <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> as a child of <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> in the search tree



Using the Navigation App example above:

![BFS Navigation App graph](.\Images\Lecture 2\bfs-nav-app-graph.png)

![BFS worked example](.\Images\Lecture 2\bfs-nav-app-graph-worked-algorithm.png)

#### BFS properties & analysis

* <img src="https://latex.codecogs.com/gif.latex\?%24b%24" />: branching factor
* <img src="https://latex.codecogs.com/gif.latex\?%24d%24" /> depth of shallowest goal node
* Complete?
  * Complete if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> is finite
* Optimal (in terms of # steps)
  * Yes, we never go beyond the depth of the goal
  * We don't consider cost in BFS since it's uninformed
* Complexity
  * Time
    * <img src="https://latex.codecogs.com/gif.latex\?%241%20%2B%20b%20%2B%20b%5E2%20%2B%20...%20%2B%20b%5Ed%20%3D%20%28b%5E%7Bd%2B1%7D%20-%201%29/%28b%20-%201%29%24" />
    * so <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" /> for # steps
  * Space
    * Explored nodes: <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5E%7Bd-1%7D%29%24" /> + unexplored nodes: <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" />
    * so <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" /> for # nodes remembered
* **Finds minimum step path, but requires exponential space and time!**



#### Bidirectional strategy

* 2 search trees and hence 2 fringe queues

![Bidirectional BFS](.\Images\Lecture 2\bidirectional-bfs.png)

* Time and space complexity is <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5E%7Bd/2%7D%29%20%5Clt%20%5Clt%20O%28b%5Ed%29%24" />



### Depth first search

* Cost = # steps  (ignore cost of the edges)
* Expand nodes path by path
  * Expand a fringe node most recently inserted to the tree
* Use **stack** to keep fringe nodes (container)
  * Abstract data structure which is LIFO (last in, first out)



1. Set initial vertex <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> as the root of the search tree

2. Push <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> to the stack

3. Loop

   1. Assign <img src="https://latex.codecogs.com/gif.latex\?%24t%3A%3D%24" /> `top of the stack`

   2. Remove <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> from the stack and mark <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> as expanded
   3. If <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> is the goal vertex, then return

   3. For each <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> in `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24t%24" />`)`:
      - If <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> is not in the path to <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> yet:
        - Push <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> to the stack
        - Put <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> as a child of <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> in the search tree



Using the navigation app example from before:

![DFS worked example](.\Images\Lecture 2\dfs-nav-app-graph-worked-algorithm.png)



#### DFS properties & analysis

- <img src="https://latex.codecogs.com/gif.latex\?%24b%24" />: branching factor
- <img src="https://latex.codecogs.com/gif.latex\?%24m%24" /> maximum depth
- Complete?
  - Complete if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> and <img src="https://latex.codecogs.com/gif.latex\?%24m%24" /> are finite and nodes are not revisited
  - If nodes can be revisited, it's possible to get stuck in a cycle
- Optimal (in terms of # steps)
  - No, we may choose the longest path straight off the bat as we just dive straight in going down
  - We don't consider cost in BFS since it's uninformed
- Complexity
  - Time
    - <img src="https://latex.codecogs.com/gif.latex\?%241%20%2B%20b%20%2B%20b%5E2%20%2B%20...%20%2B%20b%5Em%20%3D%20%28b%5E%7Bm%2B1%7D%20-%201%29/%28b%20-%201%29%24" />
    - so <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Em%29%24" /> for # steps
  - Space
    - Can be implemented using <img src="https://latex.codecogs.com/gif.latex\?%24O%28bm%29%24" /> or <img src="https://latex.codecogs.com/gif.latex\?%24O%28m%29%24" /> using backtracking DFS but be careful of revisiting vertices (states)!
- **Efficient in use of space!**

### Iterative deepening depth first search

* BFS
  * Finds minimum step path but requires exponential space
* DFS
  * Efficient in space but no path length guarantee
* Iterative deepening:
  * Best of both worlds. Run multiple DFS but increase the depth cutoff each time until goal is found.
    * For $k = 1, 2, ...  do
      * Perform DFS with depth cutoff <img src="https://latex.codecogs.com/gif.latex\?%24k%24" />
        * Only generates nodes with depth <img src="https://latex.codecogs.com/gif.latex\?%24%5Cle%20k%24" />.



Using the navigation app again:

![IDDFS worked example](.\Images\Lecture 2\iddfs-nav-app-graph-worked-algorithm.png)

#### DFS properties & analysis

- <img src="https://latex.codecogs.com/gif.latex\?%24b%24" />: branching factor

- <img src="https://latex.codecogs.com/gif.latex\?%24d%24" />: depth of shallowest goal node

- Complete?

  - Complete if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> is finite

- Optimal (in terms of # steps)

  - Yes
  - We don't consider cost in BFS since it's uninformed

- Complexity

  - Time

    - <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" /> for # steps

      Proof:

      In an iterative deepening search, the nodes at depth <img src="https://latex.codecogs.com/gif.latex\?%24d%24" /> are expanded once, those at depth <img src="https://latex.codecogs.com/gif.latex\?%24d-1%24" /> are expanded twice, and so on up to the root of the search tree, which is expanded <img src="https://latex.codecogs.com/gif.latex\?%24d%2B1%24" />. So the total number of expansions in an iterative deepening search is
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20b%5E%7Bd%7D%2B2b%5E%7Bd-1%7D%2B3b%5E%7Bd-2%7D%2B%5Ccdots%20%2B%28d-1%29b%5E%7B2%7D%2Bdb%2B%28d%2B1%29%0A" />      where <img src="https://latex.codecogs.com/gif.latex\?%24b%5Ed%24" /> is the number of expansions at depth <img src="https://latex.codecogs.com/gif.latex\?%24d%24" />, <img src="https://latex.codecogs.com/gif.latex\?%242b%5E%7Bd-1%7D%24" /> is the number of expansions at depth <img src="https://latex.codecogs.com/gif.latex\?%24d-1%24" />, etc.

      Factoring out <img src="https://latex.codecogs.com/gif.latex\?%24b%5Ed%24" /> gives
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20%7B%5Cdisplaystyle%20b%5E%7Bd%7D%281%2B2b%5E%7B-1%7D%2B3b%5E%7B-2%7D%2B%5Ccdots%20%2B%28d-1%29b%5E%7B2-d%7D%2Bdb%5E%7B1-d%7D%2B%28d%2B1%29b%5E%7B-d%7D%29%7D%0A" />      Now let <img src="https://latex.codecogs.com/gif.latex\?%24x%20%3D%201/b%20%3D%20b%5E%7B-1%7D%24" />. Then we have
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20%7B%5Cdisplaystyle%20b%5E%7Bd%7D%281%2B2x%2B3x%5E%7B2%7D%2B%5Ccdots%20%2B%28d-1%29x%5E%7Bd-2%7D%2Bdx%5E%7Bd-1%7D%2B%28d%2B1%29x%5E%7Bd%7D%29%7D.%0A" />      This is less than the infinite series
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20%7B%5Cdisplaystyle%20b%5E%7Bd%7D%281%2B2x%2B3x%5E%7B2%7D%2B4x%5E%7B3%7D%2B%5Ccdots%20%29%7D%0A" />      which converges to (see [geometric power series](https://en.wikipedia.org/wiki/Geometric_series#Geometric_power_series))
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20%7B%5Cdisplaystyle%20b%5E%7Bd%7D%281-x%29%5E%7B-2%7D%3Db%5E%7Bd%7D%7B%7B1%7D/%7B%281-x%29%5E%7B2%7D%7D%7D%2C%20%5Cquad%20%7Cx%7C%20%5Clt%201%7D%0A" />      That is, we have
<img src="https://latex.codecogs.com/gif.latex\?%20%20%20%20%20%20b%5E%7Bd%7D%2B2b%5E%7Bd-1%7D%2B3b%5E%7Bd-2%7D%2B%5Ccdots%20%2B%28d-1%29b%5E%7B2%7D%2Bdb%2B%28d%2B1%29%5Cleq%20b%5E%7Bd%7D%281-x%29%5E%7B-2%7D%0A" />      whenever <img src="https://latex.codecogs.com/gif.latex\?%24%7Cx%7C%20%5Clt%201%24" />.

      Since <img src="https://latex.codecogs.com/gif.latex\?%24%281-x%29%5E%7B-2%7D%24" /> or <img src="https://latex.codecogs.com/gif.latex\?%24%281%20-%20%7B1%7D/%7Bb%7D%29%5E%7B-2%7D%24" /> is constant independent of <img src="https://latex.codecogs.com/gif.latex\?%24d%24" /> (the depth), if <img src="https://latex.codecogs.com/gif.latex\?%24b%20%3E%201%24" /> (i.e., if the branching factor is greater than 1), the running time of the depth-first iterative deepening search is <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" /> :call_me_hand:

  - Space

    - Can be implemented using <img src="https://latex.codecogs.com/gif.latex\?%24O%28bd%29%24" />

- **Efficient in use of space!**

Since iterative deepening visits states multiple times, it may seem wasteful, but it turns out to be not so costly, since in a tree most of the nodes are in the bottom level, so it does not matter much if the upper levels are visited multiple times.

See this video as a comparison of DFS vs. IDDFS to see how much faster the latter is. The DFS progress is represented by the green line and the IDDFS progress is in red.

<iframe width="640" height="480" src="https://www.youtube.com/embed/4KEYEXW18og" frameborder="0" allow="accelerometer; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Uniform cost search

* Expand fringe node with lowest cost from root
  * So let <img src="https://latex.codecogs.com/gif.latex\?%24c%28n%29%24" /> be the cost from root to node <img src="https://latex.codecogs.com/gif.latex\?%24n%24" />
  * Expand <img src="https://latex.codecogs.com/gif.latex\?%24n%24" /> with lowest <img src="https://latex.codecogs.com/gif.latex\?%24c%24" /> value first
* Use a **priority queue (PQ)** to keep fringe nodes (container)
  * Abstract data structure where data with the highest priority is retrieved first.
  * In our navigation example, priority is the node with the shortest path length from root to the node.

![Navigation app graph](.\Images\Lecture 2\navigation-app-graph.png)

1. Set the initial vertex <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> as the root of the search tree
2. Push <img src="https://latex.codecogs.com/gif.latex\?%24I%24" /> to the PQ
3. Loop
   1. Assign <img src="https://latex.codecogs.com/gif.latex\?%24t%3A%3D%24" />`retrieve a node from PQ`
   2. Remove <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> from PQ and mark <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> as expanded
   3. If <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> is the goal vertex, then return
   4. For each <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> in `successor(`<img src="https://latex.codecogs.com/gif.latex\?%24t%24" />`)`:
      * If <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> has not been expanded yet
        * Insert <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> to the PQ
        * Put <img src="https://latex.codecogs.com/gif.latex\?%24v%24" /> as a child of <img src="https://latex.codecogs.com/gif.latex\?%24t%24" /> in the search tree

![Uniform cost search worked example](.\Images\Lecture 2\uniform-cost-search-nav-app-graph-worked-algorithm.png)

#### Uniform cost search properties & analysis

- <img src="https://latex.codecogs.com/gif.latex\?%24b%24" />: branching factor
- <img src="https://latex.codecogs.com/gif.latex\?%24m%24" /> maximum depth
- <img src="https://latex.codecogs.com/gif.latex\?%24C%5E%2A%24" />: cost of optimal solution
- <img src="https://latex.codecogs.com/gif.latex\?%24%5Cepsilon%24" />: minimum cost of a step
- Complete?
  - Complete if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> is finite and all edges have a cost <img src="https://latex.codecogs.com/gif.latex\?%24%5Cgt%20%5Cepsilon%24" /> (i.e. a small positive number) 
- Optimal (in terms of # steps)
  - Yes, if all edges have a positive cost
- Complexity
  - Time **and** space: <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5E%7B1%20%2B%20%5Cmathrm%7Bfloor%7D%28%20c%5E%2A%20/%20%5Cepsilon%20%29%7D%20%29%24" />

## Summary

* Search in discrete space
  * State graph representation
  * General structure of search algorithms
  * Uninformed (blind) search
  * Next: informed search



| Algorithm    | Complete?                                       | Optimal?                           | Time                                                         | Space                                                        |
| ------------ | ----------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| BFS          | Yes if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> finite                               | Yes                                | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" />                                                     | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" />                                                     |
| DFS          | Yes if <img src="https://latex.codecogs.com/gif.latex\?%24m%2C%20b%24" /> finite & no revisiting            | No                                 | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Em%29%24" />                                                     | <img src="https://latex.codecogs.com/gif.latex\?%24O%28bm%29%24" /> or <img src="https://latex.codecogs.com/gif.latex\?%24O%28m%29%24" /> w/ backtracking                            |
| IDDFS        | Yes if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> finite                               | Yes                                | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5Ed%29%24" />                                                     | <img src="https://latex.codecogs.com/gif.latex\?%24O%28bd%29%24" />                                                      |
| Uniform Cost | Yes if <img src="https://latex.codecogs.com/gif.latex\?%24b%24" /> finite & all edges have cost <img src="https://latex.codecogs.com/gif.latex\?%24%5Cgt%200%24" /> | Yes if all edges have cost <img src="https://latex.codecogs.com/gif.latex\?%24%5Cgt%200%24" /> | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5E%7B1%20%2B%20%5Cmathrm%7Bfloor%7D%28%20c%5E%2A%20/%20%5Cepsilon%20%29%7D%20%29%24" /> | <img src="https://latex.codecogs.com/gif.latex\?%24O%28b%5E%7B1%20%2B%20%5Cmathrm%7Bfloor%7D%28%20c%5E%2A%20/%20%5Cepsilon%20%29%7D%20%29%24" /> |

