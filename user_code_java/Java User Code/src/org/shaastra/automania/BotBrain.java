/**
 * 
 */
package org.shaastra.automania;

import org.shaastra.automania.*;

/**
 * Literally this is the brain of the bot.
 * 
 * This is the class whose functions players need to code.
 */
public class BotBrain {
	
	/**
	 * A Constructor.
	 */
	public BotBrain()
	{
		
	}
	
	/**
	 * Function to decide which move to play.
	 * @param my_info
	 * @return The move to be made.
	 */
	public int play_move(Info my_info)
	{
		// Here is where the user needs to code and return the move.
		Position temp = my_info.my_posn;
		
		temp.update( GlobalDataStore.WEST );
		if( my_info.map.moveable_position( temp ) != 0 )
		{
			return 	GlobalDataStore.WEST;
		}
		temp = my_info.my_posn;
		temp.update( GlobalDataStore.EAST );	
		if( my_info.map.moveable_position( temp ) != 0 )
			return 	GlobalDataStore.EAST;
		temp = my_info.my_posn;
		temp.update( GlobalDataStore.NORTH );	
		if( my_info.map.moveable_position( temp ) != 0 )
			return 	GlobalDataStore.NORTH;
		return GlobalDataStore.SOUTH;
	}

}
