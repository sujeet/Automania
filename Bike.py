from Bot import *
from Position import *
from Constants import *

class Bike :
    """ Represents the bike in arena. """
    
    def __init__ (self, symbol, starting_posn, code_file) :
        """ Initializes the bike. """
        self.curr_posn = starting_posn
        self.prev_posn = Position (starting_posn.x,
                                   starting_posn.y,
                                   starting_posn.max_x,
                                   starting_posn.max_y)
        self.symbol    = symbol
        self.bot       = Bot (symbol, code_file)
        self.is_dead   = False

    def __str__ (self) :
        """ For pretty printing the object. """
        return ("Current Position : " + self.curr_posn.__str__ () + linesep
                + "Previous Position : " + self.prev_posn.__str__ () + linesep
                + "Symbol : " + symbol + linesep)

    def put_trail_for_html (self, map) :
        """ The function which reports a different symbol for
        the trail for the visualizer purposes. """
        if self.symbol == BIKE_1_SYMBOL :
            trail_symbol = TRAIL1
        else :
            trail_symbol = TRAIL2
        map.log_updates (self.prev_posn.x,
                         self.prev_posn.y,
                         map.get_symbol (self.prev_posn),
                         trail_symbol)

    def get_move (self, updates, map, first_move = False) :
        """ Gets the move from the bot.
        Sets the curr_position accordingly. """
        try :
            direction = self.bot.get_move (updates, first_move)
            self.prev_posn = Position (self.curr_posn.x,
                                       self.curr_posn.y,
                                       self.curr_posn.max_x,
                                       self.curr_posn.max_y)
            self.curr_posn.update (direction)
            self.put_trail_for_html (map)
            # saying prev_pons = curr_posn won't help

        except AttributeError :
            self.is_dead = True
    
    def power_up (self, arena, power_symbol) :
        """ Take appropriate actions depending on
        the Power up symbol. """
        if power_symbol == RESET :
            # if the map cell is a bot symbol and not the head of the trail
            # ie, not the current position of the bike itself, delete all the
            map_size = arena.map.size
            for i in range (map_size) :
                for j in range (map_size) :
                    position = Position (i, j, map_size, map_size)
                    if (arena.map.get_symbol (position) in [BIKE_1_SYMBOL,
                                                            BIKE_2_SYMBOL]
                        and (arena.bikes[0].curr_posn != position)
                        and (arena.bikes[1].curr_posn != position)) :
                        arena.map.set_symbol (position, EMPTY)

        elif power_symbol == TRAVERSER :
            self.bot.traverser_left += TRAVERSER_CAPACITY + 1
            # The + 1 is necessary because later, during this move,
            # it is going to be decreased by 1.
