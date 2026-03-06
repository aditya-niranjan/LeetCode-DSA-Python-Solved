class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = len(nums)
        for i in range(num):
            for j in range(i+1,num):
                total = nums[i] + nums[j]
                if total ==target:
                    return [i,j]