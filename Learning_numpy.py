import numpy
import pandas
import matplotlib.pyplot
import torch

# For numpy documentation: [ https://numpy.org/doc/ ]


def main():
    get_version()
    basics_of_numpy()
    accessing_changing_specific_elements()
    initialising_different_arrays()
    mathematics_in_numpy()
    statistics_in_numpy()
    reorganising_arrays()
    miscellaneous()


def get_version():
    print("torch version: ", torch.__version__)
    print("matplotlib version: ", matplotlib._get_version())
    print("pandas version: ", pandas.__version__)
    print("numpy version: ", numpy.__version__)

# ||-------------------------------------------------------------------------------------------------------------------||

# NUMPY: arrays || mathematics || plotting || backend || machine learning
# Numpy is a multidimensional array library, you can use numpy to store all types of data in 1D, 2D, 3D, 4D arrays etc.
# Pythons lists are slow. They contain more information which makes them slow compared to numpy. Lists contain the
# size, reference count, object type and object value compared to just the object value(int32/int16) in numpy.
# Because numpy uses fewer bytes of memory the computer can read the bytes quicker.
# Python lists checks each element for types whereas upy does not do that.
# Numpy utilises contiguous memory - CPU performs more efficiently with numpy - More effectively utilises cache.

# ||-------------------------------------------------------------------------------------------------------------------||


def basics_of_numpy():
    print("||-------------------------------------------BASICS----------------------------------------------||")

    array1d = numpy.array([12, 76, 88, 9, 1, 1, 1], dtype='int16')
    print("1D array: ", array1d)

    array2d = numpy.array([
        [1, 4, 55, 66],
        [98, 8, 57, 14]
    ], dtype='float32')  # The multidimensional arrays must be of same size.
    print("2D array:\n", array2d)

    array3d = numpy.array([[
        [1.6, 7.3, 5.5],
        [4.9, 54.1, 12.3]],

        [[5.6, 76.2, 1.1],
         [99.9, 20.6, 4.6]
         ]])  # The multidimensional arrays must be of same size.
    print("3D array:\n", array3d)

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

# ||-------------------------------------------------------------------------------------------------------------------||


def accessing_changing_specific_elements():
    print("||-------------------------------------------ACCESSING----------------------------------------------||")

    numpy_array = numpy.array([
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14]])

    # Getting a specific element [row, column]:
    print(numpy_array[1, 5])  # Row and column start at index 0.
    print(numpy_array[1, -2])  # numpy_array has two rows therefore, the first index can only be 0 or 1 or -1
    print(numpy_array[-1, -2])
    print(numpy_array[0, :])  # This prints out the entire first row
    print(numpy_array[:, 0])  # this prints out all the rows first element

    numpy_array[1, 5] = 999
    print(numpy_array)

# ||-------------------------------------------------------------------------------------------------------------------||


def initialising_different_arrays():
    print("||-------------------------------------------INITIALISATION----------------------------------------------||")

    scalar = numpy.ones(1)  # All 1 tensor
    print("Scalar: ", scalar)

    vector = numpy.zeros(5)  # All 0 tensor
    print("Vector: ", vector)

    matrix = numpy.ones((5, 5), dtype='int16')
    print("Matrix:\n", matrix)

    tensor = numpy.zeros((5, 5, 5), dtype='float32')
    print("Tensor:\n", tensor)

    # tensor4d = numpy.ones((5, 5, 5, 5))
    # print("Tensor 4D: ", tensor4d)

    other_number_tensor = numpy.full((2, 2, 2, 2), 99, dtype='int16')
    print(other_number_tensor)

    random_array = numpy.random.rand(4, 2)
    print("Random array: ", random_array)
    random_sample_array = numpy.random.random_sample(tensor.shape)  # Takes the shape of a created array and makes the values random
    print("Random sample array:\n", random_sample_array)

    # Random integer values randint(range of value, size=())
    random_int_array = numpy.random.randint(10, size=(3, 3, 3))
    print("Random Integer array:\n", random_int_array)

    # Identity matrix:
    identity_matrix = numpy.identity(7)
    print("Identity Matrix:\n", identity_matrix)

    # Filling a matrix with zeros:
    ones = numpy.ones((7, 7))
    zeros = numpy.zeros((5, 5))

    ones[1:-1, 1:-1] = zeros  # <- From the second element to the sec ond last element
    print("Filling the middle with zeros:\n", ones)

# ||-------------------------------------------------------------------------------------------------------------------||


def mathematics_in_numpy():
    print("||-------------------------------------------MATHMATICS----------------------------------------------||")

    example_array = numpy.array([10, 10, 10, 10, 10])
    print("Example array = ", example_array)
    print(example_array + 10)
    print(example_array - 10)
    print(example_array * 10)
    print(example_array / 10)
    print(example_array ** 4)
    print(numpy.sin(example_array))
    print(numpy.cos(example_array))
    print(numpy.tan(example_array))
    # For a lot more: [ https://docs.scipy.org/doc/numpy/reference/routines.math.html ]

    # Linear Algebra:
    a = numpy.ones((5, 3))
    b = numpy.full((3, 5), 7)

    print("Multiplying two tensors using matmul(a, b):\n", numpy.matmul(a, b))
    # For a lot more: [ https://docs.scipy.org/doc/numpy/reference/routines.linalg.html ]


def statistics_in_numpy():
    print("||-------------------------------------------STATISTICS----------------------------------------------||")

    stats = numpy.array([[5, 7, 99, 100], [3, 86, 1000, 1]])
    print(stats)

    print("Minimum of the array: ", numpy.min(stats))
    print("Maximum of the array: ", numpy.max(stats))

    sum_of_array = numpy.sum(stats)
    print("Sum of the array: ", sum_of_array)
    # For a lot more: [ https://docs.scipy.org/doc/numpy/reference/routines.statistics.html ]
    # With statistics you can perform the mean, mode, median, average, standard deviation and variance.Also, a lot more.


def reorganising_arrays():
    print("||-------------------------------------------REORGANISING----------------------------------------------||")

    before = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("Before: ", before)

    after = before.reshape((2, 2, 2))  # Cannot be mismatching the shape of the array.
    print("After the reshape:\n", after)

    # Vertically stacking vectors:
    vector1 = numpy.array([44, 44, 44, 44])  # Both arrays much match in COLUMN size before stacking
    print("Vector 1: ", vector1)
    vector2 = numpy.array([77, 77, 77, 77])
    print("Vector 2: ", vector2)

    vstacked_vectors = numpy.vstack([vector1, vector2, vector1, vector2])
    print("Vertically stacking the two vectors:\n", vstacked_vectors)

    # Horizontally stacking vectors:
    vector3 = numpy.ones([2, 4])  # Both arrays much match in ROW size before stacking
    print("Vector 3:\n", vector3)
    vector4 = numpy.zeros([2, 3])
    print("Vector 4:\n", vector4)

    hstacked_vectors = numpy.hstack([vector1, vector2, vector1, vector2])
    print("Horizontally stacking the two vectors:\n", hstacked_vectors)


def miscellaneous():
    print("||-------------------------------------------MISCELLANEOUS----------------------------------------------||")

    # Loading data from a file
    filedata = numpy.genfromtxt('./Data/numbers.txt', delimiter=',')
    filedata = filedata.astype('int16')
    print("FILE DATA:\n", filedata)

    # Boolean masking and advanced indexing
    print("Boolean Masking:\n", filedata > 50)
    print("Advanced Indexing:\n", filedata[filedata > 50])

    print(numpy.any((filedata > 50) & (filedata < 100), axis=0))  # Are any of the values in the column greater than 50 AND less than 100?
    # Answer should be 17 booleans as there are 17 columns in the data


if __name__ == "__main__":
    main()
