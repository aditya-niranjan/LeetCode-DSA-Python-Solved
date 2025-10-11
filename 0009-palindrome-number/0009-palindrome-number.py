class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if num < 0:
            return False
        result = 0

        while num>0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10
        return result == x 

s1 = Solution()
n = 121
print("palindrome" if s1.isPalindrome(n) else "NOt a Palindrome")
