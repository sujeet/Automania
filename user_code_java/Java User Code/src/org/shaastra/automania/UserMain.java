/**
 * 
 */
package org.shaastra.automania;

import java.io.IOException;

import org.shaastra.automania.*;

/**
 * @author devesh
 *
 */
public class UserMain {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		Info my_info = new Info();
		BotBrain my_bot = new BotBrain();
		
	    my_info.initial_read();
	    String res[] = { "NORTH" , "WEST" , "SOUTH" , "EAST" };
		System.out.println("NORTH");
	    
		while(true)
		{
			System.out.println("Running inside loop");
			my_info.read_info();
			if( my_info.end_game() == 1 )
				break;
			
			my_info.compute_details();

			int result = my_bot.play_move(my_info);
			if( result > 4 || result < 1 )
			{
				System.out.println("INVALID");
				//disqualify.
			}
			else
			{
				System.out.println(res[result]);
			}
				
		}

	}

}
