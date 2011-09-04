from os import linesep
from Constants import *

class Map :
    """ Represents the map. """

    def __init__ (self, map_file_name) :
        """ Initializes the 2D array from
        the file. Also opens the log file. """
        map_file = file (map_file_name)
        self._map_array = [list (line.strip ())
                          for line in
                          map_file.readlines ()]
        map_file.close ()
        self._validate ()
        self.size = len (self._map_array)
        self.log_file = open (LOG_FILE, "w")

    def __str__ (self) :
        """ String representation of map. As a snapshot. """
        return linesep.join (["".join (row) for row in self._map_array])

    def _validate (self) :
        """ Checks whether the 2D array formed
        is correct. """
        # The map has to be a square.
        size_set = set ([len (row)
                         for row in
                         self._map_array])
        size_set.add (len (self._map_array))
        # If the map is a a square, the
        # size of the set should be 1
        if len (size_set) != 1 :
            raise Exception ("The map is not a square.")

    def _validate_position (self, position) :
        """ Checks whether the position is valid
        for the given _map_array. """
        pass_condition = ((0 <= position.x < len (self._map_array))
                          and
                          (0 <= position.y < len (self._map_array)))
        if (not pass_condition) :
            raise Exception ("The map does not have position : "
                             + position.__str__())

    def get_count (self, symbol) :
        """ Returns the number of occurences of the symbol in the
        character array. """
        count = 0
        for row in self._map_array :
            for letter in row :
                if (letter == symbol) :
                    count += 1
        return count
        
    def log_symbols (self, sym1, sym2, sym3, sym4) :
        """ Writes the four symbols in space seperated
        line to the log file. """
        changes = (str (sym1) + " "
                   + str (sym2) + " "
                   + str (sym3) + " "
                   + str (sym4) + linesep)
        self.log_file.write (changes)

    def log_changes (self, position, symbol) :
        """ Used for creating map diffs to send across
        to the bots. Also will be useful for the game
        visualizer. """
        self.log_symbols (position.x, position.y, ".", symbol)

    def set_symbol (self, position, symbol) :
        """ Sets the given symbol at the given position. """
        self._validate_position (position)
        self._map_array [position.x] [position.y] = symbol
        self.log_changes (position, symbol)

    def get_symbol (self, position) :
        """ Returns the symbol at the position. """
        self._validate_position (position)
        return self._map_array [position.x] [position.y]
