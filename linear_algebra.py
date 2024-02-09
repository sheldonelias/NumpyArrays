import numpy as np


def matrix_addition():
    print('-- adding matrices --')
    #two same sized arrays
    A = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    B = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    C = np.add(A, B)
    print(C)

    print('-- additive scalar --')

    #one multi-dimensional array added with scalar
    C = np.add(2, C)
    print(C)

    pass

def matrix_subtraction():
    print('-- subtracting matrices --')
    #two same sized arrays
    A = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    B = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    C = np.subtract(A, B)
    print(C)

    print('-- subtractive scalar --')

    #one multi-dimensional array subtracted with scalar
    C = np.subtract(2, A)
    print(C)

    pass

def matrix_multiplication():
    print('-- multiplying matrices --')
    A = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    B = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    C = np.multiply(A, B)
    print(C)

    print('-- multiplicative scalar --')

    C = np.multiply(3, C)
    print(C)

    pass

def matrix_division():
    print('-- dividing matrices --')
    A = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    B = np.array([[3, 2, 1], [3, 2, 1], [1, 2, 3]])
    C = np.divide(A, B)
    print(C)

    print('-- dividend scalar --')

    C = np.divide(3, A)
    print(C)

    pass

def linear_algebra():
    matrix_addition()
    matrix_subtraction()
    matrix_multiplication()
    matrix_division()
    pass