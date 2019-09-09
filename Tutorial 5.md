![1567214802803](.\Images\Tutorial 5\q1.png)

Both are incredibly difficult to solve using uniform random sampling, but problem 2 is harder to solver out of both.

The reason for this is that the $\beta$-lookout of the set of configurations on the left hand side of the obstacles is much bigger in problem 1.

In other words, problem 1 has more bridges to connect the left component to the right component in the resulting PRM.

![1567214836258](.\Images\Tutorial 5\q2.png)

Consider the three possibilities for the clues:

1. $\neg E_A \and \neg E_B \and G_B$ 
2. $\neg E_A \and E_B \and \neg G_B$
3. $E_A \and \neg E_B \and \neg G_B$



In case 1, we have both $A$ and $B$ containing gold which is not possible.

In case 2, we have that $E_B \and \neg G_B$ so the gold is not in $B$ and $\neg E_A$ which means the gold is in $A$.

In case 3, we have the contradiction that $\neg E_B \and \neg G_B$ meaning $B$ contains gold and is empty at the same time, a contradiction.



By process of elimination, we infer the gold is in trunk $A$. The gold cannot be in $C$ because only one trunk can have gold. We have determined $B$ to be empty. 



![1567214836258](.\Images\Tutorial 5\q3.png)

$(A \and B) \models (A \lrarr B)$ is correct because $(A \and B)$ implies $A \lrarr B$ in all models. 



*Proof*
$$
A \and B\\
(A \and B) \or (\neg A \and \neg B)\\
((A \and B) \or \neg A) \and ((A \and B) \or \neg B)\\
(A \or \neg A) \and (B \or \neg A) \and (A \or \neg B) \or (B \or \neg B)\\
(B \or \neg A) \and (A \or \neg B)\\
(\neg A \or B) \and (\neg B \or A)\\
(A \to B) \and (B \to A)\\
A \lrarr B \\\square
$$


![1567214836258](.\Images\Tutorial 5\q4.png)

Two questions:

1. How would we begin using resolution refutation on this? It doesn't appear to be in the correct form to begin the process.
2. Why do we need to use resolution refutation here? Isn't it enough to realise P∧¬P is unsatisfiable for all models and therefore entails every statement by vacuous truth?

