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
	 * User is requested not to try and change this.
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		Info my_info = new Info();
		BotBrain my_bot = new BotBrain();
		
	    String res[] = { "NORTH" , "WEST" , "SOUTH" , "EAST" };
	    my_info.initial_read();
	    if(my_info.end_game() != 0)
	    {
	    }
			my_info.compute_details();
	    
		while(true)
		{

			int result = my_bot.play_move(my_info);
			if( result > 4 || result < 1 )
			{
				System.out.println("INVALID");
				System.out.flush();
			}
			else
			{
				System.out.println(res[result]);
				System.out.flush();
			}
			my_info.read_info();
			if( my_info.end_game() == 1 )
				break;
			
			my_info.compute_details();
				
		}

	}

}
