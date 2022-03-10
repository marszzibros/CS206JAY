import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2) * 2 - 1
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

    def Evaluate(self):
        os.system("python simulate.py")
        file_in.open("fitness.txt","r")
        self.fitness = float(file_in.readline())
        file_in.close()
    def Mutate(self):
        
        randomRow = random.randint(1,3)
        randomColumn = random.randint(1,2)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos =[0, 0, 1.5], size = [1, 1, 1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos = [0.5,0,-0.5], size = [1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos = [-0.5,0,-0.5], size = [1, 1, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos =[2, 2, 0.5], size = [1, 1, 1])
        pyrosim.End()