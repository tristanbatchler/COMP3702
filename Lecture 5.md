# Lecture 5

## We don't always need to construct the state graph explicitly

* Build a search tree directly
* **Expansive space tree (EST)**
  * Set the initial configuration as a root node
  * Repeat:
    * Select a node $q$ to expand with probability $1/N(q)$ where $N(q)$ is the # nodes in the tree that are within $D$ distance from $q$
    * Sample a configuration $q'$ uniformly at random from all possible configurations within $D$ distance from $q$
    * If $q'$ is collision-free and the straight line segment between $q$ and $q'$ is collision-free, add $q'$ as a child of $q$
  * Usually bidirectional search
* **Rapidly exploring random trees (RRT)**
  * Set the initial configuration as a root node
  * Repeat
    * Select a configuration $q$ uniformly at random from the configuration space
    * Find a node nearest to $q$. Suppose this node is $q'$.
    * Find a configuration $q_{\mathrm{new}}$ in line segment $q'q$ such that the line segment $q'q_{\mathrm{new}}$ lies entirely in the free space and the distance between $q'$ and $q_{\mathrm{new}}$ is less than $D$.
    * Add $q_\mathrm{new}$ as a child node of $q'$ in the tree.
  * Usually bidirectional search



### On-line planning

* Rather than computing the entire path at once and execute, we can also compute the best shorter plan at each step. The latter is called **on-line planning**.
* This is used often when the problem size (size of state and/or action space) is very large
  * Usually to save memory!
  * Also to save time (more on that later)
  * The tree search method can be used for on-line search easily

## Why do sampling-based methods work?

**Intuitively**, because solutions are abundant in a continuous space and, to solve the problem, we only need to find one!

In most free spaces of real-world problems, every configuration "sees" a significant fraction of the free space.

* A configuration $q$ "sees" another configuration $q'$ whenever the straight line segment between $q$ and $q'$ lies entirely in the free space. The space of configurations "seen" by the space below is highlighted in orange.

![1566627838611](.\Images\Lecture 5\c-space-visibility.png)

A relatively small number of vertices and edges are sufficient to cover most free spaces with high probability, and hence solve the given queries.



**Slightly more formally**, the lookout of a subset $F_1$ of the free space is the set of all configurations in $F_1$ from which it is possible to "see" a significant fraction of the free space outside $F_1$.

![1566628085931](.\Images\Lecture 5\beta-lookout.png)

The $\beta\mathrm{-lookout}(F_1)$ is the set of configurations in $F_1$ from which it is possible to "see" $\beta$ fraction of the free space outside $F_1$.

So the lookout is like a chokepoint/corridor which needs to be sampled before you can access another significant portion of the configuration space.

The free space $F$ is expansive if all of its subsets have a large lookout.

$F$ is $\alpha\beta$-expansive iff. for any connected subset $F_i \subseteq F$ 

* $\mathrm{Volume}(\beta\mathrm{-lookout}(F_i)) = \alpha$

So basically, $\alpha$ is the volume of the $\beta$-lookout of $F_i$, i.e. the volume of configuration space necessary to "see" $\beta$ fraction of the free space outside of $F_i$.

The number of samples to capture the correct connectivity of the free space with probability at least $P$ is inversely proportional to $\alpha$ and $\beta$.

PRM (and its variants) perform well when the free space of the problem has large $\alpha$ and $\beta$.

Of the following C-Spaces, the one on the **right** is easiest to solve by sampling-based approaches. This is because the $\alpha$ and $\beta$ are larger on the right.

![1566628672530](C:\Users\tristan\School\COMP3702\Images\Lecture 5\ab-expansive-illustration.png)

So if we know $\alpha$ and $\beta$ of the free space, we can compute the number of samples to solve a given problem with high probability.

But, to compute $\alpha$ and $\beta$, we need the geometry of the free space.

* PRM is successful exactly because it's **not** computing the geometry of the free space
* Practically, we don't know $\alpha$ and $\beta$, nor the exact # of samples to use.

So, why bother?

* Sometimes we can "guess" $\alpha$ and $\beta$ from the workspace $\to$ known when to use PRM and when not to
* Guarantees that we will eventually get a solution (if one exists!)



## Logic

### Where is logic used?

* Action planning?
* IC design
* Databases
* Debugging
* Game player

### A formal language

Composed of both:

* Syntax
  * Which expressions are legal in our formal language
* Symantics
  * What is the meaning of legal expressions in our formal language?



### Many types of logic

* **Propositional** logic (everything is either **True** or **False**)
* **Predicate** logic / first order logic (**FOL**)
* **High order** logic



### Propositional logic - Syntax

* **Atomic**

  * An expression that is known to be either true or false
  * E.g.
    * $x + 2 = 2x$ when $x = 1$ is false
    * "What is the distance between Mars and Earth?" is not propositional

  * Typically denote a proposition as $p$ or $q$.
* **Complex sentences**

  * Constructed from atomic sentences and logical connectives:

    * Brackets $()$, negation $\neg$, and $\and$, or $\or$, implies, $\to$, iff. $\lrarr$.
  * If $S, S_1, S_2$ are sentences, then so are the following:
    * $(S)$
    * $\neg S$ is true iff. $S$ is false
    * $S_1 \and S_2$ is true iff. $S_1$ is true or $S_2$ is true
    * $S_1 \or S_2$ is true iff. $S_1$ is true and $S_2$ is true
    * $S_1 \to S_2$ is true iff. $S_2$ is true or $S_1$ is false (absurd)
    * $S_1 \lrarr S_2$ is true iff. $S_1 \to S_2 \and S_2 \to S1$ is true
* **Semantics**
  * Meaning of a sentence: truth values
  * The truth of a complex sentence can be derived from the truth values of logical connectives for the given sentence
  * i.e. truth tables
  * Interpretation: Assignment of truth values to propositional variables



### Some terminology

* A sentence is **valid** if it's true for all possible interpretations, i.e. **tautology**
* A sentence is **satisfiable** if its truth value is T fo at least one of the possible interpretations

  * e.g. $\neg P$.
  * Everything that's valid is satisfiable
* A sentence is unsatisfiable if its truth value is F for all possible interpretations

  * e.g. $P \and \neg P$
* For propositional logic, we can always decide if a sentence is valid/satisfiable/unsatisfiable in finite time (decidable)
* A **model** of a sentence is an interpretation that makes the sentence true
* A sentence $A$ **entails** another sentence $B$ (denotes $A \models B$) iff. every model of $A$ is also a model of $B$ ($A \to B$ is valid)

### Entailment

* Relation betwen sentences are based on relations between their interpretations

### How logic is used to represent a problem

*  Formulate information as propositional logic sentences
  * Create a knowledge base (KB)
  * KB: a set of sentences, such that KB is false in models that contradict what the agent knows
* Example: The Wumpus World
  * See page 236 of *Artificial Intelligence: A Modern Approach*
  * Squares adjacent to Wumpus are smelly
  * Squares adjacent to pits are breezy
  * Glitter iff. gold is in the same square

