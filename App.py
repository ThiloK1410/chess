import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        schachbrett = ChessBoard()
        schachbrett.pack(side="left")


class ChessBoard(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.squares = [[None] * 8] * 8  # [0][0] is square A1 -> [7][7] = H8
        self.colors = ("#598c00", "white")
        self.setup_board()


    def setup_board(self):
        square = tk.PhotoImage(width=1, height=1)
        for i in range(8):
            for j in range(8):
                self.squares[i][j] = tk.Button(self, image=square, width=90, height=90, background=self.colors[(i+j)%2], command="self.change_square(self, i, j)")
                self.squares[i][j].grid(row=i, column=j)

    def change_square(self, i, j):
        square = tk.Image(width=1, height=1, file="/pieces/png/b_bishop.png", imgtype="png")
        self.squares[i][j] = tk.Button(self, image=square)

if __name__ == "__main__":
    app = App()
    app.mainloop()
