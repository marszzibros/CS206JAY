import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

import constants as c


class MOTOR:

    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 50)


    def __init__(self, jointName):
        self.amplitude = c.back_amplitude
        self.frequency = c.back_frequency
        self.offset = c.back_phaseOffset

        self.jointName = jointName
        self.motorValues = numpy.zeros(c.steps)
