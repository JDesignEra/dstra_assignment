import random
from decimal import Decimal
import timeit

CONST_A = [104, 264, 448, 212, 324, 480, 435, 385, 254, 469, 110, 136, 42, 350, 456, 37, 478, 298, 106, 330, 41, 233, 323, 390, 36, 314, 210, 419, 146, 491, 3, 252, 91, 258, 454, 488, 262, 306, 65, 374, 309, 117, 123, 51, 55, 440, 196, 366, 204, 407, 474, 12, 459, 109, 179, 303, 423, 112, 498, 44, 429, 421, 185, 22, 359, 482, 57, 94, 232, 286, 280, 245, 270, 50, 278, 190, 198, 293, 170, 33, 387, 266, 443, 302, 15, 375, 229, 126, 46, 276, 247, 412, 119, 457, 444, 19, 139, 219, 499, 484]
CONST_B = [13, 10, 12, 4, 18, 2, 0, 19]

def insertionSort(a):
    for i in range(1, len(a)):
        val = a[i]
        pos = i

        while pos > 0 and val < a[pos - 1]:
            a[pos] = a[pos - 1]
            pos -= 1

        a[pos] = val


def partition(a, low, high):
    i = low - 1
    pivot = a[high]

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quickSort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)


def hybridSort(a, low, high, cutoff):
    if len(a) > cutoff:
        quickSort(a, low, high)
    else:
        insertionSort(a)


def quickSort_time():
    setup_code = '''
from __main__ import quickSort
from __main__ import CONST_A
        '''

    test_code = '''
a = CONST_A.copy()
quickSort(a, 0, len(a) - 1)
        '''

    print('QUICK SORT\n===============')
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=1, number=1)
    a = CONST_A.copy()
    quickSort(a, 0, len(a) - 1)
    print('QUICK SORT:              {}'.format(Decimal(min(times))))
    print('Sorted: {}'.format(a))


def hybridSort_quick_time():
    setup_code = '''
from __main__ import hybridSort
from __main__ import CONST_A
        '''

    test_code = '''
a = CONST_A.copy()
hybridSort(a, 0, len(a) - 1, 15)
        '''

    print('HYBRID / QUICK SORT\n===============')
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=1, number=1)
    a = CONST_A.copy()
    hybridSort(a, 0, len(a) - 1, 10)
    print('HYBRID / QUICK SORT:     {}'.format(Decimal(min(times))))
    print('Sorted: {}'.format(a))


def insertionSort_time():
    setup_code = '''
from __main__ import insertionSort
from __main__ import CONST_B
        '''
    test_code = '''
a = CONST_B.copy()
insertionSort(a)
        '''

    print('INSERTION SORT\n===============')
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=1, number=1)
    a = CONST_B.copy()
    insertionSort(a)
    print('INSERTION SORT:          {}'.format(Decimal(min(times))))
    print('Sorted: {}'.format(a))


def hybridSort_hybrid_time():
    setup_code = '''
from __main__ import hybridSort
from __main__ import CONST_B
        '''

    test_code = '''
a = CONST_B.copy()
hybridSort(a, 0, len(a) - 1, 15)
        '''

    print('HYBRID / INSERTION SORT\n===============')
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=1, number=1)
    a = CONST_B.copy()
    hybridSort(a, 0, len(a) - 1, 10)
    print('HYBRID / INSERTION SORT: {}'.format(Decimal(min(times))))
    print('Sorted: {}'.format(a))


quickSort_time()
print()
hybridSort_quick_time()
print()
insertionSort_time()
print()
hybridSort_hybrid_time()

# a = CONST_A.copy()
# print(a)
# print('INSERTION START')
# insertionSort(a, 0, len(a))
#
# print(a)
# print('HYBRID START')
# a = CONST_A.copy()
# hybridSort(a, len(a) - 1)
#
# print(a)
# print('QUICK START')
# a = CONST_A.copy()
# quickSort(a, 0, len(a) - 1)

values = random.sample(range(20), 8)
print(values)