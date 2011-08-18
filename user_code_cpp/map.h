#include<iostream>
#include<string>
#include<stdio.h>
#include "position.h"
#include "constants.h"

class Map
{
public:
	
	vector <vector <char> > array;
	int n; 	//dimensions of the array

	void initialize( string file_name);
	void set_symbol( Position, char );
	char get_symbol( Position );

	int moveable_position( Position );
};
