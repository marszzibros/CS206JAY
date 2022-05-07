import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION_A:
    def __init__(self, availableID):
        self.sensorWeights = np.random.rand(c.numSensorNeurons,c.numHiddenNeurons)
        self.hiddenWeights = np.random.rand(c.numHiddenNeurons,c.numMotorNeurons)
        self.myID = availableID
    def Set_ID(self, assignedID):
        self.myID = assignedID

    def Start_Simulation(self, directOrGUI, version):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " " + version )
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.3)
        file_in = open("./fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(file_in.readline())
        file_in.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        
        randomRow = random.randint(1,c.numSensorNeurons)
        randomColumn = random.randint(1,c.numHiddenNeurons)
        self.sensorWeights[randomRow - 1][randomColumn - 1] = random.random()
        
        randomRow = random.randint(1,c.numHiddenNeurons)
        randomColumn = random.randint(1,c.numMotorNeurons)
        self.hiddenWeights[randomRow - 1][randomColumn - 1] = random.random()


    def Generate_Body(self):
        pyrosim.Start_URDF("body"+ str(self.myID) +".urdf")
        pyrosim.Send_Cube(name="Torso", pos =[0, 0, 1.5], size = [3, 1.5, 0.6])

        pyrosim.Send_Joint( name = "Torso_FrontLeftSide" , parent= "Torso" , child = "FrontLeftSide" , type = "revolute", position = [-1.3, -0.75, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeftSide", pos = [0, -0.15, 0], size = [0.3, 0.3, 0.3])

        pyrosim.Send_Joint( name = "Torso_FrontRightSide" , parent= "Torso" , child = "FrontRightSide" , type = "revolute", position = [-1.3, 0.75, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontRightSide", pos = [0, 0.15, 0], size = [0.3, 0.3, 0.3])

        pyrosim.Send_Joint( name = "Torso_BackLeftSide" , parent= "Torso" , child = "BackLeftSide" , type = "revolute", position = [1.3, -0.75, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeftSide", pos = [0, -0.15, 0], size = [0.3, 0.3, 0.3])
        
        pyrosim.Send_Joint( name = "Torso_BackRightSide" , parent= "Torso" , child = "BackRightSide" , type = "revolute", position = [1.3, 0.75, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRightSide", pos = [0, 0.15, 0], size = [0.3, 0.3, 0.3])



        pyrosim.Send_Joint( name = "FrontLeftSide_FrontLeftUpLeg" , parent= "FrontLeftSide" , child = "FrontLeftUpLeg" , type = "revolute", position = [0.15, -0.15, -0.15], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeftUpLeg", pos = [0.15, 0, -0.25], size = [0.3, 0.3, 0.5])

        pyrosim.Send_Joint( name = "FrontRightSide_FrontRightUpLeg" , parent= "FrontRightSide" , child = "FrontRightUpLeg" , type = "revolute", position = [0.15, 0.15, -0.15], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontRightUpLeg", pos = [0.15, 0, -0.25], size = [0.3, 0.3, 0.5])

        pyrosim.Send_Joint( name = "BackLeftSide_BackLeftUpLeg" , parent= "BackLeftSide" , child = "BackLeftUpLeg" , type = "revolute", position = [0.15, -0.15, -0.15], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeftUpLeg", pos = [0.15, 0, -0.25], size = [0.3, 0.3, 0.5])

        pyrosim.Send_Joint( name = "BackRightSide_BackRightUpLeg" , parent= "BackRightSide" , child = "BackRightUpLeg" , type = "revolute", position = [0.15, 0.15, -0.15], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRightUpLeg", pos = [0.15, 0, -0.25], size = [0.3, 0.3, 0.5])



        pyrosim.Send_Joint( name = "FrontLeftUpLeg_FrontLeftDownLeg" , parent= "FrontLeftUpLeg" , child = "FrontLeftDownLeg" , type = "revolute", position = [0.3, 0, -0.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeftDownLeg", pos = [0.1, 0, -0.3], size = [0.2, 0.2, 0.6])

        pyrosim.Send_Joint( name = "FrontRightUpLeg_FrontRightDownLeg" , parent= "FrontRightUpLeg" , child = "FrontRightDownLeg" , type = "revolute", position = [0.3, 0, -0.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontRightDownLeg", pos = [0.1, 0, -0.3], size = [0.2, 0.2, 0.6])

        pyrosim.Send_Joint( name = "BackLeftUpLeg_BackLeftDownLeg" , parent= "BackLeftUpLeg" , child = "BackLeftDownLeg" , type = "revolute", position = [0.3, 0, -0.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeftDownLeg", pos = [0.1, 0, -0.3], size = [0.2, 0.2, 0.6])

        pyrosim.Send_Joint( name = "BackRightUpLeg_BackRightDownLeg" , parent= "BackRightUpLeg" , child = "BackRightDownLeg" , type = "revolute", position = [0.3, 0, -0.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRightDownLeg", pos = [0.1, 0, -0.3], size = [0.2, 0.2, 0.6])


        pyrosim.Send_Joint( name = "FrontLeftDownLeg_FrontLeftFoot" , parent= "FrontLeftDownLeg" , child = "FrontLeftFoot" , type = "revolute", position = [0.1, 0, -0.6], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeftFoot", pos = [-0.2, 0, -0.05], size = [0.4, 0.2, 0.1])

        pyrosim.Send_Joint( name = "FrontRightDownLeg_FrontRightFoot" , parent= "FrontRightDownLeg" , child = "FrontRightFoot" , type = "revolute", position = [0.1, 0, -0.6], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRightFoot", pos = [-0.2, 0, -0.05], size = [0.4, 0.2, 0.1])

        pyrosim.Send_Joint( name = "BackLeftDownLeg_BackLeftFoot" , parent= "BackLeftDownLeg" , child = "BackLeftFoot" , type = "revolute", position = [0.1, 0, -0.6], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeftFoot", pos = [-0.2, 0, -0.05], size = [0.4, 0.2, 0.1])

        pyrosim.Send_Joint( name = "BackRightDownLeg_BackRightFoot" , parent= "BackRightDownLeg" , child = "BackRightFoot" , type = "revolute", position = [0.1, 0, -0.6], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackRightFoot", pos = [-0.2, 0, -0.05], size = [0.4, 0.2, 0.1])

        
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLeftFoot")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeftFoot")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontRightFoot")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackRightFoot")

        pyrosim.Send_Hidden_Neuron(name = 4)
        pyrosim.Send_Hidden_Neuron(name = 5)

        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "FrontLeftSide_FrontLeftUpLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "BackLeftSide_BackLeftUpLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontRightSide_FrontRightUpLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackRightSide_BackRightUpLeg")
        
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "FrontLeftUpLeg_FrontLeftDownLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "BackLeftUpLeg_BackLeftDownLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "FrontRightUpLeg_FrontRightDownLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackRightUpLeg_BackRightDownLeg")


        for currentColumn in range(0,c.numHiddenNeurons):
            for currentRow in range(0,c.numSensorNeurons):
                if (currentRow == 0 or currentRow == 1) and currentColumn == 0:
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 4, weight = self.sensorWeights[currentRow][currentColumn])
                elif (currentRow == 0 or currentRow == 1) and currentColumn == 1:
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 4, weight = self.sensorWeights[currentRow][currentColumn] * -1)
                elif (currentRow == 2 or currentRow == 3) and currentColumn == 1:
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 4, weight = self.sensorWeights[currentRow][currentColumn])
                elif (currentRow == 2 or currentRow == 3) and currentColumn == 0:
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 4, weight = self.sensorWeights[currentRow][currentColumn] * -1)

        for currentColumn in range(0,c.numMotorNeurons):
            for currentRow in range(0,c.numHiddenNeurons):
                if currentRow == 0 and (currentColumn == 0 or currentColumn == 1 or currentColumn == 4 or currentColumn == 5):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow + 4, targetNeuronName = currentColumn + 6, weight = self.hiddenWeights[currentRow][currentColumn])
                elif currentRow == 0 and (currentColumn == 2 or currentColumn == 3 or currentColumn == 6 or currentColumn == 7):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow + 4, targetNeuronName = currentColumn + 6, weight = self.hiddenWeights[currentRow][currentColumn] * -1)
                elif currentRow == 1 and (currentColumn == 2 or currentColumn == 3 or currentColumn == 6 or currentColumn == 7):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow + 4, targetNeuronName = currentColumn + 6, weight = self.hiddenWeights[currentRow][currentColumn])
                elif currentRow == 1 and (currentColumn == 0 or currentColumn == 1 or currentColumn == 4 or currentColumn == 5):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow + 4, targetNeuronName = currentColumn + 6, weight = self.hiddenWeights[currentRow][currentColumn] * -1)
        

        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()