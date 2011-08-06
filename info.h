#include<iostream>


class Info
{

private:
	
int game_ended;
string map_file;


public:

int my_tag;
int enemy_tag;
Position my_posn;
Position enemy_posn;


void initial_read();	//initially reads the necessary details like the players tagetc.
void read_info();	//reads the input from the engine and updates the variables.
void compute_details();	//finds all the necessary details
void end_game();	//checks if the game has ended.

}
