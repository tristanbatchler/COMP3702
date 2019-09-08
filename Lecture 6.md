# Lecture 6

## Satisfiability Problems

* Is a given sentence satisfiable?
  * There is at least one interpretation that makes the sentence be True
* Various applications
  * Many problems can be phrased as a list of constraints, and a solution is an assignment that satisfies all constraint
    * e.g. Two airplanes are allowed on the runway at one time, etc.
  * Verify air-traffic controller
    * Write rules as a set of logical sentences
    * Check whether the set of sentences and the sentence "two airplanes on the runway at one time" is satisfiable?
    * When "the rules are followed and two airplanes on the runway at one time" is unsatisfiable: **danger** :scream:.
* Satisfiability for propositional logic (also called Boolean satisfiability) is a particular type of **Constraint Satisfaction Problem** (CSP).
  * Seen in optimisation theory
  * E.g. of CSP:
    * Given:
      * Variables ![X_1%2C%20...%2C%20X_n](https://latex.codecogs.com/gif.latex?X_1%2C%20...%2C%20X_n) where the domain for the variables are ![D_1%2C%20...%2C%20D_n](https://latex.codecogs.com/gif.latex?D_1%2C%20...%2C%20D_n) respectively
      * Constraints ![C_1%2C%20...%2C%20C_n](https://latex.codecogs.com/gif.latex?C_1%2C%20...%2C%20C_n), where each constraint defines a subset of valid combinations of the values for the variables...
    * Find:
      * A value for each variable such that all constraints are satisfied (the solution)
  * Boolean satisfiability is CSP where the variables are binary, each ![D_1](https://latex.codecogs.com/gif.latex?D_1) to ![D_n](https://latex.codecogs.com/gif.latex?D_n) are the same, i.e. True or False.
    * Some methods for Boolean satisfiability can be extended to CSP.



### Model checking for satisfiability problem (SAT solvers)

#### 1. Assign & Simplify

* Consider a search tree where at each level we consider the possible assignments to one variable, say ![V](https://latex.codecogs.com/gif.latex?V).
* On one branch, we assume ![V](https://latex.codecogs.com/gif.latex?V) is False and on the other that it is True.
* Given an assignment for a variable, we can simplify the sentence and then repeat the process for another variable.
* E.g. [David Putnam Logemann Loveland (DPLL)](#DPLL)

#### 2. Random assignment of all variables in the sentence

* E.g. [GSAT](#GSAT)



### DPLL

* Gives an ordering of which variables to check first
* `def` `DPLL`![%28%5Cmathrm%7BSentence%7D%20%5C%2C%20S%29](https://latex.codecogs.com/gif.latex?%28%5Cmathrm%7BSentence%7D%20%5C%2C%20S%29)
  * If ![S](https://latex.codecogs.com/gif.latex?S) is empty, return `True`
  * If ![S](https://latex.codecogs.com/gif.latex?S) has an empty clause, return `False`
  * If ![S](https://latex.codecogs.com/gif.latex?S) has a unit clause ![U](https://latex.codecogs.com/gif.latex?U), return `DPLL`![%28S%28U%29%29](https://latex.codecogs.com/gif.latex?%28S%28U%29%29).
    * **Unit clause**: consists of only 1 unassigned literal
    * **![S%28U%29](https://latex.codecogs.com/gif.latex?S%28U%29)** means a simplified ![S](https://latex.codecogs.com/gif.latex?S) after a value is assigned to ![U](https://latex.codecogs.com/gif.latex?U)
  * If ![S](https://latex.codecogs.com/gif.latex?S) has a pure clause ![U](https://latex.codecogs.com/gif.latex?U), return `DPLL`![%28S%28U%29%29](https://latex.codecogs.com/gif.latex?%28S%28U%29%29)
    * **Pure variable**: appears as positive only or negative only in ![S](https://latex.codecogs.com/gif.latex?S)
  * Pick a variable ![v](https://latex.codecogs.com/gif.latex?v).
    * If `DPLL`![%28S%28v%29%29](https://latex.codecogs.com/gif.latex?%28S%28v%29%29) is `True`, then return `True`; otherwise return `DPLL`![%28S%28%5Cneg%20v%29%29](https://latex.codecogs.com/gif.latex?%28S%28%5Cneg%20v%29%29)
    * Heuristics to pick the variable: Max #occurrences, Min size clauses. Basically, pick the most constrained variable first (if it's going to fail, better fail early).



### DPLL Worked Example

Can we find an assignment of the values of the following sentences so that the overall outcome is True?



1. Let ![S%20%3A%3D%20%28A%20%5Cor%20B%29%20%5Cand%20%28%5Cneg%20C%20%5Cor%20A%29%20%5Cand%20%28C%20%5Cor%20B%29](https://latex.codecogs.com/gif.latex?S%20%3A%3D%20%28A%20%5Cor%20B%29%20%5Cand%20%28%5Cneg%20C%20%5Cor%20A%29%20%5Cand%20%28C%20%5Cor%20B%29)

   * ![S](https://latex.codecogs.com/gif.latex?S) is not empty, so continue
   * ![S](https://latex.codecogs.com/gif.latex?S) has no empty clauses, so continue
   * ![S](https://latex.codecogs.com/gif.latex?S) has no unit clauses, so continue
   * ![S](https://latex.codecogs.com/gif.latex?S) has a pure clause: ![A](https://latex.codecogs.com/gif.latex?A) is always positive and ![B](https://latex.codecogs.com/gif.latex?B) is always positive so ![A](https://latex.codecogs.com/gif.latex?A) and ![B](https://latex.codecogs.com/gif.latex?B) are pure clauses of ![S](https://latex.codecogs.com/gif.latex?S).
     * We need to run `DPLL`![%28S%28A%29%29](https://latex.codecogs.com/gif.latex?%28S%28A%29%29) (choice of ![A](https://latex.codecogs.com/gif.latex?A) over ![B](https://latex.codecogs.com/gif.latex?B) is arbitrary as far as I can tell)
     * Set ![A%20%3A%3D%20%5Cmathrm%7BTrue%7D](https://latex.codecogs.com/gif.latex?A%20%3A%3D%20%5Cmathrm%7BTrue%7D) so that ![S%20%3D%20%28%5Cmathrm%7BTrue%7D%20%5Cor%20B%29%20%5Cand%20%28%5Cneg%20C%20%5Cor%20%5Cmathrm%7BTrue%7D%29%20%5Cand%20%28C%20%5Cor%20B%29%20%5Cequiv%20%5Cmathrm%7BTrue%7D%20%5Cand%20%5Cmathrm%7BTrue%7D%20%5Cand%20%28C%20%5Cor%20B%29%20%5Cequiv%20%28C%20%5Cor%20B%29](https://latex.codecogs.com/gif.latex?S%20%3D%20%28%5Cmathrm%7BTrue%7D%20%5Cor%20B%29%20%5Cand%20%28%5Cneg%20C%20%5Cor%20%5Cmathrm%7BTrue%7D%29%20%5Cand%20%28C%20%5Cor%20B%29%20%5Cequiv%20%5Cmathrm%7BTrue%7D%20%5Cand%20%5Cmathrm%7BTrue%7D%20%5Cand%20%28C%20%5Cor%20B%29%20%5Cequiv%20%28C%20%5Cor%20B%29).
       * ![S](https://latex.codecogs.com/gif.latex?S) is not empty, so continue
       * ![S](https://latex.codecogs.com/gif.latex?S) has no empty clauses, so continue
       * ![S](https://latex.codecogs.com/gif.latex?S) has no unit clauses, so continue
       * ![S](https://latex.codecogs.com/gif.latex?S) has a pure clause: ![C](https://latex.codecogs.com/gif.latex?C) is always positive and ![B](https://latex.codecogs.com/gif.latex?B) is always positive so ![C](https://latex.codecogs.com/gif.latex?C) and ![B](https://latex.codecogs.com/gif.latex?B) are pure clauses of ![S](https://latex.codecogs.com/gif.latex?S).
         * We need to run `DPLL`![%28S%28C%29%29](https://latex.codecogs.com/gif.latex?%28S%28C%29%29) (choice of ![C](https://latex.codecogs.com/gif.latex?C) over ![B](https://latex.codecogs.com/gif.latex?B) is arbitrary as far as I can tell)
         * Set ![C%20%3A%3D%20%5Cmathrm%7BTrue%7D](https://latex.codecogs.com/gif.latex?C%20%3A%3D%20%5Cmathrm%7BTrue%7D) so that ![S%20%3D%20%28%5Cmathrm%7BTrue%7D%20%5Cor%20B%29%20%5Cequiv%20%5Cmathrm%7BTrue%7D](https://latex.codecogs.com/gif.latex?S%20%3D%20%28%5Cmathrm%7BTrue%7D%20%5Cor%20B%29%20%5Cequiv%20%5Cmathrm%7BTrue%7D).
           * ![S](https://latex.codecogs.com/gif.latex?S) is empty (?) so return `True`.

   Slightly confusing but the point is we could get ![S](https://latex.codecogs.com/gif.latex?S) to be true by setting ![A](https://latex.codecogs.com/gif.latex?A) and ![C](https://latex.codecogs.com/gif.latex?C) to be ![%5Cmathrm%7BTrue%7D](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BTrue%7D),

2. Let ![S%20%3A%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28T%20%5Cor%20%5Cneg%20R%29%20%5Cand%20%28%5Cneg%20P%20%5Cor%20%5Cneg%20T%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28T%20%5Cor%20R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%20%5Cor%20T%29](https://latex.codecogs.com/gif.latex?S%20%3A%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28T%20%5Cor%20%5Cneg%20R%29%20%5Cand%20%28%5Cneg%20P%20%5Cor%20%5Cneg%20T%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28T%20%5Cor%20R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%20%5Cor%20T%29)

   * ![S](https://latex.codecogs.com/gif.latex?S) has no empty, unit, or pure clauses, so choose the variable that has the most occurrences, ![T](https://latex.codecogs.com/gif.latex?T) and run DPLL on:
     ![S%28%5Cneg%20T%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20%5Cneg%20R%29%20%5Cand%20%28%5Cneg%20P%20%5Cor%20%5Cneg%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%20%5Cor%20%5Cmathrm%7BF%7D%29](https://latex.codecogs.com/gif.latex?S%28%5Cneg%20T%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20%5Cneg%20R%29%20%5Cand%20%28%5Cneg%20P%20%5Cor%20%5Cneg%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%20%5Cor%20%5Cmathrm%7BF%7D%29)
   
     Simplified:
     ![S%28%5Cneg%20T%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28%5Cneg%20R%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%29](https://latex.codecogs.com/gif.latex?S%28%5Cneg%20T%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20R%29%20%5Cand%20%28%5Cneg%20R%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28R%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%29)
   
   * ![%5Cneg%20R](https://latex.codecogs.com/gif.latex?%5Cneg%20R) is a unit clause of ![S%28%5Cneg%20T%29](https://latex.codecogs.com/gif.latex?S%28%5Cneg%20T%29), so run DPLL on:
     ![%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28%5Cneg%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%29](https://latex.codecogs.com/gif.latex?%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%20%5Cor%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28%5Cneg%20%5Cmathrm%7BF%7D%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%20%5Cor%20S%29%20%5Cand%20%28%5Cneg%20S%29)
     Simplified:
     ![%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28S%29%20%5Cand%20%28%5Cneg%20S%29](https://latex.codecogs.com/gif.latex?%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28S%29%20%5Cand%20%28%5Cneg%20S%29)
   
   * ![S](https://latex.codecogs.com/gif.latex?S) is a unit clause of ![%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29](https://latex.codecogs.com/gif.latex?%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29), so run DPLL on:
   
     ![%28%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%29%28S%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BT%7D%29%20%5Cand%20%28%5Cneg%20%5Cmathrm%7BT%7D%29](https://latex.codecogs.com/gif.latex?%28%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%29%28S%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BT%7D%29%20%5Cand%20%28%5Cneg%20%5Cmathrm%7BT%7D%29)
     Simplified:
     ![%28%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%29%28S%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%29](https://latex.codecogs.com/gif.latex?%28%28S%28%5Cneg%20T%29%29%28%5Cneg%20R%29%29%28S%29%20%3D%20%28P%20%5Cor%20Q%29%20%5Cand%20%28P%20%5Cor%20%5Cneg%20Q%29%20%5Cand%20%28P%20%5Cor%20S%29%20%5Cand%20%28%5Cmathrm%7BF%7D%29)
   
   * One of the clauses is unsatisfiable, so return `False`.

### DPLL Algorithm Analysis

DPLL is:

* Sound (the result is correct)
* Complete (it always gives an answer)
* Speed & memory consumption depends a lot on:
  * Which symbol is being assigned first
  * Which assignment is being followed first
  * A lot of methods have been proposed



### GSAT

* `GSAT`![%28%5Cmathrm%7BSentence%7D%20%5C%2C%20S%29](https://latex.codecogs.com/gif.latex?%28%5Cmathrm%7BSentence%7D%20%5C%2C%20S%29)

  * Loop ![n](https://latex.codecogs.com/gif.latex?n) times

    * Randomly choose assignment for all variables, say ![A](https://latex.codecogs.com/gif.latex?A)

    * Loop ![m](https://latex.codecogs.com/gif.latex?m) times

      * Flip the variables that results in lowest cost

        ![%5Cmathrm%7BCost%7D%28A%29%20%3A%3D%20](https://latex.codecogs.com/gif.latex?%5Cmathrm%7BCost%7D%28A%29%20%3A%3D%20) #unsatisfied clauses

        So, i.e. flip the variables that results in lowest number of unsatisfied clauses

      * Return `True` if cost is ![0](https://latex.codecogs.com/gif.latex?0), i.e. there are no unsatisfied clauses.



### GSAT Algorithm Analysis

GSAT is:

* Sound (the result is correct)
* **Not** complete (it doesn't always give an answer)
* Cannot be used to generate **all** satisfiable assignments.



### DPLL vs. GSAT

For a moment, GSAT performs much better than DPLL.

Now,

| Problem Type                                                 | DPLL             | GSAT             |
| ------------------------------------------------------------ | ---------------- | ---------------- |
| Weakly constrained problems (large proportion of the assignments is satisfiable) | :ok_hand:        | :ok_hand:        |
| Highly constrained problems (very few satisfiable assignments, sometimes only 1) | :ok_hand:        | :nauseated_face: |
| Problems in the middle                                       | :nauseated_face: | :nauseated_face: |



---------

## Uncertainty

### Causes of uncertainty

#### System noise & errors

* Control error or disturbances from external forces
  * Effect of performing an action is non-deterministric
* Errors in sensing and in process of sensing data
  * Imperfect observation about the world (partially observable)
* Example: 
  * a boat trying to navigate rough waters

#### Too complex to model

* Lazy, e.g. rolling a dice in a casino depends on wind direction from air conditioning, number of people around the table
* Deliberate, to reduce computational complexity. We want to eliminate variables that will not affect the solution significantly.
* Accidental error, e.g. lack of understanding of the problem



#### Abstraction that may lead to modelling error

* The actual possible states of often too large
* Simplify, so it's solvable by current computing power
* But, in general, simplification means clustering several actual states the same
  * i.e. a state in our model corresponds to a set of similar states in the real problem
* Similarly with action space
* Usually bounded uncertainty



### Making decisions

* We want to find a plan that works regardless of what outcomes actually occur

* Can no longer rely on a sequence of actions

* Need a **conditional path**

  * The action to perform depends on the output of the previous action

    Need a different type of tree data structure.



### AND-OR search tree

* A tree with interleaving AND and OR levels
* At each node of an OR level, branching is introduced by the agent's own choice
* At each node of an AND level, branching is introduced by the environment