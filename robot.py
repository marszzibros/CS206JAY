import os

from motor import MOTOR
from sensor import SENSOR

import math


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
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointDownRange
                    self.nn.Multiply_Value_Of(str(neuronName),-1)

                else:
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointUpRange
                    self.nn.Multiply_Value_Of(str(neuronName),-1)
                self.motor[jointName].Set_Value(desiredAngle, self.robot)
                
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        joint_states = p.getJointStates(self.robot, range(p.getNumJoints(self.robot)))
        joint_infos = [p.getJointInfo(self.robot, i) for i in range(p.getNumJoints(self.robot))]
        joint_states = [j for j,i in zip(joint_states, joint_infos)]
        joint_positions = [state[0] for state in joint_states]

        file_in = open("tmp" + str(self.solutionID) + ".txt", "w")
        if int(self.solutionID) not in range(0,c.populationSize):

            file_in_position = open("tmpPosition" + str(int(self.solutionID) - c.populationSize) + ".txt", "r")

            self.parentPosition = file_in_position.readline().split(',')
            file_in_position.close()
            os.system("del tmpPosition"+ str(int(self.solutionID) - c.populationSize) +".txt")
        diff = 0
        for i in range(0,16,4):
            diff+=abs(float(self.parentPosition[i]) - joint_positions[i])

        self.parentPosition = joint_positions
        file_in.write(str(xCoordinateOfLinkZero * (diff)))
        file_in_position = open("tmpPosition" + str(self.solutionID) + ".txt", "w")
        for i in range(0,16):
            file_in_position.write(str(self.parentPosition[i]) + ",")
        file_in_position.close()
        file_in.close()
        os.rename("./tmp" + str(self.solutionID) + ".txt", "./fitness" + str(self.solutionID) + ".txt")

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robot = p.loadURDF("body"+self.solutionID+".urdf")

        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robot)
        os.system("del brain" + str(self.solutionID) + ".nndf")
        os.system("del body" + str(self.solutionID) + ".urdf")
        self.parentPosition = np.zeros(16)


        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        









