class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0

        # Traverse from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            
            if bit == 1:
                # odd → add 1 → becomes even
                steps += 2
                carry = 1
            else:
                # even → divide by 2
                steps += 1
                
        return steps+carry