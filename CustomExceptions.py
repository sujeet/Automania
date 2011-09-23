class BotProcessDiedError (Exception) :
    def __init__ (self, value):
           self.code = "CR" + str (value)

class InvalidMoveError (Exception) :
    def __init__ (self, value):
           self.code = "DQ" + str (value)

class BotTimedOutError (Exception) :
    def __init__ (self, value):
           self.code = "TO" + str (value)
