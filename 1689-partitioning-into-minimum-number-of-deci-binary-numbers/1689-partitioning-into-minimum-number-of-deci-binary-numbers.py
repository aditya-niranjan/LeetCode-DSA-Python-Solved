class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        numlist = list(n)
        maxValue = max(int(x) for x in numlist)

        return maxValue