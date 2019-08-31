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
* A sentence is **satisfiable** if its truth value is T for at least one of the possible interpretations

  * e.g. $\neg P$.
  * Everything that's valid is satisfiable
* A sentence is unsatisfiable if its truth value is F for all possible interpretations

  * e.g. $P \and \neg P$
* For propositional logic, we can always decide if a sentence is valid/satisfiable/unsatisfiable in finite time (decidable)
* A **model** of a sentence is an interpretation that makes the sentence true
* A sentence $A$ **entails** another sentence $B$ (denoted $A \models B$) iff. every model of $A$ is also a model of $B$ ($A \to B$ is valid)

### Entailment

* Relation between sentences are based on relations between their interpretations

### How logic is used to represent a problem

*  Formulate information as propositional logic sentences
  * Create a knowledge base (KB)
  * KB: a set of sentences, such that KB is false in models that contradict what the agent knows
* Example: The Wumpus World
  * See page 236 of *Artificial Intelligence: A Modern Approach*
  
  * Squares adjacent to Wumpus are smelly
  
  * Squares adjacent to pits are breezy
  
  * Glitter iff. gold is in the same square
  
    ![1567204910509](.\Images\Lecture 5\representing-wumpus-world-problem.png)
  
    Results of perception up to the current time can be added to the KB.
  
    E.g. Suppose the agent has only visited $(1, 1)$ and perceives:
  
    * $P_{1, 1} = \mathrm{False}$, $B_{1, 1} = \mathrm{False}$, $W_{1, 1} = \mathrm{False}$, $S_{1, 1} = \mathrm{False}$, $\mathrm{Go}_{1, 1} = \mathrm{False}$, $G_{1, 1} = \mathrm{False}$
    * Then we can add the following sentences to the initial KB:
      * $\neg P_{1, 1}$, $\neg B_{1, 1}$, $\neg W_{1, 1}$, $\neg S_{1, 1}$, $\neg \mathrm{Go}_{1, 1}$, $\neg G_{1, 1}$, 
  
    What else can we use the KB for?
  
    * Deduce new information, sentences entailed by the current KB can be added to the KB
    * Answering questions such as can we conclude there's no pit in $(1, 2)$?
    * Formally,
      * Given the knowledge base $\mathrm{KB} := S_1, S_2, \cdots, S_n$:
        * Does KB entail that $\neg P_{1, 2}$? i.e. does $\mathrm{KB} \models P_{1,2}$?
        * In other words, is the sentence valid? $S_1 \and S_2 \and \cdots \and S_n \to \neg P_{1,2}$



### (Simple) model checking

When checking if a sentence is valid, you must check if it is valid in all models.

A simple way to check this is to enumerate all the models and make a truth table.

#### Model checking terminology

* Sound: the result is correct
* Complete: It always gives an answer
* Complexity: Time, Space in $O(f(n))$ where $n$ is the number of propositional variables.

### Theorem proving

If $\alpha$ and $\beta$ are sentences, then two sentences are logically equivalent iff. true in the same models:

$\alpha \equiv\beta \lrarr \alpha \models \beta \and \beta \models\ \alpha$

Can use the following rules to show logical equivalences using the axioms

![1567205673321](.\Images\Lecture 5\logical-equivalences.png)

### Inference rules

* Modus ponens (mode that affirms)

  * $\alpha \to \beta$ says that, if $\alpha$ then $\beta$ can be inferred

  * Proof by implication

  * $$
    \alpha \to \beta\\ \alpha\\\rule{2cm}{0.4pt}\\ \beta
    $$

* Modus tollens (model that denies)

  * $\alpha \to \beta$ says that, if $\neg \beta$ then $\neg \alpha$ can be inferred

  * i.e. $\alpha \to \beta \equiv \neg \alpha \to \neg \beta$.

  * Proof by contraposition

  * $$
    \alpha \to \beta\\
    \neg \beta\\
    \rule{2cm}{0.4pt}\\
    \neg \alpha
    $$

* And-elimination (for a conjunction, any of the conjuncts can be inferred)

  * $\alpha \and \beta$ says that $\alpha$ can be inferred and $\beta$ can be inferred

  * $$
    \alpha \and \beta\\\rule{2cm}{0.4pt}\\ \alpha
    $$



### Theorem proving: natural deduction

Use the rules available to make logical steps to arrive to a new conclusion



### Theorem proving as a search problem

* $S$: all possible sets of sentences (knowledge bases)
* $A$: the set of all inference rules
* $T:S \to S$: The act of applying an inference rule to all sentences in the knowledge base that match the form of the inference and seeing the resulting new sentences that is the inference made.
* Initial state: initial knowledge base
* Goal state: the state that contains the sentence we're trying to prove



### Resolution

A single inference rule
$$
\alpha \or \beta\\
\neg \beta \or \gamma\\
\rule{2cm}{0.4pt}\\
\alpha \or \gamma
$$
But, the single inference rule is sound and complete only when applied to logical sentences written in Conjunctive Normal Form (**CNF**).

### Conjunctive Normal Form (CNF)

Conjunctions of disjunctions

e.g. $(\neg A \or B) \and (C \or D)$.

Some terminology:

* **Clause**: a disjunction of literals e.g. $(\neg A \or B)$
* **Literals**: variables or the negation of variables, e.g. $\neg A$, $B$

CNF if useful for model checking.

### Converting to CNF

Every sentence in propositional logic can be written in CNF.

Three step conversion:

1. Eliminate implications using definitions (i.e.. $A \to B \equiv \neg A \or B$)
2. Distribute negations using De Morgan's Laws (i.e. $\neg (A \or B) \equiv \neg A \and \neg B$ and $\neg (A \and B) \equiv \neg A \or \neg B$).
3. Distribute OR over AND (i.e. $A \or (B \and C) \equiv (A \or B) \and (A \or C)$)



**Example**: Convert $(A \or B) \to (C \to D)$ to CNF

1. Eliminate implications: $\neg (A \or B) \or (\neg C \or D)$

2. Distribute negations: $(\neg A \and \neg B) \or (\neg C \or D)$

3. Distribute OR over AND: 
   $$
   ((\neg A \and \neg B) \or \neg C) \and ((\neg A \and \neg B) \or D)\\
   (\neg A \or \neg C) \and (\neg B \or \neg C) \and (\neg A \or D) \and (\neg B \or D)\\
   $$
   
4. Optionally simplify:
   $$
   ((\neg A \or \neg C) \and (\neg A \or D)) \and ((\neg B \or \neg C) \and (\neg B \or D))\\
   (\neg A \or \neg C \or D) \and (\neg B \or \neg C \or D)
   $$
   

### Theorem proving: resolution refutation

Three steps:

1. Convert all sentences into CNF
2. Negate the desired conclusion
3. Apply [resolution rule](#Resolution) until
   * Derive False (a contradiction)
   * Can't apply the rule any more



Sound and complete for propositional logic

* If we derive a contradiction, the conclusion follows from the axioms
* If we can't apply any more, the conclusion cannot be proved from the axioms



Example: prove the following theorem:
$$
a \or b\\
\neg a \or c\\
\rule{2cm}{0.5pt}\\
b \or c
$$



1. Convert all sentences into CNF (already done)

2. Negate the desired conclusion

   $\neg b \and \neg c$

3. Apply resolution until a contradiction or until we can't any more
   $$
   a \or b\\
   \neg a \or c\\
   \rule{2cm}{0.5pt}\\
   a \or c
   $$
   So we can replace the theorem with
   $$
   a \or c\\
   \rule{2cm}{0.5pt}\\
   b \or c
   $$
   which is a contradiction to what we are trying to prove. Done? I'm confused.