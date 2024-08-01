def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr

arr = [90, 10, 15, 20, 100,1]
print(bubbleSort(arr))
