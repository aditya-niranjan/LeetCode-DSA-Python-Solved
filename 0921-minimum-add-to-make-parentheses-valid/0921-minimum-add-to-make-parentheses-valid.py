class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        number = 0
        answer = 0

        for ch in s:

            if ch == "(":
                number += 1

            elif ch == ")":

                if number > 0:
                    number -= 1
                else:
                    answer += 1

        answer += number

        return answer
