import subprocess
import sys
import zipfile
import tempfile
import os
from os import linesep

import Constants
from Constants import *
from CustomExceptions import *

def get_process_for_zip_file (filename) :
    """ The given filename is that of a zip file and the
    zip file is assumed to contain a file named `main.py`.
    Extracts the zip file in a temperory folder, and starts
    process corrosponding to `main.py`. """

    try:
        f = zipfile.ZipFile(filename)
    except zipfile.BadZipfile:
        raise Exception ("Invalid zip file : "
                         + filename)
    extract_path = tempfile.mkdtemp ()

    # Handle older versions of zipfile that do not contain 'extractall'
    if hasattr(f, "extractall"):
        f.extractall(path = extract_path)
    else:
        for name in f.namelist():
            path = os.path.join (extract_path, name)
            f_ = open(path, "wb")
            f_.write( f.read( name ) )
            f_.close()

    output = os.path.join(extract_path, "main.py")
    if not os.path.exists(output):
        raise Exception ("Unable to find 'main.py' in "
                         + filename)

    return subprocess.Popen (["python", output],
                             stdin = subprocess.PIPE,
                             stdout = subprocess.PIPE,
                             stderr = sys.stderr)


def get_process_according_to_filename (filename) :
    """ Starts a subprocess assuming that the filename is
    a program. That is, if filename is that of a python file,
    then the subprocess should be started with python interpreter."""

    splitup = filename.split (".")

    extension = splitup [-1]
    # Now depending on extension, start the process.
    if extension == "py" :
        return subprocess.Popen (["python", filename],
                                 stdin = subprocess.PIPE,
                                 stdout = subprocess.PIPE,
                                 stderr = sys.stderr)
    elif extension == "jar" :
        return subprocess.Popen (["java", "-jar", filename],
                                 stdin = subprocess.PIPE,
                                 stdout = subprocess.PIPE,
                                 stderr = sys.stderr)

    elif extension == "zip" :
        return get_process_for_zip_file (filename)

    else :
        try :
            # assume the file is an executable and try to run it.
            return subprocess.Popen ([filename],
                                     stdin = subprocess.PIPE,
                                     stdout = subprocess.PIPE,
                                     stderr = sys.stderr)
        except :
            raise Exception ("Could not handle the bot file : " +
                             filename)

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
        self.traverser_left = 0
        self.nitro_left = 0

    def add_to_info_to_send (self, more_info) :
        """ Appends a newline to info_to_send and then appends the more_info to it."""
        self.info_to_send += linesep + more_info

    def ensure_running (self) :
        """ Ensures that the process related the bot is still running.
            If not running, prints appropriate score (the crashing bot
            loses) and exits the program.
        """
        return_code = self.process.poll ()
        if return_code != None :
            # Player 1 dead means score is -1
            if self.symbol == BIKE_1_SYMBOL :
                print -1
            else :
                print 1
            raise BotProcessDiedError ("The player with symbol "
                                       + self.symbol
                                       + " terminated with exit code "
                                       + str (return_code))

    def get_move (self, updates, first_move = False) :
        """ Communicate with the player code and return the move. """
        if (not first_move) :
            self.add_to_info_to_send (str (len (updates)))
            self.add_to_info_to_send (updates.to_bot_format ())
            self.add_to_info_to_send (str (self.nitro_left) + " "
                                      + str (self.traverser_left) + linesep)

        self.process.stdin.write (self.info_to_send + linesep)
        print "bot number : ", self.symbol
        print "sent message : ", self.info_to_send
        self.process.stdin.flush ()
        self.info_to_send = ""
        print "waiting for response ..."
        self.ensure_running ()
        direction = self.process.stdout.readline ()
        self.ensure_running ()
        print "got response : ", direction
        updates.reset ()
        try :
            return Constants.__getattribute__ (direction)
        except :
            try :
                return Constants.__getattribute__ (direction [:-1])
            except :
                raise InvalidMoveError ("Invalid move : " +
                                        direction)
