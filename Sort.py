import decimal
import timeit


def partition(values, low, high):
    pivot = values[high]
    i = low

    for j in range(low, high):
        if values[j] < pivot:
            values[i], values[j] = values[j], values[i]
            i += 1

    values[i], values[high] = values[high], values[i]
    return i


def quickSort(values, low, high):
    if low < high:
        pivot = partition(values, low, high)

        quickSort(values, low, pivot - 1)
        quickSort(values, pivot + 1, high)


def insertionSort(values):
	for i in range(1, len(values)):
		x = values[i]
		j = i - 1
		while j >= 0 and x < values[j]:
			values[j + 1] = values[j]
			j -= 1
		values[j + 1] = x


def hybridSort(values, low, high, k):
    if low < high:
        if high - low + 1 < k:
            pivot = partition(values, low, high)
            hybridSort(values, low, pivot, k)
            hybridSort(values, pivot + 1, high, k)
    insertionSort(values)


def sortSelect_quick():
    SETUP_CODE = '''
from __main__ import quickSort
        '''

    TEST_CODE = '''
a = [17, 28, 2, 73, 98, 16, 67, 82, 68, 20, 88, 54, 43, 18, 73, 56, 40, 92, 43, 44, 41, 58, 81, 1, 45, 78, 53, 92, 74, 96, 18, 3, 30, 2, 23, 59, 26, 38, 43, 65, 27, 47, 78, 31, 91, 23, 98, 76, 50, 79, 18, 65, 52, 62, 72, 30, 6, 28, 14, 100, 1, 13, 56, 86, 47, 1, 79, 17, 90, 40, 26, 20, 73, 65, 1, 28, 73, 16, 38, 95, 95, 9, 81, 18, 44, 100, 98, 92, 36, 94, 83, 35, 78, 21, 62, 95, 1, 47, 100, 43]
print('Quick Sort')
quickSort(a, 0, len(a) - 1)
print('Sorted: {}'.format(a))
        '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=1, number=1)
    print('QUICK SORT:     {}\n'.format((decimal.Decimal(min(times)))))


def sortSelect_insertion():
    SETUP_CODE = '''
from __main__ import insertionSort
        '''

    TEST_CODE = '''
a = [17, 28, 2, 73, 98, 16, 67, 82, 68, 20, 88, 54, 43, 18, 73, 56, 40, 92, 43, 44, 41, 58, 81, 1, 45, 78, 53, 92, 74, 96, 18, 3, 30, 2, 23, 59, 26, 38, 43, 65, 27, 47, 78, 31, 91, 23, 98, 76, 50, 79, 18, 65, 52, 62, 72, 30, 6, 28, 14, 100, 1, 13, 56, 86, 47, 1, 79, 17, 90, 40, 26, 20, 73, 65, 1, 28, 73, 16, 38, 95, 95, 9, 81, 18, 44, 100, 98, 92, 36, 94, 83, 35, 78, 21, 62, 95, 1, 47, 100, 43]
print('Insertion Sort')
insertionSort(a)
print('Sorted: {}'.format(a))
        '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=1, number=1)
    print('INSERTION SORT: {}\n'.format((decimal.Decimal(min(times)))))


def sortSelect_hybrid():
    SETUP_CODE = '''
from __main__ import hybridSort
        '''

    TEST_CODE = '''
a = [17, 28, 2, 73, 98, 16, 67, 82, 68, 20, 88, 54, 43, 18, 73, 56, 40, 92, 43, 44, 41, 58, 81, 1, 45, 78, 53, 92, 74, 96, 18, 3, 30, 2, 23, 59, 26, 38, 43, 65, 27, 47, 78, 31, 91, 23, 98, 76, 50, 79, 18, 65, 52, 62, 72, 30, 6, 28, 14, 100, 1, 13, 56, 86, 47, 1, 79, 17, 90, 40, 26, 20, 73, 65, 1, 28, 73, 16, 38, 95, 95, 9, 81, 18, 44, 100, 98, 92, 36, 94, 83, 35, 78, 21, 62, 95, 1, 47, 100, 43]
print('Hybrid Sort')
hybridSort(a, 0, len(a) - 1, 10)
print('Sorted: {}'.format(a))
        '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=1, number=1)
    print('HYBRID SORT:    {}\n'.format((decimal.Decimal(min(times)))))


if __name__ == '__main__':
    sortSelect_quick()
    sortSelect_insertion()
    sortSelect_hybrid()
