class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n  = len(nums)
        my_set = set()

        for i in range(0,n):
            my_set.add(nums[i])

        logest = 0

        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count+=1
                    x+=1
    
                logest = max(logest, count)

        return logest