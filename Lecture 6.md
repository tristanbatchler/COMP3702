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
      * Variables $X_1, ..., X_n$ where the domain for the variables are $D_1, ..., D_n$ respectively
      * Constraints $C_1, ..., C_n$, where each constraint defines a subset of valid combinations of the values for the variables...
    * Find:
      * A value for each variable such that all constraints are satisfied (the solution)
  * Boolean satisfiability is CSP where the variables are binary, each $D_1$ to $D_n$ are the same, i.e. True or False.
    * Some methods for Boolean satisfiability can be extended to CSP.



### Model checking for satisfiability problem (SAT solvers)

#### 1. Assign & Simplify

* Consider a search tree where at each level we consider the possible assignments to one variable, say $V$.
* On one branch, we assume $V$ is False and on the other that it is True.
* Given an assignment for a variable, we can simplify the sentence and then repeat the process for another variable.
* E.g. [David Putnam Logemann Loveland (DPLL)](#DPLL)

#### 2. Random assignment of all variables in the sentence



### DPLL

* Gives an ordering of which variables to check first
* `def` `DPLL`$(\mathrm{Sentence} \, S)$
  * If $S$ is empty, return `True`
  * If $S$ has an empty clause, return `False`
  * If $S$ has a unit clause $U$, return `DPLL`$(S(U))$.
    * **Unit clause**: consists of only 1 unassigned literal
    * **$S(U)$** means a simplified $S$ after a value is assigned to $U$
  * If $S$ has a pure clause $U$, return `DPLL`$(S(U))$
    * **Pure variable**: appears as positive only or negative only in $S$
  * Pick a variable $v$.
    * If `DPLL`$(S(v))$ is `True`, then return `True`; otherwise return `DPLL`$(S(\neg v))$
    * Heuristics to pick the variable: Max #occurrences, Min size clauses. Basically, pick the most constrained variable first (if it's going to fail, better fail early).



### DPLL Worked Example

Can we find an assignment of the values of the following sentences so that the overall outcome is True?



1. Let $S := (A \or B) \and (\neg C \or A) \and (C \or B)$

   * $S$ is not empty, so continue
   * $S$ has no empty clauses, so continue
   * $S$ has no unit clauses, so continue
   * $S$ has a pure clause: $A$ is always positive and $B$ is always positive so $A$ and $B$ are pure clauses of $S$.
     * We need to run `DPLL`$(S(A))$ (choice of $A$ over $B$ is arbitrary as far as I can tell)
     * Set $A := \mathrm{True}$ so that $S = (\mathrm{True} \or B) \and (\neg C \or \mathrm{True}) \and (C \or B) \equiv \mathrm{True} \and \mathrm{True} \and (C \or B) \equiv (C \or B)$.
       * $S$ is not empty, so continue
       * $S$ has no empty clauses, so continue
       * $S$ has no unit clauses, so continue
       * $S$ has a pure clause: $C$ is always positive and $B$ is always positive so $C$ and $B$ are pure clauses of $S$.
         * We need to run `DPLL`$(S(C))$ (choice of $C$ over $B$ is arbitrary as far as I can tell)
         * Set $C := \mathrm{True}$ so that $S = (\mathrm{True} \or B) \equiv \mathrm{True}$.
           * $S$ is empty (?) so return `True`.

   Slightly confusing but the point is we could get $S$ to be true by setting $A$ and $C$ to be $\mathrm{True}$,

2. Let $S := (P \or Q) \and (P \or \neg Q \or R) \and (T \or \neg R) \and (\neg P \or \neg T) \and (P \or S) \and (T \or R \or S) \and (\neg S \or T)$

   * 