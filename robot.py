from motor import MOTOR
from sensor import SENSOR

import pyrosim.pyrosim as pyrosim
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
        for i in self.motor:
            self.motor[i].Set_Value(t, self.robot)

    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()










