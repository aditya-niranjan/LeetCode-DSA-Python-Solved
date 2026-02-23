class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * 101
        
        # Count frequency
        for num in nums:
            count[num] += 1
        
        # Prefix sum → count of smaller elements
        for i in range(1, 101):
            count[i] += count[i - 1]
        
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])
        
        return result