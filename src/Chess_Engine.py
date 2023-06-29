class Engine:
    def __init__(self):
        self._current_pos = [[None] * 8 for i in range(8)]
        self.current_mode = "play"

        self.start_pos = [['r', 'p', None, None, None, None, 'P', 'R'],
                          ['n', 'p', None, None, None, None, 'P', 'N'],
                          ['b', 'p', None, None, None, None, 'P', 'B'],
                          ['q', 'p', None, None, None, None, 'P', 'Q'],
                          ['k', 'p', None, None, None, None, 'P', 'K'],
                          ['b', 'p', None, None, None, None, 'P', 'B'],
                          ['n', 'p', None, None, None, None, 'P', 'N'],
                          ['r', 'p', None, None, None, None, 'P', 'R']]

    def get_layout(self):
        return self._current_pos

    def set_layout(self, layout):
        for i in range(8):
            for j in range(8):
                self._current_pos[i][j] = layout[i][j]

    def get_valid_moves(self, square):
        if square is None:
            return []
        # noinspection PyTypeChecker
        piece = self._current_pos[square[0]][square[1]]
        if piece is None:
            return []

        is_white = True if piece.isupper() else False

        moves = []

        match piece.lower():
            case "p":
                if is_white:
                    p_square = [square[0], square[1] - 1]
                    if self.is_square_free(p_square):
                        moves.append(p_square)
                    if square[1] == 6:
                        p_square = [square[0], square[1] - 2]
                        if self.is_square_free(p_square):
                            moves.append(p_square)
                else:
                    p_square = [square[0], square[1] + 1]
                    if self.is_square_free(p_square):
                        moves.append(p_square)
                    if square[1] == 1:
                        p_square = [square[0], square[1] + 2]
                        if self.is_square_free(p_square):
                            moves.append(p_square)

            case "r":
                pass
            case "n":
                pass
            case "b":
                pass
            case "q":
                pass
            case "k":
                pass
        return moves

    def is_square_free(self, square):
        if self._current_pos[square[0]][square[1]] is None:
            return True
        return False

    # function to convert a 2-dimensional layout list into a fen-string
    def to_fen(self, layout):
        pass

    # function to convert fen-notation strings into a 2-dimensional layout list
    def to_layout(self, fen):
        pos = [[None] * 8 for i in range(8)]
        rows = fen.split("/")
        for n in rows: print(n)
        allowed = ["r", "R", "p", "P", "k", "K", "q", "Q", "n", "N", "b", "B"]
        for row, x in enumerate(rows):
            file = 0
            while bool(x):
                if x[0] in allowed:
                    pos[file][row] = x[0]
                    file += 1
                else:
                    for n in range(int(x[0])):
                        pos[file][row] = None
                        file += 1
                x = x[1:]
        return pos


if __name__ == "__main__":
    engine = Engine()
    engine.set_layout(engine.start_pos)
    example_layout = engine.to_layout("r1b2bnr/ppp1p1pp/2q3k1/1n2p3/2BPP1p1/1NBQ1Q2/PPP2PPP/R3K1NR")
    for x in example_layout:
        print(x)
    pass
