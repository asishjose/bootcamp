
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        number = num
        while number>0:
            digit = number%10
            if num % digit == 0:
                count+=1
            number//=10
        return count

sol = Solution()
result = sol.countDigits(121)

print(result)