class Engine:
    def __init__(self):
        self._current_layout = [[None] * 8 for i in range(8)]
        self.current_mode = "play"

        self.start_layout = [["r", "n", "b", "q", "k", "b", "n", "r"],
                             ["p", "p", "p", "p", "p", "p", "p", "p"],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None, None, None],
                             ["P", "P", "P", "P", "P", "P", "P", "P"],
                             ["R", "N", "B", "Q", "K", "B", "N", "R"]]

    def get_layout(self):
        return self._current_layout

    def set_layout(self, layout):
        for i in range(8):
            for j in range(8):
                self._current_layout[i][j] = layout[i][j]

    def get_valid_moves(self, square):
        if square is None:
            return []
        piece = self._current_layout[square[1]][square[0]]
        print(piece)
        return [[3, 3], [4, 4]]


if __name__ == "__main__":
    engine = Engine()
    engine.set_layout(engine.start_layout)
    pass
