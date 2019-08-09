import argparse, sys

# The dimension of the board
DIM = 3

# The blank symbol
BLANK = '_'

parser = argparse.ArgumentParser()
parser.add_argument("initial_state", type=str, help="the initial state of the puzzle")
parser.add_argument("final_state", type=str, help="the desired state of the puzzle")

args = parser.parse_args()

if __name__ == "__main__":

    s_i = args.initial_state
    s_f = args.final_state

    # Need a square number of symbols in both states, each with only one blank
    if len(s_i) != DIM * DIM or len(s_f) != DIM * DIM or s_i.count(BLANK) != 1 or s_f.count(BLANK) != 1:
        print("states must be a string of %d symbols including exactly one underscore" % (DIM * DIM), file=sys.stderr)
        exit()

    # Both states need to have the same set of symbols
    if set([c for c in s_i]) != set([c for c in s_f]):
        print("states must contain the same set of symbols", file=sys.stderr)
        exit()

    # Find the position of the blank symbol for both states
    blank_idx_i = s_i.find(BLANK)
    blank_idx_f = s_f.find(BLANK)
    
    # If swapping the positions of the blank symbols doesn't result in the same state, no one action can transition to the goal state
    if s_i.replace(BLANK, s_f[blank_idx_i]) != s_f.replace(BLANK, s_i[blank_idx_f]):
        print("IMPOSSIBLE")
        exit()

    # Direction to move in (dx, dy) := blank_idx_f - blank_idx_i
    direction = (blank_idx_f % DIM - blank_idx_i % DIM, blank_idx_f // DIM - blank_idx_i // DIM)

    if direction == (0, 1):
        print("D")
    elif direction == (0, -1):
        print("U")
    elif direction == (1, 0):
        print("R")
    elif direction == (-1, 0):
        print("L")
    elif direction == (0, 0):
        print("DO NOTHING")
    else:
        # More than one move is required so we say it's impossible
        print("IMPOSSIBLE")
