GOAL_BOARD = ('123', '456', '78_')
DIM = 3
DIM_SQ = 9
BLANK = '_'
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

class Puzzle:
    def __init__(self, init_board_str):
        board = [[] for i in range(DIM)]
        for i in range(DIM):
            board[i] = init_board_str[i * DIM : (i + 1) * DIM]
        self.board = tuple(board)
        blank_idx = init_board_str.find(BLANK)
        self.x = blank_idx % DIM
        self.y = blank_idx // DIM

    """ 
    Does not change the current board. Returns a new Puzzle 
    if the move is possible, otherwise returns None.
    """
    def move(self, dir_):
        dx, dy = 0, 0
        if dir_ in (LEFT, RIGHT):
            dy = 0
            dx = (DIM - 1) * (dir_ == RIGHT) - 1
        elif dir_ in (UP, DOWN):
            dx = 0
            dy = (DIM - 1) * (dir_ == DOWN) - 1

        x_new = self.x + dx
        if x_new < 0 or x_new > DIM - 1:
            return None

        y_new = self.y + dy
        if y_new < 0 or y_new > DIM - 1:
            return None

        new_board = [[c for c in self.board[i]] for i in range(DIM)]
        new_board[self.y][self.x] = self.board[y_new][x_new]
        new_board[y_new][x_new] = BLANK
        return Puzzle(''.join([''.join(row) for row in new_board]))


    def __repr__(self):
        return '\n'.join(self.board)

    def __key(self):
        return self.board

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

if __name__ == '__main__':
    puz1 = Puzzle("12345_678")
    puz2 = Puzzle("12345678_")
    puz3 = Puzzle("12345678_")
    print(puz1 == puz2)
    print(puz2 == puz3)
    print(puz3 == puz2)
    print(puz3 == puz1)