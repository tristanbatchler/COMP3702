# Lecture 1

## Rational Agent
### Definition
A program that has the ability to perceive an environment and produce a rational decision based on that perception.

The environment can also change due to actions the agent has made allowing for a kind of feedback loop.

### The components
* Action space (<img src="https://latex.codecogs.com/gif.latex\?%24A%24" />)
  * The set of all actions the agent can perform
* Percept space (<img src="https://latex.codecogs.com/gif.latex\?%24P%24" />)
  * The set of all things the agent can perceive in the world
* State space (<img src="https://latex.codecogs.com/gif.latex\?%24S%24" />)
  * The set of all possible configurations of the world the agent is operating in
    * i.e. the internal state of the agent and the environment that matters for the interaction between the agent and the environment
* Transition function / World dynamics (<img src="https://latex.codecogs.com/gif.latex\?%24T%3A%20S%20%5Ctimes%20A%20%5Cto%20S%24" />)
  * A function that specifies how the configuration of the world changes when the agent performs acts in it
  * This will not be well-defined (i.e. representable by a lookup table)  if the world is non-deterministic.
* Perception function (<img src="https://latex.codecogs.com/gif.latex\?%24Z%3A%20S%20%5Cto%20P%24" />)
  * A function that maps a state to a perception
  * Could be the identity mapping (i.e. "do nothing") if the world is fully-observable and each state is its own percept.
* Utility function (<img src="https://latex.codecogs.com/gif.latex\?%24U%3AS%20%5Cto%20%5Cmathbb%7BR%7D%24" />) 
  * A function that measures of how good a state is.
  * This is required for the agent to gauge whether a certain action is worth performing.

### How to make an agent rational
Our agent should find a mapping from sequences of percepts to actions that maximises the utility function (so that the world state is as good as it can be).
i.e. find a mapping <img src="https://latex.codecogs.com/gif.latex\?%24M%3AP%5En%20%5Cto%20A%24" /> which maximises <img src="https://latex.codecogs.com/gif.latex\?%24U%24" />. 

**Example 1**: Navigate a robot to a point <img src="https://latex.codecogs.com/gif.latex\?%24P%24" />. The utility function could be defined to be the negative of how close in the world the robot is to <img src="https://latex.codecogs.com/gif.latex\?%24P%24" />. That way, the closer we are to <img src="https://latex.codecogs.com/gif.latex\?%24P%24" />, the more positive <img src="https://latex.codecogs.com/gif.latex\?%24U%24" /> is.

**Example 2**: Sliding puzzle.

![](https://miro.medium.com/max/1046/1*_n4hcTM-akUEoWL1i05xVg.png)

An agent to solve the sliding puzzle could be defined as <img src="https://latex.codecogs.com/gif.latex\?%24%28A%2C%20P%2C%20S%2C%20T%2C%20Z%2C%20U%29%24" /> where:
* <img src="https://latex.codecogs.com/gif.latex\?%24A%24" /> (the action space) is to move the *empty tile* up, down, left, or right

  * Note: We could define the action space to be moving every tile in each direction (which is the naive approach) however conceptually moving the empty tile is the same thing and is simpler to define

* <img src="https://latex.codecogs.com/gif.latex\?%24P%24" /> (the percept space) the order of the tiles

  * e.g. in the image on the left above, the order can be represented as the following string:
    
    ```
    1238_4765
    ```

* <img src="https://latex.codecogs.com/gif.latex\?%24S%24" /> (the state space) is the same as the percept space (i.e. <img src="https://latex.codecogs.com/gif.latex\?%24S%24" /> = <img src="https://latex.codecogs.com/gif.latex\?%24P%24" />) which is the order of the tiles

* <img src="https://latex.codecogs.com/gif.latex\?%24T%24" /> (the transition funciton) is the act of sliding the empty tile in a direction for a particular order and seeing the resulting new order

* <img src="https://latex.codecogs.com/gif.latex\?%24Z%24" /> (the percept function) is the identiy map (i.e. do nothing because the state space is already the percept space).

* <img src="https://latex.codecogs.com/gif.latex\?%24U%24" /> (the utility function) ~~could be how many tiles are in the correct position~~

  * ~~Problems with this, since sometimes you have to mess up the order temporarily to get to a better state and this utility function would discourage that~~

  Could be simply 1 for the goal state and 0 for any other state. Let the agent figure it out along the way over a number of different trials.
  
  * In practice, this isn't the approach we would normally go for but this conveys the message well.
  
  

**Example 3:** Tic Tac Toe

* <img src="https://latex.codecogs.com/gif.latex\?%24A%24" /> is to place an X or an O at a position on the board, e.g. <img src="https://latex.codecogs.com/gif.latex\?%24%5C%7B%28S%2C%20i%29%20%5C%2C%20%7C%20%5C%2C%20S%20%5Cin%20%5C%7BX%2C%20O%5C%7D%20%5Cand%20i%20%5Cin%20%5Cmathbb%7BZ%7D_9%5C%7D%24" />.

* <img src="https://latex.codecogs.com/gif.latex\?%24P%24" /> is the order of symbols on the board as a sequence reading top to bottom, left to right, e.g <img src="https://latex.codecogs.com/gif.latex\?%24%5C%7BX%2C%20O%2C%20O%2C%20%5C_%2C%20%5C_%2C%20X%2C%20O%2C%20X%2C%20%5C_%5C%7D%24" /> to represent

  ```
  X O O
      X
  O X  
  ```

* <img src="https://latex.codecogs.com/gif.latex\?%24S%20%3D%20P%24" />

* <img src="https://latex.codecogs.com/gif.latex\?%24T%24" /> is the act of placing a symbol at a position and seeing the resulting new state

* <img src="https://latex.codecogs.com/gif.latex\?%24Z%20%3D%20I_S%20%5Cbecause%20S%20%3D%20P%24" /> 

* <img src="https://latex.codecogs.com/gif.latex\?%24U%24" /> could be <img src="https://latex.codecogs.com/gif.latex\?%2410%24" /> when the agent makes a straight line, <img src="https://latex.codecogs.com/gif.latex\?%24-10%24" /> when the opponent makes a straight line, and <img src="https://latex.codecogs.com/gif.latex\?%240%24" /> for any other state.



### Challenges and considerations when modelling

Properties about the environment itself or the agent's knowledge about the environment.

* **Discrete** vs. **continuous**
  * Are the state / action / percept spaces discrete or continuous? 
  * In examples 2 and 3, they were discrete.
* **Deterministic** vs. **stochastic / non-deterministic**
  * Does the agent always know exactly which state it will be in after it performs an action from a state?
  * Is the transition function (<img src="https://latex.codecogs.com/gif.latex\?%24T%24" />) well-defined?
  * In example 2, yes. Example 3 has to factor in the opponent's turn which is non-deterministic.
* **Fully observable** vs. **partially observable**
  * Does the agent know the state of the world exactly?
  * Is the percept function (<img src="https://latex.codecogs.com/gif.latex\?%24Z%24" />) a bijection (i.e. one-to-one and onto)?
  * If not, <img src="https://latex.codecogs.com/gif.latex\?%24S%20%5Cneq%20P%24" /> because there will be aspects of the state not perceived by the agent.
* **Static** vs. **dynamic** 
  * Can the world change while the agent is "thinking" (i.e. not acting)?
  * e.g. in a video game, often the world is changing while the player is not acting

