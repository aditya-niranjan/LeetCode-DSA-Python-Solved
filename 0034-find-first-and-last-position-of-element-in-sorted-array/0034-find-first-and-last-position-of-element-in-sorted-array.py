class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        n = len(nums)
        first = -1
        last = -1

        for i in range(0,n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first,last]