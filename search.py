import os
import time
import constants as c
from parallelHillClimberA import PARALLEL_HILL_CLIMBER_A
from parallelHillClimberB import PARALLEL_HILL_CLIMBER_B
os.system("cd data&del dataA_text*.npy")
os.system("cd data&del dataB_text*.npy")
os.system("cd data&del stepsA*.npy")
os.system("cd data&del stepsB*.npy")
os.system("del tmp*.npy")
os.system("del tmp*.txt")

for i in range(0,c.times):
# Left and right 


    phcA = PARALLEL_HILL_CLIMBER_A()
    phcA.Evolve()
    phcA.Show_Best()

    os.rename("data/dataA_text.npy", "data/dataA_text" + str(i+1) + ".npy")

    time.sleep(1)
    
    os.rename("data/stepsA.npy", "data/stepsA" + str(i+1) + ".npy")

    os.system("del tmp*.txt")


for i in range(0,c.times):
    # left front and right back couple


    phcB = PARALLEL_HILL_CLIMBER_B()
    phcB.Evolve()
    phcB.Show_Best()

    os.rename("data/dataB_text.npy", "data/dataB_text" + str(i+1) + ".npy")    
    time.sleep(1)
    os.rename("data/stepsB.npy", "data/stepsB" + str(i+1) + ".npy")

    os.system("del tmp*.txt")