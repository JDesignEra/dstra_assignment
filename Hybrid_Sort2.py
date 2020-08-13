import decimal
import time


def partition(values, low, high):
    i = (low - 1)
    pivot = values[high]

    for j in range(low, high):
        if values[j] <= pivot:
            i = i + 1
            values[i], values[j] = values[j], values[i]

    values[i + 1], values[high] = values[high], values[i + 1]
    return i + 1


def quickSort(values, low, high):
    if low < high:
        pivot = partition(values, low, high)

        quickSort(values, low, pivot - 1)
        quickSort(values, pivot + 1, high)


def insertionSort(values):
    for i in range(1, len(values)):
        val = values[i]

        pos = i
        while pos > 0 and val < values[pos - 1]:
            values[pos] = values[pos - 1]
            pos -= 1

        values[pos] = val


def hybridSort(values, low, high):
    while low < high:
        if high - low < 7:
            print('INSERTION SORT')
            insertionSort(values)
            break
        else:
            print('HYBRID SORT')
            pivot = partition(values, low, high)

            if pivot - low < high - pivot:
                hybridSort(values, low, pivot - 1)
            else:
                hybridSort(values, pivot + 1, high)
                high = pivot - 1


def sortSelect(values, sortType = 'h'):
    if sortType == 'i':
        start = time.time()
        insertionSort(values)
    elif sortType == 'q':
        start = time.time()
        quickSort(values, 0, len(values) - 1)
    else:
        start = time.time()
        hybridSort(values, 0, len(values) - 1)
    print('Duration: {}'.format(decimal.Decimal(time.time() - start)))


a = [10, 51, 2, 18, 4, 31, 14, 5, 23, 64, 29, 1, 11, 55, 21, 31, 8, 55]
print('Quick Sort')
sortSelect(a, 'q')
print('Sorted: {}'.format(a))

a = [10, 51, 2, 18, 4, 31, 14, 5, 23, 64, 29, 1, 11, 55, 21, 31, 8, 55]
print('\nInsertion Sort')
sortSelect(a, 'i')
print('Sorted: {}'.format(a))

a = [10, 51, 2, 18, 4, 31, 14, 5, 23, 64, 29, 1, 11, 55, 21, 31, 8, 55]
print('\nHybrid Sort')
sortSelect(a)
print('Sorted: {}'.format(a))
