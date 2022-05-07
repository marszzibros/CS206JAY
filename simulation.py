import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import numpy

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI, solutionID, version):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            #self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.version = version
        self.steps = numpy.zeros((c.steps,4),dtype=float)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
          
    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range(0,c.steps):
            p.stepSimulation()
            self.robot.Sense(t)
            sensorValue = self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI":
                time.sleep(1/100)
                self.steps[t] = sensorValue

            sensorValue.clear()

        if self.directOrGUI == "GUI":
            numpy.save("data/steps"+self.version+".npy", self.steps)
    def Get_Fitness(self):
        time.sleep(0.1)
        self.robot.Get_Fitness()



