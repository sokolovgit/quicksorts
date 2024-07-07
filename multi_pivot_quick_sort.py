def multi_pivot_quick_sort(arr, p, r):
    if p < r:
        if r - p + 1 <= 3:
            insertion_sort(arr, p, r)
        else:
            arr[p], arr[p + 1], arr[r] = sorted([arr[p], arr[p + 1], arr[r]])

            a, b, c = multi_pivot_partition(arr, p, r)
            multi_pivot_quick_sort(arr, p, a - 1)
            multi_pivot_quick_sort(arr, a + 1, b - 1)
            multi_pivot_quick_sort(arr, b + 1, c - 1)
            multi_pivot_quick_sort(arr, c + 1, r)


def multi_pivot_partition(arr, left, right):
    a, b = left + 2, left + 2
    c, d = right - 1, right - 1
    p, q, r = arr[left], arr[left + 1], arr[right]

    while b <= c:
        while arr[b] < q and b <= c:
            if arr[b] < p:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1
            b += 1

        while arr[c] > q and b <= c:
            if arr[c] > r:
                arr[c], arr[d] = arr[d], arr[c]
                d -= 1
            c -= 1

        if b <= c:
            if arr[b] > r:
                if arr[c] < p:
                    arr[b], arr[a] = arr[a], arr[b]
                    arr[a], arr[c] = arr[c], arr[a]
                    a += 1
                else:
                    arr[b], arr[c] = arr[c], arr[b]
                arr[c], arr[d] = arr[d], arr[c]
                b += 1
                c -= 1
                d -= 1
            else:
                if arr[c] < p:
                    arr[b], arr[a] = arr[a], arr[b]
                    arr[a], arr[c] = arr[c], arr[a]
                    a += 1
                else:
                    arr[b], arr[c] = arr[c], arr[b]
                b += 1
                c -= 1

    a -= 1
    b -= 1
    c += 1
    d += 1
    arr[left + 1], arr[a] = arr[a], arr[left + 1]
    arr[a], arr[b] = arr[b], arr[a]
    a -= 1
    arr[left], arr[a] = arr[a], arr[left]
    arr[right], arr[d] = arr[d], arr[right]

    return p, q, r


def insertion_sort(arr, p, r):
    for i in range(p + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= p and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key