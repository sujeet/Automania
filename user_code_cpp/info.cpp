#include "info.h"


void Info::initial_read()
{
	game_ended = 0;
	int x,y;

	cin>>my_tag;	
	cin>>enemy_tag; 
	cin>>x>>y;	
	my_posn.initialize(x,y);
    cin>>x>>y;		
    enemy_posn.initialize(x,y);
	cin>>map_file;	
	
    map.initialize(map_file);	
}

void Info::read_info()
{
	int num_ip;
	cin>>num_ip;
	
	if( num_ip == 0 )
	{
		game_ended = 1;
		return;	
	}
	
	for( int i=0;i<num_ip;i++)
	{
		int x,y;
		char element;
		cin>>x>>y;
		cin>>element;
    	Position posn(x,y);
		map.set_symbol(posn,element);

		if( element == my_tag )
		{
			my_posn.initialize(x,y); 

		}

		if( element == enemy_tag )
		{
			enemy_posn.initialize(x,y); 
		}
	}
    cin>>nitro_moves_left>>traversers;

}

void Info::compute_details()
{
	//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
	//This can also compute other details like the area of the current region in which the bike resides etc..
	bfs player1,player2;
	player1.compute(map,my_posn);
	player2.compute(map,enemy_posn);


	int n = player1.traverser_posn.size();

	my_traverser_posn.resize(n);
	my_traverser_move.resize(n);
    my_traverser_distance.resize(n);
	for( int i=0;i<n;i++)
	{
		my_traverser_posn[i] = player1.traverser_posn[i];
		my_traverser_move[i] = player1.traverser_move[i];	
        my_traverser_distance[i] = player1.traverser_distance[i];

	}
	
	int m = player1.nitro_posn.size();

	my_nitro_posn.resize(m);
	my_nitro_move.resize(m);
    my_nitro_distance.resize(m);
	for( int i=0;i<m;i++)
	{
		my_nitro_posn[i] = player1.nitro_posn[i];
		my_nitro_move[i] = player1.nitro_move[i];	
        my_nitro_distance[i] = player1.nitro_distance[i];

	}
	
	int p = player2.traverser_posn.size();

	enemy_traverser_posn.resize(p);
	enemy_traverser_move.resize(p);
    enemy_traverser_distance.resize(p);
	for( int i=0;i<p;i++)
	{
		enemy_traverser_posn[i] = player2.traverser_posn[i];
		enemy_traverser_move[i] = player2.traverser_move[i];	
        enemy_traverser_distance[i] = player2.traverser_distance[i];

	}
	
	int q = player1.nitro_posn.size();
	
	enemy_nitro_posn.resize(q);
	enemy_nitro_move.resize(q);
    enemy_nitro_distance.resize(q);
	for( int i=0;i<q;i++)
	{
		enemy_nitro_posn[i] = player2.nitro_posn[i];
		enemy_nitro_move[i] = player2.nitro_move[i];
        enemy_nitro_distance[i] = player2.nitro_distance[i];
	}
			
}

int Info::end_game()
{
	return game_ended;
}


