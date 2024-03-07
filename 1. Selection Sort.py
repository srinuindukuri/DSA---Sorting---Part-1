def selection_sort(array, n):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if array[j] <= array[mini]:
                mini = j
        (array[i], array[mini]) = (array[mini], array[i])


data = [13, 46, 24, 52, 20, 9]
n = len(data)
selection_sort(data, n)
print("The sorted array is..")
print(data)
