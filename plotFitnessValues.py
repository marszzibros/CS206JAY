import numpy
import matplotlib.pyplot
import constants as c

A_total_Values = numpy.zeros((c.numberOfGenerations))
B_total_Values = numpy.zeros((c.numberOfGenerations))

for times in range(0, c.times):
    A_Values_Average = numpy.zeros((c.numberOfGenerations))
    B_Values_Average = numpy.zeros((c.numberOfGenerations))
    A_Values = numpy.load("data/dataA_text" + str(times + 1) + ".npy")
    B_Values = numpy.load("data/dataB_text" + str(times + 1) + ".npy")

    for i in range(0,c.numberOfGenerations):
        A_value = 0
        B_value = 0
        for j in range(0,c.populationSize):
            A_value += A_Values[j][i]
            B_value += B_Values[j][i]
        A_Values_Average[i] = A_value / c.populationSize
        B_Values_Average[i] = B_value / c.populationSize

    matplotlib.pyplot.plot(A_Values_Average, linewidth = 0.8, color = "red")
    matplotlib.pyplot.plot(B_Values_Average, linewidth = 0.8, color = "blue")

    A_total_Values += A_Values_Average
    B_total_Values += B_Values_Average


A_total_Values /= c.times
B_total_Values /= c.times

matplotlib.pyplot.plot(A_total_Values, linewidth = 2, color = "red", label = "A - Average", marker = "*")
matplotlib.pyplot.plot(B_total_Values, linewidth = 2, color = "blue", label = "B - Average", marker = "*")
matplotlib.pyplot.legend()

matplotlib.pyplot.xlabel("Generations")
matplotlib.pyplot.ylabel("Fitness (going toward the screen)")

matplotlib.pyplot.savefig("data/fitness.png")