class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0

        increasing = True
        decreasing = True

        while i< n-1:
            if nums[i] < nums[i+1]:
                decreasing = False
            elif nums[i] > nums[i+1]:
                increasing = False
            i+=1
        
        return increasing or decreasing
s1 = Solution()
n = [1,2,2,3]
s1.isMonotonic(n)