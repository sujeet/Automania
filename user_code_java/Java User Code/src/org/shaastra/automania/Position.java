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
	
	public void update(int direction[])
	{
		this.x += direction[0];
		this.y += direction[1];
	}

}
