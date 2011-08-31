from position import *

class Map:

    def initialize(self, file_name ):

        self.n = MAX_X

        self.map_file = open (file_name,"r")
            
        self.array = [[]*(MAX_X+2) for x in xrange( MAX_Y+2 ) ]

        self.temp = self.map_file.read()

        for i in range( len(self.temp) ):
            for j in range( len(self.temp) ):
                self.array[i][j] = self.temp[i][j]


    def set_symbol(self, pos, symbol):

        if pos.x >= self.n or pos.x < 0 or  pos.y >= self.n or pos.y < 0 :
    		#exception. Disqualify the player?
	    self.array[pos.x][pos.y] = symbol


    def get_symbol( self, pos ):
        if pos.x >= self.n or pos.x < 0 or  pos.y >= self.n or pos.y < 0 :
		    #exception. Disqualify the player?
	    return self.array[pos.x][pos.y]


    def moveable_position( self, pos ):
        if pos.x < 0 or pos.x >= self.n or pos.y < 0 or pos.y >= self.n :
	    	return 0
        if self.get_symbol( pos ) == EMPTY or self.get_symbol( pos ) == POWER1 or self.get_symbol( pos ) == POWER2 :
	    	return 1	#NOTE THIS MUST BE CHANGED IF PARALLEL PLAY IS DECIDED.
    	return 0
	
	
