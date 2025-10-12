class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        first = nums[0]

        answers = []

        for num in first:
            if num in answers:
                continue

            exist_in_all_array = True
            for arr in nums[1:]:
                if num not in arr:
                    exist_in_all_array = False
                    break

            if exist_in_all_array:
                answers.append(num)

        answers.sort()
        return answers

s1 = Solution()
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
result = s1.intersection(nums)
print(result)