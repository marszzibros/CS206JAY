import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1


x = 0
y = 0
z = 0.5


pyrosim.Start_SDF("boxes.sdf")
for i in range(0,5):
	for j in range(0,5):
		for k in range(0,10):
			pyrosim.Send_Cube(name="Box"+ str(i) + str(j) + str(k), pos =[x + i, y + j, z + k], size = [length * (0.90)**k, width * (0.90)**k, height * (0.90)**k])

pyrosim.End()
