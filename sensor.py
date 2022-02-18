import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    
    def Save_Values(self):
        numpy.save("data/" + self.linkNmae + ".npy", self.values)

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
