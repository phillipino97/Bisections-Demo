from matplotlib import pyplot as plt
import numpy as np
import random

x = [0]
y = [0]
true_path = 0
prev_angle = [1]
prev_choice = [0]
prev_path = [0]

j = 1
switch = 0
dont = 0

prev_b = [0]

choice = [.5, 2]

def generatePlot():
    rand = random.uniform(-1, 1)
    steep = random.uniform(0, 10)
    i = 0
    while -20 < x[i] < 20:
        x.append(rand*(i + 1))
        if rand < 0:
            y.append(x[i + 1] * -steep)
        else:
            y.append(x[i + 1] * steep)
        i += 1
    plt.plot(x, y, 'b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bisection Demo')
    plt.grid()
    plt.axis([-20, 20, 0, 20])
    plt.draw()


def generateBisections(iteration):
    b = [0]
    c = [0]
    rand = random.randint(0, 1)
    multi = 0
    global switch, j, dont

    if iteration == 0:
        if rand == 0:
            b.append(-1)
            c.append(1)
        else:
            b.append(1)
            c.append(1)
    else:
        c.append(1)
        if (true_path < 0 and not prev_path[iteration] < 0) or (true_path > 0 and not prev_path[iteration] > 0):
            prev_path[iteration] *= -1
            prev_b[iteration] *= -1
        # choose random
        if iteration == 1:
            multi = choice[rand]
            b.append(prev_b[iteration]/multi)
            prev_choice.append(rand)
        elif 1/prev_b[iteration] < true_path < 1/prev_b[iteration - 1] or 1/prev_b[iteration] > true_path > 1/prev_b[iteration - 1]:
            b.append((prev_b[iteration] + prev_b[iteration - 1])/2)
            #print(1/b[1])
            dont = 1
            switch = 1
        elif dont == 1 and switch == 1:
            if switch == 1:
                choice[1 - prev_choice[-1]] *= j
            multi = choice[1 - prev_choice[-1]]
            b.append((prev_b[iteration]*multi))
            #print(1/b[-1])
            prev_choice.append(1 - prev_choice[-1])
            switch = 0
            dont = 0
        elif prev_angle[iteration] < prev_angle[iteration - 1] or switch == 1 or iteration == 2:
            if switch == 1:
                choice[prev_choice[-1]] *= j
            multi = choice[prev_choice[-1]]
            b.append((prev_b[iteration]*multi))
            #print(1/b[-1])
            prev_choice.append(prev_choice[-1])
            switch = 0
        elif prev_angle[iteration] > prev_angle[iteration - 1]:
            multi = choice[1 - prev_choice[-1]]
            b.append((prev_b[iteration])*multi)
            #print(1 / b[1])
            prev_choice.append((1 - prev_choice[-1]))
            switch = 1

    i = 2
    while (-20 < b[i-1] < 20):
        b.append(i*b[1])
        c.append(i)
        i += 1

    plt.plot(x, y, 'b')
    plt.plot(b, c, 'g')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bisection Demo')
    plt.grid()
    plt.axis([-20, 20, 0, 20])
    plt.draw()

    curr_path = (c[-1]/b[-1])
    prev_path.append(curr_path)
    prev_b.append(b[1])

    return np.arctan(np.abs((true_path - curr_path) / (1 + (true_path * curr_path))))


plt.ion()
generatePlot()
true_path = (y[-1]/x[-1])
print(true_path)
i = 0

while prev_angle[i] > .0001:
    prev_angle.append(generateBisections(i))
    print("Angle: " + str(prev_angle[i+1]))
    plt.pause(.01)
    plt.clf()
    i += 1

print("Number of iterations: " + str(i) + "\nEnd Value: " + str(1/prev_b[i]))



