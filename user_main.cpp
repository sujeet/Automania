#include "constants.h"
#include "map.h"
#include "info.h"
#include "BotBrain.h"

int main()
{
	Info my_info;
	BotBrain my_bot;

	my_info.initial_read();

	while(1)
	{
		my_info.read_info();
		if( my_info.end_game() )
			break;
					
		my_info.compute_details();

		int result = my_bot.get_move(my_info);
		if( result > 4 || result < 1 )
			//disqualify.

		cout<<result<<endl;
		
	}	
}

