from Constants import *
from Arena import *
    
if __name__ == "__main__" :
    map_file_name = "map.txt"
    arena = Arena (map_file_name)

    for i in xrange (N_TURNS) :
        arena.get_moves ()
        arena.make_moves ()
        print arena.map
        if arena.game_over == True :
            break

    arena.terminate_game ()
