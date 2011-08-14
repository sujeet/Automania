/**
 * 
 */
package org.shaastra.automania;

import org.shaastra.automania.*;

/**
 * @author devesh
 *
 */
public class UserMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Info my_info = new Info();
		BotBrain my_bot = new BotBrain();
		
		while(true)
		{
			my_info.read_info();
			if( my_info.end_game() == 1 )
				break;
			
			my_info.compute_details();

			int result = my_bot.get_move(my_info);
			if( result > 4 || result < 1 )
				//disqualify.

			cout<<result;
		}

	}

}
