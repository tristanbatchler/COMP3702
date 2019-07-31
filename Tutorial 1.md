# Tutorial 1

## 1.

***Design a tic-tac-toe playing agent, assuming that a single time step includes a single move by the agent and the immediate move by the opponent.  The goal is to win with as few steps as possible***

***Example tic-tac-toe board*** 

```
O X O
X O 
X    
```

A rational agent is a $6$-tuple $(A, P, S, T, Z, U)$ where:

* $A$ is the action space

  * In this case, let's say an action is to place the agent's symbol at an empty position on the board and then let the opponent play their turn.
  * Because the opponent plays a turn as part of each action, actions are **non-deterministic**.

* $P$ is the percept space

  * In this case, let's say a perception is a view of the symbols on the board in the form of a string with characters representing symbols going left-to-right, top-to-bottom. Blank spaces would be represented by a special reserved character such as underscore.
    * E.g. the board depicted above would have perception OXOXO_X__

* $S$ is the state space

  * In this case, because we have a **fully-observable system**, the state is always equal to its perception, so $S = P$.

* $T:S \times A \to S$ is the transition function

  * In this case, a transition from a board followed by an action would be the resulting board after the action has been performed.
  * E.g. if $s \in S$ is the current state, OXOXO_X__ and $a \in A$ is the action to perform, putting an X at the end of the board, then $T(s, a)$ might be OXOXO**O**X_**X**. Notice both he agent and the opponent took turns highlighted in bold.
  * Because actions are non-deterministic, this transition function $T$ cannot be **well-defined**.

* $Z:S \to P$ is the percept function

  * In this case, because we have a fully-observable system, $Z$ must be the identity mapping under $S = P$, i.e. $Z=I_S$.

* $U:S\to \mathbb{R}$ is the utility function

  * We could choose many. One choice is to let $U(s) = 1$ if $s$ is a winning state and $U(s) < 1$ for all other states.
  * A more sensible and/or efficient choice may exist but we haven't got there yet in the course. All we're concerned about is the utility function giving a higher number for a better state.

  

## 2

***Consider  a  navigation  app,  like  an  app  on  your  smart  phone  or  car  that  you  use to find your way around UQ or other places.  This program is essentially a rational agent.  Assume that:***

* ***Its goal is to find the shortest path to a goal location.***
* ***The map used by the agent is 100% up to date.***
* ***The location provided by the GPS is correct.***

***Suppose that you want to develop this navigation agent,***

1. ***How will you design it?***

   * $A$: an action will be for the current or goal location to change and for the agent to calculate and suggest a "best route" in the map from the current location to the goal location.

   * $P$: a perception will be a weighted graph whose edges represent roads/paths in the map and whose nodes represent junctions in the map. The edges will be weighted with the distance along the path from each of its endpoints.

     ![Image result for weighted graph](https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/)

     A perception will also contain the current and goal locations represented as nodes in the graph which can split an edge if the location is along a road. In that case, the weight of the split edge is divided based on how far along the location is between one junction and the next.

     Finally, a perception will contain the current recommended/best route calculated by the agent.

   * $S$ = $P$ in this fully-observable environment.

   * $T:S\times A \to S$: let $s \in S$ be a current state and $a \in A$ be a route to recommend. The result of $T(s, a)$ will be a new state which has updated information about the current or goal locations and the new, re-calculated, recommended route.

   * $Z = I_S$ in this fully-observable environment.

   * $U: S \to \mathbb{R}$, again, could be something like $1$ when the current location equals the goal location but that wouldn't be great.

     * Instead, we could use the negative sum of the weights in the graph along the recommended route. This would be more positive the closer the current location is to the goal. 

2. ***Select the type of environment this agent operates in (i.e., discrete/continuous, deterministic/non-deterministic, fully/partially observable, static/dynamic)? Explain your selections, and think of the effect of each assumption above to this type.***

   * The agent operates in a **discrete** environment: this problem is a continuous one but we have discretised it into a problem of weighted graphs and paths through the graph, and that is the environment our agent operates in.
   * The agent operates in a **non-deterministic** environment because it does not know where the next current location will be (that is up to the user). For example, a GPS navigator doesn't know if I will miss my turn or not.
   * The agent operates in a **fully observable** environment because we have assumed the map used is fully up-to-date and the current location is 100% accurate. I can only further assume that the goal location is also 100% known and accurate.
   * The agent operates in a **dynamic** environment because the state could change during an action. E.g. while GPS navigator is re-calculating my new route when after I miss my turn, I could miss my turn again.

     

3. ***Define the search problem and its corresponding state graph representation for this query.***

   * This is a search in a weighted graph for the shortest path between two given points. There are many algorithms for this, such as [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm).

## 3

***A web crawler is a program that systematically browses and downloads web pagesfrom the Internet.  This is one of the programs that enables us to search the internet.Now, a web crawler can be viewed as a rational agent.  Please design the web crawleragent when the agent lives in:***

1. ***An ideal world where no broken links exist and the internet connection always works.***
   * $A$: an action is to visit a link and download the page's contents. The link would then be added to the history of links visited.
   * $P$: a perception would be the contents of the current page and all of its links. A perception would also contain the history of links visited.
   * $S = P$ in this fully-observable environment.
   * $T:S \times A \to S$: let $s \in S$ be the current page with its links and the current history. Let $a \in A$ be the act of visiting a link on the current page and adding it to the history. Then $T(s, a)$ would be the contents of the page visited and all its links and the history would contain this link as well.
   * $Z = I_S$ in this fully-observable environment.
   * $U:S \to \mathbb{R}$ could be the number of unique links in the history.
2. ***The real world, where both assumptions above are not valid.***
   * We won't know if a page exists before choosing its link to visit, so our system would be non-deterministic in this world.
     * As a result, our transition function is no longer well-defined.
   * There should be a way to "go back" through the history because the crawler could come to a dead end or a closed system (e.g. a website which only has internal links, the crawler would go around in circles forever, never finding any new links).
   * There should be a way to keep track of the current internet connectivity in the state. If it's not available, the only action should be to "do nothing".