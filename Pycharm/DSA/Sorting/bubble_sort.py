arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

