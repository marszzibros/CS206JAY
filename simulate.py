import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for i in range(0,1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = ...,
	jointName = "...",
	controlMode = ...,
	targetPosition = ...,
	maxForce = ...)
	time.sleep(1/1000)
p.disconnect()
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)
