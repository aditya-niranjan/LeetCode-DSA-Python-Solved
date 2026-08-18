from collections import defaultdict
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)

        for i in range(len(nums) - k + 1):
            window = set(nums[i:i+k])

            for num in window:
                count[num] += 1

        ans = -1

        for num, freq in count.items():
            if freq == 1:
                ans = max(ans, num)

        return ans