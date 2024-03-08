import numpy as np



def arr_3d():
    print('-- intializing 3x3d array --')
    A = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    print('A: ')
    print(A)
    # print()
    # print('A[0]:')
    # print(A[0])
    # print()
    # print('A[1][2]:')
    # print(A[1][2])
    # A[0][2] = -2
    # print()
    print('A[0][2]:')
    # print(A[0][2])
    # print(A)
    A = A + 1
    print(A)

    pass

def arrayrange_V_range():
    print('-- arrayrange() vs range() --')
    print('-- arange() data types --')
    for x in np.arange(1, 7, 2):
        print(type(x), end=': ')
        print(x)

    print('-- range() data types --')

    for x in range(1, 7, 2):
        print(type(x), end=': ')
        print(x)

    print('-- assinging and printing arange() and range() --')

    #printing directly or passing value
    #np np.arange() result is space seperated list
    print(np.arange(1, 7, 2))
    list = np.arange(1 ,7, 2)
    print(list)

    #printing directly or passing value
    ##np range() result is same function, no change
    print(range(1, 7, 2))
    list = range(1, 7, 2)
    print(list)

    #with list comprehension
    # similar result is comma separated list
    print(   [x for x in range(1, 7, 2)]    )
    list = [x for x in range(1, 7, 2)]
    print(list)

    pass




def basic_3d():
    arr_3d()
    # arrayrange_V_range()
    pass