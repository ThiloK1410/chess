import pygame.image


class Piece:
    def __init__(self, app, image, position):
        self.app = app
        print(type(self.app))
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img, (self.app.square_size*0.8, self.app.square_size*0.8))
        self.square_pos = position

    def draw(self):
        self.app.display.blit(self.img, self.app.square_to_coordinate(self.square_pos))


