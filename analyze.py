import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
FrontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy")

matplotlib.pyplot.plot(backLegSensorValues, label = "Back leg", linewidth = 4)
matplotlib.pyplot.plot(FrontLegSensorValues, label = "Front leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()