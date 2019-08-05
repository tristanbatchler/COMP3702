# Lecture 1

## Rational Agent
### Definition
A program that has the ability to perceive an environment and produce a rational decision based on that perception.

The environment can also change due to actions the agent has made allowing for a kind of feedback loop.

### The components
* Action space (![A](https://latex.codecogs.com/gif.latex?A))
  * The set of all actions the agent can perform
* Percept space (![P](https://latex.codecogs.com/gif.latex?P))
  * The set of all things the agent can perceive in the world
* State space (![S](https://latex.codecogs.com/gif.latex?S))
  * The set of all possible configurations of the world the agent is operating in
    * i.e. the internal state of the agent and the environment that matters for the interaction between the agent and the environment
* Transition function / World dynamics (![T%3A%20S%20%5Ctimes%20A%20%5Cto%20S](https://latex.codecogs.com/gif.latex?T%3A%20S%20%5Ctimes%20A%20%5Cto%20S))
  * A function that specifies how the configuration of the world changes when the agent performs acts in it
  * This will not be well-defined (i.e. representable by a lookup table)  if the world is non-deterministic.
* Perception function (![Z%3A%20S%20%5Cto%20P](https://latex.codecogs.com/gif.latex?Z%3A%20S%20%5Cto%20P))
  * A function that maps a state to a perception
  * Could be the identity mapping (i.e. "do nothing") if the world is fully-observable and each state is its own percept.
* Utility function (![U%3AS%20%5Cto%20%5Cmathbb%7BR%7D](https://latex.codecogs.com/gif.latex?U%3AS%20%5Cto%20%5Cmathbb%7BR%7D)) 
  * A function that measures of how good a state is.
  * This is required for the agent to gauge whether a certain action is worth performing.

### How to make an agent rational
Our agent should find a mapping from sequences of percepts to actions that maximises the utility function (so that the world state is as good as it can be).
i.e. find a mapping ![M%3AP%5En%20%5Cto%20A](https://latex.codecogs.com/gif.latex?M%3AP%5En%20%5Cto%20A) which maximises ![U](https://latex.codecogs.com/gif.latex?U). 

**Example 1**: Navigate a robot to a point ![P](https://latex.codecogs.com/gif.latex?P). The utility function could be defined to be the negative of how close in the world the robot is to ![P](https://latex.codecogs.com/gif.latex?P). That way, the closer we are to ![P](https://latex.codecogs.com/gif.latex?P), the more positive ![U](https://latex.codecogs.com/gif.latex?U) is.

**Example 2**: Sliding puzzle.

![](https://miro.medium.com/max/1046/1*_n4hcTM-akUEoWL1i05xVg.png)

An agent to solve the sliding puzzle could be defined as ![%28A%2C%20P%2C%20S%2C%20T%2C%20Z%2C%20U%29](https://latex.codecogs.com/gif.latex?%28A%2C%20P%2C%20S%2C%20T%2C%20Z%2C%20U%29) where:
* ![A](https://latex.codecogs.com/gif.latex?A) (the action space) is to move the *empty tile* up, down, left, or right

  * Note: We could define the action space to be moving every tile in each direction (which is the naive approach) however conceptually moving the empty tile is the same thing and is simpler to define

* ![P](https://latex.codecogs.com/gif.latex?P) (the percept space) the order of the tiles

  * e.g. in the image on the left above, the order can be represented as the following string:
    
    ```
    1238_4765
    ```

* ![S](https://latex.codecogs.com/gif.latex?S) (the state space) is the same as the percept space (i.e. ![S](https://latex.codecogs.com/gif.latex?S) = ![P](https://latex.codecogs.com/gif.latex?P)) which is the order of the tiles

* ![T](https://latex.codecogs.com/gif.latex?T) (the transition funciton) is the act of sliding the empty tile in a direction for a particular order and seeing the resulting new order

* ![Z](https://latex.codecogs.com/gif.latex?Z) (the percept function) is the identiy map (i.e. do nothing because the state space is already the percept space).

* ![U](https://latex.codecogs.com/gif.latex?U) (the utility function) ~~could be how many tiles are in the correct position~~

  * ~~Problems with this, since sometimes you have to mess up the order temporarily to get to a better state and this utility function would discourage that~~

  Could be simply 1 for the goal state and 0 for any other state. Let the agent figure it out along the way over a number of different trials.
  
  * In practice, this isn't the approach we would normally go for but this conveys the message well.
  
  

**Example 3:** Tic Tac Toe

* ![A](https://latex.codecogs.com/gif.latex?A) is to place an X or an O at a position on the board, e.g. ![%5C%7B%28S%2C%20i%29%20%5C%2C%20%7C%20%5C%2C%20S%20%5Cin%20%5C%7BX%2C%20O%5C%7D%20%5Cand%20i%20%5Cin%20%5Cmathbb%7BZ%7D_9%5C%7D](https://latex.codecogs.com/gif.latex?%5C%7B%28S%2C%20i%29%20%5C%2C%20%7C%20%5C%2C%20S%20%5Cin%20%5C%7BX%2C%20O%5C%7D%20%5Cand%20i%20%5Cin%20%5Cmathbb%7BZ%7D_9%5C%7D).

* ![P](https://latex.codecogs.com/gif.latex?P) is the order of symbols on the board as a sequence reading top to bottom, left to right, e.g ![%5C%7BX%2C%20O%2C%20O%2C%20%5C_%2C%20%5C_%2C%20X%2C%20O%2C%20X%2C%20%5C_%5C%7D](https://latex.codecogs.com/gif.latex?%5C%7BX%2C%20O%2C%20O%2C%20%5C_%2C%20%5C_%2C%20X%2C%20O%2C%20X%2C%20%5C_%5C%7D) to represent

  ```
  X O O
      X
  O X  
  ```

* ![S%20%3D%20P](https://latex.codecogs.com/gif.latex?S%20%3D%20P)

* ![T](https://latex.codecogs.com/gif.latex?T) is the act of placing a symbol at a position and seeing the resulting new state

* ![Z%20%3D%20I_S%20%5Cbecause%20S%20%3D%20P](https://latex.codecogs.com/gif.latex?Z%20%3D%20I_S%20%5Cbecause%20S%20%3D%20P) 

* ![U](https://latex.codecogs.com/gif.latex?U) could be ![10](https://latex.codecogs.com/gif.latex?10) when the agent makes a straight line, ![-10](https://latex.codecogs.com/gif.latex?-10) when the opponent makes a straight line, and ![0](https://latex.codecogs.com/gif.latex?0) for any other state.



### Challenges and considerations when modelling

Properties about the environment itself or the agent's knowledge about the environment.

* **Discrete** vs. **continuous**
  * Are the state / action / percept spaces discrete or continuous? 
  * In examples 2 and 3, they were discrete.
* **Deterministic** vs. **stochastic / non-deterministic**
  * Does the agent always know exactly which state it will be in after it performs an action from a state?
  * Is the transition function (![T](https://latex.codecogs.com/gif.latex?T)) well-defined?
  * In example 2, yes. Example 3 has to factor in the opponent's turn which is non-deterministic.
* **Fully observable** vs. **partially observable**
  * Does the agent know the state of the world exactly?
  * Is the percept function (![Z](https://latex.codecogs.com/gif.latex?Z)) a bijection (i.e. one-to-one and onto)?
  * If not, ![S%20%5Cneq%20P](https://latex.codecogs.com/gif.latex?S%20%5Cneq%20P) because there will be aspects of the state not perceived by the agent.
* **Static** vs. **dynamic** 
  * Can the world change while the agent is "thinking" (i.e. not acting)?
  * e.g. in a video game, often the world is changing while the player is not acting

