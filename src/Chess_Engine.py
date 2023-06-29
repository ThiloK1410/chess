class Engine:
    def __init__(self):
        self._current_layout = [[None] * 8 for i in range(8)]
        self.current_mode = "play"

        self.start_layout = [['r', 'p', None, None, None, None, 'P', 'R'],
                             ['n', 'p', None, None, None, None, 'P', 'N'],
                             ['b', 'p', None, None, None, None, 'P', 'B'],
                             ['q', 'p', None, None, None, None, 'P', 'Q'],
                             ['k', 'p', None, None, None, None, 'P', 'K'],
                             ['b', 'p', None, None, None, None, 'P', 'B'],
                             ['n', 'p', None, None, None, None, 'P', 'N'],
                             ['r', 'p', None, None, None, None, 'P', 'R']]

    def get_layout(self):
        return self._current_layout


    def set_layout(self, layout):
        for i in range(8):
            for j in range(8):
                self._current_layout[i][j] = layout[i][j]


    def get_valid_moves(self, square):
        if square is None:
            return []
        # noinspection PyTypeChecker
        piece = self._current_layout[square[0]][square[1]]
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
        if self._current_layout[square[0]][square[1]] is None:
            return True
        return False


if __name__ == "__main__":
    engine = Engine()
    engine.set_layout(engine.start_layout)
    pass
