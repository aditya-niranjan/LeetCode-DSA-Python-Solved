class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        positive = []
        negative = []
        result = []

        for num in range(0,len(nums)):
            if nums[num] > 0:
                positive.append(nums[num])
            else:
                negative.append(nums[num])
        
        for i in range(0,len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        return result

        