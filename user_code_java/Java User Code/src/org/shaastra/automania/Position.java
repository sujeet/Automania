/**
 * 
 */
package org.shaastra.automania;

/**
 *
 */
public class Position {
	
	public int x;
	public int y;
	
	/**
	 * A constructor.
	 * @param x
	 * @param y
	 */
	public Position(int x, int y)
	{
		this.x = x;
		this.y = y;
	}
	
	/**
	 * Function to initialize.
	 * @param x
	 * @param y
	 */
	public void initialize(int x, int y)
	{
		
	}
	
	public void update(int direction)
	{
		if( direction == GlobalDataStore.EAST )
		{	
			y += 1;
	        if( y == GlobalDataStore.MAX_Y )
	            y = 0;
		}
		if( direction == GlobalDataStore.WEST )
		{	
			y -= 1;
	        if( y == -1 )
	            y = GlobalDataStore.MAX_Y - 1;
		}
		if( direction == GlobalDataStore.NORTH )
		{	
			x -= 1;
	        if( x == -1 )
	            x = GlobalDataStore.MAX_X - 1;

		}
		if( direction == GlobalDataStore.SOUTH )
		{	
			x += 1;
	        if( x == GlobalDataStore.MAX_X )
	            x = 0;
		}
	}

}
