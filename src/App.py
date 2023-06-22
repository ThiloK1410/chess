import os

import pygame
from Piece import Piece


class App:
    # main function from where everything is called
    def __init__(self):
        # initiating a clock and setting timer of the application
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.time_per_frame = 1000 / self.fps

        # defining colors for the chessboard squares
        self.colors = {"black": (0, 0, 0), "white": (255, 255, 255), "board_outline": (63, 63, 63),
                       "ivory": (255, 233, 197), "acacia": (183, 94, 18)}
        self._running = True
        self.display = None

        # setting dimensions of the chessboard
        self.boundary_size = 20
        self.square_size = 80
        self.size = (self.square_size*8 + self.boundary_size*2, self.square_size*8 + self.boundary_size*2)

        self.temporary_start_layout = [["r", "n", "b", "q", "k", "b", "n", "r"],
                                       ["p", "p", "p", "p", "p", "p", "p", "p"],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       ["P", "P", "P", "P", "P", "P", "P", "P"],
                                       ["R", "N", "B", "Q", "K", "B", "N", "R"]]

        self.board_state = [[None]*8 for i in range(8)]

    # called once to start program
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.activate_layout(self.temporary_start_layout)

        self.on_execute()

    # handles player inputs
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
        # when a mousebutton is clicked, prints coordinates on the chessboard grid to console output
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            square = self.coordinate_to_square(mouse_pos)
            print(square)

    # loop which will be executed at fixed rate (for physics, animations and such)
    def on_loop(self):
        pass

    # loop which will only be called when enough cpu time is available
    def on_render(self):
        self.display.fill(self.colors["ivory"])

        self.draw_chessboard()

        self.draw_chess_pieces(self.board_state)

        pygame.display.update()

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        previous = pygame.time.get_ticks()
        lag = 0.0

        # advanced game loop to call on_loop() at fixed rate and on_render() as fast as possible
        # (kinda overkill right now) (also not relevant)
        while self._running:
            current = pygame.time.get_ticks()
            elapsed = current - previous
            lag += elapsed
            previous = current

            for event in pygame.event.get():
                self.on_event(event)

            while lag > self.time_per_frame:
                self.on_loop()
                lag -= self.time_per_frame
            self.on_render()
        self.on_cleanup()

    # -------- custom functions below here --------

    # draws the empty chessboard interchangeable design variables inside
    def draw_chessboard(self):
        # drawing chess squares
        square_colors = [self.colors["ivory"], self.colors["acacia"]]
        for i in range(8):
            for j in range(8):
                square = pygame.Rect(i*self.square_size + self.boundary_size, j*self.square_size + self.boundary_size,
                                     self.square_size, self.square_size)
                pygame.draw.rect(self.display, square_colors[(i+j) % 2], square)

        # drawing board outline
        line_thickness = 2
        line_length = 8 * self.square_size
        for i in range(9):     # horizontal
            start_pos = (self.boundary_size, i*self.square_size + self.boundary_size)
            end_pos = (line_length + self.boundary_size, i*self.square_size + self.boundary_size)
            pygame.draw.line(self.display, self.colors["board_outline"], start_pos, end_pos, line_thickness)
        for i in range(9):     # vertical
            start_pos = (i*self.square_size + self.boundary_size, self.boundary_size)
            end_pos = (i*self.square_size + self.boundary_size, line_length + self.boundary_size)
            pygame.draw.line(self.display, self.colors["board_outline"], start_pos, end_pos, line_thickness)

        # defining font and content
        font = pygame.font.SysFont('Arial Black', 12)
        letters = ("A", "B", "C", "D", "E", "F", "G", "H")
        numbers = ("8", "7", "6", "5", "4", "3", "2", "1")

        # writing letters in all the bottom squares
        for i, x in enumerate(letters):
            text_color = square_colors[i % 2]
            text_surface = font.render(x, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.centerx = self.boundary_size + i*self.square_size + self.square_size / 2
            text_rect.bottom = self.boundary_size + 8*self.square_size
            self.display.blit(text_surface, text_rect)

        # writing numbers in all the left squares
        for i, x in enumerate(numbers):
            text_color = square_colors[(i+1) % 2]
            text_surface = font.render(x, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.centery = self.boundary_size + i*self.square_size + self.square_size / 2
            text_rect.left = self.boundary_size + 4
            self.display.blit(text_surface, text_rect)

    # draws a given board_state
    @classmethod
    def draw_chess_pieces(cls, board_state):
        for i in board_state:
            for j in i:
                if j is not None:
                    j.draw()

    # converts window coordinates to square indexes
    def coordinate_to_square(self, coordinates):
        chess_coordinates = (coordinates[0]-self.boundary_size, coordinates[1]-self.boundary_size)
        board_size = 10 * self.square_size
        if chess_coordinates[0] > board_size or chess_coordinates[1] > board_size:
            return None
        if chess_coordinates[0] < 0 or chess_coordinates[1] < 0:
            return None
        square = (chess_coordinates[0] // self.square_size, chess_coordinates[1] // self.square_size)
        return square

    # converts square indexes to window coordinates
    def square_to_coordinate(self, square):
        coordinates = (square[0]*self.square_size+self.boundary_size,
                       square[1]*self.square_size+self.boundary_size)
        return coordinates

    # gets a 2d array fen-layout as input and sets the board accordingly
    def activate_layout(self, layout):
        for row, x in enumerate(self.board_state):
            for column, element in enumerate(x):
                if layout[row][column] is None:
                    self.board_state[row][column] = None
                else:
                    self.board_state[row][column] = Piece(self, layout[row][column], (row, column))


if __name__ == "__main__":
    theApp = App()
    theApp.on_init()
