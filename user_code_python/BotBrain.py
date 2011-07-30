class BotBrain :
    """ Literally this is the brain of the bot.

    @author Devesh Yamparala

    This is the class whose functions players need 
    to code. """

    # Some static variables here if needed
    dummy

    def __init__(self, init_map, max_map_size) :
        """ Constructor for the bot. 

        @param init_map Char[][]: Inital map
        @param max_map_size  Int: Max rows or columns in map.
        """
        self.map = init_map
        self.map_size = max_map_size
        
    def play_move(self) :
        """ Function to decide which move to play.

        """
        pass

