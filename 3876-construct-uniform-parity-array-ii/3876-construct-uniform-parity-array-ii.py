class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # Already all even
        if min_odd == float('inf'):
            return True

        # Already all odd
        if min_even == float('inf'):
            return True

        # We can make every even number odd
        # using the smallest odd number.
        return min_odd < min_even