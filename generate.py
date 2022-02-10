
import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1


x = 0
y = 0
z = 0



def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos =[x + 2, y + 2, z + 0.5], size = [length, width, height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos =[x, y, z + 1.5], size = [length, width, height])
	pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x + 0.5, y, z + 1])
	pyrosim.Send_Cube(name="BackLeg", pos = [x + 0.5,y,z - 0.5], size = [length, width, height])
	pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x - 0.5, y, z + 1])
	pyrosim.Send_Cube(name="FrontLeg", pos = [x - 0.5,y,z - 0.5], size = [length, width, height])


	pyrosim.End()

Create_World()
Create_Robot()