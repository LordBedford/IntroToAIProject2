from MapMaker import *
#from astarSearch import *
#from MapCreator import *
import time
import statistics

run = True
map = MapMaker()
map.startScreen()
while(run):
   MapMaker.tick(map)