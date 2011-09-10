from os import linesep

class Updates :
    """ Represents the updates made to the map during a move.
    This will help in sending the diff info to the the bots."""

    def __init__ (self) :
        """ diffs - a list of updates. Each update is of
                    the form [x, y, symbol_prev, symbol_curr]
        """
        self.diffs = []

    def add (self, x, y, symbol_prev, symbol_curr) :
        """ Adds the update to the diffs list. """
        self.diffs.append ([x, y, symbol_prev, symbol_curr])

    def __str__ (self) :
        """ string representation of diffs
        example : [[2, 3, 'x', 'N'],[1, 1, 'K', 'r']] will give
                  string which will be printed as the following
                  2 3 x N
                  1 1 K r
        """
        string = ""
        for diff in self.diffs :
            for elem in diff :
                string += str (elem) + " "
            string = string [:-1]
            string += linesep
        return string

    def to_bot_format (self) :
        """ string representation of diffs as expected by the
            bot code. As the bot already has the map, it does
            not require teh prev_symbols
        example : [[2, 3, 'x', 'N'],[1, 1, 'K', 'r']] will give
                  string which will be printed as the following
                  2 3 N
                  1 1 r
        """
        string = ""
        for diff in self.diffs :
            string += (str (diff [0]) + " "
                       + str (diff [1]) + " "
                       + str (diff [3]) + linesep)
        # the last linesep will be added by the bot.
        return string [:-1]

    def reset (self) :
        self.diffs = []

    def __len__ (self) :
        return len (self.diffs)
