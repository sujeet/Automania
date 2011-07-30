import BotBrain

class ServerClientInterface :
    """ Acts as an interface to server and the user code.

    @author Devesh Yamparala

    The interface will call the user code for the next move
    and communicate it to the game server and vice versa 
    also happens. Any communication happens only via text
    transfer. """

    def __init__(self) :
        """ Constructor for the Interface.

        """
        pass

    def run_client(self) :
        """ Function which does all the IO operations.

        """
        get_arena_data()
        player_bot_brain = BotBrain()

        while True :
            input_buffer = read_input()
            if not correct_input() :
                break
            else :
                input_buffer

    def get_arena_data(self) :
        """ Function to get the initial details about
        the arena.

        """
        pass

    def read_input(self):
        """ Function to read from the stdin.

        """
        pass

    def correct_input(self) :
        """ Functiont to check the correctness of the 
        text from stdin.
        
        ? Is this function needed at all or can it be ?
        ? integrated into read_input. ?

        """
        pass
