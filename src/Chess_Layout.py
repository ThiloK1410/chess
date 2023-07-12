import numpy as np

class Layout:
    def __init__(self, start=False):

        if start:
            self.layout = [["R", "P", "", "", "", "", "p", "r"],
                           ["N", "P", "", "", "", "", "p", "n"],
                           ["B", "P", "", "", "", "", "p", "b"],
                           ["Q", "P", "", "", "", "", "p", "q"],
                           ["K", "P", "", "", "", "", "p", "k"],
                           ["B", "P", "", "", "", "", "p", "b"],
                           ["N", "P", "", "", "", "", "p", "n"],
                           ["R", "P", "", "", "", "", "p", "r"]]

            self.lin_layout = np.array([0] * 64, dtype="short")

    def to_from_linear(self, layout):
        out = []
        if len(layout) == 8:

            for column in layout:

                for i in range(8):

                    out.append(column[i])

        return out





if __name__ == "__main__":
    pos = Layout(start=True)
    print(pos.lin_layout)
    pos.lin_layout = pos.to_from_linear(pos.layout)
    print(pos.lin_layout)
