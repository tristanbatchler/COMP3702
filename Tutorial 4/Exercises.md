# Tutorial 4

## 1

**Suppose you are given a workspace with two rectangular obstacles and a triangular robot. The robot can only translate and cannot rotate.**

### (a)

**Please define a configuration space for the robot**

Let $C := [0, W] \times [0, H] \subseteq \mathbb{R}^2$ be the configuration space where $W$ and $H$ are the width and height of the workspace respectively. Each $(x, y) \in C$ will represent the centre of the triangle.

### (b)

**Assuming the only invalid configurations are those that will cause the robot to collide with at least one of the obstacles, how will the forbidden region(s) in your configuration space look like?**

Let the space filled by the rectangular obstacles in the **workspace** be denoted $R_1$ and $R_2$.

Let the perpendicular height of the triangular robot be denoted $R_h$ and let the width of the base of the robot be $R_w$.

Then, the forbidden region $F$ of the configuration space is:
$$
\{(x \pm R_w, y \pm R_h) \, | \, (x, y) \in A \cup B \}
$$
*Note: I just realised this is wrong because when the triangle touches the corner of a rectangle which is above it, there is less of a margin. It would be really complicated to express the forbidden region mathematically so it would be best to draw a picture.* 

## 2.

**Suppose you are given a workspace populated by the same two obstacles as in 1.. The width and horizontal position of the upper and lower obstacles are the same. Suppose the robot is a rod robot that can only rotate about its static base which is circular and suppose the vertical position of the base is exactly in the middle of the passage. Its angle is limited to be between $0^\circ$ and $360^\circ$ and the robot hits the upper obstacle at $45^\circ$ and $135^\circ$. **

### (a)

**Please define a configuration space for the robot**

Let $C := [0^\circ, 360^\circ) \subseteq \mathbb{R}$.

### (b)

**Assuming only invalid configurations are those that will cause the robot to collide with the obstacle, how would the forbidden region(s) in your configuration look like?**

$F := [45^\circ, 135^\circ] \cup [225^\circ, 315^\circ] \subseteq \mathbb{R}$.



## 3.

**Suppose we have six 2D points, $a=(0,2), b=(3,5), c=(1,4), d=(4,3), e=(1,2),f=(6,3)$.**

### (a)

**Please check if $ab$ intersects with $cd$. How about $ab$ with $ef$?**
$$
\begin{matrix}
\
$$
