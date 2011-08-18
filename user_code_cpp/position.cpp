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

void Position::update(int direction)
{
	if( direction == EAST )
	{	
		x += 1;
		y += 0;
	}
	if( direction == WEST )
	{	
		x -= 1;
		y += 0;
	}
	if( direction == NORTH )
	{	
		x += 0;
		y -= 1;
	}
	if( direction == SOUTH )
	{	
		x += 0;
		y += 1;
	}
}


