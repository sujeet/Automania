from Map import *
from Bike import *
from Constants import *
from Position import *

class Arena :
    """ Handles the game simulation. """

    def __init__ (self, map_file_name) :
        """ Initializes the map and bikes. """
        self.map = Map (map_file_name)
        init_posns = self._generate_init_posns (self.map)
        self.bikes = [Bike (BIKE_1_SYMBOL, init_posns[0]),
                      Bike (BIKE_2_SYMBOL, init_posns[1])]
        self.power_ups = []
        self.game_over = False

    def _generate_init_posns (self, map) :
        """ Depending on map, generates initial positions
        for teh bikes. """
        # return (Position (0, 0),
        #         Position (map.size - 1, map.size - 1))
        return (Position (3, 3),
                Position (7, 7))

    def get_moves (self) :
        """ Gets moves from each bot driving the bikes. """
        for bike in self.bikes :
            bike.get_move ()

    def _check_for_collisions (self) :
        """ Checks for collisions, and if any,
        sets the appropriate flags. """
        for bike in self.bikes :
            symbol_at_new_posn = self.map.get_symbol (bike.curr_posn)
            bike.is_dead = (symbol_at_new_posn != EMPTY and
                            symbol_at_new_posn not in POWER_UP_SYMBOLS)
            if bike.is_dead :
                self.game_over = True

    def _pick_power_ups (self) :
        """ Makes the bikes pick the power-ups if they have
        landed upon one. """
        for bike in self.bikes :
            symbol_at_new_posn = self.map.get_symbol (bike.curr_posn)
            if symbol_at_new_posn in POWER_UP_SYMBOLS :
                bike.power_up (symbol_at_new_posn)

    def _update_map (self) :
        """ Based on the bike positions, updates
        the map. """
        for bike in self.bikes :
            self.map.set_symbol (bike.curr_posn, bike.symbol)

    def make_moves (self) :
        """ Checks for collisions, moves bikes on the map. """
        self._check_for_collisions ()
        self._pick_power_ups ()
        self._update_map ()

    def terminate_game (self) :
        pass
