import matplotlib.pyplot as plt

from utilities import l, index_to_coordinates, qubit_index_to_coordinates

def plot_grid(l):
    zorder = 0
    for i in range(l):
        plt.axhline(y=i, color='black', linestyle='-', linewidth=1, zorder=zorder)
        plt.axvline(x=i, color='black', linestyle='-', linewidth=1, zorder=zorder)

def plot_points(l, size):
    for x in range(l):
        for y in range(l):
            plt.scatter(x, y, color='black', s=size, zorder=2)

def plot_error(error, color, linewidth):
    zorder = 1
    for qubit in error:
        # print('qubit', qubit)
        coord, is_horizontal = qubit_index_to_coordinates(qubit)
        # print(coord, is_horizontal)
        x, y = coord
        if is_horizontal:
            plt.plot([x, x+1], [y, y], color=color, zorder=zorder, linewidth=linewidth)
            if x == l - 1:
                plt.plot([-0.5, 0], [y, y], color=color, zorder=zorder, linewidth=linewidth)
        else:
            plt.plot([x, x], [y, y+1], color=color, zorder=zorder, linewidth=linewidth)
            if y == l - 1:
                plt.plot([x, x], [-0.5, 0], color=color, zorder=zorder, linewidth=linewidth)

def plot_syndrome(syndrome, size):
    for check in syndrome:
        x, y = index_to_coordinates(check)
        plt.scatter(x, y, color='red', s=size, zorder=3)

