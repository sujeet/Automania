from sys import *
from botbrain import *


my_info = Info()
my_bot = BotBrain()

my_info.initial_read()
res = [ "NORTH" , "WEST" , "SOUTH" , "EAST" ]

print "NORTH"
sys.stdout.flush()

while(1):

    my_info.read_info()

    if my_info.end_game() > 0 : 
        break

    my_info.compute_details()

    result = my_bot.play_move(my_info)

    if result > 4 or result < 1 :

        print "INVALID"
        sys.stdout.flush()

    else:

        print res[result]
        sys.stdout.flush()

