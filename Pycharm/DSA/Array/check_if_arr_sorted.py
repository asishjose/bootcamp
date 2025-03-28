arr = [1,2,4,5,6,7,8,2]

for i in range(len(arr)-1):
    #print(arr[i])
    if arr[i]>arr[i+1]:
        print("not sorted")
        break
