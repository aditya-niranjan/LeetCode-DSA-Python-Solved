class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: intreading
        :type k: int
        :rtype: str
        """
        # Base case
        if n == 1:
            return "0"
        
        length = (1 << n) - 1          # 2^n - 1
        mid = (length // 2) + 1       # middle position
        
        if k == mid:
            return "1"
        elif k < mid:
            # Left half → same as S(n-1)
            return self.findKthBit(n - 1, k)
        else:
            # Right half
            # Mirror position in left half
            mirrored_k = length - k + 1
            
            # Recursively get bit from left
            bit = self.findKthBit(n - 1, mirrored_k)
            
            # Invert it
            return "1" if bit == "0" else "0"