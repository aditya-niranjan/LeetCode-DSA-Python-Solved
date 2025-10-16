class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i<n:
            if nums[i] == 0:
                e = nums.pop(i)
                nums.append(e)
                n-=1
            else:
                i+=1
        