/**
 * 
 */
package org.shaastra.automania;

import java.io.*;

/**
 * Info class gathers and provides all the helpful information
 * to the user.
 * @author devesh
 * 
 * Detailed explanation here.(TO BE DONE)
 */
public class Info {
	
	private int game_ended;
	private String map_file;
	
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public int tag;
	
	/**
	 * Initially
	 */
	public void initial_read()
	{
		game_ended = 0;
		
	    tag = in.read();
	    map_file = in.readLine();
	    
		Map map = new Map(map_file);
		
	}
	
	void read_info()
	{
		int num_ip;
		num_ip = in.read();
		
		if( num_ip == 0)
		{
			game_ended = 1;
			return;	
		}

		for( int i=0;i<num_ip;i++)
		{
			int x, y;
			char element;
			x = in.read();
			Position posn = new Posn(x,y);
			map.set_symbol(posn,element);
		}
	}
	
	void compute_details()
	{
		//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
		//This can also compute other details like the area of the current region in which the bike resides etc..
	}

	int end_game()
	{
		return game_ended;
	}


	}
	

}
