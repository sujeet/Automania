/**
 * 
 */
package org.shaastra.automania;

/**
 * @author devesh
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
			x += 1;
			y += 0;
		}
		if( direction == GlobalDataStore.WEST )
		{	
			x -= 1;
			y += 0;
		}
		if( direction == GlobalDataStore.NORTH )
		{	
			x += 0;
			y -= 1;
		}
		if( direction == GlobalDataStore.SOUTH )
		{	
			x += 0;
			y += 1;
		}
	}

}
