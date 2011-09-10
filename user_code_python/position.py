from constants import *

class Position:

    def __init__( self, a = 'a', b  = 'b'):
        self.x = a  # x and y co ordinate

        self.y = b

    def initialize( self, a, b ):
        self.x = a  # x and y co ordinate
        self.y = b

    def update(self,direction):  #this function updates the current position to move in the target direction.

	if direction == EAST :
            self.y += 1
            if self.y == MAX_Y:
                self.y = 0


        if direction == WEST :
            self.y -= 1
            if self.y == -1 :
                self.y = MAX_Y - 1

        if direction == NORTH :
            self.x -= 1
            if self.x == -1 :
                self.x = MAX_X -1 

        if direction == SOUTH :
            self.x += 1
            if self.x == MAX_X :
                self.x = 0
        

