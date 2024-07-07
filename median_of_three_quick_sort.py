def median_of_three_quick_sort(arr, p, r):
    if p < r:
        if r - p + 1 <= 3:
            insertion_sort(arr, p, r)
        else:
            q = median_of_three(arr, p, r)
            median_of_three_quick_sort(arr, p, q - 1)
            median_of_three_quick_sort(arr, q + 1, r)


def median_of_three(array, p, r):
    mid = (p + r) // 2

    if array[mid] < array[p]:
        array[mid], array[p] = array[p], array[mid]
    if array[r] < array[p]:
        array[r], array[p] = array[p], array[r]
    if array[r] < array[mid]:
        array[r], array[mid] = array[mid], array[r]

    array[mid], array[r - 1] = array[r - 1], array[mid]
    return partition(array, p, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def insertion_sort(arr, p, r):
    for i in range(p + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= p and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key