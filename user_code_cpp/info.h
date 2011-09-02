#include<iostream>
#include<vector>
#include "bfs.h"

class Info
{

private:
	
int game_ended;
string map_file;


public:

char my_tag;
char enemy_tag;
Position my_posn;
Position enemy_posn;
Map map;

int nitro_moves_left;
int traversers;

vector <Position> my_traverser_posn; //since the actual powers are not finalized
vector <int> my_traverser_move;	//first move to be made to reach the target point in shortest time.
vector <int> my_traverser_distance;

vector <Position> my_nitro_posn;
vector <int> my_nitro_move;
vector <int> my_nitro_distance;

vector <Position> enemy_traverser_posn;
vector <int> enemy_traverser_move;
vector <int> enemy_traverser_distance;

vector <Position> enemy_nitro_posn;
vector <int> enemy_nitro_move;
vector <int> enemy_nitro_distance;

void initial_read();	//initially reads the necessary details like the players tagetc.
void read_info();	//reads the input from the engine and updates the variables.
void compute_details();	//finds all the necessary details
int end_game();	//checks if the game has ended.

};
