class Piece:
def __init__(self, front, back, is_front=True):
self.front = front
self.back = back
self.is_front = is_front


def visible(self):
return self.front if self.is_front else self.back


def hidden(self):
return self.back if self.is_front else self.front


def flip(self):
self.is_front = not self.is_front


def serialize(self):
return {
"front": self.front,
"back": self.back,
"is_front": self.is_front,
}
