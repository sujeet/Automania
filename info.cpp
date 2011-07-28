#include "constants.h"
#include "map.h"
#include "position.h"

class Info
{

// All necessary info variables goes here.
Position my_posn
Position enemy_posn
Map map

vector <Position> my_powers		//positions of all the powers which the player can reach from the current position 
vector <int> my_distances 		//distance of the corresponding powers in increasing order. These are stuff similiar to tank wars
vector <int> my_first_moves

vector <Position> enemy_powers
vector <int> enemy_distances 		//distance of the corresponding powers in increasing order. These are stuff similiar to tank wars
vector <int> enemy_first_moves 

int my_area

void read_info()
{
	//read and update the details from text file.
	//some way to tag the current bot as player 1 or 2 is necessary here.
}

void compute_details()
{
	//This function finds all non trivial details. This may include shortest distance to all powers and the first moves to be made to reach them in shortest time
	//This can also compute other details like the area of the current region in which the bike resides etc..
}

void print_info()
{
	//print all the details into stdout. This info is used by BotBrain.
}

};
