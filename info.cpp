#include "info.h"

class Info
{

public:

void initial_read()
{
	game_ended = 0;
	int x,y;
	//what else should be read initially?

	cin>>my_tag;	//my tag
	cin>>enemy_tag //enemy tag
	cin>>x>>y;	//my initial position
	my_posn.initialize(x,y); //this function must be added to the position class
	cin>>x>>y;		//enemy initial position
	enemy_posn.initialize(x,y);
	cin>>map_file;	//name of the map file
	
	map.initialize(map_file);	//this function must be included in map class
}

void read_info()
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
			my_posn.initialize(x,y); //update my position.	THIS FUNCTION MUST BE INCLUDED IN POSITION CLASS.

		}

		if( element == enemy_tag )
		{
			enemy_posn.initialize(x,y); //update enemy position.
		}
	}		

}

void compute_details()
{
	//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
	//This can also compute other details like the area of the current region in which the bike resides etc..
	bfs player1,player2;
	player1.compute(map,my_posn);
	player2.compute(map,enemy_posn);
	
	int n = player1.power1.size();

	my_power1_posn.resize(n);
	my_power1_move.resize(n);
	for( int i=0;i<n;i++)
	{
		my_power1_posn[i] = player1.power1_posn[i];
		my_power1_move[i] = player1.power1_move[i];	

	}
	
	int m = player1.power2.size();

	my_power2_posn.resize(m);
	my_power2_move.resize(m);
	for( int i=0;i<m;i++)
	{
		my_power2_posn[i] = player1.power2_posn[i];
		my_power2_move[i] = player1.power2_move[i];	

	}
	
	int p = player2.power1.size();

	enemy_power1_posn.resize(p);
	enemy_power1_move.resize(p);
	for( int i=0;i<p;i++)
	{
		enemy_power1_posn[i] = player2.power1_posn[i];
		enemy_power1_move[i] = player2.power1_move[i];	

	}
	
	int q = player1.power2.size();
	
	enemy_power2_posn.resize(q);
	enemy_power2_move.resize(q);
	for( int i=0;i<q;i++)
	{
		enemy_power2_posn[i] = player2.power2_posn[i];
		enemy_power2_move[i] = player2.power2_move[i];	

	}
			
}

void end_game()
{
	return game_ended
}


};
;
