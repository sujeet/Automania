from Map import *
from Bike import *
from Constants import *
from Position import *

class Arena :
    """ Handles the game simulation. """

    def __init__ (self, map_file_name, bot_files) :
        """ Initializes the map and bikes. """
        self.map = Map (map_file_name)
        init_posns = self._generate_init_posns (self.map)
        self.bikes = [Bike (BIKE_1_SYMBOL, init_posns[0], bot_files[0]),
                      Bike (BIKE_2_SYMBOL, init_posns[1], bot_files[1])]
        self.map.set_symbol (self.bikes[0].curr_posn, self.bikes[0].symbol)
        self.map.set_symbol (self.bikes[1].curr_posn, self.bikes[1].symbol)
        self.game_over = False
        # Send the initialization info to the bots.
        for bike in self.bikes :
            bike.bot.add_to_info_to_send (bike.symbol)
            if bike.symbol == BIKE_1_SYMBOL :
                enemy_symbol = BIKE_2_SYMBOL
                bot_num = 0
            else :
                enemy_symbol = BIKE_1_SYMBOL
                bot_num = 1
            bike.bot.add_to_info_to_send (enemy_symbol)
            bike.bot.add_to_info_to_send (str(init_posns[bot_num].x)
                                          + " "
                                          + str(init_posns[bot_num].y))
            bike.bot.add_to_info_to_send (str(init_posns[1-bot_num].x)
                                          + " "
                                          + str(init_posns[1-bot_num].y))
            bike.bot.add_to_info_to_send (map_file_name)

    def _generate_init_posns (self, map) :
        """ Depending on map, generates initial positions
        for teh bikes. """
        # return (Position (0, 0),
        #         Position (map.size - 1, map.size - 1))
        return (Position (3, 3, map.size - 1, map.size - 1),
                Position (7, 12, map.size - 1, map.size - 1))

    def get_moves (self, first_move = False) :
        """ Gets moves from each bot driving the bikes. """
        for bike in self.bikes :
            bike.get_move (self.map.updates, self.map, first_move)

    def update_powers (self) :
        """ Updates the power up counts of bikes. """
        for bike in self.bikes :
            bot = bike.bot
            bot.nitro_left = max (0,
                                  bot.nitro_left - 1)
            bot.traverser_left = max (0,
                                      bot.traverser_left - 1)

    def _check_for_collisions (self) :
        """ Checks for collisions, and if any,
        sets the appropriate flags. """
        # Bikes colliding with some thing there on the map
        # since previous move
        for bike in self.bikes :
            symbol_at_new_posn = self.map.get_symbol (bike.curr_posn)
            # check for collision only if traverser power is not there
            if bike.bot.traverser_left == 0 :
                bike.is_dead = (symbol_at_new_posn != EMPTY and
                                symbol_at_new_posn not in POWER_UP_SYMBOLS)
                if bike.is_dead :
                    self.game_over = True
        # Bikes colliding with someting which has not shown
        # up on the map yet (say, another bike)
        if self.bikes[0].curr_posn == self.bikes[1].curr_posn :
            for bike in self.bikes :
                bike.is_dead = True
            self.game_over = True
        # Set the dead symbols on maps accordingly
        for bike in self.bikes :
            if bike.is_dead :
                self.map.set_symbol (bike.curr_posn, DEAD_SYMBOL)

    def _pick_power_ups (self) :
        """ Makes the bikes pick the power-ups if they have
        landed upon one. """
        for bike in self.bikes :
            symbol_at_new_posn = self.map.get_symbol (bike.curr_posn)
            if symbol_at_new_posn in POWER_UP_SYMBOLS :
                bike.power_up (self, symbol_at_new_posn)

    def _update_map (self) :
        """ Based on the bike positions, updates
        the map. """
        for bike in self.bikes :
            if not self.game_over :
                self.map.set_symbol (bike.curr_posn, bike.symbol)

    def check_for_bot_crash (self) :
        """ Checks if any of the bot programmes have terminated.
        If yes prints it and the exit status. """
        for bike in self.bikes :
            return_code = bike.bot.process.poll ()
            if return_code != None :
                self.game_over = True
                print "The player with symbol " + bike.symbol + " terminated with exit code " + str (return_code)
                exit (1)

    def make_moves (self) :
        """ Checks for collisions, moves bikes on the map. """
        self._check_for_collisions ()
        self._pick_power_ups ()
        self._update_map ()

    # def send_info_to_bots (self) :
        

    def print_scores (self) :
        """ Prints to stdout
        -> 0  if either both are alive or both are dead.
        -> -1 if player2 is the only surviour. 
        -> 1  if player1 is the only surviour. """
        if self.bikes[0].is_dead == self.bikes[1].is_dead :
            print 0
        elif self.bikes[0].is_dead :
            print -1
        else :
            print 1

    def terminate_game (self) :
        """ All the aftergame cleanup goes here. """
        self.print_scores ()
        for bike in self.bikes :
            bike.bot.process.kill ()
        self.map.log_file.close ()
