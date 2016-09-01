import C
import P
import syst
import random as R
class Dungeon:

    def __init__(self, oldDirection):
        self.foo = R.randint(1,5)
        self.backwards = self.invertDirection(oldDirection)
        self.firstFloor = self.mapTheDungeon()
    @staticmethod
    def invertDirection(oldDirection):
        return C.reverseDirection[oldDirection]
    @staticmethod
    def mapTheDungeon():
        dungeonMap = {} #put elements in as dungeonMap[x,y] = element
        dungeonMap[0,1] = FloorSpace()
        return dungeonMap

class FloorSpace:
    def __init__(self):
        self.name = R.randint(1,50)
