from constants import *

class Position:

    def __init__( self, a = 'a', b  = 'b'):
        self.x = a
        self.y = b

    def initialize( self, a, b ):
        self.x = a
        self.y = b

    def update(direction):

        if direction == EAST :
            self.x += 1
            self.y += 0

        if direction == WEST :
            self.x -= 1
            self.y += 0

        if direction == NORTH :
            self.x += 0
            self.y -= 1

        if direction == SOUTH :
            self.x += 0
            self.y += 1


