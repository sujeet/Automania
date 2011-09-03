#include<iostream>
#include<vector>
#include<queue>

#include "map.h"

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
