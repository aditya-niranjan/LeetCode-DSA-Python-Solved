from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]

            # Step 1: Count occurrences
            freq = Counter(sub)

            # Step 2: Sort by frequency desc, then value desc
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))

            # Step 3: Pick top x elements
            top_x = set([num for num, _ in sorted_items[:x]])

            # Step 4: Sum elements in subarray that are in top x
            x_sum = sum(num for num in sub if num in top_x)

            result.append(x_sum)

        return result


# Example testcases
nums1 = [1, 1, 2, 2, 3, 4, 2, 3]
k1, x1 = 6, 2
print("Example 1 Output:", Solution().findXSum(nums1, k1, x1))  # [6, 10, 12]

nums2 = [3, 8, 7, 8, 7, 5]
k2, x2 = 2, 2
print("Example 2 Output:", Solution().findXSum(nums2, k2, x2))  # [11, 15, 15, 15, 12]
