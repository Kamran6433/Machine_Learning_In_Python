import numpy
import pandas
import matplotlib.pyplot
import torch


def main():
    print("hello world")
    get_version()
    basics_of_numpy()


def get_version():
    print("torch version: ", torch.__version__)
    print("matplotlib version: ", matplotlib._get_version())
    print("pandas version: ", pandas.__version__)
    print("numpy version: ", numpy.__version__)


# NUMPY: arrays || mathematics || plotting || backend || machine learning
# Numpy is a multidimensional array library, you can use numpy to store all types of data in 1D, 2D, 3D, 4D arrays etc.
# Pythons lists are slow. They contain more information which makes them slow compared to numpy. Lists contain the
# size, reference count, object type and object value compared to just the object value(int32/int16) in numpy.
# Because numpy uses fewer bytes of memory the computer can read the bytes quicker.
# Python lists checks each element for types whereas upy does not do that.
# Numpy utilises contiguous memory - CPU performs more efficiently with numpy - More effectively utilises cache.


def basics_of_numpy():
    array1d = numpy.array([12, 76, 88, 9, 1, 1, 1], dtype='int16')
    print("1D array: ", array1d)

    array2d = numpy.array([
        [1, 4, 55, 66],
        [98, 8, 57, 14]
    ], dtype='float32')  # The multidimensional arrays must be of same size.
    print("2D array: ", array2d)

    array3d = numpy.array([[
        [1.6, 7.3, 5.5],
        [4.9, 54.1, 12.3]],

        [[5.6, 76.2, 1.1],
         [99.9, 20.6, 4.6]
         ]])  # The multidimensional arrays must be of same size.
    print("3D array ", array3d)

    # Getting the dimensions of arrays ^:
    print("array1d dimensions: ", array1d.ndim)
    print("array2d dimensions: ", array2d.ndim)
    print("array3d dimensions: ", array3d.ndim)

    # Getting the shape of arrays ^:
    print("array1d shape: ", array1d.shape)
    print("array2d shape: ", array2d.shape)
    print("array3d shape: ", array3d.shape)

    # Getting the data type of arrays ^:
    print("array1d data type: ", array1d.dtype)
    print("array2d data type: ", array2d.dtype)
    print("array3d data type: ", array3d.dtype)

    # Getting the size (bytes) of arrays ^:
    print("int16 size (bytes): ", array1d.itemsize)
    print("float32 size (bytes): ", array2d.itemsize)
    print("float64 size (bytes): ", array3d.itemsize)

    # Getting the total size (bytes) of arrays ^:
    print("array1d total size (bytes): ", array1d.nbytes)
    print("array2d total size (bytes): ", array2d.nbytes)
    print("array3d total size (bytes): ", array3d.nbytes)


if __name__ == "__main__":
    main()
