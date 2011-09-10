from info import *

#The user is expected to change this class to write his bot.

class BotBrain:

    def play_move( self, my_info ):

	#this sample bot tries to play a safe move at every instant.

	self.temp = Position()
	self.temp = my_info.my_posn
	self.temp.update( WEST )
	if my_info.map.moveable_position( self.temp ) == 1 :
		return 	WEST

	self.temp = my_info.my_posn
	self.temp.update( EAST )	
	if my_info.map.moveable_position( self.temp ) == 1 :
		return 	EAST

	self.temp = my_info.my_posn
	self.temp.update( NORTH )	
	if my_info.map.moveable_position( self.temp ) == 1 :
		return 	NORTH

	return SOUTH



