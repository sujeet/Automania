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

vector <Position> power1_posn;
vector <Position> power2_posn;
vector <int> power1_move;
vector <int> power2_move;
	
void compute( Map, Position );

};
