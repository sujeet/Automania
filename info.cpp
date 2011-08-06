#include<iostream>

#include "constants.h"
#include "map.h"
#include "position.h"

class Info
{

private:

int game_ended;
string map_file;

public:

int my_tag;
int enemy_tag;
Position my_posn;
Position enemy_posn;

Map map;

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
			my_posn.initialize(x,y); //update my position.
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
	
}

void end_game()
{
	return game_ended
}


};
;
