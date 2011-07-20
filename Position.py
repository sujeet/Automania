class Position :

    def __init__ (self, x, y) :
        self.x = x
        self.y = y

    def __str__ (self) :
        return "Position : " + str (self.x) + ", " + str (self.y)

    def update (self, direction) :
        self.x += direction [0]
        self.y += direction [1]
