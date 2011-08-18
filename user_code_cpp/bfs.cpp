#include "bfs.h"

node::node( Position p,int i,int d)
{
	cur_posn.initialize(p.x,p.y);	//THIS FUNCTION MUST BE INCLUDED IN POSITION CLASS
	initial_move = i;
	distance = d;		
}



void bfs::compute( Map map,Position my_posn )
{

	queue <node> Q;		

	Position temp_posn;
	vector <vector <int> > visited( MAX_X+2,vector <int> (MAX_Y+2,0) );


	//initial pushes

	//this part can be compressed
	temp_posn = my_posn;
	temp_posn.update( EAST );
	if( map.moveable_position( temp_posn) )	//THIS FUNCTION MUST BE ADDED TO THE MAP CLASS. THIS FUCNTION CHECKS WHETHER THE CURRENT POSTION IN THE MAP IS A MOVEABLE POSITION ( NOT A POSITION OUTSIDE THE MAP AND NOT A WALL OR TRAIL ) 
	{
		node n(temp_posn,EAST,1);
		Q.push(n);
	}

	temp_posn = my_posn;
	temp_posn.update( WEST );
	if( map.moveable_position( temp_posn) )
	{
		node n(temp_posn,WEST,1);
		Q.push(n);
	}

	temp_posn = my_posn;
	temp_posn.update( NORTH );
	if( map.moveable_position( temp_posn) )
	{
		node n(temp_posn,NORTH,1);
		Q.push(n);
	}

	temp_posn = my_posn;
	temp_posn.update( SOUTH );
	if( map.moveable_position( temp_posn) )
	{
		node n(temp_posn,SOUTH,1);
		Q.push(n);
	}
	
	//The main loop

	while( !Q.empty() )
	{
		node n = Q.front();
		Q.pop();
		visited[n.cur_posn.x][n.cur_posn.y] = 1;

		if( map.get_symbol( n.cur_posn ) == POWER1 )
		{
			power1_posn.push_back(n.cur_posn);
			power1_move.push_back(n.initial_move);
		}

		if( map.get_symbol( n.cur_posn ) == POWER2 )
		{
			power2_posn.push_back(n.cur_posn);
			power2_move.push_back(n.initial_move);
		}
		
		//this part can be compressed.
		temp_posn = my_posn;
		temp_posn.update( EAST );
		if( map.moveable_position( temp_posn) && visited[temp_posn.x][temp_posn.y] == 0 )
		{
			node n2(temp_posn,n.initial_move,1);
			Q.push(n2);
		}

		temp_posn = my_posn;
		temp_posn.update( WEST );
		if( map.moveable_position( temp_posn) && visited[temp_posn.x][temp_posn.y] == 0 )
		{
			node n2(temp_posn,n.initial_move,1);
			Q.push(n2);
		}
	
		temp_posn = my_posn;
		temp_posn.update( NORTH );
		if( map.moveable_position( temp_posn) && visited[temp_posn.x][temp_posn.y] == 0 )
		{
			node n2(temp_posn,n.initial_move,1);
			Q.push(n2);
		}
	
		temp_posn = my_posn;
		temp_posn.update( SOUTH );
		if( map.moveable_position( temp_posn) && visited[temp_posn.x][temp_posn.y] == 0 )
		{
			node n2(temp_posn,n.initial_move,1);
			Q.push(n2);
		}
	}

}


