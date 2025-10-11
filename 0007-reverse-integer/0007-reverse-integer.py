class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        num = abs(x)
        result = 0
        while num > 0:
            last_digit = num % 10
            result = int(result * 10) + last_digit
            num = num // 10
        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0


        return result

s1 = Solution()
print("Reversed integer", s1.reverse(123))
