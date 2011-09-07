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
	}
	if( direction == WEST )
	{	
		y -= 1;
	}
	if( direction == NORTH )
	{	
		x -= 1;
	}
	if( direction == SOUTH )
	{	
		x += 1;
	}
}


