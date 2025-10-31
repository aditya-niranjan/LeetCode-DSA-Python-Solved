class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        hash_map = {}
        result = []
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        
        for num in hash_map:
            if hash_map[num] == 2:
                result.append(num)
        return result

