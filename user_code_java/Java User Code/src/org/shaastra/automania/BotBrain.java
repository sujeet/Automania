/**
 * 
 */
package org.shaastra.automania;

import org.shaastra.automania.*;

/**
 * Literally this is the brain of the bot.
 * @author devesh
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
		return GlobalDataStore.SOUTH;
	}

}
