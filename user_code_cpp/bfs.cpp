#include "bfs.h"

node::node( Position p,int i,int d)
{
	cur_posn.initialize(p.x,p.y);	
    initial_move = i;
	distance = d;		
}


//This class is not of much importance to the user. This basically implements a bfs function. If the user wants to write his own bfs function, he can use this class as a reference
void bfs::compute( Map map,Position my_posn )
{

	queue <node> Q;		

	Position temp_posn;
	vector <vector <int> > visited( MAX_X+2,vector <int> (MAX_Y+2,0) );

	//initial pushes

	temp_posn = my_posn;
	temp_posn.update( EAST );
	if( map.moveable_position( temp_posn) )	
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
        if( visited[n.cur_posn.x][n.cur_posn.y] != 0 )
        {
            continue;
        }
		visited[n.cur_posn.x][n.cur_posn.y] = 1;

		if( map.get_symbol( n.cur_posn ) == TRAVERSER )
		{
			traverser_posn.push_back(n.cur_posn);
			traverser_move.push_back(n.initial_move);
            traverser_distance.push_back(n.distance);
		}

		if( map.get_symbol( n.cur_posn ) == NITRO )
		{
			nitro_posn.push_back(n.cur_posn);
			nitro_move.push_back(n.initial_move);
            nitro_distance.push_back(n.distance);
		}
		
		temp_posn = n.cur_posn; 
        temp_posn.update( EAST );
		if( map.moveable_position( temp_posn) && (visited[temp_posn.x][temp_posn.y] == 0) )
		{
			node n2(temp_posn,n.initial_move,n.distance+1);
			Q.push(n2);
		}

		temp_posn = n.cur_posn;
		temp_posn.update( WEST );
		if( map.moveable_position( temp_posn) && (visited[temp_posn.x][temp_posn.y] == 0) )
		{
			node n2(temp_posn,n.initial_move,n.distance+1);
			Q.push(n2);
		}
	
		temp_posn = n.cur_posn;
		temp_posn.update( NORTH );
		if( map.moveable_position( temp_posn) && (visited[temp_posn.x][temp_posn.y] == 0) )
		{
			node n2(temp_posn,n.initial_move,n.distance+1);
			Q.push(n2);
		}
	
		temp_posn = n.cur_posn;
		temp_posn.update( SOUTH );
		if( map.moveable_position( temp_posn) && (visited[temp_posn.x][temp_posn.y] == 0) )
		{
			node n2(temp_posn,n.initial_move,n.distance+1);
			Q.push(n2);
		}
	}

}


