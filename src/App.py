import pygame


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
        self.size = self.square_size*10 + self.boundary_size*2, self.square_size*10 + self.boundary_size*2

    # called once to start program
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
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

    def draw_chessboard(self):
        # drawing chess squares
        square_colors = [self.colors["ivory"], self.colors["acacia"]]
        for i in range(10):
            for j in range(10):
                square = pygame.Rect(i*self.square_size + self.boundary_size, j*self.square_size + self.boundary_size,
                                     self.square_size, self.square_size)
                pygame.draw.rect(self.display, square_colors[(i+j) % 2], square)

        # drawing board outline
        line_thickness = 2
        line_length = 10 * self.square_size
        for i in range(11):     # horizontal
            start_pos = (self.boundary_size, i*self.square_size + self.boundary_size)
            end_pos = (line_length + self.boundary_size, i*self.square_size + self.boundary_size)
            pygame.draw.line(self.display, self.colors["board_outline"], start_pos, end_pos, line_thickness)
        for i in range(11):     # vertical
            start_pos = (i*self.square_size + self.boundary_size, self.boundary_size)
            end_pos = (i*self.square_size + self.boundary_size, line_length + self.boundary_size)
            pygame.draw.line(self.display, self.colors["board_outline"], start_pos, end_pos, line_thickness)

        # drawing square names
        """
        font = pygame.font.SysFont('Arial', 48)
        text_color = self.colors["board_outline"]
        text_surface = font.render("A", True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.bottom = 10*self.square_size
        text_rect.centerx = self.square_size / 2
        self._display.blit(text_surface, text_rect)
        """

    def coordinate_to_square(self, coordinates):
        chess_coordinates = (coordinates[0]-self.boundary_size, coordinates[1]-self.boundary_size)
        board_size = 10 * self.square_size
        if chess_coordinates[0] > board_size or chess_coordinates[1] > board_size:
            return None
        if chess_coordinates[0] < 0 or chess_coordinates[1] < 0:
            return None
        square = (chess_coordinates[0] // self.square_size, chess_coordinates[1] // self.square_size)
        return square

    def square_to_coordinate(self, square):
        pass


if __name__ == "__main__":
    theApp = App()
    theApp.on_init()
