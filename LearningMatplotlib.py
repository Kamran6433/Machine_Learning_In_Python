import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# For full numpy documentation: [ https://matplotlib.org/stable/index.html ]


def main():
    graph()


def graph():
    first_plot = plt.plot([1, 2, 3], [2, 4, 6])  # [X axis], [Y axis]
    print(first_plot)
    # X axis parameter:
    xaxis = np.array([2, 8])

    # Y axis parameter:
    yaxis = np.array([4, 9])

    plt.plot(xaxis, yaxis)
    plt.show()


if __name__ == "__main__":
    main()
