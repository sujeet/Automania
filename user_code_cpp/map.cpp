#include <iostream>
#include <fstream>

#include "map.h"

using namespace std;

void Map::initialize(string file_name ) //this function is on no use to the user.

{
	char c;
	ifstream map_file;

	n = MAX_X;

	map_file.open (file_name.c_str());
	c = map_file.get();
	while( c != EOF )
	{
		vector <char> temp;
		while( c != '\n' )
		{
			temp.push_back(c);
			c = map_file.get();
		}


		array.push_back( temp );
		c = map_file.get();
	}

}

void Map::set_symbol(Position pos, char symbol) //this function updates the map with the given symbol in the given position.
{
	if( pos.x >= n || pos.x < 0 ||  pos.y >= n || pos.y < 0 )
		return;
	array[pos.x][pos.y] = symbol;
}

char Map::get_symbol( Position pos ) //this function is used to find the element present in a given position in the map.

{
	if( ! ( pos.x >= n || pos.x < 0 ||  pos.y >= n || pos.y < 0 ) )
	    return array[pos.x][pos.y];
    return 'W'; //NOTE: This means that the given position is illegal.
}

int Map::moveable_position( Position pos ) //this function is to check whether the given position is a moveable position or not. If the position contains a trail or wall or if the position is out of the bounds of the map, then it is not a moveable

{
	if( pos.x < 0 || pos.x >= n || pos.y < 0 || pos.y >= n )
		return 0;
	if( get_symbol( pos ) != WALL && get_symbol( pos ) != TRAIL )
		return 1;	
    return 0;
}
	
	
