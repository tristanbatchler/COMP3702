# Lecture 1
## Rational Agent
### Definition
A program that has the ability to perceive an environment and produce a rational decision based on that perception.

The environment can also change due to actions the agent has made allowing for a kind of feedback loop.

### The components
* Action space ($A$)
  * The set of all actions the agent can perform
* Percept space ($P$)
  * The set of all things the agent can perceive in the world
* State space ($S$)
  * The set of all possible configurations of the world the agent is operating in
    * i.e. the internal state of the agent and the environment that matters for the interaction between the agent and the environment
* Transition function / World dynamics ($T: S \times A \to S'$)
  * A function that specifies how to configuration of the world changes when the agent performs actions in it
* Perception function ($Z: S \to P$)
  * A function that maps a state to a perception
* Utility function ($U:S \to \mathbb{R}$) 
  * A function that measures of how good a state is.
  * This is required for the agent to gauge whether a certain action is worth performing.

### How to make an agent rational
Our agent should find a mapping from sequences of percepts to actions that maximises the utility function.
i.e. find a mapping $M:P^n \to A$ which maximises $U$. 
