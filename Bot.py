from Constants import *

def generate_filenames (symbol) :
    """ Generates two filenames based on symbol.
    First one will be used by player code as stdin.
    Second one will be used by player code as stdout. """
    return ("player_code_input" + symbol,
            "player_code_output" + symbol)

class Bot :
    """ Handles the user programms.
    These programs drive the bikes. """

    def __init__ (self, symbol) :
        """ Initialize the bot. """
        self.symbol = symbol
        filenames = generate_filenames (symbol)
        self._to_player_code_file_name = filenames [0]
        self._from_player_code_file_name = filenames [1]
        # The idea is to have the scores calculated at the
        # end of the game depending on how much ground the
        # bike has covered. This extra_sroce can be used
        # if we decide to award points when a certain power
        # -up is taken or something like that.
        self.extra_score = 0    

    def get_move (self) :
        """ Communicate with the player code and return the move. """
        return NORTH

