import numpy as np


class Layout:
    def __init__(self, start=False):
        self.king_pos = None

        self.k_moved = False
        self.K_moved = False
        self.r1_moved = False
        self.r8_moved = False
        self.R1_moved = False
        self.R8_moved = False

        if start:
            self.layout = [["R", "P", "", "", "", "", "p", "r"],
                           ["N", "P", "", "", "", "", "p", "n"],
                           ["B", "P", "", "", "", "", "p", "b"],
                           ["Q", "P", "", "", "", "", "p", "q"],
                           ["K", "P", "", "", "", "", "p", "k"],
                           ["B", "P", "", "", "", "", "p", "b"],
                           ["N", "P", "", "", "", "", "p", "n"],
                           ["R", "P", "", "", "", "", "p", "r"]]

            self.king_pos = [[4, 0], [4, 7]]
        else:
            self

        self.lin_layout = np.array([0] * 64, dtype="short")

    def make_move(self, move):
        if self.layout[move[0][0]][move[0][1]] == "":
            raise ValueError("you cant move empty square")

        self.layout[move[1][0]][move[1][1]] = self.layout[move[0][0]][move[0][1]]
        self.layout[move[0][0]][move[0][1]] = ""
        return self

    def place(self, square, piece):
        self.layout[square[0]][square[1]] = piece
        return self

    def remove(self, square):
        self.layout[square[0]][square[1]] = ""
        return self

    @staticmethod
    def to_from_linear(layout):
        out = []
        if len(layout) == 8:

            for column in layout:

                for i in range(8):

                    out.append(column[i])
        else:
            index = 0
            for i in range(8):

                out.append([])
                for j in range(8):

                    out[i].append(layout[index])
                    index += 1

        return out





if __name__ == "__main__":
    pos = Layout(start=True)
    print(pos.lin_layout)
    pos.lin_layout = pos.to_from_linear(pos.layout)
    print(pos.lin_layout)
    pos.layout = pos.to_from_linear(pos.lin_layout)
    print(pos.layout)
