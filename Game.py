import sys
import os
import traceback

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
        
    # can't put arena.terminate_game () into
    # the "finally" clause because it prints the scores.
    # The judge just looks at the last line of output and
    # hence errors, if any, should come after the scones.
    except (BotProcessDiedError,
            InvalidMoveError,
            BotTimedOutError), (e) :
        arena.terminate_game ()
        print e.code

    except :
        arena.terminate_game ()
        traceback.print_exc (file=sys.stdout)

    finally :
        os.system ("python log_to_html.py")
