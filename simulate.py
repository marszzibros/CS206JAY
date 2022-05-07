from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
version = sys.argv[3]

simulation = SIMULATION(directOrGUI, solutionID, version)

simulation.Run()
simulation.Get_Fitness()



