import numpy
import pandas
import matplotlib.pyplot
import torch


def main():
    print("hello world")
    print(torch.__version__)
    print(matplotlib._get_version())
    print(pandas.__version__)
    print(numpy.__version__)


if __name__ == "__main__":
    main()