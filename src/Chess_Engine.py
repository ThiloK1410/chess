class Engine:
    def __init__(self):
        self._current_pos = [[""] * 8 for i in range(8)]
        self.current_mode = "play"
        self.current_turn = 0

        self.start_pos = [['r', 'p', None, None, None, None, 'P', 'R'],
                          ['n', 'p', None, None, None, None, 'P', 'N'],
                          ['b', 'p', None, None, None, None, 'P', 'B'],
                          ['q', 'p', None, None, None, None, 'P', 'Q'],
                          ['k', 'p', None, None, None, None, 'P', 'K'],
                          ['b', 'p', None, None, None, None, 'P', 'B'],
                          ['n', 'p', None, None, None, None, 'P', 'N'],
                          ['r', 'p', None, None, None, None, 'P', 'R']]

        self.test_layout = [[None, None, None, None, None, None, None, None],
                            [None, "R", None, None, None, None, "r", None],
                            [None, None, None, None, None, None, None, None],
                            [None, "Q", None, None, "b", None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, "n", None, None, "K", None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None]]

    def get_layout(self):
        return self._current_pos

    def set_layout(self, layout):
        for i in range(8):
            for j in range(8):
                self._current_pos[i][j] = layout[i][j]

    # core method of Chess_Engine, used for getting all valid moves for a given square (can be empty square)
    def get_valid_moves(self, square):
        if square is None:
            return [[], []]
        piece = self._current_pos[square[0]][square[1]]
        if piece is None:
            return [[], []]
        if not (self.is_white(piece) == self.is_whites_turn()):
            return [[], []]

        is_white = True if piece.isupper() else False

        moves = [[], []]

        match piece.lower():
            case "p":
                if is_white:
                    # white moves
                    p_square = [square[0], square[1] - 1]
                    if self.is_square_free(p_square):
                        moves[0].append(p_square)
                    if square[1] == 6:
                        p_square = [square[0], square[1] - 2]
                        if self.is_square_free(p_square):
                            moves[0].append(p_square)
                    p_squares = [[square[0] + 1, square[1] - 1], [square[0] - 1, square[1] - 1]]
                    for p_square in p_squares:
                        if self.has_opposite_color(square, p_square):
                            moves[1].append(p_square)
                else:
                    # black moves
                    p_square = [square[0], square[1] + 1]
                    if self.is_square_free(p_square):
                        moves[0].append(p_square)
                    if square[1] == 1:
                        p_square = [square[0], square[1] + 2]
                        if self.is_square_free(p_square):
                            moves[0].append(p_square)
                    p_squares = [[square[0] + 1, square[1] + 1], [square[0] - 1, square[1] + 1]]
                    for p_square in p_squares:
                        if self.has_opposite_color(square, p_square):
                            moves[1].append(p_square)

            case "r":
                for direction in range(4):
                    p_square = square
                    if direction == 0:
                        while self.square_in_bounds([p_square[0], p_square[1] - 1]):
                            p_square = [p_square[0], p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 1:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1]]):
                            p_square = [p_square[0] + 1, p_square[1]]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 2:
                        while self.square_in_bounds([p_square[0], p_square[1] + 1]):
                            p_square = [p_square[0], p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 3:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1]]):
                            p_square = [p_square[0] - 1, p_square[1]]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
            case "n":
                p_squares = [[square[0] + 1, square[1] - 2], [square[0] - 1, square[1] - 2],
                             [square[0] + 1, square[1] + 2], [square[0] - 1, square[1] + 2],
                             [square[0] + 2, square[1] + 1], [square[0] + 2, square[1] - 1],
                             [square[0] - 2, square[1] + 1], [square[0] - 2, square[1] - 1]]
                for p_square in p_squares:
                    if self.is_square_free(p_square):
                        moves[0].append(p_square)
                    elif self.has_opposite_color(square, p_square):
                        moves[1].append(p_square)
            case "b":
                for direction in range(4):
                    p_square = square
                    if direction == 0:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1] - 1]):
                            p_square = [p_square[0] - 1, p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 1:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1] - 1]):
                            p_square = [p_square[0] + 1, p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 2:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1] + 1]):
                            p_square = [p_square[0] + 1, p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 3:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1] + 1]):
                            p_square = [p_square[0] - 1, p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
            case "q":
                for direction in range(4):
                    p_square = square
                    if direction == 0:
                        while self.square_in_bounds([p_square[0], p_square[1] - 1]):
                            p_square = [p_square[0], p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 1:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1]]):
                            p_square = [p_square[0] + 1, p_square[1]]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 2:
                        while self.square_in_bounds([p_square[0], p_square[1] + 1]):
                            p_square = [p_square[0], p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 3:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1]]):
                            p_square = [p_square[0] - 1, p_square[1]]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                for direction in range(4):
                    p_square = square
                    if direction == 0:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1] - 1]):
                            p_square = [p_square[0] - 1, p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 1:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1] - 1]):
                            p_square = [p_square[0] + 1, p_square[1] - 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 2:
                        while self.square_in_bounds([p_square[0] + 1, p_square[1] + 1]):
                            p_square = [p_square[0] + 1, p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
                    if direction == 3:
                        while self.square_in_bounds([p_square[0] - 1, p_square[1] + 1]):
                            p_square = [p_square[0] - 1, p_square[1] + 1]
                            if self.is_square_free(p_square):
                                moves[0].append(p_square)
                                continue
                            elif self.has_opposite_color(square, p_square):
                                moves[1].append(p_square)
                            break
            case "k":
                p_squares = [[square[0] + 1, square[1] + 1], [square[0], square[1] + 1],
                             [square[0] - 1, square[1] + 1], [square[0] - 1, square[1]],
                             [square[0] - 1, square[1] - 1], [square[0], square[1] - 1],
                             [square[0] + 1, square[1] - 1], [square[0] + 1, square[1]]]
                for p_square in p_squares:
                    if self.is_square_free(p_square):
                        moves[0].append(p_square)
                    elif self.has_opposite_color(square, p_square):
                        moves[1].append(p_square)

        out = [[], []]
        for i in moves[0]:
            if self.square_in_bounds(i):
                out[0].append(i)
        return out

    def make_move(self, move, allow_invalid=False):
        if self.is_white(self._current_pos[move[0][0]][move[0][1]]) != bool(self.current_turn % 2):
            if (move[1] in self.get_valid_moves(move[0])[0]) or allow_invalid:
                self._current_pos[move[1][0]][move[1][1]] = self._current_pos[move[0][0]][move[0][1]]
                self._current_pos[move[0][0]][move[0][1]] = None
                self.current_turn += 1

    def is_square_free(self, square):
        if self.square_in_bounds(square):
            if self._current_pos[square[0]][square[1]] is None:
                return True
        return False

    # returns True if white, False if black and None if square is empty
    def is_white(self, piece):
        if piece is None:
            return None
        if piece.isupper():
            return True
        return False

    def is_whites_turn(self):
        return not bool(self.current_turn % 2)

    # returns True only when both squares are occupied and pieces are of different colors (False otherwise)
    def has_opposite_color(self, square1, square2):
        if self.is_square_free(square1) or self.is_square_free(square2):
            return False
        if self.square_in_bounds(square1) and self.square_in_bounds(square2):
            piece1 = self._current_pos[square1[0]][square1[1]]
            piece2 = self._current_pos[square2[0]][square2[1]]
            if self.is_white(piece1) == (not self.is_white(piece2)):
                return True
        return False

    def square_in_bounds(self, square):
        if 0 <= square[0] <= 7:
            if 0 <= square[1] <= 7:
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
            if x != len(rows) - 1: fen += "/"
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

    # test code used to evaluate fen-2d conversion function

    # start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    # example_pos = engine.to_layout(start_fen)
    # for x in example_pos: print(x)
    # transposed = engine.transpose_pos(example_pos)
    # for x in transposed: print(x)
    # print(start_fen)
    # print(engine.to_fen(example_pos))
