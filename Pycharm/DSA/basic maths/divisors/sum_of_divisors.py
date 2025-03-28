
n = 6
total_sum = 0
for i in range(1,n+1):
    sum_div = 0

    for j in range(1,int(i**0.5)+1):
        if i%j == 0:
            sum_div += j
            if j != i // j:
                sum_div += i // j
    total_sum += sum_div

print(total_sum)