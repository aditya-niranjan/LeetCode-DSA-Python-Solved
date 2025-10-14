class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        n = len(nums)
        total_op = 0

        # store (value, index) once to avoid repeated min() calls
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))

        current_index = 0
        for i in range(n):
            val, idx = sorted_nums[i]

            # if next smallest is behind current, we simulate rotation
            if i > 0 and idx < sorted_nums[i - 1][1]:
                total_op += n - i

        total_op += n  # each pop counts as 1 operation
        return total_op


s1 = Solution()
print(s1.countOperationsToEmptyArray([1,2,4,3]))  # ✅ works fast now
print(s1.countOperationsToEmptyArray([3,4,-1]))   # ✅ 5
