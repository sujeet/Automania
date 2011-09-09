/**
 * 
 */
package org.shaastra.automania;

/**
 *
 */
public class Node {
	

	public Position cur_posn;
	public int initial_move;
	public int distance;

	
	Node(Position p,int i,int d)
	{
		cur_posn = new Position(p.x, p.y);
		initial_move = i;
		distance = d;
	}

}
