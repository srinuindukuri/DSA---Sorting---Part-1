def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = (low-1)
    j = (high+1)
    for i in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[low] = arr[low], arr[i+1]
    return (i+1)


arr = [2, 5, 3, 8, 6, 5, 4, 7]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)
