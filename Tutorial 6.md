# Tutorial 6

## Question 1

![1567577447875](.\Images\Tutorial 6\question-1.png)

#### (a) Who is correct, UQPark Management or UQPark Facilities? Please frame this problem as a satisfiability problem with propositional logic representation.

Suppose UQPark Management is correct. Then the following sentence is satisfiable.
$$
S := (B \or C) \and (\neg B \to R) \and (C \to (B \or H)) \and (H \to F) \and \neg (B \and F) \and (R \to F) \and (\neg R \to (H \or F))
$$
We need to convert this to CNF form first before we apply DPLL.
$$
S \equiv (B \or C) \and (B \or R) \and (\neg C \or B \or H) \and (\neg H \or F) \and (\neg B \or \neg F) \and (\neg R \or F) \and (R \or H \or F)
$$
We have no pure variables, so we pick a variable. Heuristically, let's pick the variable with the maximum number of occurrences.

| Variable | Occurrences |
| -------- | ----------- |
| $B$      | 4           |
| $C$      | 2           |
| $R$      | 3           |
| $H$      | 3           |
| $F$      | 4           |

Let's choose $B$. Now we need to run DPLL on
$$
\begin{align*}
S(\neg B) &= (\mathrm{False} \or C) \and (\mathrm{False} \or R) \and (\neg C \or \mathrm{False} \or H) \and (\neg H \or F) \and (\mathrm{True} \or \neg F) \and (\neg R \or F) \and (R \or H \or F)\\
&\equiv (C) \and (R) \and (\neg C \or H) \and (\neg H \or F) \and (\neg R \or F) \and (R \or H \or F)\\
\end{align*}
$$


Now $C$ is a unit clause so we need to run DPLL on
$$
\begin{align*}
(S(\neg B))(C) &= (\mathrm{True}) \and (R) \and (\mathrm{False} \or H) \and (\neg H \or F) \and (\neg R \or F) \and (R \or H \or F)\\
&\equiv (R) \and (H) \and (\neg H \or F) \and (\neg R \or F) \and (R \or H \or F)
\end{align*}
$$
Now $R$ is a unit clause so we need to run DPLL on
$$
\begin{align*}
((S(\neg B))(C))(R) &= (\mathrm{True}) \and (H) \and (\neg H \or F) \and (\mathrm{False} \or F) \and (\mathrm{True} \or H \or F)\\
&\equiv (H) \and (\neg H \or F) \and (F)
\end{align*}
$$
Now $H$ is a unit clause so we need to run DPLL on
$$
\begin{align*}
(((S(\neg B))(C))(R))(H) &= (\mathrm{True}) \and (\mathrm{False} \or F) \and (F)\\
&\equiv (F) \and (F)
\end{align*}
$$
Now $F$ is a unit clause so we need to run DPLL on
$$
\begin{align*}
((((S(\neg B))(C))(R))(H))(F) &= (\mathrm{True}) \and (\mathrm{True})\\
&\equiv (\mathrm{True})
\end{align*}
$$
Now $S$ is empty so we are done and return `True`. Therefore UQPark Management is correct and we can satisfy all the constraints by choosing

* $B := \mathrm{False}$
* $C := \mathrm{True}$
* $R := \mathrm{True}$
* $H := \mathrm{True}$
* $F := \mathrm{True}$

Just to double check, let's do a substitution on our original sentence.
$$
(B \or C) \and (\neg B \to R) \and (C \to (B \or H)) \and (H \to F) \and \neg (B \and F) \and (R \to F) \and (\neg R \to (H \or F))\\
\\
(\mathrm{False} \or \mathrm{True}) \and (\mathrm{True} \to \mathrm{True}) \and (\mathrm{True} \to (\mathrm{False} \or \mathrm{True})) \and (\mathrm{True} \to \mathrm{True}) \and \neg (\mathrm{False} \and \mathrm{True}) \and (\mathrm{True} \to \mathrm{True}) \and (\mathrm{False} \to (\mathrm{True} \or \mathrm{True}))\\

(\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True} \to \mathrm{True}) \and (\mathrm{True}) \and \neg (\mathrm{False}) \and (\mathrm{True}) \and (\mathrm{True})\\

(\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True}) \and (\mathrm{True})\\

(\mathrm{True})
$$


#### (b) Please solve the problem in (a) using DPLL. If both are correct or both are incorrect, please also explain why using DPLL.

Already solved (a) using DPLL. UQPark Management is correct because DPLL returned `True`.



#### (c) Can you answer (a) with GSAT? Please explain why or why not.

We can try.

Again, let $S$ be the following sentence that we already found in (a):
$$
S := (B \or C) \and (B \or R) \and (\neg C \or B \or H) \and (\neg H \or F) \and (\neg B \or \neg F) \and (\neg R \or F) \and (R \or H \or F)
$$


We randomly choose an assignment for all variables:

- $B := \mathrm{True}$
- $C := \mathrm{True}$
- $R := \mathrm{False}$
- $H := \mathrm{False}$
- $F := \mathrm{False}$

$$
(\mathrm{T} \or \mathrm{T}) \and (\mathrm{T} \or \mathrm{\mathrm{F}}) \and (\neg \mathrm{T} \or \mathrm{T} \or \mathrm{F}) \and (\neg \mathrm{F} \or \mathrm{F}) \and (\neg \mathrm{T} \or \neg \mathrm{F}) \and (\neg \mathrm{\mathrm{F}} \or \mathrm{F}) \and (\mathrm{\mathrm{F}} \or \mathrm{F} \or \mathrm{F})
$$



The variable we should choose to flip should be either $R$ or $H$ or $F$ because the last clause ($(R \or H \or F)$) is the only one which is unsatisfiable under this assignment.

After flipping, say, $R$, the assignment becomes 

- $B := \mathrm{True}$
- $C := \mathrm{True}$
- $R := \mathrm{True}$
- $H := \mathrm{False}$
- $F := \mathrm{False}$

$$
(\mathrm{T} \or \mathrm{T}) \and (\mathrm{T} \or \mathrm{\mathrm{F}}) \and (\neg \mathrm{T} \or \mathrm{T} \or \mathrm{F}) \and (\neg \mathrm{F} \or \mathrm{F}) \and (\neg \mathrm{T} \or \neg \mathrm{F}) \and (\neg \mathrm{\mathrm{F}} \or \mathrm{F}) \and (\mathrm{\mathrm{T}} \or \mathrm{F} \or \mathrm{F})
$$

Which has no unsatisfiable clauses so we return `True`.

Therefore, we have answered (a) with GSAT and actually got a different solution.

We didn't really need to try because, if a solution exists, GSAT can find it by guessing it initially.