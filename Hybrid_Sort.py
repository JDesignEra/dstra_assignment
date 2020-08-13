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
        pi = partition(values, low, high)

        quickSort(values, low, pi - 1)
        quickSort(values, pi + 1, high)


def insertionSort(values):
    for i in range(1, len(values)):
        val = values[i]

        pos = i
        while pos > 0 and val < values[pos - 1]:
            values[pos] = values[pos - 1]
            pos -= 1

        values[pos] = val


def hybridSort(values):
    start = time.time()
    if len(values) > 10:
        print('QUICK SORT\n================')
        quickSort(values, 0, len(values) - 1)
    else:
        print('INSERTION SORT\n================')
        insertionSort(values)

    duration = time.time() - start
    print('Duration: {} secs'.format(decimal.Decimal(duration)))


a = [10, 51, 2, 18, 4, 31, 14, 5]
hybridSort(a)
print('Sorted: {}\n'.format(a))

a = [10, 51, 2, 18, 4, 31, 14, 5, 23, 64, 29]
hybridSort(a)
print('Sorted: {}\n'.format(a))
