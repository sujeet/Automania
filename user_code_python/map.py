from position import *

class Map:

    def initialize(self, file_name ):

        self.n = MAX_X

        self.map_file = open (file_name,"r")
            
        self.array = []

        self.temp = self.map_file.read()

        for i in range( MAX_X ):
            self.array.append([])
            for j in range( MAX_Y ):
                self.array[i].append(self.temp[i*(MAX_X+1)+j])


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
	
	
