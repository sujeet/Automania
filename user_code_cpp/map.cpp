#include "map.h"

void Map::initialize(string file_name )
{
	char c = getchar();
	while( c != EOF )
	{
		vector <char> temp;
		while( c != '\n' )
		{
			temp.push_back(c);
			c = getchar();
		}
		
		array.push_back( temp );
		c = getchar();
	}

}

void Map::set_symbol(Position pos, char symbol)
{
	if( pos.x >= n || pos.x < 0 ||  pos.y >= n || pos.y < 0 );
		//exception. Disqualify the player?
	array[pos.x][pos.y] = symbol;
}

char Map::get_symbol( Position pos )
{
	if( pos.x >= n || pos.x < 0 ||  pos.y >= n || pos.y < 0 );
		//exception. Disqualify the player?
	return array[pos.x][pos.y];
}

int Map::moveable_position( Position pos )
{
	if( pos.x < 0 || pos.x >= n || pos.y < 0 || pos.y >= n )
		return 0;
	if( get_symbol( pos ) == EMPTY )
		return 1;	//NOTE THIS MUST BE CHANGED IF PARALLEL PLAY IS DECIDED.
	return 0;
}
	
	
