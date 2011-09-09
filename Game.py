import sys
import os

from Constants import *
from Arena import *
    
if __name__ == "__main__" :
    map_file_name = "map.txt"
    arena = Arena (map_file_name, sys.argv [1:])

    for i in xrange (N_TURNS) :
        arena.check_for_bot_crash ()
        arena.get_moves ((i == 0))
        arena.map.updates.reset ()
        arena.make_moves ()
        arena.map.log_updates (0, 0, "$", "$")  
        if arena.game_over == True :
            break

    arena.terminate_game ()
    os.system ("python log_to_html.py")
