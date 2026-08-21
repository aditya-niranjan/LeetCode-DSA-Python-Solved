class Solution(object):
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            n = len(coins)
            ans = 0

            for mask in range(1, 1 << n):

                common = 1
                bits = 0

                for i in range(n):

                    if mask & (1 << i):
                        common = lcm(common, coins[i])
                        bits += 1

                multiples = x // common

                if bits % 2 == 1:
                    ans += multiples
                else:
                    ans -= multiples

            return ans

        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left