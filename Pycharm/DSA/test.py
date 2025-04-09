elements = [11, 9, 29, 7, 2, 15, 28]

size = len(elements)
for i in range(1,size-1):
    anchor = elements[i]
    j = i-1
    while j>=0 and anchor<elements[j]:
        elements[j+1] = elements[j]
        j -= 1
    elements[j+1] = anchor

print(elements)