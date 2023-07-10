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

        self.test_layout = [[None, None, None, "q", None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, "R"],
                            [None, None, None, None, None, "N", None, None],
                            [None, "B", None, "K", None, None, None, None]]

    def get_layout(self):
        return self._current_pos

    def set_layout(self, layout):
        for i in range(8):
            for j in range(8):
                self._current_pos[i][j] = layout[i][j]

    def moves_pawn(self, position, moves, layout, is_white):
        if is_white:
            # white moves
            p_square = [position[0], position[1] - 1]
            if self.is_square_free(p_square, layout):
                moves[0].append(p_square)
            if position[1] == 6:
                p_square = [position[0], position[1] - 2]
                if self.is_square_free(p_square, layout):
                    moves[0].append(p_square)
            p_squares = [[position[0] + 1, position[1] - 1], [position[0] - 1, position[1] - 1]]
            for p_square in p_squares:
                if self.has_opposite_color(position, p_square, layout):
                    moves[1].append(p_square)
        else:
            # black moves
            p_square = [position[0], position[1] + 1]
            if self.is_square_free(p_square, layout):
                moves[0].append(p_square)
            if position[1] == 1:
                p_square = [position[0], position[1] + 2]
                if self.is_square_free(p_square, layout):
                    moves[0].append(p_square)
            p_squares = [[position[0] + 1, position[1] + 1], [position[0] - 1, position[1] + 1]]
            for p_square in p_squares:
                if self.has_opposite_color(position, p_square, layout):
                    moves[1].append(p_square)

    def moves_rook(self, position, moves, layout):
        for direction in range(4):
            p_square = position
            if direction == 0:
                while self.square_in_bounds([p_square[0], p_square[1] - 1]):
                    p_square = [p_square[0], p_square[1] - 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 1:
                while self.square_in_bounds([p_square[0] + 1, p_square[1]]):
                    p_square = [p_square[0] + 1, p_square[1]]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 2:
                while self.square_in_bounds([p_square[0], p_square[1] + 1]):
                    p_square = [p_square[0], p_square[1] + 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 3:
                while self.square_in_bounds([p_square[0] - 1, p_square[1]]):
                    p_square = [p_square[0] - 1, p_square[1]]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break

    def moves_knight(self, position, moves, layout):
        p_squares = [[position[0] + 1, position[1] - 2], [position[0] - 1, position[1] - 2],
                     [position[0] + 1, position[1] + 2], [position[0] - 1, position[1] + 2],
                     [position[0] + 2, position[1] + 1], [position[0] + 2, position[1] - 1],
                     [position[0] - 2, position[1] + 1], [position[0] - 2, position[1] - 1]]
        for p_square in p_squares:
            if self.is_square_free(p_square, layout):
                moves[0].append(p_square)
            elif self.has_opposite_color(position, p_square, layout):
                moves[1].append(p_square)

    def moves_bishop(self, position, moves, layout):
        for direction in range(4):
            p_square = position
            if direction == 0:
                while self.square_in_bounds([p_square[0] - 1, p_square[1] - 1]):
                    p_square = [p_square[0] - 1, p_square[1] - 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 1:
                while self.square_in_bounds([p_square[0] + 1, p_square[1] - 1]):
                    p_square = [p_square[0] + 1, p_square[1] - 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 2:
                while self.square_in_bounds([p_square[0] + 1, p_square[1] + 1]):
                    p_square = [p_square[0] + 1, p_square[1] + 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break
            if direction == 3:
                while self.square_in_bounds([p_square[0] - 1, p_square[1] + 1]):
                    p_square = [p_square[0] - 1, p_square[1] + 1]
                    if self.is_square_free(p_square, layout):
                        moves[0].append(p_square)
                        continue
                    elif self.has_opposite_color(position, p_square, layout):
                        moves[1].append(p_square)
                    break

    def moves_king(self, position, moves, layout):
        p_squares = [[position[0] + 1, position[1] + 1], [position[0], position[1] + 1],
                     [position[0] - 1, position[1] + 1], [position[0] - 1, position[1]],
                     [position[0] - 1, position[1] - 1], [position[0], position[1] - 1],
                     [position[0] + 1, position[1] - 1], [position[0] + 1, position[1]]]
        for p_square in p_squares:
            if self.is_square_free(p_square, layout):
                moves[0].append(p_square)
            elif self.has_opposite_color(position, p_square, layout):
                moves[1].append(p_square)

    def is_in_check(self, layout, white): 
        moves = [[], []]
        king_pos = []
        # search for the king
        for i in range(8):
            for j in range(8):
                # is square occupied?
                if layout[i][j] is not None:
                    # is there a king on the square?
                    if layout[i][j].lower() == "k":
                        # is the king of the correct color?
                        if layout[i][j].isupper() == white:
                            king_pos = [i, j]
                            break

        # checking for checks by looking backwards if pieces hit king
        self.moves_pawn(king_pos, moves, layout, white)
        for x in moves[1]:
            piece = layout[x[0]][x[1]]
            if piece is not None:
                if piece.lower() == "p":
                    if piece.islower() == white:
                        return True
        moves = [[], []]
        self.moves_rook(king_pos, moves, layout)
        for x in moves[1]:
            piece = layout[x[0]][x[1]]
            if piece is not None:
                if piece.lower() == "r" or piece.lower() == "q":
                    if piece.islower() == white:
                        return True
        moves = [[], []]
        self.moves_bishop(king_pos, moves, layout)
        for x in moves[1]:
            piece = layout[x[0]][x[1]]
            if piece is not None:
                if piece.lower() == "b" or piece.lower() == "q":
                    if piece.islower() == white:
                        return True
        moves = [[], []]
        self.moves_knight(king_pos, moves, layout)
        for x in moves[1]:
            piece = layout[x[0]][x[1]]
            if piece is not None:
                if piece.lower() == "n":
                    if piece.islower() == white:
                        return True
        moves = [[], []]
        self.moves_king(king_pos, moves, layout)
        for x in moves[1]:
            piece = layout[x[0]][x[1]]
            if piece is not None:
                if piece.lower() == "k":
                    if piece.islower() == white:
                        return True

        return False


    # core method of Chess_Engine, used for getting all valid moves for a given square (can be empty square)
    def get_valid_moves(self, square):
        if square is None:
            return [[], []]
        piece = self._current_pos[square[0]][square[1]]
        if piece is None:
            return [[], []]
        if not (self.is_white(piece) == self.is_whites_turn()):
            return [[], []]

        moves = [[], []]

        # adding different move sets according to piece type
        match piece.lower():
            case "p":
                self.moves_pawn(square, moves, self._current_pos, self.is_white(piece))
            case "r":
                self.moves_rook(square, moves, self._current_pos)
            case "n":
                self.moves_knight(square, moves, self._current_pos)
            case "b":
                self.moves_bishop(square, moves, self._current_pos)
            case "q":
                self.moves_rook(square, moves, self._current_pos)
                self.moves_bishop(square, moves, self._current_pos)
            case "k":
                self.moves_king(square, moves, self._current_pos)

        out = [[], []]
        # filtering out invalid moves (out of bounds, king sacrifice)
        for i in range(2):
            for move in moves[i]:
                # is the move within board boundaries?
                if self.square_in_bounds(move):
                    # will the move put your king in check?
                    next_layout = self.get_next_layout([square, move])
                    if not self.is_in_check(next_layout, self.is_white(piece)):
                        out[i].append(move)

        return out

    def make_move(self, move):
        if self.is_white(self._current_pos[move[0][0]][move[0][1]]) != bool(self.current_turn % 2):
            if (move[1] in self.get_valid_moves(move[0])[0]) or (move[1] in self.get_valid_moves(move[0])[1]):
                self._current_pos[move[1][0]][move[1][1]] = self._current_pos[move[0][0]][move[0][1]]
                self._current_pos[move[0][0]][move[0][1]] = None
                self.current_turn += 1

    # returns the possible layout after a specific move would be done
    def get_next_layout(self, move):
        layout = [row[:] for row in self._current_pos]
        # checking if there is a piece to move
        if layout[move[0][0]][move[0][1]] is None:
            raise ValueError("Layout for invalid move requested")
        layout[move[1][0]][move[1][1]] = layout[move[0][0]][move[0][1]]
        layout[move[0][0]][move[0][1]] = None
        return layout

    def is_square_free(self, square, layout):
        if self.square_in_bounds(square):
            if layout[square[0]][square[1]] is None:
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
    def has_opposite_color(self, square1, square2, layout):
        if self.is_square_free(square1, layout) or self.is_square_free(square2, layout):
            return False
        if self.square_in_bounds(square1) and self.square_in_bounds(square2):
            piece1 = layout[square1[0]][square1[1]]
            piece2 = layout[square2[0]][square2[1]]
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
