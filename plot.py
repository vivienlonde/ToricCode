import matplotlib.pyplot as plt

l = 3

def plot_grid(l):
    for i in range(l):
        plt.axhline(y=i, color='black', linestyle='-', linewidth=1)
        plt.axvline(x=i, color='black', linestyle='-', linewidth=1)

def plot_points(points):
    for x, y in points:
        plt.scatter(x, y, color='red')

plot_grid(l)
points = [(1, 1), (2, 2)]
plot_points(points)

plt.xticks([i for i in range(l)])
plt.yticks([i for i in range(l)])
plt.show()