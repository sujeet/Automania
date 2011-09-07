from map import *
from Queue import *


class node:

    def __init__( self, p, i, d):

        self.cur_posn = Position()
    	self.cur_posn.initialize(p.x,p.y)	
        self.initial_move = i
    	self.distance = d		

#This class is not of much importance to the user. This basically implements a bfs function. If the user wants to write his own bfs function, he can use this class as a reference



class bfs:

    def __init__(self):

        self.traverser_posn = []
        self.nitro_posn = []
        self.traverser_move = []
        self.nitro_move = []
        self.traverser_distance = []
        self.nitro_distance = []

    def compute( self, map,my_posn ):

    	self.Q = Queue()		

        self.temp_posn = Position()
        
        self.visited = [[0]*(MAX_X+2) for x in xrange(MAX_Y+2)]


    	#initial pushes
    
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

            if visited[self.n.cur_posn.x][self.n.cur_posn.y] == 1: 
                continue

            self.visited[self.n.cur_posn.x][self.n.cur_posn.y] = 1

            if map.get_symbol( self.n.cur_posn ) == POWER1 :
	    	
                self.traverser_posn.append(self.n.cur_posn)
                self.traverser_move.append(self.n.initial_move)
                self.traverser_distance.append(self.n.distance)
		

            if map.get_symbol( self.n.cur_posn ) == POWER2 :
		
                self.nitro_posn.append(self.n.cur_posn)
                self.nitro_move.append(self.n.initial_move)
                self.nitro_distance.append(self.n.distance)
		
		
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
