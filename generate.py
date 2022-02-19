
import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1


x = 0
y = 0
z = 0

def Generate_Body():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos =[x, y, z + 1.5], size = [length, width, height])
	pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x + 0.5, y, z + 1])
	pyrosim.Send_Cube(name="BackLeg", pos = [x + 0.5,y,z - 0.5], size = [length, width, height])
	pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x - 0.5, y, z + 1])
	pyrosim.Send_Cube(name="FrontLeg", pos = [x - 0.5,y,z - 0.5], size = [length, width, height])
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
	pyrosim.End()

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos =[x + 2, y + 2, z + 0.5], size = [length, width, height])
	pyrosim.End()






Create_World()
Generate_Body()
Generate_Brain()