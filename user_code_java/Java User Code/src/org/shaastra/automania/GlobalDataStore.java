/**
 * 
 */
package org.shaastra.automania;

/**
 * @author devesh
 *
 */
public class GlobalDataStore {
	public static int N_TURNS = 50;
	public static char BIKE_1_SYMBOL = 'a';
	public static char BIKE_2_SYMBOL = 'b';
	public static char WALL = 'w';
	public static char TRAIL = 't';
	public static char EMPTY = '.';
	public static char POWER1 = '1';
	public static char POWER2 = '2';
	public static int NORTH  = 0;
	public static int SOUTH  = 2;
	public static int WEST = 1;
	public static int EAST = 3;
	public static int MAX_X = 50;
	public static int MAX_Y = 50;

	/*
	 ##################################
	 #                                #
	 #  +----------------------> x    #
	 #  |                             #
	 #  |             north           #
	 #  |               ^             #
	 #  |               |             #
	 #  |               |             #
	 #  |    west <-----+-----> east  #
	 #  |               |             #
	 #  |               |             #
	 #  |               V             #
	 #  V             south           #
	 #                                #
	 #  y                             #
	 #                                #
	 ##################################
	*/

}
