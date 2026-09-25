class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n = len(g)
        m = len(s)
        left = 0
        right  = 0

        g.sort()
        s.sort()

        count = 0
        while left<n and right<m:
            if g[left] <= s[right]:
                count+=1
                left+=1
            right+=1
        return count