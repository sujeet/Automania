from position import *

class Map:

    def initialize(self, file_name ): #this function is on no use to the user.


        self.n = MAX_X  #dimensions of the array


        self.map_file = open (file_name,"r")
            
        self.array = []

        self.temp = self.map_file.read()

        for i in range( MAX_X ):
            self.array.append([])
            for j in range( MAX_Y ):
                self.array[i].append(self.temp[i*(MAX_X+1)+j])


    def set_symbol(self, pos, symbol): #this function updates the map with the given symbol in the given position.

        if pos.x < self.n and pos.x >= 0 and pos.y >= 0 or pos.y < self.n :
		self.array[pos.x][pos.y] = symbol


    def get_symbol( self, pos ):  #this function is used to find the element present in a given position in the map.

        if pos.x < self.n and pos.x >= 0 and pos.y >= 0 or pos.y < self.n :
		return self.array[pos.x][pos.y]
	return 'W' # this is a warning symbol


    def moveable_position( self, pos ): #this function is to check whether the given position is a moveable position or not. If the position contains a trail or wall or if the position is out of the bounds of the map, then it is not a moveable

        if pos.x < 0 or pos.x >= self.n or pos.y < 0 or pos.y >= self.n :
	    	return 0
        if self.get_symbol( pos ) == EMPTY or self.get_symbol( pos ) == TRAVERSER or self.get_symbol( pos ) == NITRO :
	    	return 1	#NOTE THIS MUST BE CHANGED IF PARALLEL PLAY IS DECIDED.
    	return 0
	
	
