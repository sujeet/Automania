#ifndef INFO_H
#define INFO_H

#include<iostream>
#include<vector>
#include "bfs.h"


//This class contains a lot of information about the game. Read the 'programming_details' file for a clear description of the class.
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

vector <Position> my_traverser_posn; 
vector <int> my_traverser_move;	
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

void initial_read();    //this function is of little importance to the user.	
void read_info();  //this function is of little importance to the user.
void compute_details();	//this function is of little importance to the user.
int end_game();		//this function is of little importance to the user.

};

#endif
