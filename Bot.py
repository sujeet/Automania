import subprocess
from os import linesep

import Constants

def get_process_according_to_filename (filename) :
    """ Starts a subprocess assuming that the filename is
    a program. That is, if filename is that of a python file,
    then the subprocess should be started with python interpreter."""

    splitup = filename.split (".")
    if len (splitup) < 2 :
        raise Exception ("Could not determine the extension of the file " +
                         filename)
    extension = splitup [-1]
    # Now depending on extension, start the process.
    if extension == "py" :
        return subprocess.Popen (["python", filename],
                                 stdin = subprocess.PIPE,
                                 stdout = subprocess.PIPE)
    else :
        raise Exception ("Can not handle files with extension : " +
                         extension)

class Bot :
    """ Handles the user programms.
    These programs drive the bikes. """

    def __init__ (self, symbol, bot_code) :
        """ Initialize the bot.
        symbol - the character which the bike and its trail will have in the map
        bot_code - the filename of the bot code which runs the bike. eg. hayabusa.py or dummybot.jar etc."""

        self.symbol = symbol
        self.process = get_process_according_to_filename (bot_code)
        # info_to_send will be built up as the turn progresses, and at the
        # end of the turn, to get the next move, the info_to_send will
        # be sent to the subprocess to get the move.
        self.info_to_send = ""
        # The idea is to have the scores calculated at the
        # end of the game depending on how much ground the
        # bike has covered. This extra_sroce can be used
        # if we decide to award points when a certain power
        # -up is taken or something like that.
        self.extra_score = 0    

    def add_to_info_to_send (self, more_info) :
        """ Appends a newline to info_to_send and then appends the more_info to it."""
        self.info_to_send += linesep + more_info

    def get_move (self) :
        """ Communicate with the player code and return the move. """
        self.process.stdin.write ("sujeet" + linesep)
        # self.process.stdin.write (self.info_to_send + linesep)
        self.process.stdin.flush ()
        direction = self.process.stdout.readline ()
        try :
            return Constants.__getattribute__ (direction)
        except :
            try :
                return Constants.__getattribute__ (direction [:-1])
            except :
                raise Exception ("Invalid move : " +
                                 direction)
