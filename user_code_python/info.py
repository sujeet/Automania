from bfs import *

class Info:

    def __init__(self):

        self.my_posn = Position()
        self.enemy_posn = Position()
        self.map = Map()

        self.my_traverser_posn = [] 
        self.my_traverser_move = []
        self.my_traverser_distance = []

        self.my_nitro_posn = []
        self.my_nitro_move = []
        self.my_nitro_distance = []

        self.enemy_traverser_posn = []
        self.enemy_traverser_move = []
        self.enemy_traverser_distance = []

        self.enemy_nitro_posn = []
        self.enemy_nitro_move = []
        self.enemy_nitro_distance = []


    def initial_read(self):
	
        self.game_ended = 0

        self.my_tag = raw_input()	
        self.enemy_tag = raw_input()
        self.temp = raw_input()

        self.a = self.temp.split(' ')
        self.x = int(self.a[0])
        self.y = int(self.a[1])

    	self.my_posn.initialize(self.x,self.y) 
	
        self.temp = raw_input()
        self.a = self.temp.split(' ')
        self.x = int(self.a[0])
        self.y = int(self.a[1])

        self.enemy_posn.initialize(self.x,self.y)

    	self.map_file = raw_input()	
	
        self.map.initialize(self.map_file)	
        return


    def read_info(self):

        self.num_ip =  input()

        if( self.num_ip == 0 ):
	    
		    self.game_ended = 1

        for i in range(self.num_ip):	

            self.temp = raw_input()
            self.a = self.temp.split(' ')
            self.x = int(self.a[0])
            self.y = int(self.a[1])
            self.element = self.a[2]

            self.posn = Position(self.x,self.y)
            self.map.set_symbol(self.posn,self.element)

            if( self.element == self.my_tag ):
	    	
                self.my_posn.initialize(self.x,self.y) #update my position.


            if( self.element == self.enemy_tag ):
	    	
                self.enemy_posn.initialize(self.x,self.y) #update enemy position.

            self.temp = raw_input()
            self.a = self.temp.split(' ')
            self.nitro_moves_left = int(self.a[0])
            self.traversers = int( self.a[1] )




    def compute_details(self):

	    #This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
    	#This can also compute other details like the area of the current region in which the bike resides etc..

    	self.player1 = bfs()
        self.player2 = bfs()
        self.player1.compute(self.map,self.my_posn)
        self.player2.compute(self.map,self.enemy_posn)
	
        self.n = len(self.player1.traverser_posn)

        for i in range(self.n):
	
            self.my_traverser_posn.append( self.player1.traverser_posn[i] )
            self.my_traverser_move.append( self.player1.traverser_move[i] )	
            self.my_traverser_distance.append( self.player1.traverser_distance[i] )
	
        self.m = len(self.player1.nitro_posn)

        for i in range(self.m):
	
            self.my_nitro_posn.append( self.player1.nitro_posn[i] )
            self.my_nitro_move.append( self.player1.nitro_move[i] )	
            self.my_nitro_distance.append( self.player1.nitro_distance[i] )
	
        self.p = len(self.player2.traverser_posn)

        for i in range(self.p):
	
            self.enemy_traverser_posn.append( self.player2.traverser_posn[i] )
            self.enemy_traverser_move.append( self.player2.traverser_move[i]	)
            self.enemy_traverser_distance.append( self.player2.traverser_distance[i] )
	
        self.q = len(self.player1.nitro_posn)

        for i in range(self.q):
	
            self.enemy_nitro_posn.append( self.player2.nitro_posn[i] )
            self.enemy_nitro_move.append( self.player2.nitro_move[i] )
            self.enemy_nitro_distance.append( self.player2.nitro_distance[i] )

	
    def end_game(self):

	    return self.game_ended



