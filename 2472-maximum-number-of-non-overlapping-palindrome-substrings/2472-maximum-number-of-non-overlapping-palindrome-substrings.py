class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum number of non-overlapping
        # palindromes using s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            # Don't use a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Palindrome of length k
            if i >= k:
                if pal[i - k][i - 1]:
                    dp[i] = max(dp[i], dp[i - k] + 1)

            # Palindrome of length k + 1
            if i >= k + 1:
                if pal[i - k - 1][i - 1]:
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]