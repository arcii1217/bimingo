from game.piece import Piece

class Player:
def __init__(self, name, secret_color):
self.name = name
self.secret_color = secret_color
self.pieces = self._init_pieces()

def _init_pieces(self):
pieces = []
pieces += [Piece("Y", "R") for _ in range(3)]
pieces += [Piece("B", "Y") for _ in range(3)]
pieces += [Piece("R", "B") for _ in range(3)]
return pieces

def has_pieces(self):
return len(self.pieces) > 0
