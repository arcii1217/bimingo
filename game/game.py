import random
from game.board import Board
from game.player import Player
from game.game_state import GameState


COLORS = ["Y", "B", "R"]


class Game:
def __init__(self):
random.shuffle(COLORS)
self.players = [
Player("Player 1", COLORS[0]),
Player("Player 2", COLORS[1]),
]
self.state = GameState(Board(), self.players, 0, 0)


def apply_action(self, action_fn):
action_fn()


player = self.state.current_player()
if self.state.board.check_bingo(player.secret_color):
return player


self.state.turn += 1
self.state.total_moves += 1
return None
