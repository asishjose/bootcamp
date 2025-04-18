# Example 1:
# Input:N = 153
# Output:True
# Explanation: 13+53+33 = 1 + 125 + 27 = 153
# Example 2:
# Input:N = 371
# Output: True
# Explanation: 33+53+13 = 27 + 343 + 1 = 371

def armstrong(n):
    l = len(str(n))
    digits = [int(d) for d in str(n)]
    cubes = [d**l for d in digits]
    res = sum(cubes)
    if res == n:
        return True
    else:
        return False

print(armstrong(371))
