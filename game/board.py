BOARD_SIZE = 4


class Board:
def __init__(self):
self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def in_bounds(self, x, y):
return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def place(self, x, y, piece):
if self.in_bounds(x, y) and self.grid[x][y] is None:
self.grid[x][y] = piece
return True
return False

def move(self, x1, y1, x2, y2):
if not all(map(self.in_bounds, [x1, x2], [y1, y2])):
return False
if self.grid[x1][y1] is None or self.grid[x2][y2] is not None:
return False
if abs(x1 - x2) + abs(y1 - y2) != 1:
return False
self.grid[x2][y2] = self.grid[x1][y1]
self.grid[x1][y1] = None
return True

def flip(self, x, y):
if self.in_bounds(x, y) and self.grid[x][y]:
self.grid[x][y].flip()
return True
return False

def check_bingo(self, color):
lines = []

for i in range(BOARD_SIZE):
lines.append([(i, j) for j in range(BOARD_SIZE)])
lines.append([(j, i) for j in range(BOARD_SIZE)])

lines.append([(i, i) for i in range(BOARD_SIZE)])
lines.append([(i, BOARD_SIZE - 1 - i) for i in range(BOARD_SIZE)])

for line in lines:
if all(
self.grid[x][y] is not None
and self.grid[x][y].visible() == color
for x, y in line
):
return True
return False

def serialize(self):
return [[cell.serialize() if cell else None for cell in row] for row in self.grid]
