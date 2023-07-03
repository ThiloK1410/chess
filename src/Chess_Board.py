import pygame

from Chess_Engine import Engine


class App:
    # main function from where everything is called
    def __init__(self):
        # initiating a clock and setting timer of the application
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.time_per_frame = 1000 / self.fps

        # Engine for handling all of logic
        self.engine = Engine()

        # defining colors for the chessboard squares
        self.colors = {"black": (0, 0, 0), "white": (255, 255, 255), "board_outline": (63, 63, 63),
                       "ivory": (255, 233, 197), "acacia": (183, 94, 18)}
        self._running = True
        self.display = None

        # images of all chess pieces
        self.valid_moves = []
        self.valid_move_size_factor = 0.5
        self.size_factor = 0.8
        self.piece_types = {"r": "b_rook.png", "n": "b_knight.png", "b": "b_bishop.png",
                            "q": "b_queen.png", "k": "b_king.png", "p": "b_pawn.png",
                            "R": "w_rook.png", "N": "w_knight.png", "B": "w_bishop.png",
                            "Q": "w_queen.png", "K": "w_king.png", "P": "w_pawn.png",
                            "move": "black_circle.png", "take": "red_square.png"}

        # setting dimensions of the chessboard
        self.boundary_size = 20
        self.square_size = 80
        self.size = (self.square_size * 8 + self.boundary_size * 2, self.square_size * 8 + self.boundary_size * 2)

        self.selected_square = None

    # called once to start program
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.engine.set_layout(self.engine.start_pos)

        self.on_execute()

    # handles player inputs
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
        # when a mouse button is clicked, prints coordinates on the chessboard grid to console output
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_buttons = pygame.mouse.get_pressed(5)
            if mouse_buttons[0]:
                mouse_pos = pygame.mouse.get_pos()
                square = list(self.coordinate_to_square(mouse_pos))
                if square in self.valid_moves[0]:
                    self.engine.make_move([self.selected_square, square])
                    self.selected_square = None
                else:
                    self.selected_square = square
                print(self.selected_square)

    # loop which will be executed at fixed rate (for physics, animations and such)
    def on_loop(self):
        pass

    # loop which will only be called when enough cpu time is available
    def on_render(self):
        self.display.fill(self.colors["ivory"])

        self.draw_chessboard()

        self.valid_moves = self.engine.get_valid_moves(self.selected_square)
        self.draw_valid_moves(self.valid_moves)

        self.draw_chess_pieces(self.engine.get_layout())

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
                square = pygame.Rect(i * self.square_size + self.boundary_size,
                                     j * self.square_size + self.boundary_size,
                                     self.square_size, self.square_size)
                pygame.draw.rect(self.display, square_colors[(i + j) % 2], square)

        # drawing board outline
        line_thickness = 2
        line_length = 8 * self.square_size
        for i in range(9):  # horizontal
            start_pos = (self.boundary_size, i * self.square_size + self.boundary_size)
            end_pos = (line_length + self.boundary_size, i * self.square_size + self.boundary_size)
            pygame.draw.line(self.display, self.colors["board_outline"], start_pos, end_pos, line_thickness)
        for i in range(9):  # vertical
            start_pos = (i * self.square_size + self.boundary_size, self.boundary_size)
            end_pos = (i * self.square_size + self.boundary_size, line_length + self.boundary_size)
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
            text_rect.centerx = self.boundary_size + i * self.square_size + self.square_size / 2
            text_rect.bottom = self.boundary_size + 8 * self.square_size
            self.display.blit(text_surface, text_rect)

        # writing numbers in all the left squares
        for i, x in enumerate(numbers):
            text_color = square_colors[(i + 1) % 2]
            text_surface = font.render(x, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.centery = self.boundary_size + i * self.square_size + self.square_size / 2
            text_rect.left = self.boundary_size + 4
            self.display.blit(text_surface, text_rect)

    # draws a given board_state
    def draw_chess_pieces(self, board_state):
        for row, i in enumerate(board_state):
            for column, j in enumerate(i):
                if j is not None:
                    image_path = "../pieces/png/" + self.piece_types[j]
                    image = pygame.transform.scale(pygame.image.load(image_path), (self.square_size * self.size_factor,
                                                                                   self.square_size * self.size_factor))
                    image_rect = image.get_rect()
                    position = self.square_to_coordinate([row, column])
                    image_rect.center = (
                        position[0] + self.square_size / 2, position[1] + self.square_size / 2)
                    self.display.blit(image, image_rect)

    # draws a given list of valid moves
    def draw_valid_moves(self, squares):
        if squares is None:
            print("no valid moves")
            return
        path = "../pieces/png/" + self.piece_types["move"]
        image = pygame.transform.scale(pygame.image.load(path),
                                       (self.square_size * self.valid_move_size_factor,
                                        self.square_size * self.valid_move_size_factor))
        image_rect = image.get_rect()
        for square in squares[0]:
            position = self.square_to_coordinate(square)
            image_rect.center = (
                position[0] + self.square_size / 2, position[1] + self.square_size / 2
            )
            self.display.blit(image, image_rect)

    # converts window coordinates to square indexes
    def coordinate_to_square(self, coordinates):
        chess_coordinates = (coordinates[0] - self.boundary_size, coordinates[1] - self.boundary_size)
        board_size = 10 * self.square_size
        if chess_coordinates[0] > board_size or chess_coordinates[1] > board_size:
            return None
        if chess_coordinates[0] < 0 or chess_coordinates[1] < 0:
            return None
        square = (chess_coordinates[0] // self.square_size, chess_coordinates[1] // self.square_size)
        return square

    # converts square indexes to window coordinates
    def square_to_coordinate(self, square):
        coordinates = (square[0] * self.square_size + self.boundary_size,
                       square[1] * self.square_size + self.boundary_size)
        return coordinates


if __name__ == "__main__":
    theApp = App()
    theApp.on_init()
