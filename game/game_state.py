class GameState:
def __init__(self, board, players, turn, total_moves):
self.board = board
self.players = players
self.turn = turn
self.total_moves = total_moves


def current_player(self):
return self.players[self.turn % 2]
