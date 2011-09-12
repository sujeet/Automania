#ifndef POSITION_H
#define POSITION_H

#include<vector>
using namespace std;

class Position
{

public:

int x,y;    // x and y co ordinate

Position();
Position( int , int );
void initialize( int , int );
void update( int ); //this function updates the current position to move in the target direction.


};

#endif
