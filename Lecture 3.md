# Lecture 3

## Recall from last lecture...

**BFS** uses a container which is first-in-first-out (FIFO, i.e. Stack).

* In the case of solving the 8-puzzle (at least with the naive implementation, this was fast(ish))

**DFS** uses a container which is first-in-last-out (FILO, i.e. Queue).

* In the case of solving the 8-puzzle this was much slower than BFS.

See Tutorial 2 for more info.

## Informed search

* Informed search: select which node to expand based on a function of the estimated cost from the current node to the goal state
* Cost: $f(n) = g(n) + h(n)$
  * $g(n)$: cost from the root node to $n$.
  * $h(n)$: estimated cost from $n$ to the goal (usually based on heuristics)
  * In informed search, the node is selected based on $f(n)$, and $f(n)$ must contain $h(n)$.

When compared to blind search, informed search uses a "bias" toward the goal; points way from the goal look "worse" to the search as it progresses.

### Examples of informed search algorithms

* [Greedy best first search](#Greedy-best-first-search)
* [A* search](#A*-search)

### Greedy best first search

* Expand fringe node with lowest estimated cost from the current node to the goal
  * $f(n) = h(n):$ estimated cost from $n$ to the goal based on heuristics
  * $g(n)$: ignored
  * Expand fringe node with the lowest $f(n)$.

For example, recall the navigation app environment from Lecture 2.

![Navigation app graph](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%202/navigation-app-graph.png)

In this example, the following estimated costs could be:

* $h($`UQLake`$) := 100$
* $h($`Bld78`$) := 50$
* $h($`AEB`$) := 53$
* $h($`Wordsmith`$) := 9999$
* $h($`Bld42`$) := 50$
* $h($`Bld50`$) := 38$
* $h($`Bld51`$) := 30$
* $h($`Bld7`$) := 0$

Notice the estimated cost of moving further away from the goal (`Bld7`) is higher (moving to `Wordsmith` which is a deadlock is very high) while moving closer gives a lower cost and moving to the goal is the lowest cost ($0$). 

* Almost the same as Uniform Cost search
* Use **priority queue (PQ)** to keep fringe nodes
  * The highest priority in PQ for Greedy Best First is the node with the smallest estimated cost from the current node to the goal (i.e. the heuristic function $h$), rather than the cost from the root to the current node ($g$) as in Uniform Cost.

1. Set the initial vertex $I$ as the root of the search tree
2. Push $I$ to the PQ
3. Loop
   1. Assign $t:=$ the node $n$ from the PQ with the lowest $h(n)$
   2. Remove $t$ from PQ and mark $t$ as expanded
   3. If $t$ is the goal vertex, then return
   4. For each $v$ in `successor(`$t$`)`:
      * If $v$ has not been expanded yet
        * Insert $v$ to the PQ
        * Put $v$ as a child of $t$ in the search tree