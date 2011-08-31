from map import *
from Queue import *


class node:

    def __init__( self, p, i, d):

        self.cur_posn = Position()
    	self.cur_posn.initialize(p.x,p.y)	
        self.initial_move = i
    	self.distance = d		


class bfs:

    def __init__(self):

        self.power1_posn = []
        self.power2_posn = []
        self.power1_move = []
        self.power2_move = []
        self.power1_distance = []
        self.power2_distance = []

    def compute( self, map,my_posn ):

    	self.Q = queue.queue()		

        self.temp_posn = Position()
        
        self.visited = [[0]*(MAX_X+2) for x in xrange(MAX_Y+2)]


    	#initial pushes
    
	    #this part can be compressed

    	self.temp_posn = my_posn
        self.temp_posn.update( EAST )

        if( map.moveable_position( self.temp_posn) ):

    		self.n = node(self.temp_posn,EAST,1)
	    	self.Q.put(self.n)

    	self.temp_posn = my_posn
        self.temp_posn.update( WEST )

        if( map.moveable_position( self.temp_posn) ):

    		self.n = node(self.temp_posn,WEST,1)
	    	self.Q.put(self.n)

    	self.temp_posn = my_posn
        self.temp_posn.update( NORTH )

        if( map.moveable_position( self.temp_posn) ):

            self.n = node(self.temp_posn,NORTH,1)
            self.Q.put(self.n)

    	self.temp_posn = my_posn
        self.temp_posn.update( SOUTH )

        if( map.moveable_position( self.temp_posn) ):

            self.n = node(self.temp_posn,SOUTH,1)
            self.Q.put(self.n)
	

    #The main loop


        while not self.Q.empty():

            self.n = self.Q.get()
            self.visited[self.n.cur_posn.x][self.n.cur_posn.y] = 1

            if map.get_symbol( self.n.cur_posn ) == POWER1 :
	    	
                self.power1_posn.append(self.n.cur_posn)
                self.power1_move.append(self.n.initial_move)
                self.power1_distance.append(self.n.distance)
		

            if map.get_symbol( self.n.cur_posn ) == POWER2 :
		
                self.power2_posn.append(self.n.cur_posn)
                self.power2_move.append(self.n.initial_move)
                self.power2_distance.append(self.n.distance)
		
		
	    	#this part can be compressed.
            self.temp_posn = self.n.cur_posn 
            self.temp_posn.update( EAST )
            if map.moveable_position( self.temp_posn) and self.visited[self.temp_posn.x][self.temp_posn.y] == 0 :
		
                self.n2 = node(self.temp_posn,self.n.initial_move,self.n.distance+1)
                self.Q.put(self.n2)
		

            self.temp_posn = self.n.cur_posn
            self.temp_posn.update( WEST )
            if map.moveable_position( self.temp_posn)  and self.visited[self.temp_posn.x][self.temp_posn.y] == 0 :
		
    			self.n2 = node(self.temp_posn,self.n.initial_move,self.n.distance+1)
	    		self.Q.put(self.n2)
		
	
            self.temp_posn = self.n.cur_posn
            self.temp_posn.update( NORTH )
            if map.moveable_position( self.temp_posn) and self.visited[self.temp_posn.x][self.temp_posn.y] == 0 :
		
                self.n2 = node(self.temp_posn,self.n.initial_move,self.n.distance+1)
                self.Q.put(self.n2)
		
	
            self.temp_posn = self.n.cur_posn
            self.temp_posn.update( SOUTH )
            if map.moveable_position( self.temp_posn) and self.visited[self.temp_posn.x][self.temp_posn.y] == 0 :
		
	    		self.n2 = node(self.temp_posn,self.n.initial_move,self.n.distance+1)
		    	self.Q.put(self.n2)
