#include "botBrain.h"

int main()
{
	Info my_info;
	BotBrain my_bot;

	my_info.initial_read();
	string res[] = { "NORTH" , "WEST" , "SOUTH" , "EAST" };

	while(1)
	{
		my_info.read_info();
		if( my_info.end_game() )
			break;
					
		my_info.compute_details();

		int result = my_bot.play_move(my_info);
		if( result > 4 || result < 1 )
			cout<<"INVALID"<<endl;
		else
			cout<<res[result]<<endl;
		
	}	
}

