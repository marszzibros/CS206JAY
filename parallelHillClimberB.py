
from solutionB import SOLUTION_B
import copy
import constants as c
import time
import numpy as np
import os

class PARALLEL_HILL_CLIMBER_B:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        #self.parent = SOLUTION()
        self.dataB = np.zeros((c.populationSize,c.numberOfGenerations))
        self.nextAvailableID = 0
        self.generation = 0
        self.parents = dict()
        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION_B(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
    def Evaluate(self, solutions):
        for i in range(0,c.populationSize):
            solutions[i].Start_Simulation("DIRECT", "B")
        for i in range(0,c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
        

    def Spawn(self):
        self.children = dict()
        for i in range(0,c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(0,c.populationSize):
            self.children[i].Mutate()
        
    def Select(self):
        for i in range(0,c.populationSize):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] =  copy.deepcopy(self.children[i])
    def Print(self):
        #print()
        for i in range(0,c.populationSize):
            self.dataB[i][self.generation] = self.parents[i].fitness
        #    print(str(self.parents[i].fitness) + " " + str(self.children[i].fitness))
        self.generation += 1
        #print()
    def Show_Best(self):
        lowest = 10000000
        
        for i in range(0,c.populationSize):
            if self.parents[i].fitness < lowest:
                solution = self.parents[i]
                lowest = solution.fitness
        solution.Start_Simulation("GUI", "B")
        np.save("data/dataB_text.npy", self.dataB)
        