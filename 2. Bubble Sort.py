def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return


arr = [13, 46, 24, 52, 20, 9]
bubble_sort(arr)
print("The sorted array is..")
print(arr)
