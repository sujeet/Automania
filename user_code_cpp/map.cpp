#include <iostream>
#include <fstream>

#include "map.h"

using namespace std;

void Map::initialize(string file_name )
{
	char c;
    ifstream map_file;
    
    map_file.open (file_name.c_str());
    map_file >> c;
	while( c != EOF )
	{
		vector <char> temp;
		while( c != '\n' )
		{
			temp.push_back(c);
            map_file >> c;
            cerr << c << flush;
		}
        cerr << "done with one line." << endl << flush;
        cerr << endl << flush;
		
		array.push_back( temp );
        map_file >> c;
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
	
	
