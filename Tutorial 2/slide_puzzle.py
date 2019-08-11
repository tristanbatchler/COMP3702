import argparse
import sys
import time
import math

GOAL = "12345678_"

parser = argparse.ArgumentParser()
parser.add_argument("initial_state", type=str, help="the initial state of the puzzle")

args = parser.parse_args()


def move(s, dir_):
    (dx, dy) = (0, 0)
    if dir_ in 'LR':
        dy = 0
        dx = 2 * (dir_ == 'R') - 1
    elif dir_ in 'UD':
        dx = 0
        dy = 2 * (dir_ == 'D') - 1

    i_old = s.find('_')
    x_old = i_old % 3
    y_old = i_old // 3
    x_new = clamp(x_old + dx, 0, 2)
    y_new = clamp(y_old + dy, 0, 2)
    i_new = x_new + 3 * y_new
    s_new = s.replace('_', s[i_new])
    return s_new[:i_new] + '_' + s_new[i_new + 1:]


def clamp(x, min_, max_):
    return max(min_, min(x, max_))


def perceive(s):
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print()


def util(s):
    ''' Returns a real which measures how close a state is to the final state. Higher is closer. '''
    if not solvable(s):
        return -math.inf
    u = 0
    for i in range(len(s)):
        if s[i] == GOAL[i]:
            u += 1
        else:
            u -= 1
    return u


def cost(s1, s2):
    ''' Returns the cost of reaching state s2 from s1. Lower is better. '''
    # If s1 is better, u(s_1) > u(s_2) => return high cost
    # If s2 is better, u(s_1) < u(s_2) => return low/negative cost
    return util(s1) - util(s2)


def heuristic(s):
    ''' Returns the estimated cost of reaching the final state from the current state s '''
    # We want h to be consistent, i.e. h(s) <= c(s, s') + h(s') where s' is adjacent to s
    if not solvable(s):
        return math.inf

    # Let's go with the sum of Manhattan distances of each tile from its desired position
    man_sum = 0
    for i in range(len(s)):
        x = i % 3
        y = i // 3

        sym = s[i]

        dist_x = abs(2 - x)
        dist_y = abs(2 - y)

        man_sum += dist_x + dist_y

    return man_sum


def bfs(s):
    t_0 = time.time()
    queue = [(s, "")]
    visited = set()
    while queue:
        t, path = queue.pop()
        visited.add(t)
        if t == GOAL:
            return('BFS found %s by by path: %s (%d steps) in %.2f secs' % (t, path, len(path), time.time() - t_0))

        for d, v in successor(t):
            if v not in visited:
                queue.insert(0, (v, path + d))
    return "could not find the goal state in the state space"


def dfs(s):
    t_0 = time.time()
    stack = [(s, "")]
    visited = set()
    while stack:
        t, path = stack.pop(0)
        visited.add(t)
        if t == GOAL:
            return('DFS found %s by by path: %s (%d steps) in %.2f secs' % (t, path, len(path), time.time() - t_0))

        for d, v in successor(t):
            if v not in visited:
                stack.insert(0, (v, path + d))
    return "could not find the goal state in the state space"


def a_star(s):
    t_0 = time.time()
    pq = [(s, 0, "", [])]
    visited = set()
    while pq:
        pq.sort(key=lambda e: e[1])
        t, c, moves, path = pq.pop(0)
        visited.add(t)
        if t == GOAL:
            return('A* found %s by by moves: %s (%d steps) in %.2f secs' % (t, moves, len(moves), time.time() - t_0))

        for d, v in successor(t):
            if v not in visited:
                g = 0
                for i in range(len(path) - 1):
                    p1 = path[i]
                    p2 = path[i + 1]
                    g += cost(p1, p2)

                path.append(v)
                pq.append((v, g + heuristic(v), moves + d, path))
    return "could not find the goal state in the state space"


def solvable(s):
    return inversions(s) % 2 == 0


def inversions(s):
    N = 0
    for i in range(0, len(s)):
        if s[i] == '_':
            continue
        pairs = 0
        for j in range(i + 1, len(s)):
            if s[j] == '_':
                continue
            if int(s[j]) < int(s[i]):
                pairs += 1
        N += pairs
    return N


def successor(s):
    succs = set()
    for dir_ in 'UDLR':
        succ = move(s, dir_)
        if s != succ:
            succs.add((dir_, move(s, dir_)))
    return succs

if __name__ == "__main__":
    s = args.initial_state

    if len(s) != 9 or s.count("_") != 1: 
        print("initial state must be a string containing the numbers 1 to 9 with exactly one underscore", file=sys.stderr)
        exit()

    if set([c for c in s]) != set([c for c in GOAL]):
        print("initial state must only contain the following symbols once each:", GOAL, file=sys.stderr)
        exit()

    if not solvable(s):
        print("impossible to reach goal from initial state", file=sys.stderr)
        exit()

    #print(dfs(s))
    #print(bfs(s))
    print(a_star(s))
    #print(inversions(s))