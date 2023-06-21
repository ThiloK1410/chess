import pygame.image


class Piece:
    def __init__(self, display, image, position):
        self._display = display
        self.img = pygame.image.load(image)
        self.square_pos = position

    def draw(self):
        self._display.blit(self.img, )


