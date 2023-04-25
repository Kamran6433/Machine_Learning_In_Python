import numpy
import pandas
import matplotlib.pyplot as mpl

# For full numpy documentation: [ https://matplotlib.org/stable/index.html ]


def main():
    graph()


def graph():
    first_plot = mpl.plot([1, 2, 3], [2, 4, 6])  # [X axis], [Y axis]
    print(first_plot)


if __name__ == "__main__":
    main()
