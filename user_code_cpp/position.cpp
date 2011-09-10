#include "position.h"
#include "constants.h"

Position::Position( )
{}

Position::Position( int a, int b )
{
	x = a;
	y = b;
}

void Position::initialize( int a, int b )
{
	x = a;
	y = b;
}

void Position::update(int direction)    //this function updates the current position to move in the target direction.
{
	if( direction == EAST )
	{	
		y += 1;
        if( y == MAX_Y )
            y = 0;
        
	}
	if( direction == WEST )
	{	
		y -= 1;
        if( y == -1 )
            y = MAX_Y - 1;
	}
	if( direction == NORTH )
	{	
		x -= 1;
        if( x == -1 )
            x = MAX_X - 1;
	}
	if( direction == SOUTH )
	{	
		x += 1;
        if( x == MAX_X )
            x = 0;
	}
}



