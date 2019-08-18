import time
import puzzle
from queue import PriorityQueue

class Node:
    def __init__(self, priority, state, chain):
        self.priority = priority
        self.state = state
        self.chain = chain
    
    def __lt__(self, other):
        return self.priority < other.priority

class Solver:
    def __init__(self, puzzle):
        self.state = puzzle

    def heuristic(self, state):
        man_sum = 0
        for y in range(puzzle.DIM):
            for x in range(puzzle.DIM):
                sym = self.state.board[y][x]
                if sym == puzzle.BLANK:
                    sym = '9'
                dist_x = abs(int(sym) % 3 - x)
                dist_y = abs(int(sym) // 3 - y)
                man_sum += dist_x + dist_y

        return man_sum


    def bfs(self):
        t_0 = time.time()
        queue = [(self.state, "")]
        visited = set()
        while queue:
            t, path = queue.pop()
            visited.add(t)
            if t.board == puzzle.GOAL_BOARD:
                return('BFS found goal by by path: %s (%d steps) in %.2f secs' % (path, len(path), time.time() - t_0))

            for d, v in self.successor(t):
                if v not in visited:
                    queue.insert(0, (v, path + d))
        return "could not find the GOAL_BOARD state in the state space"


    def dfs(self):
        t_0 = time.time()
        stack = [(self.state, "")]
        visited = set()
        while stack:
            t, path = stack.pop(0)
            visited.add(t)
            if t.board == puzzle.GOAL_BOARD:
                return('DFS found goal by by path: %s (%d steps) in %.2f secs' % (path, len(path), time.time() - t_0))

            for d, v in self.successor(t):
                if v not in visited:
                    stack.insert(0, (v, path + d))
        return "could not find the GOAL_BOARD state in the state space"


    def a_star(self):
        t_0 = time.time()
        pq = PriorityQueue()
        pq.put(Node(0, self.state, ""))
        visited = set()
        while pq:
            node = pq.get()
            c, t, moves = node.priority, node.state, node.chain
            visited.add(t)
            if t.board == puzzle.GOAL_BOARD:
                return('A* found goal by by moves: %s (%d steps) in %.2f secs' % (moves, len(moves), time.time() - t_0))

            for d, v in self.successor(t):
                if v not in visited:
                    g = len(moves)
                    pq.put(Node(g + self.heuristic(v), v, moves + d))
        return "could not find the GOAL_BOARD state in the state space"


    def solvable(self):
        return self._inversions() % 2 == 0


    def _inversions(self):
        N = 0
        for i in range(puzzle.DIM_SQ):
            x1 = i % 3
            y1 = i // 3
            if self.state.board[y1][ x1] == puzzle.BLANK:
                continue
            pairs = 0
            for j in range(i + 1, puzzle.DIM_SQ):
                x2 = j % 3
                y2 = j // 3
                if self.state.board[y2][ x2] == puzzle.BLANK:
                    continue
                if int(self.state.board[y2][x2]) < int(self.state.board[y1][x1]):
                    pairs += 1
            N += pairs
        return N


    def successor(self, state):
        dirs_succs = []
        succs = set()
        for dir_ in (puzzle.UP, puzzle.DOWN, puzzle.LEFT, puzzle.RIGHT):
            succ = state.move(dir_)
            if succ and succ != state and succ not in succs:
                succs.add(succ)
                dirs_succs.append((dir_, succ))
        return dirs_succs

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("initial_board", type=str, help="the initial board of the puzzle")
    args = parser.parse_args()

    board_str = args.initial_board

    if len(board_str) != puzzle.DIM_SQ or board_str.count(puzzle.BLANK) != 1: 
        print("initial board must be a string containing the numbers 1 to %d with exactly one underscore" % puzzle.DIM_SQ, file=sys.stderr)
        exit()


    if set([c for c in board_str]) != set([c for c in ''.join([''.join(row) for row in puzzle.GOAL_BOARD])]):
        print("initial board must only contain the following symbols once each:", puzzle.GOAL_BOARD, file=sys.stderr)
        exit()

    puz = puzzle.Puzzle(board_str)
    sol = Solver(puz)

    if not sol.solvable():
        print("impossible to reach GOAL_BOARD from initial board", file=sys.stderr)
        exit()

    print(sol.bfs())
    #print(sol.dfs())
    print(sol.a_star())