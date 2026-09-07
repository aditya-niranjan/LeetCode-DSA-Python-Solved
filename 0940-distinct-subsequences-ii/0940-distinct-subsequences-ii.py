class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:
            old = dp

            # Every existing subsequence:
            # 1. don't take ch
            # 2. take ch
            dp = (2 * dp) % MOD

            # Remove duplicates caused by previous ch
            if ch in last:
                dp = (dp - last[ch]) % MOD

            # Store dp BEFORE adding current ch
            last[ch] = old

        # Remove empty subsequence
        return (dp - 1) % MOD