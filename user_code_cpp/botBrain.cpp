#include "botBrain.h"

//The user is expected to change this file to write his bot.
int BotBrain::play_move( Info my_info )
{   //This function must return the final move.
	
	//this sample bot tries to play a safe move at every instant.
	Position temp = my_info.my_posn;
	
	temp.update( WEST );
	if( my_info.map.moveable_position( temp ) )
	{
		return 	WEST;
	}
	temp = my_info.my_posn;
	temp.update( EAST );	
	if( my_info.map.moveable_position( temp ) )
		return 	EAST;
	temp = my_info.my_posn;
	temp.update( NORTH );	
	if( my_info.map.moveable_position( temp ) )
		return 	NORTH;
	return SOUTH;
}

	
