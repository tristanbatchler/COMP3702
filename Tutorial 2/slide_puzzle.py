import argparse, sys, time

DIM = 3

parser = argparse.ArgumentParser()
parser.add_argument("initial_state", type=str, help="the initial state of the puzzle")
parser.add_argument("goal_state", type=str, help="the goal state of the puzzle")

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
    x_old = i_old % DIM
    y_old = i_old // DIM
    x_new = clamp(x_old + dx, 0, DIM-1)
    y_new = clamp(y_old + dy, 0, DIM-1)
    i_new = x_new + DIM * y_new
    s_new = s.replace('_', s[i_new])
    return s_new[:i_new] + '_' + s_new[i_new + 1:]

def clamp(x, min_, max_):
    return max(min_, min(x, max_))

def perceive(s):
    for i in range(0, DIM*DIM, DIM):
        print(s[i:i+DIM])
    print()

def bfs(s_0, s_f):
    t_0 = time.time()
    queue = [(s_0, "")]
    visited = set()
    while queue:
        t, path = queue.pop()
        visited.add(t)
        if t == s_f:
            return('found %s by by path: %s (%d steps) in %.2f secs' % (t, path, len(path), time.time() - t_0))
            for s in path:
                perceive(s)
            return
        
        for d, v in successor(t):
            if v not in visited:
                queue.insert(0, (v, path + d))
    return "could not find the goal state in the state space"

def dfs(s_0, s_f):
    t_0 = time.time()    
    stack = [(s_0, "")]
    visited = set()
    while stack:
        t, path = stack.pop(0)
        visited.add(t)
        if t == s_f:
            return('found %s by by path: %s (%d steps) in %.2f secs' % (t, path, len(path), time.time() - t_0))
            for s in path:
                perceive(s)
            return
        
        for d, v in successor(t):
            if v not in visited:
                stack.insert(0, (v, path + d))
    return "could not find the goal state in the state space"

def check_parity():
    pass

def successor(s):
    succs = set()
    for dir_ in 'UDLR':
        succ = move(s, dir_)
        if s != succ:
            succs.add((dir_, move(s, dir_)))
    return succs

if __name__ == "__main__":
    s = args.initial_state
    s_f = args.goal_state

    if len(s) != DIM*DIM or s.count("_") != 1 or len(s_f) != DIM*DIM or s_f.count("_") != 1: 
        print("states must be a string of DIM*DIM symbols including exactly one underscore", file=sys.stderr)
        exit()

    if set([c for c in s]) != set([c for c in s_f]):
        print("initial state must only contain the following symbols once each:", s_f, file=sys.stderr)
        exit()
    
    print(bfs(s, s_f))
    print(dfs(s, s_f))