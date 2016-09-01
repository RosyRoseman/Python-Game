import C
import P
import syst
import random as R
class Dungeon:

    def __init__(self, oldDirection):
        self.foo = R.randint(1,5)
        self.backwards = self.invertDirection(oldDirection)
    @staticmethod
    def invertDirection(oldDirection):
        return C.reverseDirection[oldDirection]
