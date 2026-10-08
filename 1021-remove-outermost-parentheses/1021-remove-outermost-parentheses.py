class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance = 0
        left = 0
        res = ""

        for right in range(len(s)):
            if s[right] == '(':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                res += s[left + 1:right]
                left = right + 1


        return res