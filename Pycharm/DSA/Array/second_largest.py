arr = [1,3,99,40,50,30,55,49,80,20]

largest  =  0
sec_largest = 0
for n in arr:
    if n > largest:
        sec_largest = largest
        largest = n
    if n > sec_largest and n < largest:
        sec_largest = n


print(largest, sec_largest)