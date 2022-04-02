import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, availableID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.myID = availableID
    def Set_ID(self, assignedID):
        self.myID = assignedID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        file_in = open("./fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(file_in.readline())
        print(self.fitness)
        file_in.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        
        randomRow = random.randint(1,c.numSensorNeurons)
        randomColumn = random.randint(1,c.numMotorNeurons)
        self.weights[randomRow - 1][randomColumn - 1] = random.random() * 2 - 1

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos =[0, 0, 2], size = [3, 1.5, 0.6])


        pyrosim.Send_Joint( name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , type = "revolute", position = [-1, -1, 0.7], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos = [-1, -0.6, 0.7], size = [0.2, 0.2, 0.7])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 8, weight = self.weights[currentRow][currentColumn])
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 4, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()