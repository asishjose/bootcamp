letters = ['a',"c","f","j"]
target = "g"

idx = 0
prev_idx = 0
for i in range(len(letters)):
    if letters[i]==target:
        idx=i
    elif letters[i]<target:
        prev_idx = max(i,prev_idx)

if idx != 0:
    print()
print(idx)
print(prev_idx)