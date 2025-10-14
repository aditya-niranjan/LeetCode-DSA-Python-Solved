class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k= k % n

        nums[:] = nums[-k:] + nums[:-k]

s1 = Solution()
arr = [1,2,3,4,5,6,7]
s1.rotate(arr,3)