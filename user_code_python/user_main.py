from sys import *
from BotBrain import *
from Info import *


my_info = Info()
my_bot = BotBrain()

res = [ "NORTH" , "WEST" , "SOUTH" , "EAST" ]
my_info.initial_read()
    
my_info.compute_details()


while(1):

    result = my_bot.play_move(my_info)

    if result > 4 or result < 1 :

        print "INVALID"
        stdout.flush()

    else:

        print res[result]
        stdout.flush()
    
    my_info.read_info()

    if my_info.end_game() > 0 : 
        break

    my_info.compute_details()


