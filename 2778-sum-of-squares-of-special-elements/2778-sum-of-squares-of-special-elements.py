class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        special = 0

        for i in range(len(nums)):
            if n % (i+1) == 0:
                squre = nums[i] * nums[i]
                special+=squre

        return special