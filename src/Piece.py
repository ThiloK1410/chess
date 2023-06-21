import pygame.image


class Piece:
    def __init__(self, app, image, position):
        self.app = app
        self.img = pygame.image.load(image)
        self.square_pos = position

    def draw(self):
        self.app.display.blit(self.img, )


