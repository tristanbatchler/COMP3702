# Lecture 3

## Recall from last lecture...

**BFS** uses a container which is first-in-first-out (FIFO, i.e. Stack).

* In the case of solving the 8-puzzle (at least with the naive implementation, this was fast(ish))

**DFS** uses a container which is first-in-last-out (FILO, i.e. Queue).

* In the case of solving the 8-puzzle this was much slower than BFS.

See Tutorial 2 for more info.



## Heuristics

A heuristic is specified by the designer of an agent, specifically for the search problem. It uses some top-level insight about the problem so that the search algorithm can act in an informed way.

#### Admissible heuristics

A heuristic is **admissible** if it never overestimates the cost

- ![h%28n%29%20%5Cleq%20h%5E%2A%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29%20%5Cleq%20h%5E%2A%28n%29), where ![h%5E%2A%28n%29](https://latex.codecogs.com/gif.latex?h%5E%2A%28n%29) is the true cost to reach the goal from ![n](https://latex.codecogs.com/gif.latex?n).
- i.e. the estimate never overestimates

For example, Euclidean distance (straight line path) in a maze would be admissible because it never overestimates.

#### Consistent heuristics

A heuristic is **consistent** if, for every node ![n](https://latex.codecogs.com/gif.latex?n) and for every successor ![n%27](https://latex.codecogs.com/gif.latex?n%27) of ![n](https://latex.codecogs.com/gif.latex?n) by any action ![a](https://latex.codecogs.com/gif.latex?a), the estimated cost to reach the goal for ![n](https://latex.codecogs.com/gif.latex?n) is **at most** the step cost of getting to ![n%27](https://latex.codecogs.com/gif.latex?n%27) + the estimated cost of ![n%27](https://latex.codecogs.com/gif.latex?n%27) to the goal.

In other words, ![h](https://latex.codecogs.com/gif.latex?h) is **consistent** if:
![%5Cforall%20n%20%5Cin%20S%2C%20%5Cquad%20%5Cforall%20n%27%20%5Cin%20%5Cmathrm%7Bsuccessor%7D%28n%29%2C%20%5Cquad%20%5Cforall%20a%20%5Cin%20A%20%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Cforall%20n%20%5Cin%20S%2C%20%5Cquad%20%5Cforall%20n%27%20%5Cin%20%5Cmathrm%7Bsuccessor%7D%28n%29%2C%20%5Cquad%20%5Cforall%20a%20%5Cin%20A%20%5C%5C%0A)![h%28n%29%20%5Cleq%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29%0A](https://latex.codecogs.com/gif.latex?h%28n%29%20%5Cleq%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29%0A)where ![c%28n%2C%20a%2C%20n%27%29](https://latex.codecogs.com/gif.latex?c%28n%2C%20a%2C%20n%27%29) is the step cost of getting from ![n](https://latex.codecogs.com/gif.latex?n) to ![n%27](https://latex.codecogs.com/gif.latex?n%27) via action ![a](https://latex.codecogs.com/gif.latex?a).

**Notes:**

* This is a case of the **triangle inequality** which stipulates that each side of a triangle cannot be longer than the sum of the two other sides
  ![Consistent heuristic](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%203/consistent-heuristic.png)
* Consistent is also called **monotonic**

## Informed search

* Informed search: select which node to expand based on a function of the estimated cost from the current node to the goal state
* Cost: ![f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29)
  * ![g%28n%29](https://latex.codecogs.com/gif.latex?g%28n%29): cost from the root node of the tree to ![n](https://latex.codecogs.com/gif.latex?n).
  * ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29): estimated cost from ![n](https://latex.codecogs.com/gif.latex?n) to the goal (usually based on [heuristics](#Heuristic))
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

In this example, the following estimated costs could be (there are many you can choose--this one is just arbitrary):

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
      * Insert ![v](https://latex.codecogs.com/gif.latex?v) to the PQ
      * Put ![v](https://latex.codecogs.com/gif.latex?v) as a child of ![t](https://latex.codecogs.com/gif.latex?t) in the search tree

![GBFS worked example](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%203/gbfs-nav-app-graph-worked-algorithm.png)

#### Greedy best first search properties & analysis

- ![b](https://latex.codecogs.com/gif.latex?b): branching factor
- ![m](https://latex.codecogs.com/gif.latex?m) maximum depth
- Complete?
  - No (highly depends on heuristic)
  - Imagine trying to navigate a maze where ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29) is just Euclidean distance from ![n](https://latex.codecogs.com/gif.latex?n) to the goal--if there are obstacles in the way, and the complete path is something with a higher heuristic, GBFS is not going to find it and get stuck
- Optimal (in terms of lowest cost)
  - No (highly depends on heuristic)
- Complexity
  - Highly depends on heuristic
  - Time **and** space: ![O%28b%5Em%29](https://latex.codecogs.com/gif.latex?O%28b%5Em%29)



### A* search

* Expand the fringe node with lowest estimated cost from root goal via the node.
  * ![g%28n%29](https://latex.codecogs.com/gif.latex?g%28n%29): Cost from root of the tree to node ![n](https://latex.codecogs.com/gif.latex?n)
  * ![h%28n%29](https://latex.codecogs.com/gif.latex?h%28n%29): Estimated cost from node ![n](https://latex.codecogs.com/gif.latex?n) to goal  (using heuristics)
  * ![f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29)
  * Expand fringe node with the lowest ![f%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29)

Again, recall the navigation app environment.

![Navigation app graph](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%202/navigation-app-graph.png)

Let's use the same example estimated costs which are determined by my almost arbitrary heuristic.

- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`UQLake`![%29%20%3A%3D%20100](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%20100)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld78`![%29%20%3A%3D%2050](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2050)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`AEB`![%29%20%3A%3D%2053](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2053)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Wordsmith`![%29%20%3A%3D%209999](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%209999)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld42`![%29%20%3A%3D%2050](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2050)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld50`![%29%20%3A%3D%2038](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2038)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld51`![%29%20%3A%3D%2030](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%2030)
- ![h%28](https://latex.codecogs.com/gif.latex?h%28)`Bld7`![%29%20%3A%3D%200](https://latex.codecogs.com/gif.latex?%29%20%3A%3D%200)



- Almost the same as Uniform Cost search and Greedy Best First search
- Use **priority queue (PQ)** to keep fringe nodes
  - The highest priority in PQ for A* is the node with the smallest combined estimated cost plus distance from the root node from the current node to the goal (i.e. ![g%20%2B%20h](https://latex.codecogs.com/gif.latex?g%20%2B%20h)), so it combines Uniform Cost search with Greedy Best First search.

1. Set the initial vertex ![I](https://latex.codecogs.com/gif.latex?I) as the root of the search tree
2. Push ![I](https://latex.codecogs.com/gif.latex?I) to the PQ
3. Loop
   1. Assign ![t%3A%3D](https://latex.codecogs.com/gif.latex?t%3A%3D) the node ![n](https://latex.codecogs.com/gif.latex?n) from the PQ with the lowest ![f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29)
   2. Remove ![t](https://latex.codecogs.com/gif.latex?t) from PQ and mark ![t](https://latex.codecogs.com/gif.latex?t) as expanded
   3. If ![t](https://latex.codecogs.com/gif.latex?t) is the goal vertex, then return
   4. For each ![v](https://latex.codecogs.com/gif.latex?v) in `successor(`![t](https://latex.codecogs.com/gif.latex?t)`)`:
      - Insert ![v](https://latex.codecogs.com/gif.latex?v) to the PQ
      - Put ![v](https://latex.codecogs.com/gif.latex?v) as a child of ![t](https://latex.codecogs.com/gif.latex?t) in the search tree

![1565392463831](C:\Users\trist\AppData\Roaming\Typora\typora-user-images\1565392463831.png)



#### A* search properties & analysis

- ![b](https://latex.codecogs.com/gif.latex?b): branching factor
- ![m](https://latex.codecogs.com/gif.latex?m) maximum depth
- Complete?
  - Yes as long as all edges have a positive cost (i.e. ![%5Cepsilon%20%5Cgt%200](https://latex.codecogs.com/gif.latex?%5Cepsilon%20%5Cgt%200))
- Optimal (in terms of lowest cost)
  - Yes as long as all edges have a positive cost and [the heuristic is admissible](#Admissible-heuristics)
- Complexity
  - Highly depends on heuristic e.g. [consistency](#Consistency)



#### Proof that A* search is complete as long as all edges have a positive cost

* Do later

#### Proof that A* search is optimal as long as all edges have a positive cost and [the heuristic is admissible](#Admissible-heuristics)

Suppose ![C%5E%2A](https://latex.codecogs.com/gif.latex?C%5E%2A) is the optimal cost. At any moment in time, the set of fringe nodes must contain at least one node that lies in an optimal solution. Let's call this ![K](https://latex.codecogs.com/gif.latex?K).

Right before a non-optimal goal node, ![G%27](https://latex.codecogs.com/gif.latex?G%27), is selected from the fringe, we'll have
![f%28G%27%29%20%3D%20g%28G%27%29%20%2B%20h%28G%27%29%20%5Cgeq%20g%28G%27%29%20%5Cgeq%20C%5E%2A%0A](https://latex.codecogs.com/gif.latex?f%28G%27%29%20%3D%20g%28G%27%29%20%2B%20h%28G%27%29%20%5Cgeq%20g%28G%27%29%20%5Cgeq%20C%5E%2A%0A)while ![f%28K%29%20%5Cleq%20C%5E%2A](https://latex.codecogs.com/gif.latex?f%28K%29%20%5Cleq%20C%5E%2A) (![h](https://latex.codecogs.com/gif.latex?h) is admissible).

Since A* always chooses fringe nodes with the smallest ![f](https://latex.codecogs.com/gif.latex?f) value, ![G%27](https://latex.codecogs.com/gif.latex?G%27) cannot be chosen before ![K](https://latex.codecogs.com/gif.latex?K). This is true for all levels of ![K](https://latex.codecogs.com/gif.latex?K).



### A* with revisiting nodes

Revisiting nodes will guarantee optimality regardless of whether the heuristic is admissible or not. Computational complexity takes a hit though. Some options:

* Naïve: **revisit all** vs **discard all**

* Alternative: **Discard a revisited node** if the cost to the node via this new path is more than the cost of reaching the node via a previously found path

  * The solution will be optimal in terms of cost, but may still be quite inefficient, due to revisiting nodes that are in the optimal path

* Works with a [consistent/monotonic heuristic](#Consistent-heuristics) ![h%28n%29%20%5Cleq%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29](https://latex.codecogs.com/gif.latex?h%28n%29%20%5Cleq%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29) where:

  * ![c%28n%2C%20a%2C%20n%27%29](https://latex.codecogs.com/gif.latex?c%28n%2C%20a%2C%20n%27%29) is the cost of going from node ![n](https://latex.codecogs.com/gif.latex?n) to ![n%27](https://latex.codecogs.com/gif.latex?n%27) via action ![a](https://latex.codecogs.com/gif.latex?a).

  ![Consistent heuristic](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%203/consistent-heuristic.png)

* If the heuristic is consistent/monotonic, when A* expands a node ![n](https://latex.codecogs.com/gif.latex?n), the path to ![n](https://latex.codecogs.com/gif.latex?n) is **optimal**.
  * Therefore, we don't need to revisit nodes that have been expanded

Therefore, if ![h](https://latex.codecogs.com/gif.latex?h) is consistent, we can adjust the algorithm for A* to be:

1. Set the initial vertex ![I](https://latex.codecogs.com/gif.latex?I) as the root of the search tree
2. Push ![I](https://latex.codecogs.com/gif.latex?I) to the PQ
3. Loop
   1. Assign ![t%3A%3D](https://latex.codecogs.com/gif.latex?t%3A%3D) the node ![n](https://latex.codecogs.com/gif.latex?n) from the PQ with the lowest ![f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20%2B%20h%28n%29)
   2. Remove ![t](https://latex.codecogs.com/gif.latex?t) from PQ and mark ![t](https://latex.codecogs.com/gif.latex?t) as expanded
   3. If ![t](https://latex.codecogs.com/gif.latex?t) is the goal vertex, then return
   4. For each ![v](https://latex.codecogs.com/gif.latex?v) in `successor(`![t](https://latex.codecogs.com/gif.latex?t)`)`:
      * **If ![v](https://latex.codecogs.com/gif.latex?v) has not been expanded**:
        * Insert ![v](https://latex.codecogs.com/gif.latex?v) to the PQ
        * Put ![v](https://latex.codecogs.com/gif.latex?v) as a child of ![t](https://latex.codecogs.com/gif.latex?t) in the search tree

This algorithm is identical to Uniform Cost search except it uses ![g%2Bh](https://latex.codecogs.com/gif.latex?g%2Bh) instead of ![g](https://latex.codecogs.com/gif.latex?g). This algorithm is **complete** and **optimal** as long as ![h](https://latex.codecogs.com/gif.latex?h) is **admissible** and **consistent**.

#### Proof that if ![h](https://latex.codecogs.com/gif.latex?h) is consistent, the path to ![k](https://latex.codecogs.com/gif.latex?k) is optimal when A* expands ![K](https://latex.codecogs.com/gif.latex?K)

Start by assuming ![h](https://latex.codecogs.com/gif.latex?h) is consistent and ![n%2C%20n%27%20%5Cin%20S](https://latex.codecogs.com/gif.latex?n%2C%20n%27%20%5Cin%20S) such that ![n%27%20%5Cin%20%5Cmathrm%7Bsuccessor%7D%28n%29](https://latex.codecogs.com/gif.latex?n%27%20%5Cin%20%5Cmathrm%7Bsuccessor%7D%28n%29). 

Then,
![%5Cbegin%7Balign%2A%7D%0A](https://latex.codecogs.com/gif.latex?%5Cbegin%7Balign%2A%7D%0A)![f%28n%29%20%26%3D%20g%28n%29%20%2B%20h%28n%29%20%5C%5C%0A](https://latex.codecogs.com/gif.latex?f%28n%29%20%26%3D%20g%28n%29%20%2B%20h%28n%29%20%5C%5C%0A)![%26%5Cleq%20g%28n%29%20%2B%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29%20%5Cquad%20%5Cbecause%20h%20%5Ctext%7B%20is%20consistent%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%26%5Cleq%20g%28n%29%20%2B%20c%28n%2C%20a%2C%20n%27%29%20%2B%20h%28n%27%29%20%5Cquad%20%5Cbecause%20h%20%5Ctext%7B%20is%20consistent%7D%5C%5C%0A)![%26%3D%20g%28n%27%29%20%2B%20h%28n%27%29%20%5Cquad%20%5Cbecause%20g%28n%27%29%20%3D%20g%28n%29%20%2B%20c%28n%2C%20a%2C%20n%27%29%20%5C%5C%0A](https://latex.codecogs.com/gif.latex?%26%3D%20g%28n%27%29%20%2B%20h%28n%27%29%20%5Cquad%20%5Cbecause%20g%28n%27%29%20%3D%20g%28n%29%20%2B%20c%28n%2C%20a%2C%20n%27%29%20%5C%5C%0A)![%26%3D%20f%28n%27%29.%0A](https://latex.codecogs.com/gif.latex?%26%3D%20f%28n%27%29.%0A)![%5Cend%7Balign%2A%7D%0A](https://latex.codecogs.com/gif.latex?%5Cend%7Balign%2A%7D%0A)Therefore, ![f%28n%29%20%5Cleq%20f%28n%27%29](https://latex.codecogs.com/gif.latex?f%28n%29%20%5Cleq%20f%28n%27%29) i.e. ![f](https://latex.codecogs.com/gif.latex?f) is non-decreasing.

Suppose ![K%20%5Cin%20S](https://latex.codecogs.com/gif.latex?K%20%5Cin%20S) is chosen to be expanded. Then ![f%28K%29%20%5Cleq%20f%28N%29](https://latex.codecogs.com/gif.latex?f%28K%29%20%5Cleq%20f%28N%29) where ![N](https://latex.codecogs.com/gif.latex?N) is all other nodes in the fringe (due to the nature of A*).

Suppose ![N](https://latex.codecogs.com/gif.latex?N) is in a path leading to ![K](https://latex.codecogs.com/gif.latex?K) via node ![N%27](https://latex.codecogs.com/gif.latex?N%27). Then ![f%28K%29%20%5Cleq%20f%28N%27%29%20%5Cleq%20f%28N%29](https://latex.codecogs.com/gif.latex?f%28K%29%20%5Cleq%20f%28N%27%29%20%5Cleq%20f%28N%29). Since ![h](https://latex.codecogs.com/gif.latex?h) is consistent, ![h%28N%27%29%20%5Cleq%20h%28K%29](https://latex.codecogs.com/gif.latex?h%28N%27%29%20%5Cleq%20h%28K%29) and therefore ![g%28K%29%20%5Cleq%20g%28N%27%29](https://latex.codecogs.com/gif.latex?g%28K%29%20%5Cleq%20g%28N%27%29).

Hence, the cost to reach ![K](https://latex.codecogs.com/gif.latex?K) via ![N](https://latex.codecogs.com/gif.latex?N) is at **least** equal to the cost to reach ![K](https://latex.codecogs.com/gif.latex?K) when it's first expanded.

#### For a graph search, consistent and admissible heuristic guarantees optimality for regular A*

For a **tree** search, only admissibility is required for optimality.

#### Consistency implies admissibility

Consistent ![%5Cimplies](https://latex.codecogs.com/gif.latex?%5Cimplies) admissible but the converse isn't always true!

So really, the statement above that a consistent and admissible heuristic implies optimality in a graph search can be rewritten to: **The graph-search version of A* is optimal if ![h](https://latex.codecogs.com/gif.latex?h) is consistent**.

Note: The tree-search version of A* is optimal if ![h](https://latex.codecogs.com/gif.latex?h) is admissible (because there's no loops and no need to revisit nodes).

#### Consistency is not always great

A basic example is when ![h%28n%29%20%3D%200](https://latex.codecogs.com/gif.latex?h%28n%29%20%3D%200). Then we simply have Uniform Cost search which isn't ways best.



### How to generate heuristics

We need:

* Information about the problem (domain knowledge)
* Knowledge about the sub-problems
* Learn from prior results of solving the same or similar problems

Examples:

* How can this apply to the 8-puzzle?



