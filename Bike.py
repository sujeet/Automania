from Bot import *

class Bike :
    """ Represents the bike in arena. """
    
    def __init__ (self, symbol, starting_posn) :
        """ Initializes the bike. """
        self.curr_posn = starting_posn
        self.prev_posn = starting_posn
        self.symbol    = symbol
        self.bot       = Bot (symbol)
        self.is_dead   = False

    def __str__ (self) :
        """ For pretty printing the object. """
        return ("Current Position : " + self.curr_posn.__str__ () + linesep
                + "Previous Position : " + self.prev_posn.__str__ () + linesep
                + "Symbol : " + symbol + linesep)

    def get_move (self) :
        """ Gets the move from the bot.
        Sets the curr_position accordingly. """
        self.curr_posn.update (self.bot.get_move ())
    
    def power_up (self, power_symbol) :
        """ """
        pass

