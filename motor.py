import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

import constants as c


class MOTOR:
    def Prepare_To_Act(self):
        if self.jointName == "Torso_BackLeg":
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.offset, 2 * self.frequency * numpy.pi, 1000))
        else:
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(self.offset, 2 * (self.frequency / 2) * numpy.pi, 1000))

    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 50)

    def Save_Values(self):
        numpy.save("data/" + self.jointName + ".npy", self.motorValues)

    def __init__(self, jointName):
        self.amplitude = c.back_amplitude
        self.frequency = c.back_frequency
        self.offset = c.back_phaseOffset

        self.jointName = jointName
        self.motorValues = numpy.zeros(1000)
        self.Prepare_To_Act()
    