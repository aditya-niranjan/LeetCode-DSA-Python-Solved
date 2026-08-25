class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        num_set = set(nums)

        res = k

        while res in num_set:
            res+=k

        return res
        