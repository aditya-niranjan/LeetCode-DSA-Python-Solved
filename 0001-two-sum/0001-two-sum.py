class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff],i]
            hash_map[num]=i
        return []

s1 = Solution()
print(s1.twoSum([2,7,11,15],9))
print(s1.twoSum([3,2,4],6))
print(s1.twoSum([3,3],6))