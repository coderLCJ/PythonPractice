import time
from random import choice
from matplotlib import pyplot as plt

class RandomWalk():
    def __init__(self, num_points=50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_valuse = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_dir = choice([1, -1])
            x_dis = choice([0, 1, 2, 3, 4])
            x_step = x_dis * x_dir

            y_dir = choice([1, -1])
            y_dis = choice([0, 1, 2, 3, 4])
            y_step = y_dis * y_dir

            if x_step == 0 and y_step == 0:
                continue

            x_next = self.x_values[-1] + x_step
            y_next = self.y_valuse[-1] + y_step

            self.x_values.append(x_next)
            self.y_valuse.append(y_next)


r = RandomWalk()
r.fill_walk()
point_numbers = list(range(r.num_points))
plt.scatter(r.x_values, r.y_valuse, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
plt.scatter(0, 0, c='yellow')
plt.scatter(r.x_values[-1], r.y_valuse[-1], c='red')
plt.show()