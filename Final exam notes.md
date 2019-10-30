### Preparation resources

* Past exams: http://robotics.itee.uq.edu.au/~ai/doku.php/wiki/resources
* Tutorials: https://learn.uq.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_124076_1&content_id=_4679265_1



### Rational agents

**Q: **What are the components that define a rational agent?

**A:**

**Q: **Describe the difference between discrete and continuous.

**A: **

**Q: **Describe the difference between deterministic and non-deterministic.

**A: **

**Q: **Describe the difference between observable and partially observable.

**A: **

**Q: **Describe the difference between static and dynamic.

**A: **

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
  * Pop a node from the queue and call it $t$
  * Mark $t$ as "explored"
  * If $t$ holds the goal state, return success
  * For each node $v$ that is a successor of $t$:
    * If $v$ is not "explored" or in the queue:
      * Insert $v$ into the queue

**Q: ** Describe the computational complexity of BFS.

**A: **

**Q: ** Is BFS complete? Is it optimal?.

**A: **



**Q:** What kind of container does depth first search use? Is it FIFO or FILO? What does the abbreviation stand for?

**A:** Stack, FILO, first in last out.



**Q:** Describe the steps for the DFS algorithm.

**A:** 

* Let $I$ be a node holding the initial state of the problem
* Put $I$ on the stack
* Loop:
  * If the queue is empty, return failure
  * Pop a node off the stack and call it $t$
  * Mark $t$ as "explored"
  * If $t$ holds the goal state, return success
  * For each node $v$ that is a successor of $t$
    * If $v$ is not yet "explored" or in the stack:
      * Put $v$ on the stack



**Q: ** Describe the computational complexity of DFS.

**A: **

**Q: ** Is DFS complete? Is it optimal?.

**A: **



**Q:** What kind of container does iterative deepening depth first search use? How are nodes in the container removed?

**A:** 



**Q:** Describe the steps for the IDDFS algorithm.

**A:** 



**Q: ** Describe the computational complexity of IDDFS.

**A: **

**Q: ** Is IDDFS complete? Is it optimal?.

**A: **



**Q:** What kind of container does depth first search use? How are nodes in the container removed?

**A:** Priority queue, nodes with a lower value (i.e. lesser numbers) are removed first.



**Q:** Describe the steps for the UCS algorithm.

**A:** 

- Let $I$ be a node holding the initial state of the problem and a value of $0$
- Add $I$ to the priority queue
- Loop:
  - If the priority queue is empty, return failure
  - Remove a node from the priority queue and call it $t$
  - Mark $t$ as "explored"
  - If $t$ holds the goal state, return success
  - For each node $v$ that is a successor of $t$
    - If $v$ is not yet "explored" or in the priority queue:
      - Add $v$ to the priority queue  



**Q: ** Describe the computational complexity of UCS.

**A: **

**Q: ** Is UCS complete? Is it optimal?.

**A: **

### Informed search

**Q:** What is the definition of informed search?

**A:** A search for a solution in a space where we use additional information to base a "guess" on the cost of moving to the goal. In other words, we use a heuristic.



**Q:** What is the difference between UCS and A* search?

**A:**



**Q:** What is the difference between A* Greedy Best First search?

**A:**



**Q:** What is the definition of an **admissible** heuristic?

**A:** A heuristic is admissible if it never overestimates the cost.



**Q:** What is the definition of a **consistent** heuristic?

**A:** The estimated cost of moving from node $A$ to $C$ is never more than the true cost of moving from $A$ to $B$ plus the estimated cost of moving from $B$ to $C$. In other words:
$$
h(AB) \leq c(AB) + h(BC)
$$


**Q: **

**A:**



**Q:**

**A:**



### Logic

**Q: ** What does it mean for an FOL sentence to be **valid**?

**A: ** 

**Q: ** What does it mean for an FOL sentence to be **satisfiable**?

**A: ** 

**Q: ** What does it mean for an FOL sentence to be **unsatisfiable**?

**A: ** 

**Q: ** What is the model of an FOL sentence?

**A: ** 

**Q: **What does it mean for an FOL sentence $A$ to **entail** another sentence $B$? How is it denoted?

**A: **Either is acceptable:

* Every model of $A$ is also a model of $B$. 
* $A \to B$ is valid/always true.

It is denoted $A \models B$.

**Q: ** List all logical equivalence laws and their definitions.

**A: **

| $A$                 | $B$                         | Name                                |
| ------------------- | --------------------------- | ----------------------------------- |
| $a \and b$          | $b \and a$                  | Commutativity of $\and$             |
| $a \or b$           | $b \or a$                   | Commutativity of $\or$              |
| $(a \and b) \and c$ | $a \and (b \and c)$         | Associativity of $\and$             |
| $(a \or b) \or c$   | $a \or (b \or c)$           | Associativity of $\or$              |
| $\neg(\neg a)$      | $a$                         | Double-negation elimination         |
| $a \to b$           | $\neg b \to \neg a$         | Contrapositive                      |
| $a \to b$           | $\neg a \or b$              | Implication elimination             |
| $a \lrarr b$        | $(a \to b) \and (b \to a)$  | Biconditional elimination           |
| $\neg(a \and b)$    | $\neg a \or \neg b$         | De Morgan's law                     |
| $\neg (a \or b)$    | $\neg a \and \neg b$        | De Morgan's law                     |
| $a \and (b \or c)$  | $(a \and b) \or (a \and c)$ | Distributivity of $\and$ over $\or$ |
| $a \or (b \and c)$  | $(a \or b) \and (a \or c)$  | Distributivity of $\or$ over $\and$ |

**Q: ** What is modus ponens?

**A: ** 

**Q: ** What is modus tollens?

**A: ** 

**Q: ** What is and-elimination?

**A: ** 

**Q: ** Describe the steps to convert an FOL statement to conjunctive normal form

**A: ** 

**Q: ** Describe the steps to the resolution refutation algorithm

**A: **



### Decision theory

**Q: **What is Bayes' rule?

**A: **



