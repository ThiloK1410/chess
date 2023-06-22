import pygame.image


class Piece:
    piece_types = {"r": "b_rook.png", "n": "b_knight", "b": "b_bishop.png",
                   "q": "b_queen.png", "k": "b_king.png", "p": "b_pawn.png",
                   "R": "w_rook.png", "N": "w_knight.png", "B": "w_bishop.png",
                   "Q": "w_queen.png", "K": "w_king.png", "P": "w_pawn.png"}

    def __init__(self, app, piece_type, position):
        self.app = app
        self.square_pos = position
        self.color = [0 if piece_type.isupper() else 1]     # 0=white; 1=black
        print(self.color)

        self.size_factor = 0.7      # 1 = size of square
        image_path = "pieces/png/" + Piece.piece_types[piece_type]
        self.img = pygame.image.load(image_path)
        self.img = pygame.transform.scale(self.img, (self.app.square_size*self.size_factor,
                                                     self.app.square_size*self.size_factor))
        self.img_rect = self.img.get_rect()

    def draw(self):
        position = self.app.square_to_coordinate(self.square_pos)
        self.img_rect.center = (position[0] + self.app.square_size/2, position[1] + self.app.square_size/2)
        self.app.display.blit(self.img, self.img_rect)


