/**
 * 
 */
package org.shaastra.automania;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

import org.shaastra.automania.*;

/**
 * @author devesh
 *
 */
public class Bfs {
	ArrayList <Position> power1_posn;
	ArrayList <Position> power2_posn;
	ArrayList <Integer> power1_move;
	ArrayList <Integer> power2_move;
	ArrayList <Integer> power1_distance;
	ArrayList <Integer> power2_distance;
	
	public void compute(Map map, Position my_posn) {
		// TODO Auto-generated method stub
		Queue <Node> Q = new LinkedList <Node>();		

		Position temp_posn;
		int[][] visited;
		visited = new int[(GlobalDataStore.MAX_X)+2][(GlobalDataStore.MAX_Y)+2];

		int i = 0, j = 0;
		for(i = 0; i < GlobalDataStore.MAX_X + 2; i++)
		{
			for(j = 0; j < GlobalDataStore.MAX_Y + 2; j++)
			{
				visited[i][j] = 0;
			}
		}
		//initial pushes
		visited[my_posn.x][my_posn.y] = 1;;

		//this part can be compressed
		temp_posn = my_posn;
		temp_posn.update( GlobalDataStore.EAST );
		if( map.moveable_position( temp_posn) != 0 )	//THIS FUNCTION MUST BE ADDED TO THE MAP CLASS. THIS FUCNTION CHECKS WHETHER THE CURRENT POSTION IN THE MAP IS A MOVEABLE POSITION ( NOT A POSITION OUTSIDE THE MAP AND NOT A WALL OR TRAIL ) 
		{
			Node n = new Node(temp_posn,GlobalDataStore.EAST,1);
			Q.add(n);
			System.out.println("EAST");
		}

		temp_posn = my_posn;
		temp_posn.update( GlobalDataStore.WEST );
		if( map.moveable_position( temp_posn) != 0 )
		{
			Node n = new Node(temp_posn,GlobalDataStore.WEST,1);
			Q.add(n);
			System.out.println("WES");
		}

		temp_posn = my_posn;
		temp_posn.update( GlobalDataStore.NORTH );
		if( map.moveable_position( temp_posn) != 0 )
		{
			Node n = new Node(temp_posn,GlobalDataStore.NORTH,1);
			Q.add(n);
			System.out.println("North");
		}

		temp_posn = my_posn;
		temp_posn.update( GlobalDataStore.SOUTH );
		if( map.moveable_position( temp_posn) != 0)
		{
			Node n = new Node(temp_posn,GlobalDataStore.SOUTH,1);
			Q.add(n);
			System.out.println("south");
		}
		
		//The main loop

		while( !Q.isEmpty())
		{
			System.out.println(Q.size());
			Node n = Q.remove();
			System.out.println(Q.size());
			visited[n.cur_posn.x][n.cur_posn.y] = 1;
			System.out.println(n.cur_posn.x + " " + n.cur_posn.y);
			

			if( map.get_symbol( n.cur_posn ) == GlobalDataStore.POWER1 )
			{
				power1_posn.add(n.cur_posn);
				power1_move.add(n.initial_move);
	            power1_distance.add(n.distance);
			}

			if( map.get_symbol( n.cur_posn ) == GlobalDataStore.POWER2 )
			{
				power2_posn.add(n.cur_posn);
				power2_move.add(n.initial_move);
	            power2_distance.add(n.distance);
			}
			
			//this part can be compressed.
			temp_posn.x = n.cur_posn.x;
			temp_posn.y = n.cur_posn.y;
			temp_posn.update( GlobalDataStore.EAST );
			System.out.println("Temp " + temp_posn.x + " " + temp_posn.y);
			if( map.moveable_position( temp_posn) != 0 )
			{
				if(visited[temp_posn.x][temp_posn.y] == 0 )
				{
					Node n2 = new Node(temp_posn,n.initial_move,n.distance+1);
					System.out.println("Adding node with value" + n2.cur_posn.x + n2.cur_posn.y);
					Q.add(n2);
				}
			}

			temp_posn.x = n.cur_posn.x;
			temp_posn.y = n.cur_posn.y;
			temp_posn.update( GlobalDataStore.WEST );
			System.out.println("Temp " + temp_posn.x + " " + temp_posn.y);
			if( map.moveable_position( temp_posn) != 0 )
			{
				if(visited[temp_posn.x][temp_posn.y] == 0 )
				{
					Node n2 = new Node(temp_posn,n.initial_move,n.distance+1);
					System.out.println("Adding node with value" + n2.cur_posn.x + n2.cur_posn.y);
					Q.add(n2);
				}
			}
		
			temp_posn.x = n.cur_posn.x;
			temp_posn.y = n.cur_posn.y;
			temp_posn.update( GlobalDataStore.NORTH );
			System.out.println("Temp " + temp_posn.x + " " + temp_posn.y);
			if( map.moveable_position( temp_posn) == 0 )
			{
				if(visited[temp_posn.x][temp_posn.y] != 0 )
				{
					Node n2 = new Node(temp_posn,n.initial_move,n.distance+1);
					System.out.println("Adding node with value" + n2.cur_posn.x + n2.cur_posn.y);
					Q.add(n2);
				}
			}
		
			temp_posn.x = n.cur_posn.x;
			temp_posn.y = n.cur_posn.y;
			temp_posn.update( GlobalDataStore.SOUTH );
			System.out.println("Temp " + temp_posn.x + " " + temp_posn.y);
			if( map.moveable_position( temp_posn) == 0 )
			{
				if(visited[temp_posn.x][temp_posn.y] != 0 )
				{
					Node n2 = new Node(temp_posn,n.initial_move,n.distance+1);
					System.out.println("Adding node with value" + n2.cur_posn.x + n2.cur_posn.y);
					Q.add(n2);
				}
			}
		}
	}

}
