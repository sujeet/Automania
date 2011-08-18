#include<iostream>
#include<vector>
#include "bfs.h"

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

vector <Position> my_power1_posn; //since the actual powers are not finalized
vector <int> my_power1_move;	//first move to be made to reach the target point in shortest time.

vector <Position> my_power2_posn;
vector <int> my_power2_move;

vector <Position> enemy_power1_posn;
vector <int> enemy_power1_move;

vector <Position> enemy_power2_posn;
vector <int> enemy_power2_move;

void initial_read();	//initially reads the necessary details like the players tagetc.
void read_info();	//reads the input from the engine and updates the variables.
void compute_details();	//finds all the necessary details
int end_game();	//checks if the game has ended.

};
