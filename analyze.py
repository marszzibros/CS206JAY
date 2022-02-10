import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load("datls/backLegSensorValues.npy")
# FrontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label = "Back leg", linewidth = 4)
# matplotlib.pyplot.plot(FrontLegSensorValues, label = "Front leg")

targetAnglesFront = numpy.load("data/targetAnglesFront.npy")
targetAnglesBack = numpy.load("data/targetAnglesBack.npy")

matplotlib.pyplot.plot(targetAnglesFront, label = "Back leg", linewidth = 4)
matplotlib.pyplot.plot(targetAnglesBack, label = "Front leg")
# matplotlib.pyplot.plot(numpy.sin(targetAngles))

matplotlib.pyplot.legend()
matplotlib.pyplot.show()