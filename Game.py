import sys
import os

from Constants import *
from Arena import *

    
if __name__ == "__main__" :
    map_file_name = "map.txt"
    arena = Arena (map_file_name, sys.argv [1:])

    # a desperate attempt to avoud zombies :
    try :
        for i in xrange (N_TURNS) :
            arena.check_for_bot_crash ()
            arena.get_moves ((i == 0))
            arena.make_moves ()
            arena.update_powers ()
            arena.turn_count += 1
            arena.map.log_updates (0, 0, "$", "$")  
            if arena.game_over == True :
                break
            
        arena.terminate_game ()
        os.system ("python log_to_html.py")
        
    except :
        for bike in arena.bikes :
            try :
                bike.bot.process.kill ()
            except OSError :
                # the process was already terminated
                pass
