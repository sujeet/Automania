class Position :

    def __init__ (self, x, y, max_x, max_y) :
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y

    def __str__ (self) :
        return "Position : " + str (self.x) + ", " + str (self.y)

    def update (self, direction) :
        self.x += direction [0]
        self.y += direction [1]
        # comment the following two lines to
        # disable toroidal geometry.
        self.x = self.x % (self.max_x + 1)
        self.y = self.y % (self.max_y + 1)
