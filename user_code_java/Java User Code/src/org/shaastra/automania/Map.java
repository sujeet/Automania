/**
 * 
 */
package org.shaastra.automania;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import org.shaastra.automania.*;

/**
 * Represents the map.
 * @author devesh
 *
 */
public class Map {
	
	int MAP_SIZE;
	char [][]array;
	
	public Map()
	{
	}
	
	/*
	 * Initializes various things.
	 */
	public void initialize(String file_name ) throws IOException
	{
		FileReader map_file = new FileReader(file_name);
		
		BufferedReader bufRead = new BufferedReader(map_file);
		
		String temp;
		temp = bufRead.readLine();
		//System.err.println("the length of map must be");
		//System.err.print(temp.length());
		
		MAP_SIZE = temp.length();
		array = new char[MAP_SIZE][MAP_SIZE];
		
		int i;
		for(i = 0; i < array.length; i++)
		{
			int j;
			
			char debug_var;
			char[] temp_array = temp.toCharArray();
			for(j = 0; j < array[i].length; j++)
			{
				debug_var = temp_array[j];
				array[i][j] = debug_var;
			}
			temp = bufRead.readLine();
		}

	}
	
	/**
	 * Sets a position to a symbol.
	 * @param position
	 * @param symbol
	 */
	public void set_symbol(Position pos, char symbol)
	{
	        if( pos.x >= MAP_SIZE || pos.x < 0 ||  pos.y >= MAP_SIZE || pos.y < 0 );
	                //exception. Disqualify the player?
	        array[pos.x][pos.y] = symbol ;
	}
	

	/**
	 * Gets a symbol at a position.
	 * @param pos Position to get object from.
	 * @return Character at the position and 'W' if invalid.
	 */
	char get_symbol( Position pos )
	{
	        if( pos.x >= MAP_SIZE || pos.x < 0 ||  pos.y >= MAP_SIZE || pos.y < 0 )
	        	return array[pos.x][pos.y];
	        return 'W';
	}

	int moveable_position( Position pos )
	{
	        if( pos.x < 0 || pos.x >= MAP_SIZE || pos.y < 0 || pos.y >= MAP_SIZE )
	                return 0;
	        if( get_symbol( pos ) == GlobalDataStore.EMPTY || get_symbol(pos) == GlobalDataStore.NITRO || get_symbol(pos) == GlobalDataStore.TRAVERSER)
	                return 1;       //NOTE THIS MUST BE CHANGED IF PARALLEL PLAY IS DECIDED.
	        return 0;
	}

}
