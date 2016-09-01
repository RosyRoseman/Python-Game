import C
from P import Player as P
import syst
import random as R
from D import Dungeon as D

dungeonOfDoom = D("north") #new instance of dungeon class
print(dungeonOfDoom.backwards)
print(dungeonOfDoom.firstFloor[0, 1].name)
player = P()
