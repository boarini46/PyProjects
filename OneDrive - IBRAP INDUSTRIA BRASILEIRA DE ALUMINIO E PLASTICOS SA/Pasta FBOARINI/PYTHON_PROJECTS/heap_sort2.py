import random

arr = random.sample(range(100),25)
#arr.sort()

def func(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        func(arr, n, largest)

def ordena(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        func(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        func(arr, i, 0)

ordena(arr)

print(arr)
