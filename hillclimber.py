
from solution import SOLUTION
import copy
import constants as c

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(numberOfGenerations):
            self.Spawn()
            self.Mutate()
            self.child.Evaluate()
            self.Select()
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    def Mutate(self):
        self.child.Mutate()
        print
        
    def Select(self):
        pass