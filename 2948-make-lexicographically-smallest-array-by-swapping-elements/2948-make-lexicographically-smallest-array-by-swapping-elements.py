class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # value + original index
        arr = [(nums[i], i) for i in range(n)]

        # Sort by value
        arr.sort()

        ans = nums[:]

        start = 0

        for i in range(1, n + 1):

            # Group ends here
            if i == n or arr[i][0] - arr[i - 1][0] > limit:

                # Values in this group
                values = [arr[j][0] for j in range(start, i)]

                # Original indexes in this group
                indexes = [arr[j][1] for j in range(start, i)]

                # Put smallest values at smallest indexes
                values.sort()
                indexes.sort()

                for j in range(len(values)):
                    ans[indexes[j]] = values[j]

                start = i

        return ans