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
 * 
 * Detailed explanation here.(TO BE DONE)
 */
public class Info {
	
	private int game_ended;
	int nitro_moves_left;
	int traversers;

	private String map_file;
	private BufferedReader in ;
	
	public char my_tag;
	public char enemy_tag;
	public char newline_buf;
	public Position my_posn;
	public Position enemy_posn;
	public Map map;
	public String line = "";
	
	public List<Position> my_nitro_posn;
	public List<Integer> my_nitro_move;
	public List<Integer> my_nitro_distance;
	
	public List<Position> my_traverser_posn;
	public List<Integer> my_traverser_move;
	public List<Integer> my_traverser_distance;

	public List<Position> enemy_nitro_posn;
	public List<Integer> enemy_nitro_move;
	public List<Integer> enemy_nitro_distance;

	public List<Position> enemy_traverser_posn;
	public List<Integer> enemy_traverser_move;
	public List<Integer> enemy_traverser_distance;
	
	public Info()
	{
		my_nitro_posn = new ArrayList<Position>();
		my_nitro_move = new ArrayList<Integer>();
		my_nitro_distance = new ArrayList<Integer>();
		
		my_traverser_posn = new ArrayList<Position>();
		my_traverser_move = new ArrayList<Integer>();
		my_traverser_distance = new ArrayList<Integer>();
	
		enemy_nitro_posn = new ArrayList<Position>();
		enemy_nitro_move = new ArrayList<Integer>();
		enemy_nitro_distance = new ArrayList<Integer>();
	
		enemy_traverser_posn = new ArrayList<Position>();
		enemy_traverser_move = new ArrayList<Integer>();
		enemy_traverser_distance = new ArrayList<Integer>();
	}
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
			my_tag = (char) in.read();
			newline_buf = (char) in.read();
			enemy_tag =(char) in.read();
			newline_buf = (char) in.read();
			String line = in.readLine();
			while(line.length()<1)
			{
				line = in.readLine();
			}
			String[] myNumbers=line.split(" ");
			//System.err.println(line + line.length()); 
			y = Integer.parseInt(myNumbers[0]);
			x = Integer.parseInt(myNumbers[1]);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
	    // x and y are my initial positions
		my_posn = new Position(x, y);
	    
	    try {
			String line = in.readLine();
			while(line == "")
			{
				line = in.readLine();
			}
			String[] myNumbers=line.split(" ");
			y = Integer.parseInt(myNumbers[0]);
			x = Integer.parseInt(myNumbers[1]);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		enemy_posn = new Position(x, y);
	    
		map_file = new String();
	    try {
			map_file = in.readLine();
			while(map_file == "")
			{
				map_file = in.readLine();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
		map = new Map();
		map.initialize(map_file);
		
	}
	
	void read_info() throws IOException
	{
		int num_ip = 0;
		try {
			String line = in.readLine();
			while(line.length()< 1)
			{
				line = in.readLine();
			}
			String[] myNumbers=line.split(" ");
			num_ip =  Integer.parseInt(myNumbers[0]);
			//System.err.print(num_ip);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if( num_ip == 0)
		{
			game_ended = 1;
			return;	
		}
		map.set_symbol( my_posn, GlobalDataStore.TRAIL );
		map.set_symbol( enemy_posn, GlobalDataStore.TRAIL );


		for( int i=0;i<num_ip;i++)
		{
			int x = 0, y = 0;
			char element = 0;
			try {
				String line = in.readLine();
				while(line == "")
				{
					line = in.readLine();
				}
				String[] updateValues=line.split(" ");
				//System.err.println(line); 
				y = Integer.parseInt(updateValues[0]);
				x = Integer.parseInt(updateValues[1]);
				element = updateValues[2].charAt(0);
			
				//System.err.print(x);
				//System.err.print(y);
				//System.err.print(element);
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
		String line = in.readLine();
		while(line == "")
		{
			line = in.readLine();
		}
		String[] myNumbers=line.split(" ");
		System.err.println(line);
		nitro_moves_left = Integer.parseInt(myNumbers[0]);
		traversers = Integer.parseInt(myNumbers[1]);
		System.err.println(nitro_moves_left + traversers);
	}
	
	void compute_details()
	{
		//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
		//This can also compute other details like the area of the current region in which the bike resides etc..

		Bfs player1 = new Bfs();
		Bfs player2 = new Bfs();
		player1.compute(map,my_posn);
		player2.compute(map,enemy_posn);
		int n = player1.nitro_posn.size();

		my_nitro_posn.clear();
		my_nitro_move.clear();
	    my_nitro_distance.clear();
	    Position[] nitro_posn = (Position[]) player1.nitro_posn.toArray(new Position[player1.nitro_posn.size()]);
	    Integer[] nitro_move =  (Integer[]) player1.nitro_move.toArray(new Integer[player1.nitro_move.size()]);
	    Integer[] nitro_distance = (Integer[]) player1.nitro_distance.toArray(new Integer[player1.nitro_distance.size()]);
		for( int i=0;i<n;i++)
		{
			my_nitro_posn.add(nitro_posn[i]);
			my_nitro_move.add(nitro_move[i]);	
	        my_nitro_distance.add(nitro_distance[i]);

		}
		
		int m = player1.traverser_posn.size();

		my_traverser_posn.clear();
		my_traverser_move.clear();
	    my_traverser_distance.clear();
	    Position[] traverser_posn = (Position[]) player1.traverser_posn.toArray(new Position[player1.traverser_posn.size()]);
	    Integer[] traverser_move =  (Integer[]) player1.traverser_move.toArray(new Integer[player1.traverser_move.size()]);
	    Integer[] traverser_distance = (Integer[]) player1.traverser_distance.toArray(new Integer[player1.traverser_distance.size()]);
		for( int i=0;i<m;i++)
		{
			my_nitro_posn.add(traverser_posn[i]);
			my_nitro_move.add(traverser_move[i]);	
	        my_nitro_distance.add(traverser_distance[i]);
		}
		
		int p = player2.nitro_posn.size();

		enemy_nitro_posn.clear();
		enemy_nitro_move.clear();
	    enemy_nitro_distance.clear();
	    Position[] player2_nitro_posn = (Position[]) player2.nitro_posn.toArray(new Position[player2.nitro_posn.size()]);
	    Integer[] player2_nitro_move =  (Integer[]) player2.nitro_move.toArray(new Integer[player2.nitro_move.size()]);
	    Integer[] player2_nitro_distance = (Integer[]) player2.nitro_distance.toArray(new Integer[player2.nitro_distance.size()]);
		for( int i=0;i<p;i++)
		{
			enemy_nitro_posn.add(player2_nitro_posn[i]);
			enemy_nitro_move.add(player2_nitro_move[i]);	
	        enemy_nitro_distance.add(player2_nitro_distance[i]);

		}
		
		int q = player1.traverser_posn.size();
		
		enemy_traverser_posn.clear();
		enemy_traverser_move.clear();
	    enemy_traverser_distance.clear();
	    Position[] player2_traverser_posn = (Position[]) player2.traverser_posn.toArray(new Position[player2.traverser_posn.size()]);
	    Integer[] player2_traverser_move =  (Integer[]) player2.traverser_move.toArray(new Integer[player2.traverser_move.size()]);
	    Integer[] player2_traverser_distance = (Integer[]) player2.traverser_distance.toArray(new Integer[player2.traverser_distance.size()]);
		for( int i=0;i<q;i++)
		{
			enemy_traverser_posn.add(player2_traverser_posn[i]);
			enemy_traverser_move.add(player2_traverser_move[i]);	
	        enemy_traverser_distance.add(player2_traverser_distance[i]);
		}

	}

	int end_game()
	{
		return game_ended;
	}


}
