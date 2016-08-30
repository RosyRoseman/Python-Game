import C
import random as R
class Dungeon:

    def __init__(self, oldDirection):
        self.foo = R.randint(1,5)
        self.backwards = self.invertDirection(oldDirection)
    @staticmethod
    def invertDirection(oldDirection):
        if oldDirection == "northeast":
            return C.SW
        elif oldDirection == "southwest":
            return C.NE
        elif oldDirection == "northwest":
            return C.SE
        elif oldDirection == "southeast":
            return C.NW
        elif oldDirection == "north":
            return C.S
        elif oldDirection == "south":
            return C.N
        else:
            return "ERROR"
