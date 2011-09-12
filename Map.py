from os import linesep
from Constants import *
from Updates import *
from Position import *

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
        self.updates = [Updates (), Updates ()]
        # Now, read the map again for the sake of logging
        # TODO : find a better way of doing this.
        for i in range (self.size) :
            for j in range (self.size) :
                position = Position (i, j, self.size, self.size)
                self.set_symbol (position, self.get_symbol (position))

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
        
    def log_updates (self, x, y, previous_symbol, current_symbol) :
        """ Writes the updates in the log file. """
        self.log_file.write (str (x) + " "
                             + str (y) + " "
                             + str (previous_symbol) + " "
                             + str (current_symbol) + linesep)

    def set_symbol (self, position, symbol) :
        """ Sets the given symbol at the given position. """
        self._validate_position (position)
        for update in self.updates :
            update.add (position.x,
                        position.y,
                        self.get_symbol (position),
                        symbol)
        self.log_updates (position.x,
                          position.y,
                          self.get_symbol (position),
                          symbol)
        self._map_array [position.y] [position.x] = symbol

    def get_symbol (self, position) :
        """ Returns the symbol at the position. """
        self._validate_position (position)
        return self._map_array [position.y] [position.x]

    def get_position (self, symbol) :
        """ Returns the first encountered position of
            the symbol. (use only on unique symbols for
            desired results.)
            Returns None if no symbol found.
        """
        for i in range (self.size) :
            for j in range (self.size) :
                if self._map_array [i][j] == symbol :
                    return Position (i, j,
                                     self.size - 1,
                                     self.size - 1)
        return None
