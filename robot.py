from enum import Enum


class Direction(Enum):
    NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class Robot:
    def __init__(self, x, y, direction, board, robo_id=1):
        self.x = x
        self.y = y
        self.robo_id = robo_id
        self.direction = direction
        self.board = board

    def move(self):
        if self.direction == Direction.NORTH.value and self.board.is_inbounds(self.x, self.y + 1):
            self.y += 1
        elif self.direction == Direction.EAST.value and self.board.is_inbounds(self.x + 1, self.y):
            self.x += 1
        elif self.direction == Direction.WEST.value and self.board.is_inbounds(self.x - 1, self.y):
            self.x -= 1
        elif self.direction == Direction.SOUTH.value and self.board.is_inbounds(self.x, self.y - 1):
            self.y -= 1

    def left(self):
        self.direction = (self.direction - 1) % 4

    def right(self):
        self.direction = (self.direction + 1) % 4

    def report(self):
        print(f"{self.x},{self.y},{Direction(self.direction).name}")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
