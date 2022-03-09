from motor import MOTOR
from sensor import SENSOR

import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p


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
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motor[jointName].Set_Value(desiredAngle, self.robot)
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()


    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robot)
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()










