#include "botBrain.h"

//The user need not worry about this file
int main()
{
	Info my_info;
	BotBrain my_bot;

	string res[] = { "NORTH" , "WEST" , "SOUTH" , "EAST" };
	my_info.initial_read();
	if( my_info.end_game() )
		return 1;
	my_info.compute_details();

	while(1)
	{
		int result = my_bot.play_move(my_info);
		if( result > 4 || result < 1 )
			cout<<"INVALID"<<endl << flush;
		else
			cout<<res[result]<<endl<<flush;

		my_info.read_info();
		if( my_info.end_game() )
			break;

		my_info.compute_details();

	}	
	return 1;
}

