import os

from motor import MOTOR
from sensor import SENSOR


import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import constants as c
import numpy as np


class ROBOT:
    def Prepare_To_Sense(self):
        self.sensors = dict()

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Prepare_To_Act(self):
        self.motor = dict()

        for jointName in pyrosim.jointNamesToIndices:
            self.motor[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                if int(neuronName) >= 10 and int(neuronName) <= 13:
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointDownRange * -1

                else:
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointUpRange * -1
                self.motor[jointName].Set_Value(desiredAngle, self.robot)
                
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        file_in = open("tmp" + str(self.solutionID) + ".txt", "w")

        file_in.write(str(xCoordinateOfLinkZero))
        file_in.close()
        os.rename("./tmp" + str(self.solutionID) + ".txt", "./fitness" + str(self.solutionID) + ".txt")

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robot)
        os.system("del brain" + str(self.solutionID) + ".nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        









