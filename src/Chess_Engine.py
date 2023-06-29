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

    # transposes an array (mirrors it along its diagonal)
    def transpose_pos(self, pos):
        transposed_pos = [[None] * len(pos) for i in range(len(pos[0]))]
        for x in range(len(pos)):
            for y in range(len(pos[x])):
                transposed_pos[x][y] = pos[y][x]
        return transposed_pos

    # function to convert a 2-dimensional layout list into a fen-string
    def to_fen(self, pos):
        fen = ""
        rows = engine.transpose_pos(pos)
        allowed = ["r", "R", "p", "P", "k", "K", "q", "Q", "n", "N", "b", "B"]
        for x in range(len(rows)):
            empties = 0
            for y in range(len(rows[x])):
                if rows[x][y] in allowed:
                    if empties != 0:
                        fen += str(empties)
                        empties = 0
                    fen += rows[x][y]
                else:
                    empties += 1
            if empties != 0:
                fen += str(empties)
            if x != len(rows)-1: fen += "/"
        return fen

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
    start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    example_pos = engine.to_layout(start_fen)
    for x in example_pos: print(x)
    transposed = engine.transpose_pos(example_pos)
    for x in transposed: print(x)
    print(start_fen)
    print(engine.to_fen(example_pos))
