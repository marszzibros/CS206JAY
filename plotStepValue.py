import numpy as np
import matplotlib.pyplot as plt
import constants as c
for a in range(1, c.times + 1):
    A_Values = np.load("data/stepsA" + str(a) + ".npy")

    plt.figure(figsize = (20,2))
    final_A_Values = np.ones((8,c.steps)) * -1
    A_Values = np.swapaxes(A_Values,0,1)
    for i in range(0,8):
        if i % 2 == 0:
            final_A_Values[i] = A_Values[i // 2]
    plt.imshow(final_A_Values, cmap='Greys', interpolation='nearest', extent=[0, c.steps, 0, 16],aspect = 2)
    plt.savefig("data/stepA" + str(a) + ".png")
    plt.close()

    B_Values = np.load("data/stepsB" + str(a) + ".npy")

    plt.figure(figsize = (20,2))
    final_B_Values = np.ones((8,c.steps)) * -1
    B_Values = np.swapaxes(B_Values,0,1)
    for i in range(0,8):
        if i % 2 == 0:
            final_B_Values[i] = B_Values[i // 2]
    plt.imshow(final_B_Values, cmap='Greys', interpolation='nearest', extent=[0, c.steps, 0, 16],aspect = 2)
    plt.savefig("data/stepB" + str(a) + ".png")
    plt.close()

#B_Values = numpy.load("data/stepsB.npy")

#y_left = numpy.zeros((c.steps)) + 1
#y_right = numpy.zeros((c.steps)) + 2

#x_left_front = numpy.zeros((c.steps))
#x_left_back = numpy.zeros((c.steps))
#x_right_front = numpy.zeros((c.steps))
#x_right_back = numpy.zeros((c.steps))

#count = 0
#for value in B_Values:
#	x_left_front[count] = value[0]
#	x_left_back[count] = value[1]
#	x_right_front[count] = value[2]
#	x_right_back[count] = value[3]
#	count += 1
#plt.scatter(x_left_front, y_left_front, label = "left front")
#plt.scatter(x_left_back, y_left_back, label = "left back")
#plt.scatter(x_right_front, y_right_front, label = "right front")
#plt.scatter(x_right_back, y_right_back, label = "right back")

#plt.xlabel("x postion")
#plt.ylabel("left front - 1 left back- 3 right front - 2 right back - 4")
#plt.legend()
#plt.savefig("data/stepB.png")
#plt.close()