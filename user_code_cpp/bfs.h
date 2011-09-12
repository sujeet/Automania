#ifndef BFS_H
#define BFS_H

#include<iostream>
#include<vector>
#include<queue>

#include "map.h"

//This class is not of much importance to the user. This basically implements a bfs function. If the user wants to write his own bfs function, he can use this class as a reference

class node
{

public:

Position cur_posn;
int initial_move;
int distance;

node( Position p,int i,int d);
};

class bfs
{

public:

vector <Position> traverser_posn;
vector <Position> nitro_posn;
vector <int> traverser_move;
vector <int> nitro_move;
vector <int> traverser_distance;
vector <int> nitro_distance;
	
void compute( Map, Position );

};

#endif
