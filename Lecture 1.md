# Lecture 1
## Rational Agent
### Definition
A program that has the ability to perceive an environment and produce a rational decision based on that perception.

The environment can also change due to actions the agent has made allowing for a kind of feedback loop.

$e=mc^2$

### The components
* Action space ($A$)
  * The set of all actions the agent can perform
* Percept space ($P$)
  * The set of all things the agent can perceive in the world
* State space ($S$)
  * The set of all possible configurations of the world the agent is operating in
    * i.e. the internal state of the agent and the environment that matters for the interaction between the agent and the environment
* Transition function / World dynamics ($T: S \times A \to S$)
  * A function that specifies how the configuration of the world changes when the agent performs acts in it
  * This will not be well-defined (i.e. representable by a lookup table)  if the world is non-deterministic.
* Perception function ($Z: S \to P$)
  * A function that maps a state to a perception
  * Could be the identity mapping (i.e. "do nothing") if the world is fully-observable and each state is its own percept.
* Utility function ($U:S \to \mathbb{R}$) 
  * A function that measures of how good a state is.
  * This is required for the agent to gauge whether a certain action is worth performing.

### How to make an agent rational
Our agent should find a mapping from sequences of percepts to actions that maximises the utility function (so that the world state is as good as it can be).
i.e. find a mapping $M:P^n \to A$ which maximises $U$. 

**Example 1**: Navigate a robot to a point $P$. The utility function could be defined to be the negative of how close in the world the robot is to $P$. That way, the closer we are to $P$, the more positive $U$ is.

**Example 2**: Sliding puzzle.

![](https://miro.medium.com/max/1046/1*_n4hcTM-akUEoWL1i05xVg.png)

An agent to solve the sliding puzzle could be defined as $(A, P, S, T, Z, U)$ where:
* $A$ (the action space) is to move the *empty tile* up, down, left, or right

  * Note: We could define the action space to be moving every tile in each direction (which is the naive approach) however conceptually moving the empty tile is the same thing and is simpler to define

* $P$ (the percept space) the order of the tiles

  * e.g. in the image on the left above, the order can be represented as the following string:
    
    ```
    1238_4765
    ```

* $S$ (the state space) is the same as the percept space (i.e. $S$ = $P$) which is the order of the tiles

* $T$ (the transition funciton) is the act of sliding the empty tile in a direction for a particular order and seeing the resulting new order

* $Z$ (the percept function) is the identiy map (i.e. do nothing because the state space is already the percept space).

* $U$ (the utility function) ~~could be how many tiles are in the correct position~~

  * ~~Problems with this, since sometimes you have to mess up the order temporarily to get to a better state and this utility function would discourage that~~

  Could be simply 1 for the goal state and 0 for any other state. Let the agent figure it out along the way over a number of different trials.
  
  * In practice, this isn't the approach we would normally go for but this conveys the message well.
  
  

**Example 3:** Tic Tac Toe

* $A$ is to place an X or an O at a position on the board, e.g. $\{(S, i) \, | \, S \in \{X, O\} \and i \in \mathbb{Z}_9\}$.

* $P$ is the order of symbols on the board as a sequence reading top to bottom, left to right, e.g $\{X, O, O, \_, \_, X, O, X, \_\}$ to represent

  ```
  X O O
      X
  O X  
  ```

* $S = P$

* $T$ is the act of placing a symbol at a position and seeing the resulting new state

* $Z = I_S \because S = P$ 

* $U$ could be $10$ when the agent makes a straight line, $-10$ when the opponent makes a straight line, and $0$ for any other state.



### Challenges and considerations when modelling

Properties about the environment itself or the agent's knowledge about the environment.

* **Discrete** vs. **continuous**
  * Are the state / action / percept spaces discrete or continuous? 
  * In examples 2 and 3, they were discrete.
* **Deterministic** vs. **stochastic / non-deterministic**
  * Does the agent always know exactly which state it will be in after it performs an action from a state?
  * Is the transition function ($T$) well-defined?
  * In example 2, yes. Example 3 has to factor in the opponent's turn which is non-deterministic.
* **Fully observable** vs. **partially observable**
  * Does the agent know the state of the world exactly?
  * Is the percept function ($Z$) a bijection (i.e. one-to-one and onto)?
  * If not, $S \neq P$ because there will be aspects of the state not perceived by the agent.
* **Static** vs. **dynamic** 
  * Can the world change while the agent is "thinking" (i.e. not acting)?
  * e.g. in a video game, often the world is changing while the player is not acting

