### Blind search

**Q:** What is the definition of blind search?

**A:** A search for a solution in a space where we do not have any additional information to base a "guess" on the cost of moving to the goal. In other words, there is no heuristic.



**Q:** What kind of container does Breadth First Search use? Is it FIFO or FILO? What does the abbreviation stand for?

**A:** Queue, FIFO, first in first out.



**Q:** Describe the steps for the BFS algorithm.

**A:**

* Let $I$ be a node holding the initial state of the problem
* Push $I$ to the queue
* Loop
  * If the queue is empty, return failure
  * Pop a vertex from the queue and call it $t$
  * Mark $t$ as "explored"
  * If $t$ holds the goal state, return success
  * For each vertex $v$ that is a successor of $t$:
    * If $v$ is not "explored" or in the queue:
      * Insert $v$ into the queue



**Q:**

**A:**

### Informed search

**Q:** What is the definition of informed search?

**A:** A search for a solution in a space where we use additional information to base a "guess" on the cost of moving to the goal. In other words, we use a heuristic.



**Q:**

**A:**



**Q:**

**A:**



**Q:**

**A:**



**Q:**

**A:**



**Q:**

**A:**



**Q:**

**A:**



