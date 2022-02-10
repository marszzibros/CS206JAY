import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

back_amplitude = numpy.pi / 4
back_frequency = 10
back_phaseOffset = numpy.pi / 2.6

front_amplitude = numpy.pi / 4
front_frequency = 10
front_phaseOffset = 0

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

front_targetAngles = front_amplitude * numpy.sin(numpy.linspace(front_phaseOffset, 2 * front_frequency * numpy.pi, 1000))
back_targetAngles = back_amplitude * numpy.sin(numpy.linspace(back_phaseOffset, 2 * back_frequency * numpy.pi, 1000))
for i in range(0,1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = "Torso_BackLeg",
	controlMode = p.POSITION_CONTROL,
	targetPosition = back_targetAngles[i],
	maxForce = 50)
		
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = "Torso_FrontLeg",
	controlMode = p.POSITION_CONTROL,
	targetPosition = front_targetAngles[i],
	maxForce = 50)

	time.sleep(1/1000)
p.disconnect()
numpy.save("data/targetAnglesBack.npy", back_targetAngles)
numpy.save("data/targetAnglesFront.npy", front_targetAngles)
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)


