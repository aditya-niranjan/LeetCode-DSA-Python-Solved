class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        change0 = 0   # pattern starting with '0' -> 010101...
        change1 = 0   # pattern starting with '1' -> 101010...

        for i in range(len(s)):
            
            # expected char if pattern starts with '0'
            if s[i] != ('0' if i % 2 == 0 else '1'):
                change0 += 1

            # expected char if pattern starts with '1'
            if s[i] != ('1' if i % 2 == 0 else '0'):
                change1 += 1

        return min(change0, change1)