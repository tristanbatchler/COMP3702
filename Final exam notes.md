### Preparation resources

* Past exams: http://robotics.itee.uq.edu.au/~ai/doku.php/wiki/resources
* Tutorials: https://learn.uq.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_124076_1&content_id=_4679265_1
* I should make sure to practice DPLL **lots** (see UQ theme park question from tutorial 6)

### Known facts

* There **will** be a question on logic rules including De Morgan's laws and conversion to CNF.
* There **will** be a question on decision theory including Bayes' rule.
* There will be **no** continuous search or motion planning questions! :grin:
* There is **no** need to memorise the DPLL algorithm -- only need to know how to use it.
* The exam has a total of 120 marks over 6 questions.
* The exam will have a total time of 120 minutes.
* The exam is closed book.
* The exam will be fairly similar to other previous exams. :grin:



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

**Q: ** Describe the space and time complexity of BFS.

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



**Q: ** Describe the space and time complexity of DFS.

**A: **

**Q: ** Is DFS complete? Is it optimal?.

**A: **



**Q:** What kind of container does iterative deepening depth first search use? How are nodes in the container removed?

**A:** 



**Q:** Describe the steps for the IDDFS algorithm.

**A:** 



**Q: ** Describe the space and time complexity of IDDFS.

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



**Q: ** Describe the space and time complexity of UCS.

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

**A:** The estimated cost of moving from node $A$ to the goal is never more than the true cost of moving from $A$ to $B$ plus the estimated cost of moving from $B$ to the goal. In other words:
$$
h(A) \leq c(\overline{AB}) + h(B)
$$

**Q: **What is the implication between admissibility and consistency of a heuristic?

**A: **Consistency implies admissibility but the converse is not true.



**Q: **

**A:**



### Logic

**Q: ** What does it mean for a sentence to be **valid**?

**A: **The sentence is true for all possible interpretations. Also acceptable: the sentence is a logical tautology.



**Q: ** What does it mean for a sentence to be **satisfiable**?

**A: ** The sentence is true for at least one interpretation.



**Q: ** What does it mean for a sentence to be **unsatisfiable**?

**A: ** The sentence is false for all possible interpretations. Also acceptable: the sentence is a logical contradiction.



**Q: ** What is the model of a sentence?

**A: ** An interpretation that makes the sentence true.



**Q: **What does it mean for a sentence $A$ to **entail** another sentence $B$? How is it denoted?

**A: **Either is acceptable:

* Every model of $A$ is also a model of $B$. 
* $A \to B$ is valid/always true.

It is denoted $A \models B$.



**Q: **What does it mean for an algorithm to be sound?

**A: **If it produces a result, the result is correct.



**Q: **What does it mean for an algorithm to be complete?

**A: **It will always produce a result.



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

**Q: ** What is modus ponens? What does it translate to? What is your favourite example? How is it written with atoms $a$ and $b$?

**A: ** 

* Suppose $a$ implies $b$ and $a$ is true. Then $b$ must be true. 

* Mode that affirms. 

* The sky is blue implies the water is blue. The sky is blue. Therefore the water is blue.

* $$
  a \to b\\ a\\\rule{2cm}{0.4pt}\\ a
  $$



**Q: ** What is modus tollens? What does it translate to? What is your favourite example?

**A: ** 

* Suppose $a$ implies $b$ and $b$ is false. Then $a$ must also be false. 

* Mode that denies. 

* The sky is blue implies the water is blue. The water is red. Therefore the sky cannot be blue.

* $$
  a \to b \\\ \neg b \\ \rule{2cm}{0.4pt}\\\neg a
  $$



**Q: ** What is conjunction elimination? How is it written with atoms $a$ and $b$?

**A: ** 

* Suppose $a$ and $b$ is true. Then $a$ is true.

* $$
  a \and b\\
  \rule{2cm}{0.4pt}\\
  a
  $$



**Q: **How resolution is it written with atoms $a$, $b$, and $c$?

**A: **
$$
a \or b\\
\neg a \or c\\
\rule{2cm}{0.4pt}\\
b \or c
$$




**Q: **What is model checking?

**A: **A way of determining whether a sentence is true for all possible interpretations.



**Q:** Was is the simplest approach to model checking?

**A: **Enumerate the models, i.e. all true/false combinations for the sentence and checking if the sentence is true in each case.



**Q: **What is a better approeach to model checking? How does it work?

**A: **Theorem proving. Use logical equivalence laws and inference rules to make legal steps from the initial statement to the goal statement.



**Q: **What is a logical atom?

**A: **A single symbol with no logical connectives.



**Q: **What is a logical literal?

**A: **An atom or the negation of an atom.



**Q: **What is a logical clause?

**A: **A disjunction of literals.



**Q: **What does it mean to convert a sentence to conjunctive normal form?

**A: **We convert the sentence into a (either of these is acceptable):

* conjunction of disjunctions of atoms or the negation of atoms
* conjunction of disjunctions of literals
* conjunction of clauses



**Q: **What are the only logical connectives in a sentence that is in CNF?

**A:** **And** ($\and$), **or** ($\or$), and **not** ($\neg$).



**Q: **Describe the steps to convert a sentence to CNF.

**A:** 

1. Eliminate arrows using definitions
2. Drive in negations using De Morgan's laws
3. Distribute **or** ($\or$) over **and** ($\and$)



**Q: ** Describe the steps to the resolution refutation algorithm

**A: **

1. Convert all sentences to CNF
2. Negate the desired conclusion
3. Keep applying resoluton until a contradiction arises



**Q: **What is a satisfiability problem or a constraint satisfaction problem?

**A: **A question of assigning values to each variable in a problem such that all the constraints are satisfied.



**Q: **Is the Davis-Putnam-Logeman-Loveland algorithm sound and complete?

**A: ** Yes to both.



**Q: **Alternative to DPLL, name another method to solve satisfiability problems? Describe its steps. Is it sound and complete?

**A: **GSAT.

* Loop $n$ times:
  * Randomly an assignment for all variables
  * Loop $m$ times:
    * Flip the variable that results in the lowest number of unsatisfied clauses
    * If there are no unsatisfied clauses, return the assignment chosen

It is sound but not complete.



**Q: **What is a unit clause?

**A: **A clause that consists of only one unassigned literal.



**Q: **What is a pure variable within a sentence?

**A: **A variable which appears in the sentence as (either of these is acceptable):

* only ever positive or only ever negative
* always atomic or always negated



### Decision theory

**Q: **What does the branching at each interleaving level of an AND-OR tree represent?

**A: **Branching at an AND level represents the agent's choices of action while branching at an OR level represents actions taken by the environment.



**Q: **What are the two types of nodes in an AND-OR tree? What level are these types found at?

**A: **

* State node found at each OR level
* Action node found at each AND level



**Q: **Describe the steps required to find a solution to an AND-OR tree.

**A: **

* Mark all the leaf nodes as "solved" if their state is a goal state

* Working up the tree:
  * label action nodes as "solved" if **all** its children are "solved"
  * label state nodes as "solved" if **at least one of** its children is "solved"
* If you reach the root, the solution is the sub-tree from the root where all nodes are "solved"



**Q: **What does the branching at each interleaving level of a minimax tree represent?

**A: **Branching at a MAX level represents the agent's choices of action while branching at a MIN level represents actions taken by the opponent.



**Q: **What is the thing each player of a minimax game are trying to minimise or maximise? What does it represent?

**A: **An evaluation function (also acceptable: a heuristic). Represents an estimate as to how favourable a game state is for the agent.



**Q: **Describe the steps of the minimax algorithm.

**A: **

* Compute the evaluation function at every leaf of the tree

* Working up the tree:
  * label MAX nodes as the maximum evaluation of its immediate children (i.e. successors)
  * label MIN nodes as the minimum evaluation of its immediate children




**Q: **

**A: **




**Q: **

**A: **




**Q: **

**A: **




**Q: **

**A: **




**Q: **

**A: **




**Q: **

**A: **



**Q: **What is Bayes' rule?

**A: **