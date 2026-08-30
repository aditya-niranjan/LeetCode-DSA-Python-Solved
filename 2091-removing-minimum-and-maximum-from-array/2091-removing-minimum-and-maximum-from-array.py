class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))

        left = min(mini, maxi)
        right = max(mini, maxi)

        # 1. Remove both from the left
        option1 = right + 1

        # 2. Remove both from the right
        option2 = n - left

        # 3. Remove left one from left, right one from right
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)