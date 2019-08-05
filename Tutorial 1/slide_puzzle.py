import argparse, sys, math, random, subprocess

parser = argparse.ArgumentParser()
parser.add_argument("initial_state", type=str, help="the initial state of the puzzle")

args = parser.parse_args()

s_f = "12345678_"

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

def util(s):
    u = 0
    for i in range(9):
        if s[i] == s_f[i]:
            u += 1
    return u

def perceive(s):
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print()

if __name__ == "__main__":
    s = args.initial_state
    score = util(s)

    if len(s) != 9 or s.count("_") != 1:
        print("states must be a string of 9 symbols including exactly one underscore", file=sys.stderr)
        exit()

    if set([c for c in s]) != set([c for c in s_f]):
        print("initial state must only contain the following symbols once each:", s_f, file=sys.stderr)
        exit()

    dir_ = subprocess.run(["python", "which_action.py", s, "1234567_8"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print("moving %s" % dir_)
    s = move(s, dir_)
    perceive(s)