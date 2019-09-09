# Lecture 5

## We don't always need to construct the state graph explicitly

* Build a search tree directly
* **Expansive space tree (EST)**
  * Set the initial configuration as a root node
  * Repeat:
    * Select a node ![q](https://latex.codecogs.com/gif.latex?q) to expand with probability ![1/N%28q%29](https://latex.codecogs.com/gif.latex?1/N%28q%29) where ![N%28q%29](https://latex.codecogs.com/gif.latex?N%28q%29) is the # nodes in the tree that are within ![D](https://latex.codecogs.com/gif.latex?D) distance from ![q](https://latex.codecogs.com/gif.latex?q)
    * Sample a configuration ![q%27](https://latex.codecogs.com/gif.latex?q%27) uniformly at random from all possible configurations within ![D](https://latex.codecogs.com/gif.latex?D) distance from ![q](https://latex.codecogs.com/gif.latex?q)
    * If ![q%27](https://latex.codecogs.com/gif.latex?q%27) is collision-free and the straight line segment between ![q](https://latex.codecogs.com/gif.latex?q) and ![q%27](https://latex.codecogs.com/gif.latex?q%27) is collision-free, add ![q%27](https://latex.codecogs.com/gif.latex?q%27) as a child of ![q](https://latex.codecogs.com/gif.latex?q)
  * Usually bidirectional search
* **Rapidly exploring random trees (RRT)**
  * Set the initial configuration as a root node
  * Repeat
    * Select a configuration ![q](https://latex.codecogs.com/gif.latex?q) uniformly at random from the configuration space
    * Find a node nearest to ![q](https://latex.codecogs.com/gif.latex?q). Suppose this node is ![q%27](https://latex.codecogs.com/gif.latex?q%27).
    * Find a configuration ![q_%7B%5Cmathrm%7Bnew%7D%7D](https://latex.codecogs.com/gif.latex?q_%7B%5Cmathrm%7Bnew%7D%7D) in line segment ![q%27q](https://latex.codecogs.com/gif.latex?q%27q) such that the line segment ![q%27q_%7B%5Cmathrm%7Bnew%7D%7D](https://latex.codecogs.com/gif.latex?q%27q_%7B%5Cmathrm%7Bnew%7D%7D) lies entirely in the free space and the distance between ![q%27](https://latex.codecogs.com/gif.latex?q%27) and ![q_%7B%5Cmathrm%7Bnew%7D%7D](https://latex.codecogs.com/gif.latex?q_%7B%5Cmathrm%7Bnew%7D%7D) is less than ![D](https://latex.codecogs.com/gif.latex?D).
    * Add ![q_%5Cmathrm%7Bnew%7D](https://latex.codecogs.com/gif.latex?q_%5Cmathrm%7Bnew%7D) as a child node of ![q%27](https://latex.codecogs.com/gif.latex?q%27) in the tree.
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

* A configuration ![q](https://latex.codecogs.com/gif.latex?q) "sees" another configuration ![q%27](https://latex.codecogs.com/gif.latex?q%27) whenever the straight line segment between ![q](https://latex.codecogs.com/gif.latex?q) and ![q%27](https://latex.codecogs.com/gif.latex?q%27) lies entirely in the free space. The space of configurations "seen" by the space below is highlighted in orange.

![1566627838611](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%205/c-space-visibility.png)

A relatively small number of vertices and edges are sufficient to cover most free spaces with high probability, and hence solve the given queries.



**Slightly more formally**, the lookout of a subset ![F_1](https://latex.codecogs.com/gif.latex?F_1) of the free space is the set of all configurations in ![F_1](https://latex.codecogs.com/gif.latex?F_1) from which it is possible to "see" a significant fraction of the free space outside ![F_1](https://latex.codecogs.com/gif.latex?F_1).

![1566628085931](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%205/beta-lookout.png)

The ![%5Cbeta%5Cmathrm%7B-lookout%7D%28F_1%29](https://latex.codecogs.com/gif.latex?%5Cbeta%5Cmathrm%7B-lookout%7D%28F_1%29) is the set of configurations in ![F_1](https://latex.codecogs.com/gif.latex?F_1) from which it is possible to "see" ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) fraction of the free space outside ![F_1](https://latex.codecogs.com/gif.latex?F_1).

So the lookout is like a chokepoint/corridor which needs to be sampled before you can access another significant portion of the configuration space.

The free space ![F](https://latex.codecogs.com/gif.latex?F) is expansive if all of its subsets have a large lookout.

![F](https://latex.codecogs.com/gif.latex?F) is ![%5Calpha%5Cbeta](https://latex.codecogs.com/gif.latex?%5Calpha%5Cbeta)-expansive iff. for any connected subset ![F_i%20%5Csubseteq%20F](https://latex.codecogs.com/gif.latex?F_i%20%5Csubseteq%20F) 

* ![%5Cmathrm%7BVolume%7D%28%5Cbeta%5Cmathrm%7B-lookout%7D%28F_i%29%29%20%3D%20%5Calpha](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BVolume%7D%28%5Cbeta%5Cmathrm%7B-lookout%7D%28F_i%29%29%20%3D%20%5Calpha)

So basically, ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) is the volume of the ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta)-lookout of ![F_i](https://latex.codecogs.com/gif.latex?F_i), i.e. the volume of configuration space necessary to "see" ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) fraction of the free space outside of ![F_i](https://latex.codecogs.com/gif.latex?F_i).

The number of samples to capture the correct connectivity of the free space with probability at least ![P](https://latex.codecogs.com/gif.latex?P) is inversely proportional to ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta).

PRM (and its variants) perform well when the free space of the problem has large ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta).

Of the following C-Spaces, the one on the **right** is easiest to solve by sampling-based approaches. This is because the ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) are larger on the right.

![1566628672530](C:\Users\tristan\School\COMP3702\Images\Lecture 5\ab-expansive-illustration.png)

So if we know ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) of the free space, we can compute the number of samples to solve a given problem with high probability.

But, to compute ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta), we need the geometry of the free space.

* PRM is successful exactly because it's **not** computing the geometry of the free space
* Practically, we don't know ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta), nor the exact # of samples to use.

So, why bother?

* Sometimes we can "guess" ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) from the workspace ![%5Cto](https://latex.codecogs.com/gif.latex?%5Cto) known when to use PRM and when not to
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
    * ![x%20%2B%202%20%3D%202x](https://latex.codecogs.com/gif.latex?x%20%2B%202%20%3D%202x) when ![x%20%3D%201](https://latex.codecogs.com/gif.latex?x%20%3D%201) is false
    * "What is the distance between Mars and Earth?" is not propositional

  * Typically denote a proposition as ![p](https://latex.codecogs.com/gif.latex?p) or ![q](https://latex.codecogs.com/gif.latex?q).
* **Complex sentences**

  * Constructed from atomic sentences and logical connectives:

    * Brackets ![%28%29](https://latex.codecogs.com/gif.latex?%28%29), negation ![%5Cneg](https://latex.codecogs.com/gif.latex?%5Cneg), and ![%5Cand](https://latex.codecogs.com/gif.latex?%5Cand), or ![%5Cor](https://latex.codecogs.com/gif.latex?%5Cor), implies, ![%5Cto](https://latex.codecogs.com/gif.latex?%5Cto), iff. ![%5Clrarr](https://latex.codecogs.com/gif.latex?%5Clrarr).
  * If ![S%2C%20S_1%2C%20S_2](https://latex.codecogs.com/gif.latex?S%2C%20S_1%2C%20S_2) are sentences, then so are the following:
    * ![%28S%29](https://latex.codecogs.com/gif.latex?%28S%29)
    * ![%5Cneg%20S](https://latex.codecogs.com/gif.latex?%5Cneg%20S) is true iff. ![S](https://latex.codecogs.com/gif.latex?S) is false
    * ![S_1%20%5Cand%20S_2](https://latex.codecogs.com/gif.latex?S_1%20%5Cand%20S_2) is true iff. ![S_1](https://latex.codecogs.com/gif.latex?S_1) is true or ![S_2](https://latex.codecogs.com/gif.latex?S_2) is true
    * ![S_1%20%5Cor%20S_2](https://latex.codecogs.com/gif.latex?S_1%20%5Cor%20S_2) is true iff. ![S_1](https://latex.codecogs.com/gif.latex?S_1) is true and ![S_2](https://latex.codecogs.com/gif.latex?S_2) is true
    * ![S_1%20%5Cto%20S_2](https://latex.codecogs.com/gif.latex?S_1%20%5Cto%20S_2) is true iff. ![S_2](https://latex.codecogs.com/gif.latex?S_2) is true or ![S_1](https://latex.codecogs.com/gif.latex?S_1) is false (absurd)
    * ![S_1%20%5Clrarr%20S_2](https://latex.codecogs.com/gif.latex?S_1%20%5Clrarr%20S_2) is true iff. ![S_1%20%5Cto%20S_2%20%5Cand%20S_2%20%5Cto%20S1](https://latex.codecogs.com/gif.latex?S_1%20%5Cto%20S_2%20%5Cand%20S_2%20%5Cto%20S1) is true
* **Semantics**
  * Meaning of a sentence: truth values
  * The truth of a complex sentence can be derived from the truth values of logical connectives for the given sentence
  * i.e. truth tables
  * Interpretation: Assignment of truth values to propositional variables



### Some terminology

* A sentence is **valid** if it's true for all possible interpretations, i.e. **tautology**
* A sentence is **satisfiable** if its truth value is T for at least one of the possible interpretations

  * e.g. ![%5Cneg%20P](https://latex.codecogs.com/gif.latex?%5Cneg%20P).
  * Everything that's valid is satisfiable
* A sentence is unsatisfiable if its truth value is F for all possible interpretations

  * e.g. ![P%20%5Cand%20%5Cneg%20P](https://latex.codecogs.com/gif.latex?P%20%5Cand%20%5Cneg%20P)
* For propositional logic, we can always decide if a sentence is valid/satisfiable/unsatisfiable in finite time (decidable)
* A **model** of a sentence is an interpretation that makes the sentence true
* A sentence ![A](https://latex.codecogs.com/gif.latex?A) **entails** another sentence ![B](https://latex.codecogs.com/gif.latex?B) (denoted ![A%20%5Cmodels%20B](https://latex.codecogs.com/gif.latex?A%20%5Cmodels%20B)) iff. every model of ![A](https://latex.codecogs.com/gif.latex?A) is also a model of ![B](https://latex.codecogs.com/gif.latex?B) (![A%20%5Cto%20B](https://latex.codecogs.com/gif.latex?A%20%5Cto%20B) is valid)

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
  
    ![1567204910509](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%205/representing-wumpus-world-problem.png)
  
    Results of perception up to the current time can be added to the KB.
  
    E.g. Suppose the agent has only visited ![%281%2C%201%29](https://latex.codecogs.com/gif.latex?%281%2C%201%29) and perceives:
  
    * ![P_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?P_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D), ![B_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?B_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D), ![W_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?W_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D), ![S_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?S_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D), ![%5Cmathrm%7BGo%7D_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BGo%7D_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D), ![G_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D](https://latex.codecogs.com/gif.latex?G_%7B1%2C%201%7D%20%3D%20%5Cmathrm%7BFalse%7D)
    * Then we can add the following sentences to the initial KB:
      * ![%5Cneg%20P_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20P_%7B1%2C%201%7D), ![%5Cneg%20B_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20B_%7B1%2C%201%7D), ![%5Cneg%20W_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20W_%7B1%2C%201%7D), ![%5Cneg%20S_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20S_%7B1%2C%201%7D), ![%5Cneg%20%5Cmathrm%7BGo%7D_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20%5Cmathrm%7BGo%7D_%7B1%2C%201%7D), ![%5Cneg%20G_%7B1%2C%201%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20G_%7B1%2C%201%7D), 
  
    What else can we use the KB for?
  
    * Deduce new information, sentences entailed by the current KB can be added to the KB
    * Answering questions such as can we conclude there's no pit in ![%281%2C%202%29](https://latex.codecogs.com/gif.latex?%281%2C%202%29)?
    * Formally,
      * Given the knowledge base ![%5Cmathrm%7BKB%7D%20%3A%3D%20S_1%2C%20S_2%2C%20%5Ccdots%2C%20S_n](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BKB%7D%20%3A%3D%20S_1%2C%20S_2%2C%20%5Ccdots%2C%20S_n):
        * Does KB entail that ![%5Cneg%20P_%7B1%2C%202%7D](https://latex.codecogs.com/gif.latex?%5Cneg%20P_%7B1%2C%202%7D)? i.e. does ![%5Cmathrm%7BKB%7D%20%5Cmodels%20P_%7B1%2C2%7D](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BKB%7D%20%5Cmodels%20P_%7B1%2C2%7D)?
        * In other words, is the sentence valid? ![S_1%20%5Cand%20S_2%20%5Cand%20%5Ccdots%20%5Cand%20S_n%20%5Cto%20%5Cneg%20P_%7B1%2C2%7D](https://latex.codecogs.com/gif.latex?S_1%20%5Cand%20S_2%20%5Cand%20%5Ccdots%20%5Cand%20S_n%20%5Cto%20%5Cneg%20P_%7B1%2C2%7D)



### (Simple) model checking

When checking if a sentence is valid, you must check if it is valid in all models.

A simple way to check this is to enumerate all the models and make a truth table.

#### Model checking terminology

* Sound: the result is correct
* Complete: It always gives an answer
* Complexity: Time, Space in ![O%28f%28n%29%29](https://latex.codecogs.com/gif.latex?O%28f%28n%29%29) where ![n](https://latex.codecogs.com/gif.latex?n) is the number of propositional variables.

### Theorem proving

If ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) are sentences, then two sentences are logically equivalent iff. true in the same models:

![%5Calpha%20%5Cequiv%5Cbeta%20%5Clrarr%20%5Calpha%20%5Cmodels%20%5Cbeta%20%5Cand%20%5Cbeta%20%5Cmodels%5C%20%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cequiv%5Cbeta%20%5Clrarr%20%5Calpha%20%5Cmodels%20%5Cbeta%20%5Cand%20%5Cbeta%20%5Cmodels%5C%20%5Calpha)

Can use the following rules to show logical equivalences using the axioms

![1567205673321](https://raw.githubusercontent.com/tristanbatchler/COMP3702/master/Images/Lecture%205/logical-equivalences.png)

### Inference rules

* Modus ponens (mode that affirms)

  * ![%5Calpha%20%5Cto%20%5Cbeta](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cto%20%5Cbeta) says that, if ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) then ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) can be inferred

  * Proof by implication

![%20%20%20%20%5Calpha%20%5Cto%20%5Cbeta%5C%5C%20%5Calpha%5C%5C%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%20%5Cbeta%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Calpha%20%5Cto%20%5Cbeta%5C%5C%20%5Calpha%5C%5C%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%20%5Cbeta%0A)
* Modus tollens (model that denies)

  * ![%5Calpha%20%5Cto%20%5Cbeta](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cto%20%5Cbeta) says that, if ![%5Cneg%20%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cneg%20%5Cbeta) then ![%5Cneg%20%5Calpha](https://latex.codecogs.com/gif.latex?%5Cneg%20%5Calpha) can be inferred

  * i.e. ![%5Calpha%20%5Cto%20%5Cbeta%20%5Cequiv%20%5Cneg%20%5Calpha%20%5Cto%20%5Cneg%20%5Cbeta](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cto%20%5Cbeta%20%5Cequiv%20%5Cneg%20%5Calpha%20%5Cto%20%5Cneg%20%5Cbeta).

  * Proof by contraposition

![%20%20%20%20%5Calpha%20%5Cto%20%5Cbeta%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Calpha%20%5Cto%20%5Cbeta%5C%5C%0A)![%20%20%20%20%5Cneg%20%5Cbeta%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Cneg%20%5Cbeta%5C%5C%0A)![%20%20%20%20%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%0A)![%20%20%20%20%5Cneg%20%5Calpha%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Cneg%20%5Calpha%0A)
* And-elimination (for a conjunction, any of the conjuncts can be inferred)

  * ![%5Calpha%20%5Cand%20%5Cbeta](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cand%20%5Cbeta) says that ![%5Calpha](https://latex.codecogs.com/gif.latex?%5Calpha) can be inferred and ![%5Cbeta](https://latex.codecogs.com/gif.latex?%5Cbeta) can be inferred

![%20%20%20%20%5Calpha%20%5Cand%20%5Cbeta%5C%5C%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%20%5Calpha%0A](https://latex.codecogs.com/gif.latex?%20%20%20%20%5Calpha%20%5Cand%20%5Cbeta%5C%5C%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%20%5Calpha%0A)


### Theorem proving: natural deduction

Use the rules available to make logical steps to arrive to a new conclusion



### Theorem proving as a search problem

* ![S](https://latex.codecogs.com/gif.latex?S): all possible sets of sentences (knowledge bases)
* ![A](https://latex.codecogs.com/gif.latex?A): the set of all inference rules
* ![T%3AS%20%5Cto%20S](https://latex.codecogs.com/gif.latex?T%3AS%20%5Cto%20S): The act of applying an inference rule to all sentences in the knowledge base that match the form of the inference and seeing the resulting new sentences that is the inference made.
* Initial state: initial knowledge base
* Goal state: the state that contains the sentence we're trying to prove



### Resolution

A single inference rule
![%5Calpha%20%5Cor%20%5Cbeta%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cor%20%5Cbeta%5C%5C%0A)![%5Cneg%20%5Cbeta%20%5Cor%20%5Cgamma%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Cneg%20%5Cbeta%20%5Cor%20%5Cgamma%5C%5C%0A)![%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Crule%7B2cm%7D%7B0.4pt%7D%5C%5C%0A)![%5Calpha%20%5Cor%20%5Cgamma%0A](https://latex.codecogs.com/gif.latex?%5Calpha%20%5Cor%20%5Cgamma%0A)But, the single inference rule is sound and complete only when applied to logical sentences written in Conjunctive Normal Form (**CNF**).

### Conjunctive Normal Form (CNF)

Conjunctions of disjunctions

e.g. ![%28%5Cneg%20A%20%5Cor%20B%29%20%5Cand%20%28C%20%5Cor%20D%29](https://latex.codecogs.com/gif.latex?%28%5Cneg%20A%20%5Cor%20B%29%20%5Cand%20%28C%20%5Cor%20D%29).

Some terminology:

* **Clause**: a disjunction of literals e.g. ![%28%5Cneg%20A%20%5Cor%20B%29](https://latex.codecogs.com/gif.latex?%28%5Cneg%20A%20%5Cor%20B%29)
* **Literals**: variables or the negation of variables, e.g. ![%5Cneg%20A](https://latex.codecogs.com/gif.latex?%5Cneg%20A), ![B](https://latex.codecogs.com/gif.latex?B)

CNF if useful for model checking.

### Converting to CNF

Every sentence in propositional logic can be written in CNF.

Three step conversion:

1. Eliminate implications using definitions (i.e.. ![A%20%5Cto%20B%20%5Cequiv%20%5Cneg%20A%20%5Cor%20B](https://latex.codecogs.com/gif.latex?A%20%5Cto%20B%20%5Cequiv%20%5Cneg%20A%20%5Cor%20B))
2. Distribute negations using De Morgan's Laws (i.e. ![%5Cneg%20%28A%20%5Cor%20B%29%20%5Cequiv%20%5Cneg%20A%20%5Cand%20%5Cneg%20B](https://latex.codecogs.com/gif.latex?%5Cneg%20%28A%20%5Cor%20B%29%20%5Cequiv%20%5Cneg%20A%20%5Cand%20%5Cneg%20B) and ![%5Cneg%20%28A%20%5Cand%20B%29%20%5Cequiv%20%5Cneg%20A%20%5Cor%20%5Cneg%20B](https://latex.codecogs.com/gif.latex?%5Cneg%20%28A%20%5Cand%20B%29%20%5Cequiv%20%5Cneg%20A%20%5Cor%20%5Cneg%20B)).
3. Distribute OR over AND (i.e. ![A%20%5Cor%20%28B%20%5Cand%20C%29%20%5Cequiv%20%28A%20%5Cor%20B%29%20%5Cand%20%28A%20%5Cor%20C%29](https://latex.codecogs.com/gif.latex?A%20%5Cor%20%28B%20%5Cand%20C%29%20%5Cequiv%20%28A%20%5Cor%20B%29%20%5Cand%20%28A%20%5Cor%20C%29))



**Example**: Convert ![%28A%20%5Cor%20B%29%20%5Cto%20%28C%20%5Cto%20D%29](https://latex.codecogs.com/gif.latex?%28A%20%5Cor%20B%29%20%5Cto%20%28C%20%5Cto%20D%29) to CNF

1. Eliminate implications: ![%5Cneg%20%28A%20%5Cor%20B%29%20%5Cor%20%28%5Cneg%20C%20%5Cor%20D%29](https://latex.codecogs.com/gif.latex?%5Cneg%20%28A%20%5Cor%20B%29%20%5Cor%20%28%5Cneg%20C%20%5Cor%20D%29)

2. Distribute negations: ![%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20%28%5Cneg%20C%20%5Cor%20D%29](https://latex.codecogs.com/gif.latex?%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20%28%5Cneg%20C%20%5Cor%20D%29)

3. Distribute OR over AND: 
![%20%20%20%28%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20D%29%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%28%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%28%5Cneg%20A%20%5Cand%20%5Cneg%20B%29%20%5Cor%20D%29%5C%5C%0A)![%20%20%20%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20A%20%5Cor%20D%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20D%29%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20A%20%5Cor%20D%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20D%29%5C%5C%0A)   
4. Optionally simplify:
![%20%20%20%28%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20A%20%5Cor%20D%29%29%20%5Cand%20%28%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20D%29%29%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%28%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20A%20%5Cor%20D%29%29%20%5Cand%20%28%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20D%29%29%5C%5C%0A)![%20%20%20%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%20%5Cor%20D%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%20%5Cor%20D%29%0A](https://latex.codecogs.com/gif.latex?%20%20%20%28%5Cneg%20A%20%5Cor%20%5Cneg%20C%20%5Cor%20D%29%20%5Cand%20%28%5Cneg%20B%20%5Cor%20%5Cneg%20C%20%5Cor%20D%29%0A)   

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
![a%20%5Cor%20b%5C%5C%0A](https://latex.codecogs.com/gif.latex?a%20%5Cor%20b%5C%5C%0A)![%5Cneg%20a%20%5Cor%20c%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Cneg%20a%20%5Cor%20c%5C%5C%0A)![%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A)![b%20%5Cor%20c%0A](https://latex.codecogs.com/gif.latex?b%20%5Cor%20c%0A)


1. Convert all sentences into CNF (already done)

2. Negate the desired conclusion

   ![%5Cneg%20b%20%5Cand%20%5Cneg%20c](https://latex.codecogs.com/gif.latex?%5Cneg%20b%20%5Cand%20%5Cneg%20c)

3. Apply resolution until a contradiction or until we can't any more
![%20%20%20a%20%5Cor%20b%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20a%20%5Cor%20b%5C%5C%0A)![%20%20%20%5Cneg%20a%20%5Cor%20c%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%5Cneg%20a%20%5Cor%20c%5C%5C%0A)![%20%20%20%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A)![%20%20%20a%20%5Cor%20c%0A](https://latex.codecogs.com/gif.latex?%20%20%20a%20%5Cor%20c%0A)   So we can replace the theorem with
![%20%20%20a%20%5Cor%20c%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20a%20%5Cor%20c%5C%5C%0A)![%20%20%20%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A](https://latex.codecogs.com/gif.latex?%20%20%20%5Crule%7B2cm%7D%7B0.5pt%7D%5C%5C%0A)![%20%20%20b%20%5Cor%20c%0A](https://latex.codecogs.com/gif.latex?%20%20%20b%20%5Cor%20c%0A)   which is a contradiction to what we are trying to prove. Done? I'm confused.