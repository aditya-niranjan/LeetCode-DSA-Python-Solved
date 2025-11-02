class Solution(object):

    def Lower_Bound(self, nums, target):
        n = len(nums)
        lower_bound = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return lower_bound

    def Upper_Bound(self, nums, target):
        n = len(nums)
        upper_bound = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return upper_bound

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        lb = self.Lower_Bound(nums, target)
        ub = self.Upper_Bound(nums, target) - 1  # subtract 1 to get last occurrence

        # Check if target actually exists
        if lb < len(nums) and nums[lb] == target:
            return [lb, ub]
        else:
            return [-1, -1]
