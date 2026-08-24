class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Build prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Start with the case where we take all stones
        dp = prefix[n - 1]

        # Try every valid stopping point
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp