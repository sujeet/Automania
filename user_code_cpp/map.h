#include<iostream>
#include<string>
#include<stdio.h>
#include "position.h"
#include "constants.h"

class Map
{
public:
	
	vector <vector <char> > array;  //this array stores the map.
	int n; 	//dimensions of the array

	void initialize( string file_name); //this function is on no use to the user.  
	void set_symbol( Position, char );  //this function updates the map with the given symbol in the given position.
	char get_symbol( Position );    //this function is used to find the element present in a given position in the map.

	int moveable_position( Position );  //this function is to check whether the given position is a moveable position or not. If the position contains a trail or wall or if the position is out of the bounds of the map, then it is not a moveable
};
