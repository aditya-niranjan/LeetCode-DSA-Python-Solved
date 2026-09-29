class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxi = 0

        for i in range(0,len(nums)):
            if i>maxi:
                return False

            maxi = max(maxi,i+nums[i])

        return True