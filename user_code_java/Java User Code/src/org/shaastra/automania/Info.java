/**
 * 
 */
package org.shaastra.automania;

import java.io.*;
import java.util.*;

import org.shaastra.automania.*;
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
	private BufferedReader in ;
	
	public int my_tag;
	public int enemy_tag;
	public Position my_posn;
	public Position enemy_posn;
	public Map map;
	
	public ArrayList<Position> my_power1_posn;
	public ArrayList<Integer> my_pwer1_move;
	
	public ArrayList<Position> my_power2_posn;
	public ArrayList<Integer> my_power2_move;

	public ArrayList<Position> enemy_power1_posn;
	public ArrayList<Integer> enemy_power1_move;

	public ArrayList<Position> enemy_power2_posn;
	public ArrayList<Integer> enemy_power2_move;
	
	/**
	 * Initially
	 * @throws IOException 
	 */
	public void initial_read() throws IOException
	{
		game_ended = 0;
		int x = 0, y = 0;
		
		this.in = new BufferedReader(new InputStreamReader(System.in));
	    try {
			my_tag = in.read();
			enemy_tag = in.read();
		    x = in.read();
		    y = in.read();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
		System.out.println("my_tag = " + my_tag + " enemy_tag = " + enemy_tag + "\n");
		System.out.println("x = " + x + " y = " + y);
	    // x and y are my initial positions
	    my_posn.initialize(x, y);
	    
	    try {
			x = in.read();
		    y = in.read();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    enemy_posn.initialize(x, y);
	    
	    try {
			map_file = in.readLine();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
		map = new Map();
		map.initialize(map_file);
		
	}
	
	void read_info()
	{
		int num_ip = 0;
		try {
			num_ip = in.read();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if( num_ip == 0)
		{
			game_ended = 1;
			return;	
		}

		for( int i=0;i<num_ip;i++)
		{
			int x = 0, y = 0;
			char element = 0;
			try {
				x = in.read();
				y = in.read();
				element = (char) in.read();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			Position posn = new Position(x,y);
			map.set_symbol(posn,element);
			
			if(element == my_tag )
			{
				my_posn.initialize(x, y);
			}
			
			if(element == enemy_tag)
			{
				enemy_posn.initialize(x, y);
			}
		}
	}
	
	void compute_details()
	{
		//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
		//This can also compute other details like the area of the current region in which the bike resides etc..
		Bfs player1,player2;
		player1.compute(map,my_posn);
		player2.compute(map,enemy_posn);
		
		int n = player1.power1_posn.size();

		my_power1_posn.resize(n);
		my_power1_move.resize(n);
		for( int i=0;i<n;i++)
		{
			my_power1_posn[i] = player1.power1_posn[i];
			my_power1_move[i] = player1.power1_move[i];	

		}
		
		int m = player1.power2_posn.size();

		my_power2_posn.resize(m);
		my_power2_move.resize(m);
		for( int i=0;i<m;i++)
		{
			my_power2_posn[i] = player1.power2_posn[i];
			my_power2_move[i] = player1.power2_move[i];	

		}
		
		int p = player2.power1_posn.size();

		enemy_power1_posn.resize(p);
		enemy_power1_move.resize(p);
		for( int i=0;i<p;i++)
		{
			enemy_power1_posn[i] = player2.power1_posn[i];
			enemy_power1_move[i] = player2.power1_move[i];	

		}
		
		int q = player1.power2_posn.size();
		
		enemy_power2_posn.resize(q);
		enemy_power2_move.resize(q);
		for( int i=0;i<q;i++)
		{
			enemy_power2_posn[i] = player2.power2_posn[i];
			enemy_power2_move[i] = player2.power2_move[i];	

		}

	}

	int end_game()
	{
		return game_ended;
	}


}
