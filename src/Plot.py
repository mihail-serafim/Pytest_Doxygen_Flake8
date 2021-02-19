## @file Plot.py
#  @author Mihail Serafimovski
#  @brief Defines the plot module
#  @date Feb 10, 2021
#  @details The plot module plots the results of a simulation
#           as three graphs, using matplotlib

import matplotlib.pyplot as plt

## @brief The plot module
#  @details Uses matplotlib to create 3 plots of:
#   x vs t, y vs t, and y vs x
#  @param w A sequence of real numbers which is generated
#           by the sim method in Scene.py
#  @param t A sequence of real numbers which represent
#           the time steps in the simulation
#  @throws ValueError if lengths of w and t are not equal


def plot(w, t):
    if not(len(w) == len(t)):
        raise ValueError

    fig, axs = plt.subplots(3)
    fig.suptitle('Motion Simulation')

    x = [w[i][0] for i in range(len(w))]
    y = [w[i][1] for i in range(len(w))]

    axs[0].plot(t, x)
    axs[0].set_xlabel('t(seconds)')
    axs[0].set_ylabel('x(m)')
    axs[1].plot(t, y)
    axs[1].set_xlabel('t(seconds)')
    axs[1].set_ylabel('y(m)')
    axs[2].plot(x, y)
    axs[2].set_xlabel('x(m)')
    axs[2].set_ylabel('y(m)')

    plt.show()
